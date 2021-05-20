import subprocess

host="10.0.0."

for item in range(1,138):
    newHost= host + str(item)
    result = subprocess.call('ping','-c','3',newHost)
    if result ==0 :
        print("the host is running ",host)
    else:
        print("no response",host)