#Constants (Modify these to match your own settings)
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
   checkBatteryLevel = True
   logData = True
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
   while True :                  #Endless loop
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

################## CHECKING FOR BATTERY LEVELS
                  if batteryLevel <= lowLevelBattery and battery Level > warningLevelBattery and lowOnWarning == True:
                     w = warningLevel.warningCheck()
                     w.monthlyReport()
                     w.warningMessage75()
                     print("Check battery")
                     lowOnWarning = False
                  if batteryLevel > lowLevelBattery and lowOnWarning == False:
                     lowOnWarning = True

                  if batteryLevel <= warningLevelBattery and battery Level > dangerLevelBattery and onWarning == True:
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
################## CHECKING FOR BATTERY LEVELS

               if key == 'BATTV':
                  key = 'Battery Voltage'

               finalValues = (key + ": " + val)
               print(finalValues)
               finalList.insert(0, finalValues + "\n")
      finalString = ''.join(finalList)
      # txt_file = open("batteryLogData.txt", "w")
      # txt_file.write(finalString + "\n")
      # txt_file.close()      

      counter = counter + 1
      print(counter) 
      if counter > 30:
         counter = 0
         # print("Hello world")
         m = monthlyReport.monthlyCheck()
         m.monthlyReport()
         # m.exportInfo()
         finalList = []

      else:
         with open("batteryLogData.txt", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(finalString + "\n")
            finalString = None 
            # print(finalList)

      time.sleep(86400) #Take one day break in between the loops

#Main Loop
apc_probe()