#Constants (Modify these to match your own settings)
import warningLevel
import monthlyReport
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
   onWarning = True
   warningLevelBattery = 50
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
                  # print(onWarning)
                  # print(batteryLevel)
                  # print(warningLevelBattery)
                  if batteryLevel <= warningLevelBattery and onWarning == True:
                     warningLevel.warningMessage()
                     print("Check battery")
                     onWarning = False
                  if batteryLevel > warningLevelBattery and onWarning == False:
                     onWarning = True

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
      if counter > 3:
         counter = 0
         monthlyReport.monthlyReport()

      else:
         with open("batteryLogData.txt", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(finalString + "\n")
            finalString = None 
            del finalList[:]

      time.sleep(2) #Take a 5 second break

#Main Loop
apc_probe()
