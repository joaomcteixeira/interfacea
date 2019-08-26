
class InterfaceaError(Exception):
    emsg = "OMG THERES AN EXCEPTION!"
    
    def __init__(self, *args):
        self.args = args or ['']
    
    def __str__(self):
        return self.emsg.format(*self.args)
    
    def __repr__(self):
        return f"{self.__class__.__name__}: {self}"