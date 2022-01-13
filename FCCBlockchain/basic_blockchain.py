  1 from hashlib import sha256                                                      
  2 import json                                                                     
  3 import time                                                                     
  4                                                                                 
  5                                                                                 
  6 # the sha256 function will give us the ability to compute hashe                 
  7 #Json is used for parsing our data and time is used for timestamping            
  8                                                                                 
  9                                                                                 
 10 #defining a class for our blockchain                                            
 11                                                                                 
 12 # a blockchain is a ledger of "blocks" and blocks are a collection of transactions.
 13 # each block in the blockchain is linked to its predecessor.                    
 14 # Let's create a class that will serve as our blockchain:                       
 15                                                                                 
 16                                                                                 
 17 class Chain:                                                                    
 18     def __init__(self):                                                         
 19         self.blockchain = []                                                    
 20                                                                                 
 21         self.pending = []                                                       
 22                                                                                 
 23                                                                                 
 24         self.add_block(prevhash= "Genesis", proof = 123)                        
 25                                                                                 
 26                                                                                 
 27                                                                                 
 28 #blockchain is the acutal list of our blocks and pending is the list of transactions 
 29 #that are yet to be added.                                                      
 30 # We are calling a method add_block that adds a new block to our blockchian     
 31 # this is our genesis block, the first block to our chain                       
 32                                                                                 
 33                                                                                 
 34                                                                                 
 35                                                                                 
 36     def add_transaction(self,sender,recipient, amount):                         
 37         transaction = {                                                         
 38                 "sender" : sender,                                              
 39                 "recipient": recipient,                                         
 40                 "amount": amount                                                
 41                 }                                                               
 42                                                                                 
 43                                                                                 
 44         self.pending.append(transaction)                                        
 45                                                                                 
 46                                                                                 
 47                                                                                 
 48                                                                                 
 49     def compute_hash(self,block):                                               
 50                                                                                 
 51         json_block = json.dumps(block, sort_keys = True).encode()               
 52                                                                                 
 53         curhash = sha256(json_block).hexdigest()                                
 54                                                                                 
 55                                                                                 
 56         return curhash                                                          
 57                                                                                 
 58                                                                                 
 59                                                                                 
 60                                                                                 
 61     def add_block(self,proof, prevhash= None):                                  
 62                                                                                 
 63         block = {                                                               
 64                                                                                 
 65                                                                                 
 66                 "index": len(self.blockchain),                                  
 67                                                                                 
 68                 "timestamp": time.time(),                                       
 69                                                                                 
 70                 "transactions": self.pending,                                   
 71                                                                                 
 72                                                                                 
 73                 "proof" : proof,                                                
 74                                                                                 
 75                                                                                 
 76                 "prevhash": prevhash or self.compute_hash(self.blockchain[-1])  
 77                                                                                 
 78                     }                                                           
 79                                                                                 
 80                                                                                 
 81                                                                                 
 82         self.pending = []                                                       
 83                                                                                 
 84                                                                                 
 85         self.blockchain.append(block)                                           
 86                                                                                 
 87                                                                                 
 88                                                                                 
 89                                                                                 
 90 if __name__== "__main__":                                                       
 91                                                                                 
 92     chain = Chain()                                                             
 93                                                                                 
 94     t1 =chain.add_transaction("vitalik","satoshi",100)                          
 95                                                                                 
 96     t2 = chain.add_transaction("satoshi","alice",10)                            
 97                                                                                 
 98                                                                                 
 99     chain.add_block(12345)                                                      
100                                                                                 
101                                                                                 
102                                                                                 
103     print(chain.blockchain)                                                     
104                                                                                 
105                                                                                 
106                                                                                 
107                                                                                 
108                                                                                 
~         
