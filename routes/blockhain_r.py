from database.models import Chain, Vote
from routes import users
from repositories.utils import Utils as helper
from fastapi import APIRouter, status, HTTPException, Response
from collections import Counter
from api.schema import vote as ResponseVote
from repositories.blockchain import BlockChain
from repositories.calculators import Calculators
from database.connector import *
from repositories.utils import Utils

pollchain = BlockChain()
getter = Calculators()
db = database


router = APIRouter(
    prefix= '/api/blockchain',
    tags=['BlockChain']
)


@router.get('/check/user')
async def check_user_and_confirm(cnic):

    return await CheckVoter(cnic)





@router.post('/poll')
async def poll(id):

        candidate = await get_single_candidate(id)

        previous_block = pollchain.previous_block()
        previous_proof = previous_block['proof']
        proof = pollchain.proof_of_work(previous_proof)
        previous_hash = pollchain.hash(previous_block)
        block = pollchain.create_block(proof, previous_hash, candidate.name, candidate.party, candidate.slogan)
        vote = block['vote']
        
        response = {"timestamp" : block['timestamp'],
                "previous_hash" : block['previous_hash'],
                "candidate" : f"{vote['candidate']['name']} of {vote['candidate']['party']}",

        }

        getter.get_vote_from_block(vote['candidate'])
        getter.get_party_from_block(vote['candidate'])
        rev_chain = Chain(instance=pollchain.chain)
        await insert(rev_chain)
      
        return response



@router.get('/validate_chain')
async def valid():

    valid = pollchain.chain_valid(pollchain.chain)


     
    if valid:
        response = {'message': 'Proccess Integrity confirmed.',"chain" : True}
    else:
        response = {'message': 'The Blockchain is not valid.' , "state" : False}
    
    return response
	

@router.get('/chain')
async def display_chain():



    response = {'chain': pollchain.chain,
                'length': len(pollchain.chain)}
    return response


@router.get('/stats')
def display_stats():

    print(f"candidate : {getter.candidates}")
    print(f"parties : {getter.parties}")
    
    
    results = Counter(getter.candidates)


            

    response = { 'total_votes' : len(pollchain.chain)-1,
                   'last_vote_polled_for' : f"{getter.candidates[-1]} of {getter.parties[-1]}",

                   'results' : results
                  }

    return response

@router.get('/generate_keys')
def keys():

    return helper.generate_keys()




@router.post('/get_candidates/{id}')
async def Candidate(id):

    candidate = await get_single_candidate(id)
    votes = getter.get_single_candidates_votes(candidate.name)

    return { "candidate" : candidate, "votes" : votes}
