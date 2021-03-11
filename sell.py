#!/usr/bin/python

####ES 201912####

from ib_insync import *
import os

# util.startLoop()
b = os.path.exists("spk.txt")
if b == True:

	ib = IB()
	ib.connect('127.0.0.1', 7497, clientId=1)
	####ES 201912####
	contract = Future('ES', '201912', 'GLOBEX')
	ib.qualifyContracts(contract)
	#order=MarketOrder('SELL', 1)
	order = MarketOrder('SELL',2,transmit = True)
	trade = ib.placeOrder(contract, order)
	ib.sleep(30)
	if trade.orderStatus.status != "Filled":
		ib.cancelOrder(order)
		ib.sleep(2)
		contract = Future('ES', '201912', 'GLOBEX')
		ib.qualifyContracts(contract)
		order = MarketOrder('SELL',2,transmit = True)
		trade = ib.placeOrder(contract, order)
		if trade.orderStatus.status != "Filled":
			ib.sleep(30)
			print(trade.orderStatus.status)
	elif trade.orderStatus.status == "Filled":
		print("成交")
		print(trade.orderStatus.status)
		ib.disconnect()
	####ES 201912####
	
	####ES 202003####
	'''contract1 = Future('ES', '202003', 'GLOBEX')
	ib.qualifyContracts(contract1)
	#order1=MarketOrder('BUY', 1)
	order1 = MarketOrder('BUY',1,transmit = True)
	trade = ib.placeOrder(contract1, order1)
	ib.sleep(30)
	if trade.orderStatus.status != "Filled":
		ib.cancelOrder(order1)
		ib.sleep(2)
		contract1 = Future('ES', '202003', 'GLOBEX')
		ib.qualifyContracts(contract1)
		order1 = MarketOrder('BUY',1,transmit = True)
		trade = ib.placeOrder(contract1, order1)
		if trade.orderStatus.status != "Filled":
			ib.sleep(30)
			print(trade.orderStatus.status)
			
	elif trade.orderStatus.status == "Filled":
		print("03成交")
		print(trade.orderStatus.status)
	####ES 202003####
	'''
	
elif b == False:
	file = open("spk.txt",'w')#生成spk的txt文件
	ib = IB()
	ib.connect('127.0.0.1', 7497, clientId=1)
	####ES 201912####
	contract = Future('ES', '201912', 'GLOBEX')
	ib.qualifyContracts(contract)
	#order=MarketOrder('SELL', 1)
	order = MarketOrder('SELL',1,transmit = True)
	trade = ib.placeOrder(contract, order)
	ib.sleep(30)
	if trade.orderStatus.status != "Filled":
		ib.cancelOrder(order)
		ib.sleep(2)
		contract = Future('ES', '201912', 'GLOBEX')
		ib.qualifyContracts(contract)
		order = MarketOrder('SELL',1,transmit = True)
		trade = ib.placeOrder(contract, order)
		if trade.orderStatus.status != "Filled":
			ib.sleep(30)
			print(trade.orderStatus.status)
	elif trade.orderStatus.status == "Filled":
		print("成交")
		print(trade.orderStatus.status)
		ib.disconnect()
	####ES 201912####
	
'''	####ES 202003####
	contract1 = Future('ES', '202003', 'GLOBEX')
	ib.qualifyContracts(contract1)
	#order1=MarketOrder('BUY', 1)
	order1 = MarketOrder('BUY',1,transmit = True)
	trade = ib.placeOrder(contract1, order1)
	ib.sleep(30)
	if trade.orderStatus.status != "Filled":
		ib.cancelOrder(order1)
		ib.sleep(2)
		contract1 = Future('ES', '202003', 'GLOBEX')
		ib.qualifyContracts(contract1)
		order1 = MarketOrder('BUY',1,transmit = True)
		trade = ib.placeOrder(contract1, order1)
		if trade.orderStatus.status != "Filled":
			ib.sleep(30)
			print(trade.orderStatus.status)
	elif trade.orderStatus.status == "Filled":
		print("03成交")
		print(trade.orderStatus.status)
		ib.disconnect()
	####ES 201912####
'''