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
	avg_Rtt='{:.2f}'.format(rtt/float(i))
	request_throughput = '{:.1f}'.format(request_bytes_sent/rtt)
	request_goodput = '{:.1f}'.format(request_data_sent/rtt)
	avg_reply_delay = '{:.2f}'.format(reply_delay/float(j))
	avg_hops = '{:.2f}'.format(hops/k)
	metrics =[request_sent, request_received, replies_sent, replies_received, request_bytes_sent, request_bytes_received, request_data_sent, request_data_received, avg_Rtt, request_throughput, request_goodput, avg_reply_delay, avg_hops]
	
	return format(metrics)
def format(metrics):
	rows = []
	rows.append(["Echo Requests Sent", "Echo Requests Received", "Echo Replies Sent", "Echo Replies Received"])
	rows.append([str(metrics[0]), str(metrics[1]), str(metrics[2]), str(metrics[3])])
	rows.append(["Echo Request Bytes Sent (bytes)", "Echo Request Data Sent (bytes)"])
	rows.append([str(metrics[4]), str(metrics[6])])
	rows.append(["Echo Request Bytes Received (bytes)", "Echo Request Data Received (bytes)"])
	rows.append([str(metrics[5]), str(metrics[7])])
	rows.append([])
	rows.append(["Average RTT (milliseconds)", str(metrics[8])])
	rows.append(["Echo Request Throughput (kB/sec)", str(metrics[9])])
	rows.append(["Echo Request Goodput (kB/sec)", str(metrics[10])])
	rows.append(["Average Reply Delay (microseconds)", str(metrics[11])])
	rows.append(["Average Echo Request Hop Count", str(metrics[12])])
	rows.append([])
	return rows