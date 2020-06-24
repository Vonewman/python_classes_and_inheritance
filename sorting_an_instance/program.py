class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


L = [
    Fruit('Cherry', 10),
    Fruit('Apple', 5),
    Fruit('Blueberry', 20)
]


for f in sorted(L, key=lambda x : x.sort_priority()):
    print(f.name)

    
