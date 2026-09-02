class GoalsMem():
    '''
    ## Goals Memory
    This Class store Chat goals and and facts
    #### Methods:
    * set_goals:\n
        This method can just Store goals and facts in chat
    
    * resault:\n
        This methed can return Stored data
    
        
    for more information checkout **A-memory** docs.
    '''

    def __init__(self):
        self.context_goals = []
        self.recent_goal = None
        self.active_goal = None
        self.chat_facts = []
        self.cn = 0
        self.fn = 0

    # This method set and store goals in list 
    def set_goals(self, contextgoals:str | None, recentgoal:str | None, 
            activegoal:str | None, chatfacts:str | None) -> str:

        if activegoal:
            self.active_goal = activegoal

        if recentgoal:
            self.recent_goal = recentgoal

        if contextgoals:
            self.context_goals.append(f"number{self.cn}: "+contextgoals)
            self.cn+=1

        if chatfacts:
            self.chat_facts.append(f"number{self.fn}: "+chatfacts)
            self.fn=+1

    # The resault methed return data stored in lists
    def resault(self, cg:bool | False, ag:bool | False, 
            rg:bool | False, cf:bool | False, al:bool | False):
        resu = []

        if cg == True:
            resu.append(self.context_goals)

        if ag == True:
            resu.append(self.active_goal)

        if rg == True:
            resu.append(self.recent_goal)

        if cf == True:
            resu.append(self.chat_facts)

        if al == True:
            return f"Active Goal: {self.active_goal}\nRecent Goal: {self.recent_goal}\nContaxt Goals: {self.context_goals}\nChat Facts: {self.chat_facts}"
        if resu!=None:
            return resu


class ShortMem():
    '''
    ## Short Memory
    This class is A **Short-term-Memory** for agents Store **Agent** and **user** chat.

    ### methods:
    * store_messages:\n
        this method store agent and user messages and remove 
        first old messages after 8 message betwinn user and agent.
    
    * remind_messages:\n
        This method just return stored messages.
    

    for more information checkout **A-memory** docs.
    '''

    def __init__(self):
        self.messages = []
        self.message_number = 0
    # Storing messages with 8 limit and forget first and old message after add new message
    def store_messages(self, role:str | None, message:str | None) -> str:
        # Add new messages
        if self.message_number != 8:
            self.messages.append({"role": role, "content": message})
            self.message_number+=1
        # Remove old message after 8 message
        else:
            self.messages.pop(0)
            self.message_number = 0
            self.messages.append({"role": role, "content": message})
    # Return all stored Messages
    def remind_messages(self):
        return self.messages

