
import sys
from easysnmp import Session

if len(sys.argv) != 3:
    print("Usage: {} community_string ip_address".format(sys.argv[0]))
    sys.exit(1)

community_string = sys.argv[1]
ip_address = sys.argv[2]

s = Session(hostname=ip_address, community=community_string, version=2, use_numeric = True ,use_sprint_value = True)

print("{:<20}\t{:<20}\t{:<20}\t{:<20}".format("IP Address","MAC Address","Interface","Mapping Type"))
print("{:<20}\t{:<20}\t{:<20}\t{:<20}".format("----------","-----------------","----------------","-------"))
MAC = []
ip = []
Mapping = []
interface =[]
i = counter =  0
r = s.get_next('1.3.6.1.2.1.4.35.1.4')
intfName = '.1.3.6.1.2.1.2.2.1.2.'

while r.oid[20] == '4':
	mac_address = [index_str.zfill(2) for index_str in r.value.split(":")]
	MAC.append(":".join(mac_address))
	ip.append((r.oid[28::]+ '.' +r.oid_index))
	r = s.get_next(r.oid[1::] + '.' + r.oid_index)
	i += 1
	counter = i	
i = 0
while i != counter:
    tmp = s.get(intfName+r.oid[22])
    interface.append(tmp.value)
    r = s.get_next(r.oid[1::] + '.' + r.oid_index)
    i += 1
r = s.get_next('1.3.6.1.2.1.4.35.1.6')
while r.oid[20] == '6':
    Mapping.append(r.value)
    r = s.get_next(r.oid[1::] + '.' + r.oid_index)
 
for x in range(counter):
     print("{:<20}\t{:<20}\t{:<20}\t{:<20}".format(ip[x],MAC[x],interface[x],Mapping[x]))