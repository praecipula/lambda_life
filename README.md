Lambda Life
======

A getting started location for working with Amazon Lambda for day to day life automation

Goals:

I want to:
* Automate looking at the BART system alerts to see what the BART schedule is like
* Automate using the Google Maps API to see how traffic is progressing along my commute
* Automate using the Google Maps API to predict the best route to take to work based on historical trends as applied to "today" (low-level ML)
* Use some weather API in order to identify whether it's going to be particularly hot, particularly wet, and so on.
* Use my Philips Hue lights to create easy-to-understand basic reports (traffic is slow, BART is delayed, weather is bad).
* Most importantly, get experience and documentation around creating Lambda apps


Steps to set up:

2fa with Google Authenticator (or similar)


Locally:

virtualenv -p python3 venv
python --version => 3.5.1 :check:
pip install boto3

Make sure you have your boto config set up with your aws credentials (e.g. ~/.aws/config) 
http://boto.cloudhackers.com/en/latest/boto_config_tut.html



Development strategy

Each "lambda function" is its own deployment - that means all the required fields / libraries / dependencies all have to be in one location.

On the plus side, however, that function is not directly tied to the router, so we can disambiguate the Lambda code by having all requests come in to a router/dispatcher, which sees this:

dispatcher(event, context):

event{'resource': '/handleGetStatusAlternate', 'path': '/handleGetStatusAlternate', 'httpMethod': 'GET', 'headers': {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch, br', 'Accept-Language': 'en-US,en;q=0.8', 'cache-control': 'max-age=0', 'CloudFront-Forwarded-Proto': 'https', 'CloudFront-Is-Desktop-Viewer': 'true', 'CloudFront-Is-Mobile-Viewer': 'false', 'CloudFront-Is-SmartTV-Viewer': 'false', 'CloudFront-Is-Tablet-Viewer': 'false', 'CloudFront-Viewer-Country': 'US', 'Host': 'ji0cx7b3bd.execute-api.us-west-2.amazonaws.com', 'Referer': 'https://us-west-2.console.aws.amazon.com/apigateway/home?region=us-west-2', 'upgrade-insecure-requests': '1', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36', 'Via': '2.0 d8f42fc9558e3e49ebfdf8834baeb756.cloudfront.net (CloudFront)', 'X-Amz-Cf-Id': 'mRMumChsGfuGJstlSu8EsxXqeFCK88EGE3atpzGzriaBuB--lk-z8A==', 'X-Amzn-Trace-Id': 'Root=1-5913ca08-1ea572d53874725d7cb9d2bb', 'X-Forwarded-For': '107.192.1.131, 54.239.134.94', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'queryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'path': '/prod/handleGetStatusAlternate', 'accountId': '789554281416', 'resourceId': 'x31b2g', 'stage': 'prod', 'requestId': '2ae2336f-35f0-11e7-80e9-6556848fcd3f', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'apiKey': '', 'sourceIp': '107.192.1.131', 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36', 'user': None}, 'resourcePath': '/handleGetStatusAlternate', 'httpMethod': 'GET', 'apiId': 'ji0cx7b3bd'}, 'body': None, 'isBase64Encoded': False}

context<__main__.LambdaContext object at 0x7fda74687d68>
