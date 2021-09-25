import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluate_asteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = []
    for test_case in data["test_cases"]:
        result.append(asteroid(test_case))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def asteroid(str):
    # possible origins
    i = 0
    ch = None
    mid_pts = []
    while i < len(str):
        if ch is None or ch != str[i]:
            ch = str[i]
            r = i + 1
            while r < len(str):
                if str[r] != ch: break
                r += 1
            mid_pts.append((i + r-1) //2)
            i = r
    # return optimal point, assume asteroid length > 3
    score = 0
    final_origin = None
    for origin in mid_pts:
        sum = 0
        l = origin-1
        r = origin+1
        #1st asteroid
        while l >= 0 and r < len(str) and str[origin] == str[l] == str[r]:
            l -= 1
            r += 1
        dist = r - l - 1
        sum += multiplier(dist)
        # others
        while l >= 0 and r < len(str) and str[l] == str[r]:
            more_l = l - 1
            while more_l >= 0 and str[more_l] == str[l]:
                more_l -= 1
            more_r = r + 1
            while more_r < len(str) and str[more_r] == str[r]:
                more_r += 1
            dist = (l - more_l + more_r - r)
            l = more_l
            r = more_r
            sum += multiplier(dist)
        if score < sum:
            score = sum
            final_origin = origin
    return {"input" : str, "score" : score, "origin" : final_origin}

def multiplier(dist):
    if 7 <= dist <= 9: return dist * 1.5
    if dist >= 10: return dist * 2
    return dist



