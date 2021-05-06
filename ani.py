import subprocess
import os


devices = subprocess.check_output(['netsh','wlan','show','network'])
  

devices = devices.decode('ascii')
devices= devices.replace("\r","")
  
#print(devices)

file=open('wifi.txt','w')
file.write(devices)
file.close()

file2=open('wifi.txt','r')

names=[]
authentication=[]
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

while 1:
    line=file2.readline()
    if not line:
        break
    x=line.split()
    #print(x)
    if 'SSID' in x:
        print(x[3])
        names.append(x[3])
    if 'Authentication' in x:
        print(x[2])
        authentication.append(x[2])

#print(names)
#print(Repeat(names))
evil=Repeat(names)
#print(len(evil))
if len(evil)==0:
    print("There are no Evil Twins")
else:
    print("This Access Point may be a Rogue Access Point and an Evil Twin-")
    print(evil[0])

print("Checking Authentication....")

file3=open('wifi.txt','r')
a=[]
c=0
print(names)

while 1:
    line=file3.readline()
    if not line:
        break
    x=line.split()
    if evil[0] in x:
        c=1
    c+=1

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

source = "ABABDBAAEDSBQEWBAFLSAFB"
print(list_duplicates_of(names, evil[0]))
dup=list_duplicates_of(names, evil[0])

if len(dup)!=0:
    print("There are access points with the same name...")
    print("Checking their authentication....")


print(authentication[dup[0]])
print(authentication[dup[1]])

if authentication[dup[0]]=='Open':
    print("Evil Twin "+evil[0])
elif authentication[dup[1]]=='Open':
    print("Evil Twin "+evil[0])
else:
    print("NO Evil Twins")