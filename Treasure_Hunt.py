class Player:
   def __init__(self,name):
      self.name=name
      self.bag=[]

   def get_item(self,item):
      self.bag.append(item)

   def show_item(self):
      for a in self.bag:
         print(a)

class Place:
 def __init__(self,name,description,item):
       self.name=name 
       self.description=description
       self.item=item

 def enter(self, player):
   print(f"you are at {self.name}")
   print(self.description)
   if self.item :
      print(f"you spotted the item {self.item}")
      player.get_item(self.item)
      self.item=None 


class SpecialPlace(Place):
   def __init__(self,name,description,required_item,item):
      super().__init__(name,description,item)
      self.required_item=required_item
      self.is_unlocked=False

   def enter(self, player):
      print(f"you are at: {self.name}")
      print(self.description)
      if self.required_item=="Key" and not self.is_unlocked:
         if "Key" in player.bag:
            print(f"you spotted the item {self.item}")
            player.get_item(self.item)
            self.is_unlocked=True
         else:
            print("Please follow the required sequence__collect Key first")
      elif self.required_item=="Secret Code" :
         check_elements=["Key","Secret Code"]
         result=all(item in player.bag for item in check_elements)
         if result:
            print(f"you spotted the item {self.item}---CONGRATS YOU WIN")
            player.get_item(self.item)
         else:
           print("Please follow the required sequence_first key than Secret_code than come here") 

tc=Player("tarun")
Canteen=Place("Canteen","Messy_Place","Key")
ComputerLab=SpecialPlace("ComputerLab","ALL Computer Area","Key","Secret Code")
MainStage=SpecialPlace("MainStage","Top area","Secret Code","Trophy")

#WINNING ROUTE
Canteen.enter(tc)
ComputerLab.enter(tc)
MainStage.enter(tc)

#LOOSING ROUTE

# ENTERING THE COMPUTER LAB FIRST 
rc=Player("raghav")
ComputerLab1=SpecialPlace("ComputerLab1","ALL Computer Area","Key","Secret Code")
ComputerLab1.enter(rc)
# ENTERING THE MAIN STGE FIRST 
MainStage1=SpecialPlace("MainStage1","Top area","Secret Code","Trophy")
MainStage1.enter(rc)
# ENTERING THE CANTEEN THAN MAIN STGE 
Canteen1=Place("Canteen1","Messy_Place","Key")
Canteen1.enter(rc)
MainStage1.enter(rc)






            
           
      