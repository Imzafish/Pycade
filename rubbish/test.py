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
pika.lose_health(21)
print(pika.health)



import random
import time
start=time.time()
nums=[55,56, 57,57,55,64,64,3,2,1,3]
print ("Sorting Nums...")
#Sorts Multiple Times getting closer and closer with evey sort.
for a in range(len(nums)):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
print("Sorting ended..."+"\n Sorted list: "+str(nums))
end=time.time()
print("Time to sort is " + str(end-start))