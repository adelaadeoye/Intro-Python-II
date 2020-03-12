# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self,name,description, items=[]):
        super().__init__()
        self.name = name
        self.description = description
        self.items=items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += str(self.items)
        return_string += "\n\n"
        return return_string

    
   


    
