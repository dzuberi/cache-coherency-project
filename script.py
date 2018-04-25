#import os
#s = os.system("./procsim -r12 -f4 -j1 -k2 -l3 -p32 < traces/gcc.100k.trace ")
#print s;

import commands
#s = commands.getstatusoutput("./procsim -r12 -f4 -j1 -k2 -l3 -p32 < traces/gcc.100k.trace ")


def getRT(a):
	splitout = a[1].split('\n')
	line = ""
	#for i in reversed(range(1,6)):
		#line = line + splitout[len(splitout)-i]+"\n"
	line = splitout[len(splitout)-5]
	runtimestring = line.split(': ')[1].split(' ')
	runtimestring = runtimestring[len(runtimestring)-2]
	#ipcfloat = float(ipcstring[1])
	return int(runtimestring);
	#return line
#tracename = raw_input("insert trace name: ")
protocols = ["MESI","MOSI","MOESIF"]


for expnum in range(1,9):
	print "Experiment number: " + str(expnum) + "\n"
	for p in protocols:
		#print type(tracename)
		s = commands.getstatusoutput("./sim_trace -t traces/experiment"+str(expnum)+"/ -p "+p)
		print p + " " + str(getRT(s))
	print "\n"