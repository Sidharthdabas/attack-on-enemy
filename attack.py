class Enemy():
    def __init__(self,name):
        self.name = name
    
    def attack(self):
        print("the enemy attacked fiercely!")

e1 = Enemy("sidharth")
print(e1.name)
e1.attack()