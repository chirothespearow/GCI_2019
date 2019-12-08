import subprocess
a=(subprocess.check_output(["arp", "-a"])) #Runs argument in terminal
x=str(a,'utf-8')   #To convert it into string type, as subprocess returns byte stream
x.replace('/n',' ')
count=0
for i in x:
	if i=='?':
		count+=1
print(x)

print('Number of devices connected:',count)