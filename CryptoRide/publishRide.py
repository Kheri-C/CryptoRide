from web3 import Web3
import json
import os
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abiFile = open(os.path.dirname(__file__).replace("\\","/")+"/bin/CryptoRide.abi","r")
abi = json.loads(abiFile.read())
abiFile.close()
addressFile = open(os.path.dirname(__file__).replace("\\","/")+"/contractAddress.txt","r")
address = web3.toChecksumAddress(addressFile.read())

web3.eth.defaultAccount = web3.eth.accounts[0]
contract = web3.eth.contract(address = address, abi= abi)

print("ID:")
_id= int(input())
print("Starting time:")
fromTime = input()
print("Finish time:")
toTime = input()
print("Location:")
location = input()
print("Base cost:")
baseCost = int(input())
print("Bidding time (in seconds):")
biddingTime = int(input())
print("Available seats")
avSeats = int(input())
tx_hash = contract.functions.publishRide(_id,fromTime,toTime,location,baseCost,biddingTime,avSeats).transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print("Successful ride publishment!")