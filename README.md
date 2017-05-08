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

