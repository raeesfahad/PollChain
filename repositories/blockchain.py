from datetime import datetime
import hashlib
import json
from collections import Counter
from database.connector import insert


class BlockChain:

    # initializing blockchain with adding first block

    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_block='0',
                       public_key = None, candidate_name=None, candidate_party=None, seat=None)

    def create_block(self, proof, previous_block, public_key, candidate_name, candidate_party, seat):

        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_block,
                 'vote' : {
                   "public_key" : public_key,
                   "candidate"  : {
                    
                    "name" : candidate_name,
                    "party" : candidate_party,
                     "seat" : seat
                   }
                 }}

        
        
        self.chain.append(block)
        return block

    def previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
            encoded_block = json.dumps(block, sort_keys=True).encode()
            return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
            previous_block = chain[0]
            block_index = 1

            while block_index < len(chain):
                block = chain[block_index]
                if block['previous_hash'] != self.hash(previous_block):
                    return False

                previous_proof = previous_block['proof']
                proof = block['proof']
                hash_operation = hashlib.sha256(
                    str(proof**2 - previous_proof**2).encode()).hexdigest()

                if hash_operation[:5] != '00000':
                    return False
                previous_block = block
                block_index += 1

            return True


        

            
                




          


