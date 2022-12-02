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
	j=0
	k=0
	rtt=0.0
	reply_delay=0.0
	hops=0
	for x in range(0, len(L)):
		item = L[x]
		type = item[6]["type"].lower()
		requestHost = item[2]
		if(type == 'request'):
			if(requestHost == host):
				request_sent += 1
				request_bytes_sent += int(item[5])
				request_data_sent += (int(item[5])-42)
				request_time = float(item[1])
				sent_ttl = int(item[6]["ttl"])
			else:
				request_received +=1
				request_bytes_received += int(item[5])
				request_data_received +=(int(item[5])-42)
				receive_time = float(item[1])
		elif(type == 'reply'):
			if(requestHost == host):
				replies_sent += 1
				reply_delay += (float(item[1]) - receive_time)*1000000
				j+=1
				
			else:
				replies_received +=1
				rtt += (float(item[1])-request_time) *1000
				i+=1
				if((sent_ttl-int(item[6]["ttl"]))==0):
					hops+=1
					k+=1
				else:
					hops+=3
					k+=1
	avg_Rtt=rtt/float(i)
	request_throughput = request_bytes_sent/rtt
	request_goodput = request_data_sent/rtt
	avg_reply_delay = reply_delay/float(j)
	avg_hops = hops/k	
	metrics =[request_sent, request_received, replies_sent, replies_received, request_bytes_sent, request_bytes_received, request_data_sent, request_data_received, avg_Rtt, request_throughput, request_goodput, avg_reply_delay, avg_hops]
	return metrics