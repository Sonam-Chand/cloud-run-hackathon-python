
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
moves = [ 'L','T','R','F']
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


    # Assign Arena width and height to variables
    tot_width=data['arena']['dims'][0]
    tot_ht=data['arena']['dims'][1]
    

    # Create two lists for x values,y values , directions for all the players except you
    xlist=[]
    ylist=[]
    player_direc=[]
    for key,value in data['arena']['state'].items():
        if key==url:
           #Assign user x, y coordinates, direction, hit satus and score to diff variables 
            my_x= data['arena']['state'][url]['x']
            my_y= data['arena']['state'][url]['y']
            direc=data['arena']['state'][url]['direction']
            hit_stat=data['arena']['state'][url]['wasHit']
            my_score=data['arena']['state'][url]['score']
            print("For my url: {}, x coordinates: {}, y coordinates :{}, direction is : {}, hit status is: {}, score is :{}" .format(url,my_x,my_y,direc,hit_stat,my_score))
        else:
            xlist.append(value['x'])
            ylist.append(value['y'])
            player_direc.append(value['direction'])
    j=0
    k=0
    for i in range(0,len(xlist)):
        j=i
        k=i
        print"********* to test*********")
        if ((xlist[i]-my_x==3) and (direc=='E')) or ((ylist[j]-my_y==3) and (direc=='S')):
            return 'T'
        elif ((xlist[i]-my_x== -3) and (player_direc[k]=='E')) or ((ylist[j]-my_y == -3) and (player_direc[k]=='S')):
            return 'F'
        elif (my_x==0 and my_y==0) and (direc == 'N' or direc == 'W'):
	        return 'R'
        elif (my_x==tot_width and my_y==0) and (direc == 'N' or direc == 'E'):
	        return 'L'
        elif (my_x==0 and my_y==tot_ht) and (direc == 'S' or direc == 'W') :
	        return  'R'
        elif (my_x==tot_width and my_y==tot_ht) and (direc == 'S' or direc == 'E'):
	        return 'L'
        else:
            return random.choice(moves)
            
      
   
if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
