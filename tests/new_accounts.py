from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8546"))
# w3 = Web3(Web3.IPCProvider("/tmp/geth.ipc"))
# w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io"))

from sys import argv
for i in range(int(argv[1])):
    address = w3.personal.newAccount("")
    w3.eth.sendTransaction({'from':w3.eth.accounts[0], 'to': address, 'value': 100 * 10 **18, 'gas': 4 * 10 **6})
    print(address, "100 ether")