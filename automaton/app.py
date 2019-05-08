#! /usr/bin/env python

import boto3

from flask import Flask

app = Flask("Automaton")

#from controllers.ping import mod_ping
#app.register_blueprint(mod_ping)

@app.route('/')
def hello():
    return 'Hello\n'

if __name__ == "__main__":
    app.run(port=8090, debug=True)

#from controller.controller import Controller
#from controller.controller import Ping
#
#
#Ping().draw_routes()
#
#class Dispatcher(object):
#    class __Dispatcher:
#        def __init__(self):
#            self._routes = {}
#        def __str__(self):
#            return repr(self)
#
#        def route(self, verb, path, callback):
#            if not verb in self._routes:
#                self._routes[verb] = {}
#            self._routes[verb][path] = callback
#
#        def find_callback(method, path):
#            if not method in self._routes:
#                return None
#            if not path in self._routes[method]:
#                return None
#            return self._routes[method][path]
#
#
#        def dispatch(self, event, context):
#            cb = find_callback(event['httpMethod'], event['path'])
#            if cb is None:
#                return {'statusCode': 404, 'body': "Can't find that route"}
#            return cb(event)
#
#
#    instance = None
#
#    def __init__(self):
#        if not Dispatcher.instance:
#            Dispatcher.instance = Dispatcher.__Dispatcher()
#        return Dispatcher.instance
#    def __getattr__(self, name):
#        return getattr(self.instance, name)
#
#def list_domains():
#    client = boto3.client('sdb')
#    client.list_domains()
#
#def dispatch(event, context):
#    try:
#        return Dispatcher().dispatch(event, context)
#    except Exception as e:
#        return handleError(e)
#    
#def handleError(ex):
#    response = {}
#    response['headers'] = {}
#    response['statusCode'] = 502
#    response['body'] = "Error: " + str(ex)
#    return response
