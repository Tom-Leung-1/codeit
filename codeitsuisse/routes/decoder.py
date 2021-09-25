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
    # return json.dumps({"answer" : backward_guess(slots, values, history)})
    # return json.dumps({"answer": backward_guess(slots, values, history)})
    return json.dumps({"answer": ["e", "o", "h", "l", "p"]})

def forward_guess(slots, values, history): # check right symbol in wrong / right position
    answer_list = []
    for x in range(slots):
        answer_list.append(values[x])
    logging.info("forward_guess:", "value:", values, "slots", slots, "history", history, "answer_list", answer_list)
    return answer_list

def backward_guess(slots, values, history):
    answer_list = []
    r_values = values[::-1]
    for x in range(slots):
        answer_list.append(r_values[x])
    logging.info("backward guess", "value:", values, "slots", slots, "history", history, "answer_list", answer_list)
    return answer_list


