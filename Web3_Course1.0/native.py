from web3 import Web3, EthereumTesterProvider
# Importing web3 library module.

eth = 'https://mainnet.infura.io/v3/91a749f8f60d46eeb78f01be61a6983a'
# Using infura for a provider to be connected to the blockchain.

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())
# Prints a boolean 'True' or 'False' if you're connected to the blockchain.

adress = '0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326'
balance = web3.eth.get_balance(adress)
print(balance / 10 ** 18)
# Prints the balance of a wallet in eth (orignally it'll print in wei) provided in the 'adress'.

balance = web3.eth.get_balance('0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326')
print(web3.from_wei(balance, 'ether'))
# Prints the balance of a wallet in eth (orignally it'll print in wei) provided in the 'adress'. It's also more accurtate.

tx = web3.eth.get_transaction('0x202823fc39aeb8f3e463461e26662bbc4de87520df77e567d02d621248c2317c')
print(tx)
# Prints data of a transaction, all is in wei.

