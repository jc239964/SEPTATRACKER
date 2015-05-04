# SEPTA JSON Parser for SEPTA Tracker

import json
import os
import pprint
import SeptaTracker
from tabulate import tabulate

SeptaTracker.pullSEPTA()

trains = open('SEPTA_current_trains.json').read()

breakout = json.loads(trains)

for i in breakout:
  x = str((i['trainno'], i['SOURCE'], i['nextstop'], i['dest'], i['late']))
  pprint.pformat(x, indent=1, width=80)
  pprint.pprint(x)
  

os.remove('SEPTA_Current_Trains.json')

SeptaTracker.pullSEPTA()