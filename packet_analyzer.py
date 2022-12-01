from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter("./captures/Node1.txt", "./Filtered1.txt") 
print(parse("./Filtered1.txt"))
compute()
