from sys import argv
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8546"))
# w3 = Web3(Web3.IPCProvider("/tmp/geth.ipc"))
# w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io"))

with open('account_id', 'w') as id:
    id.write(argv[1])

print("set to " + argv[1], 'balanace ' + str(w3.eth.gethBalance(w3.eth.accounts[int(argv[1])]) / (10 ** 18)) + ' ether')