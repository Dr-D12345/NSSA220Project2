from filter_packets import *
from packet_parser import *
from compute_metrics import *
import csv
final_results = []
node_ip = ["192.168.100.1","192.168.100.2","192.168.200.1","192.168.200.2"]
output = open("output.csv", 'w', encoding='UTF8', newline='')
writer= csv.writer(output)
for i in range(1, 5):
    writer.writerow(["Node "+str(i)])
    writer.writerow([])
    filter("./captures/Node" + str(i) + ".txt", "./Node"+str(i)+"_filtered.txt")
    parsed = parse("./Node"+str(i)+"_filtered.txt")
    results = compute(node_ip[i-1], parsed)
    writer.writerows(results)
output.close()
