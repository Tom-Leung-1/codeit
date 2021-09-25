import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)
# import requests

@app.route('/tic-tac-toe', methods=['POST'])
def evaluate_tic():
    pass
    # data = request.get_json()
    # logging.info("data sent for evaluation {}".format(data))
    # id = data.get("batteId")
    # url = "https://cis2021-arena.herokuapp.com/tic-tac-toe/play/" + id
    # print(url)
    # response = requests.get(url)
    # x = requests.post(url, data={})
    # logging.info(response)
    # logging.info(x)
    # return json.dumps(response)


