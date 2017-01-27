#!/usr/bin/env python2
import commands,time

print 'Listing your Lan cards'
time.sleep(1)
print commands.getoutput('tcpdump -D')
Lan=raw_input('Lan Card Name>>>')
x=commands.getoutput('ifconfig' + Lan)
z=x.split('ether')[1]
a=z.split()[0]


y='your ip is' + a
print y













