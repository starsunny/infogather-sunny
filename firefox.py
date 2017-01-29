#!/usr/bin/env python2
import time,commands,webbrowser,urllib2
print "Welcome to Browser"
print "__________________"
time.sleep(1)
x=raw_input("Enter your word >> ")
time.sleep(1)
menu='''
     .______________________________________
     |                                      |
     | 	Enter 1 for search                  |
     |	Enter 2 for Image Search            |
     |	Enter 3 for Location search         |
     |	Enter 4 for Video Search            |
     |	Enter 5 for Download first 10 links |
     |	Enter 6 for Run Commands            |
     |______________________________________|
'''
x == command
print commands.getoutput(x)

print menu
ch=raw_input()
y=('https://www.google.co.in/search?q=' + x)
video=('https://www.google.co.in/search?q=' + x)

 
if ch == '1' : 
	 webbrowser.open_new_tab('https://www.google.co.in/search?q= ' + x)
elif ch == '2' :
	 webbrowser.open_new_tab(y + '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj6rNDM1-fRAhWIqY8KHTuGA9YQ_AUICCgB&biw=1366&bih=596')
elif ch == '3' :
         webbrowser.open_new_tab('https://www.google.co.in/maps?q=' + x)
elif ch == '4' :
	webbrowser.open_new_tab(video + '&biw=1366&bih=596&tbm=vid&source=lnms&sa=X&ved=0ahUKEwiG9rrf3efRAhUBvo8KHb0vB_UQ_AUICSgC')
elif ch == '5' :
	txt = urllib2.urlopen('https://www.google.co.in/search?q= ' + x).read()
	print txt	
	
else :
      	print "Please Enter any word"

