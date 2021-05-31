from random import randint

class pokemon:


    def __init__(self, name, lvl, hp, attack, defense, speed, type, move_1, move_2, move_3, move_4):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type = type
        self.move_1 = move_1

        self.move_2 = move_2
        
        self.move_3 = move_3
        
        self.move_4 = move_4

    def insert_move(self, move_number, pokemon_move):
        if move_number == 1:
            self.move_1 = pokemon_move
        elif move_number == 2:
            self.move_2 = pokemon_move
        elif move_number == 3:
            self.move_3 = pokemon_move
        elif move_number == 4:
            self.move_4 = pokemon_move


    def changeName(self, new_name):
        self.name = new_name

    def pkmn_stats(self):
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntype:  {self.type}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2}\n\t{self.move_3}\n\t{self.move_4}\n")

class battles:
    
    def typeChart(self, otherpokemon, move_number):
        if move_number.move_type == "normal" and otherpokemon.type == "rock":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "normal" and otherpokemon.type == "ghost":
            typeCheck = 0
            return typeCheck
        elif move_number.move_type == "normal" and otherpokemon.type == "steel":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "fire":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "water":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "grass":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "ice":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "bug":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "rock":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "dragon":
            typeCheck = 1/2
            return typeCheck
        elif move_number.move_type == "fire" and otherpokemon.type == "steel":
            typeCheck = 2
            return typeCheck
        elif move_number.move_type == "grass" and otherpokemon.type == "fire":
            typeCheck = 1/2
            return typeCheck
        else:
            typeCheck = 1
            return typeCheck

    
    def attack_damage(self, otherpokemon, move_number):
        if move_number == 1:
            move_number = self.move_1
        elif move_number == 2:
            move_number = self.move_2
        elif move_number == 3:
            move_number = self.move_3
        elif move_number == 4:
            move_number = self.move_4
        multiplier = battles.typeChart(self, otherpokemon, move_number)
        
        damage = (((((((((self.lvl/5+2)*self.attack*     move_number.power) / otherpokemon.defense)/50)+2)*(     multiplier     ))*randint(217, 255)))/255)
        rounded_damage = round(damage, 0)
        return rounded_damage

    def start_battle_1v1(self, otherpokemon):
        print(f"{self.name} is attacking {otherpokemon.name}!")
        if self.speed > otherpokemon.speed:
            # empieza el atacante
            while (self.hp >= 0) or (otherpokemon.hp >= 0):
                i = 0
                while i == 0:
                    
                    print("atacante, decime que hacer:")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input("Decime que movimiento vas a elegir:  ")
                        if choose_move == "1":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 1)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        elif choose_move == "2":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 2)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        elif choose_move == "3":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 3)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        elif choose_move == "4":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 4)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {otherpokemon.name}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {self.name}!")
                    return "FIN DE LA BATALLA"
                o = 0
                while o == 0:
                    
                    print("defensor, decime que hacer:")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input("Decime que movimiento vas a elegir:  ")
                        if choose_move == "1":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 1)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        elif choose_move == "2":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 2)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        elif choose_move == "3":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 3)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        elif choose_move == "4":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 4)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {otherpokemon.name}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {self.name}!")
                    return "FIN DE LA BATALLA"

        else:
            #empieza el defensor
            while (self.hp >= 0) or (otherpokemon.hp >= 0):
                o = 0
                while o == 0:
                    
                    print("defensor, decime que hacer:")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input("Decime que movimiento vas a elegir:  ")
                        if choose_move == "1":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 1)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        elif choose_move == "2":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 2)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        elif choose_move == "3":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 3)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        elif choose_move == "4":
                            self.hp = self.hp - battles.attack_damage(otherpokemon, self, 4)
                            print (f"{self.name} has {self.hp}hp left!")
                            o += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {otherpokemon.name}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {self.name}!")
                    return "FIN DE LA BATALLA"

                i = 0
                while i == 0:
                    
                    print("atacante, decime que hacer:")
                    command = input()
                    if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                        choose_move = input("Decime que movimiento vas a elegir:  ")
                        if choose_move == "1":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 1)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        elif choose_move == "2":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 2)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        elif choose_move == "3":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 3)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        elif choose_move == "4":
                            otherpokemon.hp = otherpokemon.hp - battles.attack_damage(self, otherpokemon, 4)
                            print (f"{otherpokemon.name} has {otherpokemon.hp}hp left!")
                            i += 1
                        else:
                            print("wrong command")
                if self.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {otherpokemon.name}!")
                    return "FIN DE LA BATALLA"
                elif otherpokemon.hp <= 0:
                    print(f"Fin de la batalla! Ganador: {self.name}!")
                    return "FIN DE LA BATALLA"

class moveset:

    def __init__(self, name, type, power, pp, accuracy):
        self.name = name
        self.move_type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
    

razorleaf = moveset("Razor Leaf", "grass", 55, 25, 95)
fire_breath = moveset("Fire Breath", "fire", 55, 15, 95)



(bulbasaur) = pokemon("Bulbasaur", 5, 21, 11, 11, 11, "grass", razorleaf, 1, 1, 1)

bulbasaur.pkmn_stats()

(charmander) = pokemon("Charmander", 5, 20, 11, 10, 13, "fire", 40, 1, 1, 1)

charmander.insert_move(1, fire_breath)

charmander.pkmn_stats()



battles.start_battle_1v1(charmander, bulbasaur)