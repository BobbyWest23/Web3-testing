from web3 import Web3, EthereumTesterProvider
# Importing web3 library module.

eth = 'https://mainnet.infura.io/v3/91a749f8f60d46eeb78f01be61a6983a'
# Using infura for a provider to be connected to the blockchain.

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())
# Prints a boolean 'True' or 'False' if you're connected to the blockchain.

addressA = web3.to_checksum_address('0xF929897a3250dD0EEba44c1b267bfD36D54FB58E')
addressB = web3.to_checksum_address('0x36c149AB2236AA6F0A5543C77a43248425AD1f77')
# 'adressA' is the sender and 'adressB' is the reciever.

privateKey = '0xf44d1a991a4babd20c35d11e66538ecd962364725f20ac500080ec3970393542'
# Private key for 'addressA' (sender), this is needed to sign the transaction.

nonce = web3.eth.get_transaction_count(addressA)
# Only the sender adress needs a nonce.

tx = {
    'nonce': nonce,
    'to': addressB,
    'value': web3.to_wei(0.005, 'ether'),
    'gas': 100000,
    'gasPrice': web3.to_wei('10', 'gwei')
}
# All of the needed values for the transaction (I think you can do the 'gasPrice' differently).
# Also when making a transaction within Ethereum you don't need to add the 'chainId', but if that is the case the Id is 1

signed_tx = web3.eth.account.sign_transaction(tx, privateKey)
# Makes the signed transaction variable to use later.

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
# Makes the transaction hash variable to get back later and it sends the transaction.

print(web3.to_hex(tx_hash))
# Prints the transaction hash