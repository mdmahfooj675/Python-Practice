# basic example of abstraction in object oriented

# it shows only necessary thing like car started 
# hide the unwanted like how clutch and acc are goes false to true

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started successfully....")

car1 = car()
car1.start()

print("code execution completed....")