from web3 import Web3, EthereumTesterProvider
# Importing web3 library module.

eth = 'https://mainnet.infura.io/v3/91a749f8f60d46eeb78f01be61a6983a'
# Using infura for a provider to be connected to the blockchain.

web3 = Web3(Web3.HTTPProvider(eth))
print(web3.is_connected())
# Prints a boolean 'True' or 'False' if you're connected to the blockchain.

accounts = web3.eth.account.create('iyhbujnawfoawapolwa')
# Creates an account and add random letters to make the private key better.

print(accounts.address)
print(web3.to_hex(accounts.key))
# Prints an address and a private key that is readable.

