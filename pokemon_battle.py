from random import randint

class pokemon:


    def __init__(self, name, lvl, hp, attack, defense, speed, type_1, type_2, move_1, move_2, move_3, move_4):    #to create a pokemon
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type_1 = type_1
        self.type_2 = type_2
        self.move_1 = move_1

        self.move_2 = move_2
        
        self.move_3 = move_3
        
        self.move_4 = move_4

    def insert_move(self, move_number, pokemon_move):  #insert a move into a pokemon
        if move_number == 1:
            self.move_1 = pokemon_move
        elif move_number == 2:
            self.move_2 = pokemon_move
        elif move_number == 3:
            self.move_3 = pokemon_move
        elif move_number == 4:
            self.move_4 = pokemon_move

    def tell_my_moves(self):   #movelist
        return f"Your moves are:\n\n\t1.-{self.move_1.name}\n\t2.-{self.move_2.name}\n\t3.-{self.move_3.name}\n\t4.-{self.move_4.name}"

    def nickname(self, new_name): 
        self.name = new_name

    def pkmn_stats(self):     #prints desired pokemon's stats
      if self-type_2 != "none"
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntypes:\n\t{self.type_1}\n\t{self.type_2}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2.name}\n\t{self.move_3.name}\n\t{self.move_4.name}\n")
      else:
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntypes:\n\t{self.type_1}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2.name}\n\t{self.move_3.name}\n\t{self.move_4.name}\n")

class battles:
    
    def typeChart_1(self, otherpokemon, move_number):                
        if move_number.move_type == "normal" and otherpokemon.type_1 == "rock":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "normal" and otherpokemon.type_1 == "ghost":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "normal" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "water":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "grass":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "ice":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "bug":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "rock":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "dragon":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_1 == "steel":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "water" and otherpokemon.type_1 == "fire":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "water" and otherpokemon.type_1 == "water":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "water" and otherpokemon.type_1 == "grass":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "water" and otherpokemon.type_1 == "ground":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "water" and otherpokemon.type_1 == "rock":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "water" and otherpokemon.type_1 == "dragon":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_1 == "water":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_1 == "electric":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_1 == "grass":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_1 == "ground":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_1 == "flying":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_1 == "dragon":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "water":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "grass":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "poison":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "ground":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "flying":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "bug":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "rock":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "dragon":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "water":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "grass":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "ice":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "ground":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "flying":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "dragon":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "normal":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "ice":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "poison":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "flying":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "psychic":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "bug":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "rock":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "ghost":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "dark":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "steel":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_1 == "fairy":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "grass":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "poison":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "ground":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "rock":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "ghost":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "steel":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_1 == "fairy":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "fire":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "electric":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "grass":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "poison":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "flying":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "bug":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "rock":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_1 == "steel":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "electric":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "grass":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "fighting":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "bug":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "rock":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "electric":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_1 == "fighting":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_1 == "poison":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_1 == "psychic":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_1 == "dark":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "grass":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "fighting":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "poison":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "flying":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "psychic":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "ghost":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "dark":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_1 == "fairy":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "fire":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "ice":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "fighting":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "ground":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "flying":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "bug":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_1 == "normal":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_1 == "psychic":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_1 == "ghost":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_1 == "dark":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "dragon" and otherpokemon.type_1 == "dragon":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "dragon" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "dragon" and otherpokemon.type_1 == "fairy":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_1 == "fighting":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_1 == "psychic":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_1 == "ghost":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_1 == "dark":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_1 == "fairy":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "water":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "electric":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "ice":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "rock":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_1 == "fairy":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_1 == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_1 == "fighting":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_1 == "poison":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_1 == "ghost":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_1 == "dark":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_1 == "steel":
            typeCheck = 1/2
            return typeCheck
        else:
            typeCheck = 1
            return typeCheck

    def typeChart_2(self, otherpokemon, move_number):                
        if move_number.move_type == "normal" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "normal" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "normal" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "water":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "ice":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "bug":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "dragon":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fire" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "water" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "water" and otherpokemon.type_2 == "water":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "water" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "water" and otherpokemon.type_2 == "ground":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "water" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "water" and otherpokemon.type_2 == "dragon":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_2 == "water":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_2 == "electric":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_2 == "ground":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "electric" and otherpokemon.type_2 == "dragon":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "water":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "ground":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "bug":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "dragon":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "grass" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "water":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "ice":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "ground":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "dragon":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ice" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "normal":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "ice":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "psychic":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "bug":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "dark":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fighting" and otherpokemon.type_2 == "fairy":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "ground":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "poison" and otherpokemon.type_2 == "fairy":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "electric":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "bug":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ground" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "electric":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "fighting":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "bug":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "electric":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "flying" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_2 == "fighting":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_2 == "psychic":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_2 == "dark":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "psychic" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "grass":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "fighting":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "psychic":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "dark":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "bug" and otherpokemon.type_2 == "fairy":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "ice":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "fighting":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "ground":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "flying":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "bug":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "rock" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_2 == "normal":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_2 == "psychic":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "ghost" and otherpokemon.type_2 == "dark":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "dragon" and otherpokemon.type_2 == "dragon":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "dragon" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "dragon" and otherpokemon.type_2 == "fairy":
            otherTypeCheck = 0
            return otherTypeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_2 == "fighting":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_2 == "psychic":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_2 == "dark":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "dark" and otherpokemon.type_2 == "fairy":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "water":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "electric":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "ice":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "rock":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "steel" and otherpokemon.type_2 == "fairy":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_2 == "fire":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_2 == "fighting":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_2 == "poison":
            otherTypeCheck = 1/2
            return otherTypeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_2 == "ghost":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_2 == "dark":
            otherTypeCheck = 2
            return otherTypeCheck
        elif move_number.move_type == "fairy" and otherpokemon.type_2 == "steel":
            otherTypeCheck = 1/2
            return otherTypeCheck
        else:
            otherTypeCheck = 1
            return otherTypeCheck
    
    def effectiveness(self, otherpokemon, move_number):
        if move_number == 1:
            move_number = self.move_1
        elif move_number == 2:
            move_number = self.move_2
        elif move_number == 3:
            move_number = self.move_3
        elif move_number == 4:
            move_number = self.move_4     
        x = battles.typeChart_1(self, otherpokemon, move_number)
        y = battles.typeChart_2(self, otherpokemon, move_number)        
        z = x * y        
        if z > 1:
            return "It's super effective!"
        elif z < 1:
            return "It's not very effective..."
        elif z == 0:
            return "Has no effect!"
        else:
            return ""

    def attack_damage(self, otherpokemon, move_number):   #calculates the damage of an attack
        
        if move_number == 1:
            move_number = self.move_1
        elif move_number == 2:
            move_number = self.move_2
        elif move_number == 3:
            move_number = self.move_3
        elif move_number == 4:
            move_number = self.move_4
        acc = move_number.accuracy
        acc_check = randint(1, 100)
        if acc_check < acc:
            x = battles.typeChart_1(self, otherpokemon, move_number)
            y = battles.typeChart_2(self, otherpokemon, move_number)
            z = x * y
            damage = (((((((((self.lvl/5+2)*self.attack*     move_number.power) / otherpokemon.defense)/50)+2)*(     z     ))*randint(217, 255)))/255)
            rounded_damage = round(damage, 0)
            otherpokemon.hp = otherpokemon.hp - rounded_damage
            if otherpokemon.hp <= 0:
                otherpokemon.hp = 0
                return otherpokemon.hp
            print(f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
            return otherpokemon.hp
        else:
            print (f"{self.name} missed!")
        
    def check_pp(self, move):
        if move == "1":
            move_used = self.move_1
        elif move == "2":
            move_used = self.move_2
        elif move == "3":
            move_used = self.move_3
        elif move == "4":
            move_used = self.move_4


        if move_used.pp > 0:
            move_used.pp -= 1
            return move
        elif move_used.pp <= 0: 
            print (f"{move_used.name} has no pp left")
            move = "0"
            return move

    def start_battle_1v1(self, otherpokemon):  
        attacker = input("tell me your name, attacker: ")
        defender = input("tell me your name, defender: ")
        print(f"{self.name} is attacking {otherpokemon.name}!")
        if self.speed > otherpokemon.speed:
            # empieza el atacante
            while (self.hp >= 0) or (otherpokemon.hp >= 0):
                i = 0
                while i == 0:
                    
                    print(f"\n{attacker.title()}, what would you like to do?")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input(f"\n{self.tell_my_moves()}\nWhat move will {self.name} use: ")
                        choose_move = battles.check_pp(self, choose_move)
                        if choose_move == "1":
                            print(f"{self.name} used {self.move_1.name}! {battles.effectiveness(self, otherpokemon, 1)}")
                            battles.attack_damage(self, otherpokemon, 1)
                            i += 1
                        elif choose_move == "2":
                            print(f"{self.name} used {self.move_2.name}! {battles.effectiveness(self, otherpokemon, 2)}")
                            battles.attack_damage(self, otherpokemon, 2)
                            i += 1
                        elif choose_move == "3":
                            print(f"{self.name} used {self.move_3.name}! {battles.effectiveness(self, otherpokemon, 3)}")
                            battles.attack_damage(self, otherpokemon, 3)
                            i += 1
                        elif choose_move == "4":
                            print(f"{self.name} used {self.move_4.name}! {battles.effectiveness(self, otherpokemon, 4)}")
                            battles.attack_damage(self, otherpokemon, 4)
                            i += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"\n{self.name} fainted!")
                    print(f"End of the battle! winner: {defender.title()}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"\n{otherpokemon.name} fainted!")
                    print(f"End of the battle! winner: {attacker.title()}!")
                    return "FIN DE LA BATALLA"
                o = 0
                while o == 0:
                    
                    print(f"\n{defender.title()}, what would you like to do?")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input(f"\n{otherpokemon.tell_my_moves()}\nWhat move will {otherpokemon.name} use: ")
                        choose_move = battles.check_pp(otherpokemon, choose_move)
                        if choose_move == "1":
                            print(f"{otherpokemon.name} used {otherpokemon.move_1.name}! {battles.effectiveness(otherpokemon, self, 1)}")
                            battles.attack_damage(otherpokemon, self, 1)
                            o += 1
                        elif choose_move == "2":
                            print(f"{otherpokemon.name} used {otherpokemon.move_2.name}! {battles.effectiveness(otherpokemon, self, 2)}")
                            battles.attack_damage(otherpokemon, self, 2)
                            o += 1
                        elif choose_move == "3":
                            print(f"{otherpokemon.name} used {otherpokemon.move_3.name}! {battles.effectiveness(otherpokemon, self, 3)}")
                            battles.attack_damage(otherpokemon, self, 3)
                            o += 1
                        elif choose_move == "4":
                            print(f"{otherpokemon.name} used {otherpokemon.move_4.name}! {battles.effectiveness(otherpokemon, self, 4)}")
                            battles.attack_damage(otherpokemon, self, 4)
                            o += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"\n{self.name} fainted!")
                    print(f"End of the battle! winner: {defender.title()}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"\n{otherpokemon.name} fainted!")
                    print(f"End of the battle! winner: {attacker.title()}!")
                    return "FIN DE LA BATALLA"

        else:
            #empieza el defensor
            while (self.hp >= 0) or (otherpokemon.hp >= 0):
                o = 0
                while o == 0:
                    
                    print(f"\n{defender.title()}, what would you like to do?")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input(f"\n{otherpokemon.tell_my_moves()}\nWhat move will {otherpokemon.name} use: ")
                        choose_move = battles.check_pp(otherpokemon, choose_move)
                        if choose_move == "1":
                            print(f"{otherpokemon.name} used {otherpokemon.move_1.name}! {battles.effectiveness(otherpokemon, self, 1)}")
                            battles.attack_damage(otherpokemon, self, 1)
                            o += 1
                        elif choose_move == "2":
                            print(f"{otherpokemon.name} used {otherpokemon.move_2.name}! {battles.effectiveness(otherpokemon, self, 2)}")
                            battles.attack_damage(otherpokemon, self, 2)
                            o += 1
                        elif choose_move == "3":
                            print(f"{otherpokemon.name} used {otherpokemon.move_3.name}! {battles.effectiveness(otherpokemon, self, 3)}")
                            battles.attack_damage(otherpokemon, self, 3)
                            o += 1
                        elif choose_move == "4":
                            print(f"{otherpokemon.name} used {otherpokemon.move_4.name}! {battles.effectiveness(otherpokemon, self, 4)}")
                            battles.attack_damage(otherpokemon, self, 4)
                            o += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"\n{self.name} fainted!")
                    print(f"End of the battle! winner: {defender.title()}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"\n{otherpokemon.name} fainted!")
                    print(f"End of the battle! winner: {attacker.title()}!")
                    return "FIN DE LA BATALLA"

                i = 0
                while i == 0:
                    
                    print(f"\n{attacker.title()}, what would you like to do?")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input(f"\n{self.tell_my_moves()}\nWhat move will {self.name} use: ")
                        choose_move = battles.check_pp(self, choose_move)
                        if choose_move == "1":
                            print(f"{self.name} used {self.move_1.name}! {battles.effectiveness(self, otherpokemon, 1)}")
                            battles.attack_damage(self, otherpokemon, 1)
                            i += 1
                        elif choose_move == "2":
                            print(f"{self.name} used {self.move_2.name}! {battles.effectiveness(self, otherpokemon, 2)}")
                            battles.attack_damage(self, otherpokemon, 2)
                            i += 1
                        elif choose_move == "3":
                            print(f"{self.name} used {self.move_3.name}! {battles.effectiveness(self, otherpokemon, 3)}")
                            battles.attack_damage(self, otherpokemon, 3)
                            i += 1
                        elif choose_move == "4":
                            print(f"{self.name} used {self.move_4.name}! {battles.effectiveness(self, otherpokemon, 4)}")
                            battles.attack_damage(self, otherpokemon, 4)
                            i += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"\n{self.name} fainted!")
                    print(f"End of the battle! winner: {defender.title()}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"\n{otherpokemon.name} fainted!")
                    print(f"End of the battle! winner: {attacker.title()}!")
                    return "FIN DE LA BATALLA"

class moveset:     #to create moves

    def __init__(self, name, type, power, pp, accuracy):
        self.name = name
        self.move_type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp



# move list
razorleaf = moveset("Razor Leaf", "grass", 55, 25, 95)
flamethrower = moveset("Flamethrower", "fire", 90, 24, 100)
water_pulse = moveset("Water pulse", "water", 60, 20, 100)
tackle = moveset("Tackle", "normal", 40, 35, 100)
scratch = moveset("Scratch", "normal", 40, 35, 100)
dragon_pulse = moveset("Dragon Pulse", "dragon", 85, 16, 100)

#character list
bulbasaur = pokemon("Bulbasaur", 5, 21, 11, 11, 11, "grass", "none", razorleaf, razorleaf, razorleaf, razorleaf)

charmander = pokemon("Charmander", 5, 20, 11, 10, 13, "fire", "none", razorleaf, flamethrower, scratch, flamethrower)

charmander.insert_move(1, flamethrower)

squirtle = pokemon("Squirtle", 5, 20, 11, 13, 10, "water", "none", water_pulse, tackle, tackle, tackle)

dragapult = pokemon("Dragapult", 5, 25, 17, 14, 20, "dragon", "ghost", dragon_pulse, dragon_pulse, dragon_pulse, dragon_pulse)

battles.start_battle_1v1(charmander, squirtle)
