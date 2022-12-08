
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
moves = [ 'L', 'R']
@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"
@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    data=request.json

    # Assign user url to a variable
    url=data['_links']["self"] ["href"]

    #Assign user x, y coordinates, direction, hit satus and score to diff variables
    my_x= data['arena']['state'][url]['x']
    my_y= data['arena']['state'][url]['y']
    direc=data['arena']['state'][url]['direction']
    hit_stat=data['arena']['state'][url]['wasHit']
    my_score=data['arena']['state'][url]['score']
    # Assign Arena width and height to variables
    tot_width=data['arena']['dims'][0]
    tot_ht=data['arena']['dims'][1]
    print("For my url: {}, x coordinates: {}, y coordinates :{}, direction is : {}, hit status is: {}, score is :{}" .format(url,my_x,my_y,direc,hit_stat,my_score))
    for key,value in data['arena']['state'].items():
        if key==url:
           pass
        elif ((value['x']-my_x==3) and (direc=='E')) or ((value['y']-my_y==3) and (direc=='S')):
           move='T'
        elif ((value['x']-my_x== -3) and (value['direction']=='E')) or ((value['y']-my_y == -3) and (value['direction']=='S')):
           move = 'F'
        elif my_x == 0 and my_y == 0 and direc =='N':
           move = 'R'
        elif my_x !=0 and my_y == 0 and direc =='N':
           if my_x + 1 <= tot_width:
            move = 'R'
           else:
            move= 'L'
        elif my_x!=0 and my_y != 0 and direc =='S':
           if my_y+ 1 <= tot_ht:
            move = 'F'
           else:
            move= random.choice(moves)
        else:
            move='F'
        return move
   
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
