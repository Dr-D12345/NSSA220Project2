from filter_packets import *
from packet_parser import *
from compute_metrics import *
import csv
filter("./captures/Node1.txt", "./Filtered1.txt")
filter("./captures/Node2.txt", "./Filtered2.txt")
filter("./captures/Node3.txt", "./Filtered3.txt")
filter("./captures/Node4.txt", "./Filtered4.txt")  
parsed1 = parse("./Filtered1.txt")
parsed2 = parse("./Filtered2.txt")
parsed3 = parse("./Filtered3.txt")
parsed4 = parse("./Filtered4.txt")
results1 = compute('192.168.100.1', parsed1)
#print(L)
output = open("output.csv", 'w', encoding='UTF8', newline='')
rows=[["Echo Request Sent", "Echo Request Recieved", "Echo Replies Sent", "Echo Replies Recieved"], [str(results1[0]), str(results1[1]), str(results1[2]), str(results1[3])], ["Echo Request bytes Sent (bytes)", "Echo Request Data Sent (bytes)"], [str(results1[4]), str(results1[6])], ["Echo Request Bytes Recieved", "Echo Request Data Recieved (bytes)"], [str(results1[5]), str(results1[7])], [""], ["Average RTT (milliseconds)", str(results1[8])],  ["Echo Request Throughput (kB/sec)", str(results1[9])], ["Echo Request Goodput (kB/sec)", str(results1[10])], ["Average Reply Delay (microseconds)", str(results1[11])], ["Average Echo Request Hop Count", str(results1[12])], [""]]
writer= csv.writer(output)
writer.writerow("Node 1")
writer.writerow()
writer.writerows(rows)
output.close()
