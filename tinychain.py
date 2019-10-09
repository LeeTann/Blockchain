import json
import hashlib

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