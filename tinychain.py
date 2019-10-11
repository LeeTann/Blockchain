import json
import hashlib

"""
1. Make some transactions
2. Find a proof for the hash of each transaction, and put the hash/proof combo in the next transaction
3. Test that a transaction is correct with the hash and the proof
4. Turn a transaction into a block
5. Create a function to make a transaction
6. Create a function to make a block 
7. Store the transaction in a transaction list 
8. Stroe blocks in a blocks list
9. Refactor 'make a proof' into two functions
"""


firstTransaction = {
  'tim': -10,
  'steve': 10
}

firstHash = hash(json.dumps(firstTransaction))

# make lots of guesses until we find the pattern we want
proof = 0
def make_a_proof(block_hash):
  while hashlib.sha256(f'{block_hash}{proof}'.encode()).hexdigest()[:2] != '00':
    proof += 1
  return proof

print(proof)

# combine this proof with my hash

secondTransaction = {
  'javier': -20,
  'arpita': 20,
  'proof': make_a_proof(firstHash),
  'previous_hash': firstHash
}

secondHash = hash(json.dumps(secondTransaction))

thirdTransaction = {
  'joshua': -30,
  'johnathan': 30,
  'previous_hash': secondHash
}

thirdHash = hash(json.dumps(thirdTransaction))