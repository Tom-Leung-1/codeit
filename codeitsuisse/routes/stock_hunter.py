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
    risk = [list(x) for x in zip(*risk)]
    cost = get_smallest_cost(risk, exit)
    return {"gridMap": grid, "minimumCost": cost}

def get_smallest_cost(risk, exit):
    # dp
    dp = [[get_int(risk[x][y] % 3) for y in range(len(risk[0]))] for x in range(len(risk))]
    print(dp)
    for x in range(len(risk)):
        for y in range(len(risk[0])):
            if x == 0 and y == 0: dp[x][y] = 0
            elif x == 0:
                dp[x][y] = dp[x][y] + dp[x][y-1]
            elif y == 0:
                dp[x][y] = dp[x-1][y] + dp[x][y]
            else:
                dp[x][y] = min(dp[x][y] + dp[x-1][y], dp[x][y] + dp[x][y-1])
    print(dp)
    return dp[exit["first"]][exit["second"]]

def get_sym(x):
    if x == 0: return "L"
    if x == 1: return "M"
    return "S"

def get_int(x):
    if x == 0: return 3
    if x == 1: return 2
    return 1


