from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8546"))
# w3 = Web3(Web3.IPCProvider("/tmp/geth.ipc"))
# w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io"))
switch_acc = 'set_acc.py '
new_accounts = 'new_accounts.py '

from subprocess import check_output
from shlex import split

def switch(id):
    execute(switch_acc + str(id))

def newAccounts(num):
    execute(new_accounts + str(num))

def execute(comand):
    print("******")
    print("******")
    return check_output(['python3'] + split(comand)).rstrip(b'\n').decode('utf-8')

def check(comand, result):
    response = execute(comand)
    assert response == result

