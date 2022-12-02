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
	Rtt=0.0
	reply_delay=0.0
	TTL='128'
	hops=0
	for x in range(0, len(L)):
		item = L[x]
		type = item[6]["type"].lower()
		requestHost = item[2]
		time_to_live = item[6]["ttl"]
		if(type == 'request'):
			if(requestHost == host):
				request_sent += 1
				request_bytes_sent += int(item[5])
				request_data_sent += (int(item[5])-42)
				request_time = float(item[1])
				if (time_to_live == TTL):
					hops+=1
					k+=1
				else:
					hops+=3
					k+=1
			else:
				request_received +=1
				request_bytes_received += int(item[5])
				request_data_received +=(int(item[5])-42)
				receive_time = float(item[1])
				if (time_to_live == TTL):
					hops+=1
					k+=1
				else:
					hops+=3
					k+=1
		elif(type == 'reply'):
			if(requestHost == host):
				replies_sent += 1
				reply_delay += (float(item[1]) - receive_time)*1000000
				j+=1
				if(time_to_live == TTL):
					hops+=1
					k+=1
				else:
					hops+=3
					k+=1
			else:
				replies_received +=1
				Rtt += (float(item[1])-request_time) *1000
				i+=1
				if(time_to_live == TTL):
					hops+=1
					k+=1
				else:
					hops+=3
					k+=1
	Avg_Rtt=Rtt/float(i)
	Avg_reply_delay = reply_delay/float(j)
	print(hops/k)
	