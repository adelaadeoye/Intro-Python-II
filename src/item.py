class Item():
    def __init__(self,name, description):
        super().__init__()
        self.name = name
        self.description = description


class Light(Item):
    def __init__(self, name, description,light_status):
        super().__init__(name, description)
        self.light_status=light_status

class Axe(Item):
    def __init__(self, name, description,axe_status):
        super().__init__(name, description)
        self.axe_status=axe_status