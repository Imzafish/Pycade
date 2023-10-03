class Pokemon:
    def __init__(self,name,attack,health):
        print("Building...")
        self.name=name
        self.attack=attack
        self.health=health
    def lose_health(self,damage):
        self.health=self.health-damage
        
pika=Pokemon("Pikachu",6.9,69)
charmander=Pokemon("Charmander",6.9,69)
print(pika.health,pika.attack,pika.name)
pika.lose_health(12)
print(pika.health)