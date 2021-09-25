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
    if len(history) == 0: return json.dumps({"answer" : forward_guess(slots, values, history)})
    if len(history) == 1: return json.dumps({"answer": next_guess(slots, values, history, 0, 5)})
    if len(history) == 2:
        ans, counts, excludes = study_2(history, 0, 1)
        logging.info("ans", ans, counts, excludes)
        return json.dumps({"answer": next_guess(slots, values, history, 0, 6)})
    if len(history) == 3: return json.dumps({"answer": next_guess(slots, values, history, 1, 2)})
    if len(history) == 4: return json.dumps({"answer": next_guess(slots, values, history, 2, 3)})
    if len(history) == 5: return json.dumps({"answer": next_guess(slots, values, history, 3, 4)})
    if len(history) == 6: return json.dumps({"answer": next_guess(slots, values, history, 4, 5)})
    return json.dumps({"answer": ["w", "w", "w", "l", "l"]})

def study_2(h, _0, _1):
    history = reversed(h)
    ans = [0, 0, 0, 0, 0]
    counts = []
    excludes = []
    rw0, rr0 = list(str(history[_0]["result"])) if history[_0]["result"] >= 10 else [0, history[_0]["result"]]
    rw1, rr1 = list(str(history[_1]["result"])) if history[_0]["result"] >= 10 else [0, history[_0]["result"]]
    rw0, rr0, rw1, rr1 = [int(rw0), int(rr0), int(rw1), int(rr1)]
    if (rw0 < rw1): # old leave new come
        counts.append(history[_1]["output_received"][0])
        excludes.append(history[_0]["output_received"][0])
    elif (rw0 > rw1):
        counts.append(history[_0]["output_received"][0])
        excludes.append(history[_1]["output_received"][0])
    if (rr0 < rr1): # new is correct
        ans[0] = history[_1]["output_received"][0]
    elif (rr0 > rr1):
        ans[0] = history[_0]["output_received"][0]
    return ans, counts, excludes




def forward_guess(slots, values, history): # check right symbol in wrong / right position
    answer_list = []
    for x in range(slots):
        answer_list.append(values[x])
    logging.info("forward_guess:", "value:", values, "slots", slots, "history", history, "answer_list", answer_list)
    return answer_list

def next_guess(slots, values, history, old, new):
    answer_list = []
    for x in range(slots):
        answer_list.append(values[x])
    answer_list[old] = values[new]
    logging.info("forward_guess:", "value:", values, "slots", slots, "history", history, "answer_list", answer_list)
    return answer_list

def two_guess(slots, values, history, st, nd):
    a = values[st]
    b = values[nd]
    logging.info("2 guess:", "value:", values, "slots", slots, "history", history, "answer_list", [a,a,a,b,b])
    return [a,a,a,b,b]

def backward_guess(slots, values, history):
    answer_list = []
    r_values = values[::-1]
    for x in range(slots):
        answer_list.append(r_values[x])
    logging.info("backward guess", "value:", values, "slots", slots, "history", history, "answer_list", answer_list)
    return answer_list


