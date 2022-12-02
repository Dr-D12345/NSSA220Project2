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
	Rtt=0
	for item in L:
		if (item[2] == host):
			info = item[6].split()
			if (info[2] == 'request'):
				request_sent += 1
				request_bytes_sent += int(item[5])
				request_data_sent += (int(item[5])-42)
				request_time = float(item[1])
				i+=1
			elif (info[2] == 'reply'):
				replies_sent += 1
				Rtt += (float(item[1])-request_time)*1000
		elif (item[3] == host):
			info = item[6].split()
			if (info[2] == 'request'):
				request_received +=1
				request_bytes_received += int(item[5])
				request_data_received +=(int(item[5])-42)
				request_time = float(item[1])
				i+=1
			elif (info[2] == 'reply'):
				replies_received += 1
				Rtt += (float(item[1])-request_time)*1000
	
	Avg_Rtt=Rtt/float(i)
	print(Avg_Rtt)