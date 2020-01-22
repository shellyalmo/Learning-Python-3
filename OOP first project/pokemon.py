
class Pokemon:
    def __init__(self, name, level, type, maximum_health, current_health, was_knocked_out, maximum_experience=100, current_experience=0):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.was_knocked_out = was_knocked_out
        self.maximum_experience = maximum_experience
        self.current_experience = current_experience
        
        
        
    def __repr__(self):
      return "\nPokemon Name: {name} \nLevel: {level} \nType: {type} \nMaximum health: {maximum_health} \nCurrent health: {current_health} \nWas knocked out: {was_knocked_out}.".format(name=self.name, level = self.level, type=self.type,maximum_health = self.maximum_health,current_health=self.current_health,was_knocked_out=self.was_knocked_out)
      
   
    def lose_health(self, health_lost):
      self.current_health = self.current_health - health_lost 
      if health_lost >= self.maximum_health + self.current_health:
        self.level = 0
        self.current_health = self.maximum_health + self.current_health
      elif self.current_health < 0:
        self.level -= 1
        self.current_health = self.maximum_health + self.current_health
      elif health_lost == self.current_health:
        self.current_health = 0
        
      return "\nSince {name} has lost {health_lost} health points,\nHis current health is: {current_health}\nHis current level is: {current_level}".format(name=self.name, health_lost=health_lost,current_health=self.current_health,current_level=self.level)
      
    def gain_health(self, health_gain):
      self.current_health = self.current_health + health_gain 
      if self.current_health > self.maximum_health:
        #   self.level += 1
          self.current_health -= self.maximum_health
      print("\n{name} gained {health_gain} health points.\nHis current health is: {current_health}\nHis current level is: {current_level}".format(name=self.name, health_gain=health_gain,current_health=self.current_health,current_level=self.level))
      return self.current_health

    def knock_out(self):
      if self.current_health <= 0 :
        self.was_knocked_out = "yes"
      else:
        self.was_knocked_out = "no"
      return "\nWas {name} knocked out: {was_knocked_out}".format(name=self.name,was_knocked_out=self.was_knocked_out)
      
    def revive(self):
      if self.level == 0:
        return "\n{name} has to be revived.".format(name=self.name)
      
    """if attacking pokemon has advantage (fire>grass, water>fire, grass>water) then damage = 2 * level of the attacking
    if attacking had disadvantage (grass<fire, fire<water, water<grass) then 
    damage = 0.5 * level of attacking
    """  
    def attack(self,other_pokemon):
      damage = 0
      if self.type == "Fire" and other_pokemon.type == "Grass" or self.type == "Water" and other_pokemon.type == "Fire" or self.type == "Grass" and other_pokemon.type == "Water":
        damage = 2 * self.level
      if self.type == "Grass" and other_pokemon.type == "Fire" or self.type == "Fire" and other_pokemon.type == "Water" or self.type == "Water" and other_pokemon.type == "Grass":
        damage = 0.5 * self.level
      else:
          damage = 1 * self.level
      print("\n{first_pokemon_name} has attacked {second_pokemon_name}. \n{the_second_pokemon_name} has lost {damage} health points.".format(first_pokemon_name=self.name,second_pokemon_name=other_pokemon.name,the_second_pokemon_name=other_pokemon.name,damage=damage))
      self.experience_in_battle(damage)
      return damage

    def experience_in_battle(self, damage):
        if damage > 0:
            self.current_experience += 5
        if self.current_experience == self.maximum_experience:
            self.level += 1
            self.current_experience = 0
        return self.current_experience
 

class Trainer:
  def __init__(self,name,pokemons_list,potions,currently_active_pokemon):
    self.name = name
    self.pokemons_list = pokemons_list
    self.potions = potions
    self.currently_active_pokemon = currently_active_pokemon
    
  def __repr__(self):
      return "\nTrainer Name: {name} \n\nPokemons: {pokemons_list} \n\nNumber of health potions: {potions} \n\nCurrently active Pokemon: {currently_active_pokemon}".format(name=self.name, pokemons_list = self.pokemons_list, potions=self.potions, currently_active_pokemon=self.currently_active_pokemon)
    
  def healing_potion(self,number_of_potions):
    #   a potion should not heal a pokemon past it's 100 maximum health
      if self.currently_active_pokemon.current_health == 100:
          return "\nCan't use a potion past the maximum health."
      else:
          health = 5 * number_of_potions
          return self.currently_active_pokemon.gain_health(health)
    
  def attack_other_trainer(self, other_trainer):
    #   a pokemon that was knocked out should not attack another pokemon
      if self.currently_active_pokemon.was_knocked_out == "yes":
          return "\nCan't attack if was knocked out."
      else:
          return self.currently_active_pokemon.attack(other_trainer.currently_active_pokemon)
      
  def switch_pokemon(self, different_pokemon):
      self.currently_active_pokemon = different_pokemon
      if self.currently_active_pokemon.was_knocked_out == "yes":
          return "\nCan't switch if was knocked out."
      else:
          return self.currently_active_pokemon


first_pokemon_trainer1 = Pokemon("Charmander",81,"Fire",100,70,"no",100,34)
second_pokemon_trainer1 = Pokemon("Balbazor",1,"Grass",100,60,"no",100,12)
trainer1 = Trainer("Ash",[first_pokemon_trainer1,second_pokemon_trainer1],2,first_pokemon_trainer1)

first_pokemon_trainer2 = Pokemon("Squirtle",13,"Water",100,4,"yes",100,5)
second_pokemon_trainer2 = Pokemon("Vulpix",4,"Fire",100,60,"no",100,87)
second_trainer = Trainer("Misty",[first_pokemon_trainer2,second_pokemon_trainer2],1,second_pokemon_trainer2)

