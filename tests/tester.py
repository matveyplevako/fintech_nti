'''

git add tester.py
git commit -m ""
git push origin master

'''

from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8546"))
# w3 = Web3(Web3.IPCProvider("/tmp/geth.ipc"))
# w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io"))
switch_acc = 'set_acc.py '
new_accounts = 'new_accounts.py '

from subprocess import check_output
from shlex import split


def set_acc(id):
    execute(switch_acc + str(id))


def newAccounts(num):
    execute(new_accounts + str(num))


def execute(comand):
    print("******")
    print("******")
    try:
        response = check_output(['python3'] + split(comand)).rstrip(b'\n').decode('utf-8')
        print(response)
        return True
    except:
        return False


failed_tests = []


if len(w3.eth.accounts) == 1:
    newAccounts(6)

file = 'identity.py'
set_acc(0)

print('test1')
if not execute(file + " --deploy "):
    failed_tests.append('test1')

print('test2')
if not execute(file + " --setfee 1 "):
    failed_tests.append('test2')

set_acc(1)
print('test3')
if execute(file + " --setfee 1 "):
    failed_tests.append('test3')


print('test4')
set_acc(2)
if not execute(file + " --getfee "):
    failed_tests.append('test4')


print('test5')
set_acc(1)
if not execute(file + " --vendreg comp CMP 2 "):
    failed_tests.append('test5')


print('test6')
set_acc(2)
if  execute(file + " --vendreg comp CMP 1 "):
    failed_tests.append('test6')

print('test7')
set_acc(1)
if not execute(file + " --vendreg compa CNN 1.5 "):
    failed_tests.append('test7')

print('test8')
print('test9')

print('test10')
set_acc(1)
if not execute(file + " --create 4 "):
    failed_tests.append('test10')

print('test12')
set_acc(1)
if not execute(file + " --setprop Omega 3 "):
    failed_tests.append('test12')

print(failed_tests)





