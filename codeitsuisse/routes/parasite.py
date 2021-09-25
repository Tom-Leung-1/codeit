import logging
import json

from flask import request, jsonify

from codeitsuisse import app
from collections import deque

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
    queue = deque()
    room, grid, interested_ind = [test_case['room'], test_case["grid"], test_case["interestedIndividuals"]]
    infect = [[ 0 if x == 3 else -1 for x in row] for row in grid]
    # print("infect_initial", infect)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 3:
                queue.append([row, col, 0])
                # infection(infect, grid, row, col, 0)
    bfs_infection(queue, grid, infect)
    p1_dict = {}
    # print("infect_final", infect)
    # print("grid", grid)
    for x in interested_ind:
        p1_dict[x] = get_ind(x, infect)
    p2 = get_time_A(infect, grid)
    return {"room": room, "p1" : p1_dict, "p2": p2, "p3": 0, "p4": 0}


def get_ind(x, infect):
    [row, col] = x.split(',')
    row = int(row)
    col = int(col)
    return -1 if infect[row][col] == 0 else infect[row][col]

def get_time_A(infect, grid):
    max_time = 0
    for row in range(len(infect)):
        for col in range(len(infect[0])):
            if infect[row][col] == -1 and grid[row][col] == 1:
                return -1
            max_time = max(infect[row][col], max_time)
    return max_time

def bfs_infection(queue, grid, infect):
    while len(queue):
        row, col, time = queue.popleft()
        if row - 1 >= 0 and (infect[row - 1][col] == -1 or time + 1 < infect[row - 1][col]) and grid[row - 1][col] == 1:
            # print("from", row, col, "to", row-1, col, "time", time+1)
            queue.append([row-1, col, time + 1])
            infect[row-1][col] = time + 1
        if row + 1 < len(grid) and (infect[row + 1][col] == -1 or time + 1 < infect[row + 1][col]) and grid[row + 1][col] == 1:
            # print("from", row, col, "to", row + 1, col, "time", time + 1)
            queue.append([row + 1, col, time + 1])
            infect[row + 1][col] = time + 1
        if col - 1 >= 0 and (infect[row][col - 1] == -1 or time + 1 < infect[row][col - 1]) and grid[row][col - 1] == 1:
            # print("from", row, col, "to", row, col - 1, "time", time + 1)
            queue.append([row, col - 1, time + 1])
            infect[row][col - 1] = time + 1
        if col + 1 < len(grid[0]) and (infect[row][col + 1] == -1 or time + 1 < infect[row][col + 1]) and grid[row][col + 1] == 1:
            # print("from", row, col, "to", row, col + 1, "time", time + 1)
            queue.append([row, col + 1, time + 1])
            infect[row][col + 1] = time + 1

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




