
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)
app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"
@app.route("/", methods=['POST'])
def move():
    request.get_data()
    print("******** testing ************")
    logger.info(request.json)
    data=request.json
    url="https://cloud-run-hackathon-python-c5p6tue2hq-uc.a.run.app"
    x= data['arena']['state'][url]['x']
    y= data['arena']['state'][url]['y']
    direc=data['arena']['state'][url]['direction']
    hit_stat=data['arena']['state'][url]['wasHit']
    score=data['arena']['state'][url]['score']
    print("For my url: {}, x coordinates: {}, y coordinates :{}, direction is : {}, hit status is: {}, score is :{}" .format(url,x,y,direc,hit_stat,score))
    return  moves[random.randrange(len(moves))]
    # TODO add your implementation here to replace the random response
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))