from CandidateState1_20220324212440 import CandidateState
import enum
    
class Algorithms(enum.Enum):
    DSF = 'dsf'
    BSF = 'bsf'

class UninformedSearch:
    def __init__ (self, initialState, finalStates):
        self.initialState = initialState
        self.finalStates = finalStates

    def search(self, typee = Algorithms.BSF):
        visited = []

        candidate = CandidateState.CandidateState(self.initialState)
        pending = [candidate]

        i = 0

        while len(pending):
            candidates = typee == Algorithms.DSF if pending.pop() else pending.pop(0)
            i += 1

            if i % 1000 == 0:
                print(i)

            if self.initialState.equals(candidate.state):
                result = []
                while (candidates):
                    result.append(candidate)
                    candidate = candidate.parent
                return result.reverse()
            else:
                visited.append(candidate.state)
                successors = candidate.getSuccessors()

                for sucessor in successors:
                    for state in visited:
                        if not state.equals(sucessor.state):
                            pending.append(sucessor)
                
        return None