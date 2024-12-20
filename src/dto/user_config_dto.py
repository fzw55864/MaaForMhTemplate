class user_config_stop():
    def __init__(self,stoptime):
        super().__init__()
        self.stoptime = stoptime
    
    @property
    def stoptime(self):
        return self.stoptime
