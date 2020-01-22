from pokemon import Pokemon, Trainer  

def test_potion():
    first_pokemon_trainer1 = Pokemon("Charmander",81,"Fire",100,70,"no",100,45)
    second_pokemon_trainer1 = Pokemon("Balbazor",1,"Grass",100,100,"no",100,6)
    trainer1 = Trainer("Brooke",[first_pokemon_trainer1,second_pokemon_trainer1],1,second_pokemon_trainer1)
    assert trainer1.healing_potion(2) == "\nCan't use a potion past the maximum health."

def test_attack_trainer():
    first_pokemon_trainer2 = Pokemon("WaterDuck",13,"Water",100,4,"yes")
    second_pokemon_trainer2 = Pokemon("Balbazor",1,"Grass",100,60,"no")
    first_pokemon_trainer3 = Pokemon("Charmander",11,"Fire",100,70,"no")
    second_pokemon_trainer3 = Pokemon("WaterDuck",34,"Water",100,90,"no")
    trainer2 = Trainer("Ash",[first_pokemon_trainer2,second_pokemon_trainer2],2,first_pokemon_trainer2)
    trainer3 = Trainer("Misty",[first_pokemon_trainer3,second_pokemon_trainer3],1,second_pokemon_trainer3)
    assert trainer2.attack_other_trainer(trainer3) == "\nCan't attack if was knocked out."

def test_switch_pokemon():
    first_pokemon_trainer3 = Pokemon("Charmander",11,"Fire",100,70,"yes")
    second_pokemon_trainer3 = Pokemon("WaterDuck",34,"Water",100,90,"no")
    trainer3 = Trainer("Misty",[first_pokemon_trainer3,second_pokemon_trainer3],1,second_pokemon_trainer3)
    assert trainer3.switch_pokemon(first_pokemon_trainer3) == "\nCan't switch if was knocked out."
