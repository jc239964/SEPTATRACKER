# SEPTA Tracker -- Pulls information on current train locations 
# from SEPTA website

import urllib

def pullSEPTA():
  septaFile = 'SEPTA_Current_Trains.json'	
  SEPTA_raw = urllib.urlopen("http://www3.septa.org/hackathon/TrainView/")
  SEPTA_data = SEPTA_raw.read()
  update = open(septaFile, 'wbr')
  update.write(SEPTA_data)
  update.close()
