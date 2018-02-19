def send_tx(priv_key, to, value, gas_price=1):
    address = "0x" + utils.privtoaddr(priv_key).hex()
    nonce = w3.eth.getTransactionCount(address)
    gas = w3.eth.estimateGas({"to": to, "value": value})
    ex = transactions.Transaction(nonce, gas_price, gas, to, value, "")
    ex.sign(priv_key)

    raw = "0x" + rlp.encode(ex).hex()
    try:
        resp = w3.eth.sendRawTransaction(raw)
        print("Payment of " + str(value) + ' to "' \
              + to + '" scheduled\n'
                     "Transaction Hash: " + resp)
    except:
        print("No enough funds for payment")