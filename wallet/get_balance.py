def get_balance(priv_key):
    publ_key = '0x' + utils.privtoaddr(priv_key).hex()
    responde = str(w3.eth.getBalance(publ_key))
    print('Balance on ' + '"' + publ_key + '" is ' + responde)
