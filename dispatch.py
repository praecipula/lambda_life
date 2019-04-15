import boto3


def list_domains():
    client = boto3.client('sdb')
    client.list_domains()

def dispatch(event, context):
    try:
        response = {}
        response['headers'] = {}
        response['statusCode'] = 200
        response['body'] = "Function dispatch called, event" + str(event) + "context" + str(context)
        return response
    except Exception as e:
        return handleError(e)


def handleGetStatusAlternate(event, context):
    try:
        response = {}
        response['headers'] = {}
        response['statusCode'] = 200
        response['body'] = "SDB domains: " + str(list_domains()) + "event" + str(event) + "context" + str(context)
        return response
    except Exception as e:
        return handleError(e)
    
def handleError(ex):
    response = {}
    response['headers'] = {}
    response['statusCode'] = 502
    response['body'] = "Error: " + str(ex)
    return response
