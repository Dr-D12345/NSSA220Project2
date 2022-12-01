import re

def parse(fileName):
	packetList = []
	input = open(fileName, "r")
	totalLines = input.read().split("No.")
	for line in totalLines:
		if line != "":
			group = "No." +line
			#print(group)
			result = parseLine(group)
			if result!=[]:
				packetList.append(result)
	input.close()
	return packetList

def parseLine(line):
	info = line.split("\n")

	matches = re.finditer("(\d+)\s+(\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+)\s+(\d+)\s+(.*)", info[1])
	
	num = None
	for match in matches:
		num    = match.group(1)
		time   = match.group(2)
		ipSrc  = match.group(3)
		ipDes  = match.group(4)
		protcol= match.group(5)
		length = match.group(6)     
		extra   = match.group(7)
	if(num is None):
		return []
	"""
	Parsing for hex
	hexString = ""
		for x in range(2, len(info)):
		if info[x]!="":
			hexMatch = re.finditer("\d{4}\s+(\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+\s\w+)", info[x])
			for hexM in hexMatch:
				hexData = hexM.group(1)
				print(hexData.replace(" ",""))
				print(bytes.fromhex(hexData).decode('ASCII'))
				for hex in hexData.split(" "):
					hexString += chr(int("0x"+hex, 16))
	print(hexString)
	"""				

	return [num, time, ipSrc, ipDes, protcol, length, extra] 	