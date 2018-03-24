import sys
from web3 import Web3
from web3.main import to_checksum_address
from json import loads, dump
from web3.contract import ConciseContract
from time import sleep
from sha3 import keccak_256
from solc import compile_files

compiled = compile_files(["Integrated_ManagementContract.sol"])
Manager = compiled['Integrated_ManagementContract.sol:ManagementContract']
ERC721 = compiled['Integrated_ERC721Token.sol:ERC721Token']

abi_for_manager = Manager['abi']
abi_for_erc721 = ERC721['abi']
bytecode_for_deployment = Manager['bin']
args = sys.argv
w3 = Web3()

# with open('account.json') as data:
#     account_data = loads(data.read())
#     account_address = to_checksum_address(account_data['account'])
#     passwd = account_data['passwd']
#     w3.personal.unlockAccount(account_address, passwd, 4)

with open('account_id') as ac:
    account_address = w3.eth.accounts[int(ac.read())]
    w3.personal.unlockAccount(account_address, "", 4)

if len(args) > 2:
    args = args[args.index('Integrated_identity.py'):]

def waitTillMine(txhash):
    sleep(1)
    while w3.eth.getTransactionReceipt(txhash) is None:
        sleep(1)
    if w3.eth.getTransactionReceipt(txhash)['status'] == 0:
        raise Exception("Error while calling a func")

def deploy():
    contract = w3.eth.contract(abi=abi_for_manager, bytecode=bytecode_for_deployment)
    trans_hash = contract.deploy({'from': account_address, 'gas': 5 * 10**6}).hex()
    waitTillMine(trans_hash)
    txn_receipt = w3.eth.getTransactionReceipt(trans_hash)
    contract_address = txn_receipt['contractAddress']
    print('Management contract address: ' + contract_address)
    with open('database.json', 'w') as file:
        dump({"mgmtContract": contract_address}, file)

def getManagementContract():
    with open('database.json') as data:
        mgmt_address = loads(data.read())['mgmtContract']
    contract = w3.eth.contract(address=mgmt_address, abi=abi_for_manager, ContractFactoryClass=ConciseContract)
    return contract

def getERC721Contract():
    with open('database.json') as data:
        token_address = loads(data.read())['tokenContract']
    contract = w3.eth.contract(address=token_address, abi=abi_for_erc721, ContractFactoryClass=ConciseContract)
    return contract

def setFee(new_price):
    contract = getManagementContract()
    txhash = contract.setFee(int(new_price * 10 **18), transact={'from': account_address, 'gas': 4 * 10**6})
    waitTillMine(txhash)
    print("Successfully configured")

def getFee():
    contract = getManagementContract()
    price = contract.getFee()
    print('Service fee: ' + ('%f' % (price / 10**18)).rstrip("0").rstrip('.'))

def regVender(company_name, symbols, fee):
    contract = getManagementContract()
    txhash = contract.regVender(company_name, symbols, transact={'from':account_address, 'gas': 4 * 10**6, 'value': int(fee * 10 **18)})
    waitTillMine(txhash)
    company_address = contract.CompanyAddresses(keccak_256(company_name.encode('utf-8')).digest())
    print("Token contract address: " + company_address)
    with open('database.json') as prev_info:
        data = loads(prev_info.read())
    data["tokenContract"] = company_address
    with open('database.json', 'w') as file:
        dump(data, file)

def create(num):
    contract = getERC721Contract()
    last_id = contract.getId(call={'from': account_address, 'gas': 4 * 10**6})
    txhash = contract.create(num, transact={'from': account_address, 'gas': 4 * 10**6})
    waitTillMine(txhash)
    for i in range(last_id + 1, num + last_id + 1):
        print(i)

def setProperty(prop, tokenId):
    contract = getERC721Contract()
    txhash = contract.setProperty(prop, tokenId, transact={'from': account_address, 'gas': 4 * 10**6})
    waitTillMine(txhash)
    print("Successfully updated")

def getProperty(tokenId):
    ERC721 = getERC721Contract()
    Manager = getManagementContract()
    owner = Manager.MerchName(ERC721.tokenOwner(tokenId))
    prop = ERC721.getProperty(tokenId)
    status = ERC721.getStatus(tokenId)
    print('Owner: ' + owner + '\nProperties: ' + prop + '\nStatus: ' + status)

def regMerch(name):
    contract = getManagementContract()
    txhash = contract.regMerch(name, transact={'from': account_address, 'gas': 4 * 10**6})
    waitTillMine(txhash)
    print('Merchant registered')

def TransferToken(to, tokenId):
    contract = getERC721Contract()
    txhash = contract.transferByMerchName(to, tokenId, transact={'from': account_address, 'gas': 4 * 10**6})
    waitTillMine(txhash)
    print("Ownership transfered")

def destroy(tokenId):
    contract = getERC721Contract()
    if account_address == contract.tokenOwner(tokenId):
        txhash = contract.requestBurning(tokenId, transact={'from': account_address, 'gas': 4 * 10 ** 6})
        waitTillMine(txhash)
        print("Destruction requested")
    else:
        txhash = contract.burn(tokenId, transact={'from': account_address, 'gas': 4 * 10**6})
        waitTillMine(txhash)
        print("Destruction confirmed")


def repair(tokenId):
    contract = getERC721Contract()
    txhash = contract.repair(tokenId, transact={'from': account_address, 'gas': 4 * 10**6})
    waitTillMine(txhash)
    print("Destruction declined")


if args[1] == '--deploy':
    deploy()

if args[1] == '--setfee':
    setFee(float(args[2]))

if args[1] == '--getfee':
    getFee()

if args[1] == '--vendreg':
    company_name, symbols, fee = args[2], args[3], float(args[4])
    regVender(company_name, symbols, fee)

if args[1] == '--create':
    create(int(args[2]))

if args[1] == '--setprop':
    setProperty(args[2], int(args[3]))

if args[1] == '--data':
    getProperty(int(args[2]))

if args[1] == '--merchreg':
    regMerch(args[2])

if args[1] == '--owner':
    TransferToken(args[2], int(args[3]))

if args[1] == '--destroy':
    args[2] = int(args[2])
    destroy(args[2])

if args[1] == '--repair':
    repair(int(args[2]))