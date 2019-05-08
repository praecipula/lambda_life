from controllers.controller import Controller


class Databases(Controller)

def draw_routes(dispatcher):
    dispatcher.route(Controller.GET, "/databases", self.list_domains)

def list_domains():
    client = boto3.client('sdb')
    client.list_domains()
