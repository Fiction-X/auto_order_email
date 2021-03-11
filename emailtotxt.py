#!/usr/bin/python
import os
import re

def txtout():
	val = os.system('python email111.py > main.txt')  #输出到txt
def delblock():
	
	ifn = r"main.txt"
	ofn = r"main_o.txt"
	infile = open(ifn, "r") #打开main文件
	outfile = open(ofn, "w") # 内容输出到main_o文件
	for line in infile: #按行读文件
		outfile.write(line.replace(' ', ''))
	infile.close() #文件关闭
	val = os.system('del main.txt')
	outfile.close()
	
def chosestring():
	file='main_o.txt'
	#关键字
	#买或卖，BPK/SPK
	w1='文华交易提示--信号'
	w2='发出'
	#id
	w3='Id'
	w4='\n'
	#合约名
	w5='合约名:'
	w6='主连周期:'
	#发件人
	w7='Web'
	w8='.com.cn'
	#日期
	w9='com>\nDate'
	w10='08:00'
	f=open(file,'r')
	buff=f.read()

	#buff=buff.replace('\n','')
	pat=re.compile(w1+'(.*?)'+w2,re.S)
	result=pat.findall(buff)
	
	pat1=re.compile(w3+'(.*?)'+w4,re.S)
	result1=pat1.findall(buff)
	
	pat2=re.compile(w5+'(.*?)'+w6,re.S)
	result2=pat2.findall(buff)
	

	pat3=re.compile(w7+'(.*?)'+w8,re.S)
	result3=pat3.findall(buff)
	
	pat4=re.compile(w9+'(.*?)'+w10,re.S)
	result4=pat4.findall(buff)
	print(result)
	print(result1)
	print(result2)
	print(result3)
	print(result4)
	#print(result+'\n'+result1+result2+result3)

if __name__ == "__main__":
	txtout()
	delblock()
	chosestring()