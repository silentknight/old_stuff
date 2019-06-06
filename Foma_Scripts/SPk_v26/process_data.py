#/usr/bin/python
import os
import random
import time
import re

def main():
	dirPath = "/mnt/data/SP_v26_Data"

	# lang = "SP2"
	# lang = "SP4"
	# lang = "SP6"
	# lang = "SP8"
	lang = "SP10"
	datasets = [[60,100]]

	for dr in datasets:
		data = []
		for i in range(dr[0],dr[1]+1):
			filename = lang+"_"+str(i)+".dat"
			print(filename)
			path = os.path.join(dirPath,lang,filename)
			try:
				f = open(path,"r")
				data += f.readlines()[2:]
				f.close()
			except TypeError as e:
				print(e)
			except FileNotFoundError as e:
		 		print(e)

		random.shuffle(data)
		data = ''.join(data)
		data = re.sub(r'([[1-9])\w+', '', data)
		data = data.replace('] ','')

		f = open(os.path.join(dirPath, lang, "Data_"+lang+"_"+str(dr[1])+".dat"),"w")
		f.write(data)
		f.close()

if __name__ == '__main__':
	main()