#!/usr/bin/python
import os
import time  
from ib_insync import *

def out():
	val = os.system('python emailtotxt.py > finally.txt')  #输出到txt
	
def txtdel():
	ifn = r"finally.txt"
	ofn = r"final.txt"
	infile = open(ifn, "r") #打开finally文件
	outfile = open(ofn, "w") # 内容输出到final文件
	for line in infile: #按行读文件
		outfile.write(line.replace('[', '').replace(']', '').replace("'", "").replace("+", "").replace("-", "").replace(":", "")) #替换掉[]'+-符号
	infile.close() #文件关闭
	val = os.system('del finally.txt') 
	outfile.close()


if __name__ == "__main__":
	out()
	txtdel()
