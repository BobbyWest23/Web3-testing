from web3 import Web3, EthereumTesterProvider
# Importing web3 library module.

eth = 'https://mainnet.infura.io/v3/91a749f8f60d46eeb78f01be61a6983a'
# Using infura for a provider to be connected to the blockchain.

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())
# Prints a boolean 'True' or 'False' if you're connected to the blockchain.

block = web3.eth.get_block('latest')
#print(block)
# Making a variable called 'block' where I'm getting the info about the 'latest' block and then printing the result.

block = web3.eth.get_block('latest')
print(block['timestamp'])
# Making a variable called 'block' where I'm getting only the 'timestamp' of the 'latest' block and then printing the result.

blocknr = web3.eth.block_number
print(blocknr)
# Another way of getting the current block number



