def compute(host, L) :
	request_sent = 0
	request_bytes_sent=0
	request_data_sent=0
	request_received = 0
	request_bytes_received=0
	request_data_received=0
	replies_sent =0
	replies_received=0
	i=0
	Rtt=0.0
	"""	
	for item in L:
		type = item[6]["type"]
		if (item[2] == host):
			if (type == 'request'):
				request_sent += 1
				request_bytes_sent += int(item[5])
				request_data_sent += (int(item[5])-42)
				request_time = float(item[1])
				i+=1
			elif (type == 'reply'):
				replies_sent += 1
				Rtt += (float(item[1])-request_time)*1000
		elif (item[3] == host):
			if (type == 'request'):
				request_received +=1
				request_bytes_received += int(item[5])
				request_data_received +=(int(item[5])-42)
				request_time = float(item[1])
				i+=1
			elif (type == 'reply'):
				replies_received += 1
				Rtt += (float(item[1])-request_time)*1000
	"""
	i=0
	request_time =0
	for x in range(0, len(L)):
		item = L[x]
		type = item[6]["type"].lower()
		requestHost = item[2]
		
		if(type == 'request'):
			if(requestHost == host):
				request_sent += 1
				request_time = float(item[1])
			else:
				request_received +=1
			request_bytes_sent += int(item[5])
			request_data_sent += (int(item[5])-42)
		elif(type == 'reply'):
			if(requestHost == host):
				replies_sent += 1
			else:
				replies_received +=1
				Rtt += (float(item[1])-request_time) *1000
				i+=1
	Avg_Rtt=Rtt/float(i)
	print(Avg_Rtt)