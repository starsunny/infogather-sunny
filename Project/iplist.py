#!/usr/bin/env python2
import os
import time
import commands
import webbrowser

print 'Gathering all ip address >>'
print 'Listing Your LAN Card Name'
print commands.getoutput('tcpdump -D')
Lan=raw_input('Type your LAN card name from above list >> ')
x=commands.getoutput('ifconfig  '+ Lan )
y=x.split('inet')[1]
ip_address=y.split()[0]
f=open('myip.txt','w')
f.write(ip_address)
f.close()

z='Your IP address of given Lan Card ' + Lan + ' is : ',ip_address
print z
f=open('myip.txt')
ip=f.read()
f.close()
list=range(255)[1:]
s=ip.split('.')[0:3]
y='.'.join(s)
iplistfinal=[]

for i in list :
	x=os.system('arping -I wlp2s0 '+s+'.'+str(i))
	if x == 0 :
	 	iplistfinal.append(y+'.'+str(i))
	else :
		print ""

print 'my ip list is given below !!'
print iplistfinal
