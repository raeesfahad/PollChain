from collections import Counter

class Calculators():

        def __init__(self):

            self.candidates = []
            self.parties = []
          

            
        
        def get_vote_from_block(self, polledVote):
           
            self.candidates.append(polledVote['name'].replace(" ","_"))
        

        
        def get_party_from_block(self, polledVote):
    
            self.parties.append(polledVote['party'].replace(" ","_"))


        def get_single_candidates_votes(self, candidate):
    
            parameter = candidate.replace(" ", "_")
            query = Counter(self.candidates)
            
            return query.get(parameter)


            

            