import boto3

client = boto3.client('sdb')

def list_domains():
    client.list_domains()

def handleGetStatusAlternate(event, context):
    try:
        response = {}
        response['headers'] = {}
        response['statusCode'] = 200
        response['body'] = "SDB domains: " + str(list_domains())
        return response
    except Exception as e:
        return handleError(e)
    
def handleError(ex):
    response = {}
    response['headers'] = {}
    response['statusCode'] = 502
    response['body'] = "Error: " + str(ex)
    return response
