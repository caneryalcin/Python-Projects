class Fruits():
    def __init__(self,fruit_list):
        self.fruit_list = fruit_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=1
        if (self.index < len(self.fruit_list)):
            return self.fruit_list[self.index]
        else:
            self.index = -1
            raise StopIteration

fruits = Fruits(["Apple","Banana","Strawberry","Pear","Grape"])

for fruit in fruits:
    print(fruit)
