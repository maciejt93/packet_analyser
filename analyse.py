from scapy.all import *
import os

path = "/home/krol/Desktop/tcpdump_app/pocket_analyse/dumps"
dir_list = os.listdir(path)
pcap = rdpcap("dumps/vuclip_test_1.pcap")

def ip_gen(pcap):
	ip_list = []
	for p in pcap:
		if TCP in p:
			ans = p.sprintf("{IP:%IP.src%,%IP.dst%\n}")
			if ans:
				ans = ans.strip()
				ans = ans.split(',')
				ip_list.append(ans[0])
				ip_list.append(ans[1])
	return ip_list


whole_data_set = []

for i in dir_list:
	pcap = rdpcap("dumps/" + i)
	ip_list = ip_gen(pcap)
	print("file: ", i)
	print("ip list: ", len(ip_list))
	ip_set = list(set(ip_list))
	whole_data_set = whole_data_set + ip_set
	print("set of ip list", len(ip_set))
print("whole data set: ", len(whole_data_set))