import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluate_fixed_race():
    data = request.data
    lines = []
    racer_rank = {}
    ranking = []
    with open('./racer.txt') as f:
        lines = f.readlines()
    for line in lines:
        winner, racers =  line.split("|")
        winner = winner.strip()
        racers = racers.strip().split(", ")
        if winner not in racer_rank:
            racer_rank[winner] = []
        for (racer) in racers:
            if not racer in racer_rank[winner]:
                racer_rank[winner].append(racer)
    print(racer_rank)


    logging.info("data sent for evaluation {}".format(data))
    logging.info("My result :{}".format(data))
    return data



