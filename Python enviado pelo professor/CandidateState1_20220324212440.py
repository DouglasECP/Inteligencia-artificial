class CandidateState:
  def __init__(self, state, parent = None, action = None):
    self.state = state
    self.parent = parent
    self.action = action
    self.children = []

  def getSuccessors(self):
    lists = self.state.getActions()
    successors = []

    for action in lists:
      state = self.state.doAction(action)

      successor = CandidateState(state,self,action)
      self.children.append(successor)

      successors.append(successor)

    return successors
  
  def toString(self):
    if (self.action):
      return f"{self.action} > {str(self.state)}"
    else:
      return f"start > {str(self.state)}"
