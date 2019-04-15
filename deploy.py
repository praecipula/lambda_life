#!/usr/bin/env python

# Deploy to Lambda:
# Package up all needed dependencies minus Amazon provided ones (i.e. boto) and this file
# Zip up those files
# Push them to Amazon

# Future:
# Ping the check date function to see that new version has been uploaded

import boto3
import glob
import fnmatch
import os
import datetime
import zipfile
import re

# According to the AWS Lambda docs at http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html, for virtualenv installs:
# We need to create a zip file as so:
# * Add the content of the root directory python files (and just the files in this directory. Sorry, submodules :/
# * Add the contet of the site-packages directory in venv to the root of the zip file.
# * boto3 comes pre-installed, so we don't need that (or deps).
# * We also don't need this deployment file.

whitelist= ["./*.py", "venv/lib/python3*/site-packages/*"]
blacklist = ["./deploy.py",
# These are provided by Amazon for lamba installs
        "venv/lib/python3*/site-packages/boto3*", 
        "venv/lib/python3*/site-packages/botocore*", 
        "venv/lib/python3*/site-packages/s3transfer*",
# These are part of the python / pip dependency chain
        "venv/lib/python3*/site-packages/pip*",
        "./deploy/*"]

unfiltered_whitelist_files = []
for wl in whitelist:
    unfiltered_whitelist_files.extend(glob.glob(wl))

print("Whitelisted: " + str(unfiltered_whitelist_files))

# Now that we've globbed a whitelist, we need to use fnmatch (which works on strings) instead of glob to blacklist.
# We'll match the files that match blacklist names, then remove them (because fnmatch.filter is more performant than nested loops)
blacklisted_files = []
for bl in blacklist:
    blacklisted_files.extend(fnmatch.filter(unfiltered_whitelist_files, bl))

print("Blacklisted: " + str(blacklisted_files))

includes = set(unfiltered_whitelist_files) - set(blacklisted_files)
print("Includes: " + str(includes))

# Now zip 'em

# Make the dest dir
os.makedirs("./deploy", exist_ok=True)
# We need to strip the leading directory from any pip packages
strip_regex = re.compile(".*/site-packages/(?P<branch>.*)")

zipfilename = ("./staged_bundle/" + datetime.datetime.utcnow().isoformat() + ".zip").replace(':', '_')
with zipfile.ZipFile(zipfilename, 'w') as zipfile:
    for filename in includes:
        # Here's where we match and strip any package prefix (so unzip will inflate into the root dir)
        destination = filename
        branch_match = strip_regex.match(filename)
        if branch_match:
            destination = branch_match.group('branch')
        zipfile.write(filename, destination)
    zipfile.close()

print("Created zipfile: " + zipfilename)

# OK, after all that, we have to deploy with boto.
session = boto3.Session(profile_name='autodash')
client = session.client('lambda')

#Reopen the file to read it, but just as bytes now.
with open(zipfilename, 'rb') as zipfile:
    function_name = 'dispatch'
    if function_name in [fn['FunctionName'] for fn in client.list_functions()['Functions']]:
        # Do an update, not a create
        response = client.update_function_code(FunctionName=function_name, ZipFile=zipfile.read())
    else:
        response = client.create_function(
            FunctionName='dispatch',
            Runtime='python3.6',
            Role='arn:aws:iam::789554281416:role/autodashLambda',
            Handler='dispatch.dispatch',
            Code={
                'ZipFile': zipfile.read(),
                },
            Description='Testing of Amazon Lambda functionality',
            Timeout=10,
            MemorySize=128,
            Publish=True
            #Environment={
            #    'Variables': {
            #        'string': 'string'
            #        }
            #    },
            #Tags={
            #    'string': 'string'
            #    }
            )
    zipfile.close()
print(response)

# At this point, the function exists; we need to tie in Amazon API Gateway to it.
# http://docs.aws.amazon.com/lambda/latest/dg/with-on-demand-https-example-configure-event-source.html
