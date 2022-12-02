from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter("./captures/Node1.txt", "./Filtered1.txt") 
L = parse("./Filtered1.txt")
compute('192.168.100.1', L)
#print(L)
