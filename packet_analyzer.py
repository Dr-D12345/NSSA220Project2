from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter("./captures/Node1.txt", "./Filtered1.txt")
filter("./captures/Node2.txt", "./Filtered2.txt")
filter("./captures/Node3.txt", "./Filtered3.txt")
filter("./captures/Node4.txt", "./Filtered4.txt")  
parsed1 = parse("./Filtered1.txt")
parsed2 = parse("./Filtered2.txt")
parsed3 = parse("./Filtered3.txt")
parsed4 = parse("./Filtered4.txt")
compute('192.168.100.1', parsed1)
#print(L)
