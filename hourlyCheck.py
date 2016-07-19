#!/usr/bin/python
#Constants (Modify these to match your own settings)
import subprocess   #For OS calls
import time
import requests      #For URL calls
import monthlyReport 
import warningLevel
import shutil
import os

APCACCESS   = "/sbin/apcaccess"         #Location of apcaccess program
# LINEV      = "40"                     #Idx for Line Voltage
# LOADPCT      = "45"                     #Idx for Load Percentage
BATTV      = "44"                     #Idx for Battery Voltage
BCHARGE      = "46"                     #Idx for Battery Charge
STATUS = "47"
DATE = "48"
MINBATT = 10                     #Shut down when battery power is at 10%
finalList = []
#Variables

def apc_probe():
   finalList = []
   logData = 85
   lowOnWarning = True
   lowLevelBattery = 75
   onWarning = True
   warningLevelBattery = 50
   dangerOnWarning = True
   dangerLevelBattery = 20   
   counter = 0
   batt = 100   #Needs to be >MINBATT to not do a false processor stop
   # dict = {'LINEV' : LINEV, 'BATTV' : BATTV, 'LOADPCT' : LOADPCT, 'BCHARGE' : BCHARGE}
   dict = {'BCHARGE' : BCHARGE, 'BATTV' : BATTV, 'STATUS' : STATUS, 'DATE' : DATE}

   res = subprocess.check_output(APCACCESS)
   print("---------")
   finalList.insert(0, "-------------" + "\n")
   for line in res.split('\n') :
      (key,spl,val) = line.partition(': ')
      key = key.rstrip()         #Strip spaces right of text
      val = val.strip()         #Remove outside spaces
      # val = val.split(' ',1)[0]    #Split using space and only take first part
      # print(val)
      if key in dict :          #Are we interested in this parameter?
            if key == 'DATE':
               val = val.split('+',1)[0]

            if key == 'BCHARGE':
               key = 'Battery Charge'
               batteryLevel = val.split(' ',1)[0]
               batteryLevel = float(batteryLevel)
               batteryLevel = int(batteryLevel)

            if key == 'BATTV':
               key = 'Battery Voltage'

            finalValues = (key + ": " + val)
            print(finalValues)
            finalList.insert(0, finalValues + "\n")
   finalString = ''.join(finalList)     

   if batteryLevel <= logData:
      with open("batteryLogData.txt", 'a+') as f:
         content = f.read()
         f.seek(0, 0)
         f.write(finalString + "\n")
         finalString = None 

#################### CHECKING FOR BATTERY LEVELS
   if batteryLevel <= lowLevelBattery and batteryLevel > warningLevelBattery and lowOnWarning == True:
      w = warningLevel.warningCheck()
      w.monthlyReport()
      w.warningMessage75()
      print("Check battery")
      lowOnWarning = False
   if batteryLevel > lowLevelBattery and lowOnWarning == False:
      lowOnWarning = True

   if batteryLevel <= warningLevelBattery and batteryLevel > dangerLevelBattery and onWarning == True:
      w = warningLevel.warningCheck()
      w.monthlyReport()
      w.warningMessage()
      print("Check battery")
      onWarning = False
   if batteryLevel > warningLevelBattery and onWarning == False:
      onWarning = True

   if batteryLevel <= dangerLevelBattery and dangerOnWarning == True:
      w = warningLevel.warningCheck()
      w.monthlyReport()
      w.warningMessage20()
      print("Check battery")
      dangerOnWarning = False
   if batteryLevel > dangerLevelBattery and dangerOnWarning == False:
      dangerOnWarning = True
#################### CHECKING FOR BATTERY LEVELS


#Main Loop
apc_probe()