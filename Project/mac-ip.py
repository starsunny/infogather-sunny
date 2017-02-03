#!/usr/bin/env python2
import commands,time

print 'Listing Your LAN Card Name'
print commands.getoutput('tcpdump -D')
Lan=raw_input('Type your LAN card name from above list >> ')
x=commands.getoutput('ifconfig  '+ Lan )
y=x.split('ether')[1]
mac_address=y.split()[0]
print 'mac_address'


x=commands.getoutput('ifconfig  '+ Lan )
y=x.split('inet')[1]
ip_address=y.split()[0]
print 'ip_address'


z='Your IP address is >> ' + ip_address
a='your Mac address is >> ' + mac_address
print z 
print '!!!!!!!!!!!!!!!!!!!!!!!!!'
print a

time.sleep(2)
print 'Going Back to Main Menu'
execfile('/root/Desktop/Project/menuStyle2.py')
