class Calculators():

        def __init__(self):

            self.candidates = []
            self.parties = []
          

            
        
        def get_vote_from_block(self, polledVote):
            self.candidates.append(polledVote.candidate.name)
        

        
        def get_party_from_block(self, polledVote):
            self.parties.append(polledVote.candidate.party)
            