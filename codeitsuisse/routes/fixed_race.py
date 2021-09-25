import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluate_fixed_race():
    data = request.data
    logging.info("data sent for evaluation {}".format(data))
    logging.info("My result :{}".format(data))
    return json.dumps(data)



