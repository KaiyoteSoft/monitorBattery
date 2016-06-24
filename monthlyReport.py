def monthlyReport():
	with open("batteryLogData.txt", 'r') as myFile:
		data = myFile.read()
		print (data)
	open("batteryLogData.txt", 'w').close()