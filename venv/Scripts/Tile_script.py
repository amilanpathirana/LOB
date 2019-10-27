

class Tile:

    def __init__(self):
        self.item=False
        self.player = False
        self.box = False

    def __del__(self):
       print ("deleted")
