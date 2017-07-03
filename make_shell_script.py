import sys, os, string
data = []
fp = open('fasta_files.txt', 'r')
for line in fp:
	temp = str.split(line)
	if temp[0] not in data:
		data.append(temp[0])
fp.close

fpx = open('run_HMM.sh', 'w')
for name in data:
	temp_name = name[:-4]
	fpx.write('./superfamily.pl '+name+'\n')
	fpx.write('mv .ass '+temp_name+'.ass'+'\n')
	fpx.write('mv .html '+temp_name+'.html'+'\n')
fpx.close
