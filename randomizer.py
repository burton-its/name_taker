import random
import re

seq = open("file.txt","r")
fout =  open("rrandom.txt","w+")
seq2 = seq.readlines()

res = re.findall(r"B\w+",str(seq2))
simul={}
i=0
while i <= 10:
	nums = random.sample(res,k=15)
	simul[i] = nums
	line = str(i) + " " + " ".join(nums) + "\n"
	fout.write(line)	
	i+=1
