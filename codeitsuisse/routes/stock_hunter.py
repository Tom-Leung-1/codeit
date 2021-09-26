import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stock-hunter', methods=['POST'])
def evaluate_sh():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result =[]
    for test_case in data:
        result.append(sh(test_case))
    logging.info("My result :{}".format(result))
    return json.dumps({})

def sh(test_case):
    entry, exit, depth, key, h_step, v_step = test_case['entryPoint'] , test_case['targetPoint'], test_case['gridDepth'], test_case['gridKey'], \
    test_case['horizontalStepper'], test_case['verticalStepper']
    rows = exit['second'] - entry['second'] #assume down
    cols = exit['first'] - entry['first']
    grid = [[0 for x in range(rows)] for y in range(cols)]
    # categorize
    return {"gridMap": grid, "minimumCost": 9}




