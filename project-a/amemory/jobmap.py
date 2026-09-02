class JobMap():
    '''
    ## Job Map
    This class can add A map to agent when it want to do A job.
    
    ### methods:
    * addjob:
        Agent should sort a map before do A job like:\n
            a>b>c>... 
    
    * usejob:
        It's A simple method that return one job after calling it and then remove used jobs.

    for more information checkout **A-memory** docs. 
    '''

    def __init__(self, data=None):
        self.job = []

    def addjob(self, data=None) -> str:

        words = ''
        symbol = '>'
        num = 1
        raw_data = data+symbol

        for j in raw_data:
        
            if not symbol in j:
                words+=j
            
            else:
                self.job.append(words)
                num+=1
                words=''

    def usejob(self):
        try:
            self.job.reverse()

            return self.job.pop()
        
        except IndexError:
            return "JOB ENDED"

        except Exception as e:
            return f"An Unexpected error: {e}"

    # def checkjob(self): # Temporary Method

    #     return self.job
