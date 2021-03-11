#!/usr/bin/python
import os
import time 
from ib_insync import *

def out():
	val = os.system('python txt.py')
def readtoarr():	
	sender = "StockWh8@wenhua"
	buy = "BPK"
	sell = "SPK"
	bnum=0
	snum=0
	name1 = ""
	name2 = "MSP"
	with open(r'final.txt','r',encoding='GB2312') as file:
		list = file.readlines() #读取所有行并返回列表
	arr = [x.strip() for x in list] #文本内容输出到txt
	file.close()
	#[买卖][id][合约名][发件人][日期]
		
	
	if arr[3] == sender:   #判断发件人是否正确
	#ES 201912#
		if arr[2] == name1: 
			if arr[0] == buy:  #检测为购买，查看是否为第一次购买，如果是，则创建文件，并购买，如果不是，直接购买*2
				#date = str(arr[4][0:8]) #只保留日期没有时间
				b = os.path.exists("bpk.txt")
				if  b == True:
					with open("bpk.txt",'r',encoding='GB2312') as file:
						list1 = file.readlines() #读取所有行并返回列表
					a = [x.strip() for x in list1]
					#a[0]=[买卖],a[1]=[id],a[2]=[购买次数]
				
					if a[1] == arr[1]:
						print("无新邮件")
					#id覆盖
					elif a[1] != arr[1]:
						file = open("bpk.txt",'w')#生成bpk的txt文件
						bnum = bnum + 2 
						file.write(arr[2]+"\n"+arr[1]+"\n"+str(bnum))
						file.close()
						val = os.system('python buy.py')#当天购买*2
						#val = os.system('python sell03.py')
						print("新的购买邮件")



					
				elif b == False:
				
					file = open("bpk.txt",'w')#生成的txt文件
					bnum = 1
					file.write(arr[2]+"\n"+arr[1]+"\n"+str(bnum))
					file.close()
					print("第一次购买邮件")
					val = os.system('python buy.py')
					#val = os.system('python sell03.py')
					##ib购买*1##
					
			if arr[0] == sell: #检测为出售，查看是否为当天第一次出售，如果是，则创建文件，并出售，如果不是，直接出售*2
				#date = str(arr[4][0:8]) #只保留日期没有时间
				s = os.path.exists("spk.txt")
				if  s == True:
					with open("spk.txt",'r',encoding='GB2312') as file:
						list1 = file.readlines() #读取所有行并返回列表
					sa = [x.strip() for x in list1]
					#a[0]=[买卖],a[1]=[id],a[2]=[购买次数]
				
					if sa[1] == arr[1]:
						print("无新邮件")
					#id覆盖
					elif sa[1] != arr[1]:
						file = open("spk.txt",'w')#生成spk的txt文件
						snum = snum + 2
						file.write(arr[2]+"\n"+arr[1]+"\n"+str(snum))
						file.close()
						print("新的卖出邮件")
						##ib出售*2##
						val = os.system('python sell.py')
						#val = os.system('python buy03.py')

					
				elif s == False:
					#stock = arr[2] 
					file = open("spk.txt",'w')#生成spk的txt文件
					snum = 1
					file.write(arr[2]+"\n"+arr[1]+"\n"+str(snum))
					file.close()
					print("第一次出售邮件")
					##ib出售*1##
					val = os.system('python sell.py') #第一次卖出*1
					#val = os.system('python buy03.py')
					
					#ES 201912#
					
					#ES 202003#
						
		if arr[2] == name2: 
			if arr[0] == buy:  #检测为购买，查看是否为第一次购买，如果是，则创建文件，并购买，如果不是，直接购买*2
				#date = str(arr[4][0:8]) #只保留日期没有时间
				b = os.path.exists("bpk03.txt")
				if  b == True:
					with open("bpk03.txt",'r',encoding='GB2312') as file:
						list1 = file.readlines() #读取所有行并返回列表
					a = [x.strip() for x in list1]
					#a[0]=[买卖],a[1]=[id],a[2]=[购买次数]
				
					if a[1] == arr[1]:
						print("无新邮件")
					#id覆盖
					elif a[1] != arr[1]:
						file = open("bpk03.txt",'w')#生成bpk的txt文件
						bnum = bnum + 2 
						file.write(arr[2]+"\n"+arr[1]+"\n"+str(bnum))
						file.close()
						val = os.system('python buy03.py')#当天购买*2
						#val = os.system('python sell03.py')
						print("新的购买邮件")



					
				elif b == False:
				
					file = open("bpk03.txt",'w')#生成的txt文件
					bnum = 1
					file.write(arr[2]+"\n"+arr[1]+"\n"+str(bnum))
					file.close()
					print("第一次购买邮件")
					val = os.system('python buy03.py')
					#val = os.system('python sell03.py')
					##ib购买*1##
					
			if arr[0] == sell: #检测为出售，查看是否为当天第一次出售，如果是，则创建文件，并出售，如果不是，直接出售*2
				#date = str(arr[4][0:8]) #只保留日期没有时间
				s = os.path.exists("spk03.txt")
				if  s == True:
					with open("spk03.txt",'r',encoding='GB2312') as file:
						list1 = file.readlines() #读取所有行并返回列表
					sa = [x.strip() for x in list1]
					#a[0]=[买卖],a[1]=[id],a[2]=[购买次数]
				
					if sa[1] == arr[1]:
						print("无新邮件")
					#id覆盖
					elif sa[1] != arr[1]:
						file = open("spk03.txt",'w')#生成spk的txt文件
						snum = snum + 2
						file.write(arr[2]+"\n"+arr[1]+"\n"+str(snum))
						file.close()
						print("新的卖出邮件")
						##ib出售*2##
						val = os.system('python sell03.py')
						#val = os.system('python buy03.py')

					
				elif s == False:
					#stock = arr[2] 
					file = open("spk03.txt",'w')#生成spk的txt文件
					snum = 1
					file.write(arr[2]+"\n"+arr[1]+"\n"+str(snum))
					file.close()
					print("第一次出售邮件")
					##ib出售*1##
					val = os.system('python sell03.py') #第一次卖出*1
					#val = os.system('python buy03.py')
				#ES 202003#'''	
	else:
		val = os.system('del final.txt')
		print("发件人错误")
		
if __name__ == "__main__":
	while True:
		out()
		readtoarr()
		time.sleep(60)