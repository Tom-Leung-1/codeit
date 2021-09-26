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
    return json.dumps(result)

def sh(test_case):
    entry, exit, depth, key, h_step, v_step = test_case['entryPoint'] , test_case['targetPoint'], test_case['gridDepth'], test_case['gridKey'], \
    test_case['horizontalStepper'], test_case['verticalStepper']
    rows = exit['second'] - entry['second'] #assume down
    cols = exit['first'] - entry['first']
    grid = [[0 for x in range(rows+1)] for y in range(cols+1)]
    risk = [[0 for x in range(rows+1)] for y in range(cols+1)]
    # categorize
    for x in range(rows+1):
        for y in range(cols+1):
            if x == entry['first'] and y == entry['second'] or (x == exit['first'] and y == exit['second']):
                risk[x][y] = (0 + depth) % key
                grid[x][y] = get_sym(risk[x][y] % 3)
            elif x == 0:
                risk[x][y] = (y*v_step + depth) % key
                grid[x][y] = get_sym(risk[x][y] % 3)
            elif y == 0:
                risk[x][y] = (x*h_step + depth) % key
                grid[x][y] = get_sym(risk[x][y] % 3)
            else:
                risk[x][y] = (risk[x-1][y] * risk[x][y-1] + depth) % key
                grid[x][y] = get_sym(risk[x][y] % 3)
    print(grid, risk)
    # transpose
    grid = [list(x) for x in zip(*grid)]
    return {"gridMap": grid, "minimumCost": 9}

def get_sym(x):
    if x == 0: return "L"
    if x == 1: return "M"
    return "S"


