
from flask import Blueprint
mod_ping = Blueprint('ping', __name__, url_prefix='/ping')

@mod_ping.route('/', methods=['GET'])
def ping():
    return "Ping called!"

