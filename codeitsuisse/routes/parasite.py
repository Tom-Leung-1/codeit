import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def evaluate_parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
        result.append(parasite(test_case))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def parasite(test_case):
    room, grid, interested_ind = [test_case['room'], test_case["grid"], test_case["interestedIndividuals"]]
    infect = [[ 0 if x == 3 else -1 for x in row] for row in grid]
    # print("infect_initial", infect)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if infect[row][col] == 0:
                infection(infect, grid, row, col, 0)
    p1_dict = {}
    # print("infect_final", infect)
    # print("grid", grid)
    for x in interested_ind:
        p1_dict[x] = get_ind(x, infect)
    return {"room": room, "p1" : p1_dict, "p2": 0, "p3": 0, "p4": 0}


def get_ind(x, infect):
    [row, col] = x.split(',')
    row = int(row)
    col = int(col)
    return -1 if infect[row][col] == 0 else infect[row][col]

def infection(infect, grid, row, col, time):
    # print("infect", row, col, time)
    infect[row][col] = time
    grid[row][col] = 3
    if row - 1 >= 0 and (infect[row - 1][col] == -1 or time < infect[row - 1][col]) and (grid[row - 1][col] == 1 or grid[row - 1][col] == 3):
        #print("from", row, col, "to", row-1, col, "time", time+1)
        infection(infect, grid, row - 1, col, time + 1)
    if row + 1 < len(grid) and (infect[row + 1][col] == -1 or time < infect[row + 1][col]) and (grid[row + 1][col] == 1 or grid[row + 1][col] == 3):
        #print("from", row, col, "to", row+1, col, "time", time+1)
        infection(infect, grid, row + 1, col, time + 1)
    if col - 1 >= 0 and (infect[row][col - 1] == -1 or time < infect[row][col - 1]) and (grid[row][col - 1] == 1 or grid[row][col - 1] == 3):
        #print("from", row, col, "to", row, col-1, "time", time+1)
        infection(infect, grid, row, col - 1, time + 1)
    if col + 1 < len(grid[0]) and (infect[row][col + 1] == -1 or time < infect[row][col + 1]) and (grid[row][col+1] == 1 or grid[row][col+1] == 3):
        #print("from", row, col, "to", row, col + 1, "time", time+1)
        infection(infect, grid, row, col + 1, time + 1)




