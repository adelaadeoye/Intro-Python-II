# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self,name,current_room):
        super().__init__()
        self.name = name
        self.current_room = current_room
        self.items = []

    
    def travel(self,direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
            
            
        else:
            print("You cannot move in that direction")
    def print_inventory(self):
        print("You are holding: ")
        for item in self.items:
            print(item.name)

    def pick_item(self,item):
        self.items.append(item)
       
    def drop_item(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} not in the list of your items")
    def __str__(self):
        return_string = str(self.items)
        return return_string