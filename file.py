class File:
    def __init__(self, name):
        self.name = name


    def open(self):
        try:
            f = open(self.name, "r")
            content = f.readlines()
            print =(content)
            f.close()

        except Exception as e:
            print(f"ERROR {e} trying to open file: {self.name}")

    
    def write(self, characters):
        print("")

    #def update(self, characters):