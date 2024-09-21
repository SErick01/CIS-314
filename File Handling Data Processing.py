"""
Author: Samantha Erickson
Date:   09-21-2024
"""
import re

dataList, addressList = [], []
x, y = 0, 0
ipPattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')


fileIn = open("access.log")
dataList = fileIn.readlines()
fileIn.close()
while x < len(dataList):
    x += 1
print("Log entries with 'BotPoke' is", x)


while y < len(dataList):
    if dataList[y].find("BotPoke") > 0:
        dataList.pop(y)
    else:
        y += 1
print("Log entries without 'BotPoke' is", y)


for z in dataList:
    addressList.append(ipPattern.search(z)[0])
print("\nList of all IP addresses\n", addressList)


addressList = list(set(addressList))
print("\nList of only unique IP addresses\n", addressList)