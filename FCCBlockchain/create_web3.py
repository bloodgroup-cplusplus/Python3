from web3 import Web3


infura_url = "YOUR INFURA URL"

web3= Web3(Web3.HTTPProvider(infura_url))

web3.isConnected()

web3.eth.blockNumber


