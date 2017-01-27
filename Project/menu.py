#!/usr/bin/env python2

import time,os,sys,platform

print ""
print "           Welcome to my Information Gathering Tool       "
print "        _______________________________________________   "
print "        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   "
print ""
time.sleep(1)
print "        Loading...."
time.sleep(2)
x='''
	       :::::::::::::::::::::::::::::::::::::::::::::::::::::                  
               !                                                   !
               !  Enter 1 to Check your ip Address            >>   !
	       !                                                   !
               !  Enter 2 to Check your OS Name               >>   !
	       !                                                   !
               !  Enter 3 to Check your Mac Address with IP   >>   !
	       !                                                   !
               !  Enter 4 to Check your IP with OS            >>   !
	       !                                                   !
               !  Enter 5 to Scan Port and Service list       >>   !
	       !                                                   !
               !  Enter 6 to Scan for Particular Service      >>   !
	       !                                                   !
               !  Enter 7 to Change IP Address                >>   !
	       !                                                   !
               !  Enter 8 to Change Mac Address               >>   !
	       !                                                   !
               !  Enter 9 to NMAP Search Engine               >>   !
               !                                                   !
	       :::::::::::::::::::::::::::::::::::::::::::::::::::::  
'''

print (x)
print 'your Choice >>> '
ch=raw_input()

if ch == '1' :
	execfile('/root/Desktop/Project/1.py')
elif ch == '2' :
	execfile('/root/Desktop/Project/2.py')
elif ch == '3' :
	execfile('/root/Desktop/Project/3.py')
elif ch == '4' :
	execfile()
elif ch == '5' :
	execfile()
elif ch == '6' :
	execfile()
elif ch == '7' :
	execfile()
elif ch == '8' :
	execfile()
elif ch == '9' :
	execfile()
else :
 print 'Enter Valid Choice'


