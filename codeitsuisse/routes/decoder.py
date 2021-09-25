import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluate_decoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    values, slots, history = [data["possible_values"], data["num_slots"], data["history"]]
    logging.info("value:", values, "slots", slots, "history", history)
    return json.dumps({})


