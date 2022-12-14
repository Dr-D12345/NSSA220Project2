import re

def parse(fileName):
	packetList = []
	input = open(fileName, "r")
	totalLines = input.read().split("No.")
	for line in totalLines:
		if line != "":
			group = "No." +line
			result = parseLine(group)
			if result!=[]:
				packetList.append(result)
	input.close()
	return packetList
def parseInfo(info):
	matches = re.finditer("Echo \(ping\) (\w+)\s+id=(\w+), seq=(\d+\/\d+), ttl=(\d+) \(\w+ in (\d+)\)", info)
	ty = None
	for match in matches:
		ty   = match.group(1)
		id  = match.group(2)
		seq  = match.group(3)
		ttl  = match.group(4)
		idCorresponding = match.group(5)
	if (ty is None):
		return {}
	return { "type":ty, "id": id, "seq":seq, "ttl":ttl, "idCorresponding":idCorresponding}

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
	return [num, time, ipSrc, ipDes, protcol, length, parseInfo(extra)] 	

