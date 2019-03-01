class Gamepiece:
    def __init__(self, owner, type):
        self.beneath = None
        self.owner = owner
        self.type = type

    def toString(self):
        sys.stdout.write(owner + ": " +type+"\n")
        if(self.beneath is not None):
            self.beneath.toString()
