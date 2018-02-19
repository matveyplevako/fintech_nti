def get_status(tx_hash):
    response = w3.eth.getTransaction(tx_hash)
    if response is None:
        print("No such transaction in the local copy of the chain")
    value = str(response["value"])
    to = response["to"]
    if response["blockNumber"] is None:
        print("Delay in payment of " + value + ' to "' + to + '"')
    print('Payment of ' + value + ' to "' + to + '" confirmed')