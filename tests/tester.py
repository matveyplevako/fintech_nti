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
    print(check_output(['python3'] + split(comand)).rstrip(b'\n').decode('utf-8'))


switch(0)

print("Deploy from 0")
(execute('identity.py --deploy'))

# print("new accounts")
# (execute('new_accounts.py 4'))

print("getfee")
(execute('identity.py --getfee'))

print("switching to account 2")
switch(2)

print("setfee not as owner")
try:
    execute('identity.py --setfee 1')
    print("Did`nt pass")
except:
    print("pass")

print("switched to owner of contract")
switch(0)

print("changing fee")
(execute('identity.py --setfee 1'))

print("switch 1")
switch(1)

print("regvender")
(execute('identity.py --vendreg "Very Big Company" "VBC" 2'))

print("create 4")
(execute('identity.py --create 4'))

print("get data of token 4")
(execute('identity.py --data 4'))

print('set prop to 4 token')
(execute('identity.py --setprop "Very nice token to buy" 4'))

print('get data')
execute('identity.py --data 4')

print('switch to new merch')
switch(2)

print('merchreg')
execute('identity.py --merchreg "The richest investor"')

print('switch to token owner')
switch(1)

print("transfer to richest")
execute('identity.py --owner "The richest investor" 4')

print('get data of 4 token')
execute('identity.py --data 4')

print('switch to merch')
switch(2)

print('request deleting')
execute('identity.py --destroy 4')

print('switch to token owner')
switch(1)

print('reject')
execute('identity.py --repair 4')

print('get data of 4 token')
execute('identity.py --data 4')

print('switch to merch')
switch(2)

print('request deleting')
execute('identity.py --destroy 4')

print('switch to token owner')
switch(1)

print('destroy token')
execute('identity.py --destroy 4')