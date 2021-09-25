import logging
import json
import sseclient
import pprint
from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)
import requests

@app.route('/tic-tac-toe', methods=['POST'])
def evaluate_tic():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    id = data["battleId"]
    url = "https://cis2021-arena.herokuapp.com/tic-tac-toe/play/" + id
    headers = {'Accept': 'text/event-stream'}
    response = with_requests(url, headers)
    client = sseclient.SSEClient(response)
    for event in client.events():
        logging.info(event)
    # x = requests.post(url, data={})
    logging.info(response['data'])
    # logging.info(x)
    return json.dumps({})

def with_requests(url, headers):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True, headers=headers)

