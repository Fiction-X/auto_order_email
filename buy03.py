#!/usr/bin/python

####ES 202003####

from ib_insync import *
import os

# util.startLoop()
b = os.path.exists("bpk03.txt")
if b == True:
	
	ib = IB()
	ib.connect('127.0.0.1', 7497, clientId=1)
	#ES 202003
	contract = Future('ES', '202003', 'GLOBEX')
	ib.qualifyContracts(contract)
	order = MarketOrder('BUY',2,transmit = True)
	trade = ib.placeOrder(contract, order)
	ib.sleep(30)
	if trade.orderStatus.status != "Filled":
		ib.cancelOrder(order)
		ib.sleep(2)
		contract = Future('ES', '202003', 'GLOBEX')
		ib.qualifyContracts(contract)
		order = MarketOrder('BUY',2,transmit = True)
		trade = ib.placeOrder(contract, order)
		if trade.orderStatus.status != "Filled":
			ib.sleep(30)
			print(trade.orderStatus.status)
	elif trade.orderStatus.status == "Filled":
		print("成交")
		print(trade.orderStatus.status)
		ib.disconnect()
	#ES 202003

elif b == False:
	file = open("bpk03.txt",'w')#生成bpk的txt文件
	ib = IB()
	ib.connect('127.0.0.1', 7497, clientId=1)
	####ES 202003####
	contract = Future('ES', '202003', 'GLOBEX')
	ib.qualifyContracts(contract)
	
	order = MarketOrder('BUY',1,transmit = True)
	trade = ib.placeOrder(contract, order)
	ib.sleep(30)
	if trade.orderStatus.status != "Filled":
		ib.cancelOrder(order)
		ib.sleep(2)
		contract = Future('ES', '202003', 'GLOBEX')
		ib.qualifyContracts(contract)
		order = MarketOrder('BUY',1,transmit = True)
		trade = ib.placeOrder(contract, order)
		
		if trade.orderStatus.status != "Filled":
			ib.sleep(30)
			print(trade.orderStatus.status)
	elif trade.orderStatus.status == "Filled":
		print("成交")
		print(trade.orderStatus.status)
		ib.disconnect()
####ES 202003####

