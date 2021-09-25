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
    return json.dumps({"answer" : random_guess(slots, values, history)})

def random_guess(slots, values, history): # check right symbol in wrong / right position
    answer_list = []
    for x in range(slots):
        answer_list.append(values[x])
    logging.info("value:", values, "slots", slots, "history", history)
    logging.info("answer_list", answer_list)
    return answer_list


