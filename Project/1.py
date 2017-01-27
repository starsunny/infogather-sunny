#!/usr/bin/env python2
import os,sys,platform,time,commands
print("")
print '3'
time.sleep(1)
print '2'
time.sleep(1)
print '1'
time.sleep(1)
print 'Loading...'
time.sleep(1)
print 'Listing Your LAN Card Name'
print commands.getoutput('tcpdump -D')
Lan=raw_input('Type your LAN card name from above list >> ')
x=commands.getoutput('ifconfig  '+ Lan )
y=x.split('inet')[1]
ip_address=y.split()[0]

z='Your IP address of given Lan Card ' + Lan + ' is : ',ip_address
print z
time.sleep(3)
print 'Going Back to Main Menu'
execfile('/root/Desktop/Project/menuStyle2.py')





