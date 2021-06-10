from random import randint
import pandas as pd

typechart = pd.read_csv(r'D:\Codigos\test_chart.csv', index_col= "att/def") #cambiar el string por el path en donde tienen el type_chart.csv

class Watcher:

    def __init__(self, value):
        self.variable = value
    
    def set_value(self, new_value, pokemon_, otherpokemon):
        if self.variable != new_value:
            self.pre_change(pokemon_, otherpokemon)
            self.variable = new_value
            self.post_change(pokemon_, otherpokemon)
            
    def pre_change(self, pokemon_, otherpokemon):
        if pokemon_.status_time == 0:
            pokemon_.status_effect = "none"
        if otherpokemon.status_time == 0:
            otherpokemon.status_effect = "none"
        
    def post_change(self, pokemon_, otherpokemon):
        if pokemon_.status_time > 0:
            pokemon_.status_time -= 1
        if otherpokemon.status_time > 0:
            otherpokemon.status_time -= 1

class pokemon:


    def __init__(self, name, lvl, hp, attack, defense, sp_attack, sp_defense, speed, type_1, type_2, move_1, move_2, move_3, move_4):    #to create a pokemon
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.type_1 = type_1
        self.type_2 = type_2
        self.move_1 = move_1
        self.move_2 = move_2
        self.move_3 = move_3
        self.move_4 = move_4
        self.status_effect = "none"
        self.status_time = 0

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
      if self.type_2 != "none":
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntypes:\n\t{self.type_1}\n\t{self.type_2}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2.name}\n\t{self.move_3.name}\n\t{self.move_4.name}\n")
      else:
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntypes:\n\t{self.type_1}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2.name}\n\t{self.move_3.name}\n\t{self.move_4.name}\n")

class battles:
    
    def typeChart_1 (self, otherpokemon, move_number):
        
        z = typechart[otherpokemon.type_1][move_number.move_type]
        return z

    def typeChart_2 (self, otherpokemon, move_number):                
        
        if otherpokemon.type_2 != "none":
            z = typechart[otherpokemon.type_2][move_number.move_type]
        else:
            z = 1
        return z
    
    def effectiveness(self, otherpokemon, move_number):
        if move_number == 1:
            move_number = self.move_1
        elif move_number == 2:
            move_number = self.move_2
        elif move_number == 3:
            move_number = self.move_3
        elif move_number == 4:
            move_number = self.move_4 
        if move_number.attack_type == "status":
            return ""
        else:
            x = battles.typeChart_1(self, otherpokemon, move_number)
            y = battles.typeChart_2(self, otherpokemon, move_number)        
            z = x * y        
            if z > 1:
                return "It's super effective!"
            elif z < 1 and z > 0:
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
        move_number.pp -= 1
        
        if acc_check < acc:
            x = battles.typeChart_1(self, otherpokemon, move_number)
            y = battles.typeChart_2(self, otherpokemon, move_number)
            z = x * y
            if move_number.attack_type == "physical":
                damage = (((((((((self.lvl/5+2)*self.attack*move_number.power)/otherpokemon.defense)/50)+2)*(z))*randint(217, 255)))/255)
            elif move_number.attack_type == "special":
                damage = (((((((((self.lvl/5+2)*self.sp_attack*move_number.power)/otherpokemon.sp_defense)/50)+2)*(z))*randint(217, 255)))/255)
            elif move_number.attack_type == "status":
                damage = battles.status_move(self, move_number, otherpokemon)


            rounded_damage = int(round(damage, 0))
            otherpokemon.hp = otherpokemon.hp - rounded_damage
            if otherpokemon.hp <= 0:
                otherpokemon.hp = 0
                return otherpokemon.hp
            print(f"{otherpokemon.name} has {otherpokemon.hp} hp left!")
            return otherpokemon.hp
        else:
            print (f"{self.name} missed!")
            return ""      
        
    def status_move(self, move_number, otherpokemon):
        if otherpokemon.status_time <= 0:
            #tiene que existir una funcion para los status moves que son acumulables, ej: "Growl"
            if move_number.effect == "sleep":
                affected_time = randint(1, 7)
                otherpokemon.status_time = affected_time
                otherpokemon.status_effect = "sleep"
                print(f"{otherpokemon.name} is affected with {otherpokemon.status_effect}!")
                return 0
            else:
                return 0
        else:
            #tiene que existir una funcion para los status moves que son acumulables, ej: "Growl"
            if move_number.effect == "sleep":
                print(f"{otherpokemon.name} has been already affected with something!")
                return 0
            else:
                return 0
            
    def check_pp(self, move):
        if move == "1":
            move_used = self.move_1
        elif move == "2":
            move_used = self.move_2
        elif move == "3":
            move_used = self.move_3
        elif move == "4":
            move_used = self.move_4
        else:
            move_used = move


        if move == 0 or move == 1:
            return move
        elif move_used.pp > 0:
            return move
        elif move_used.pp <= 0: 
            print (f"{move_used.name} has no pp left")
            move = 0
            return move

    def check_status(self, move):
        if move == 0:
            move = 0
            return move

        if self.status_effect == "sleep":
            print(f"{self.name} is sleeping!")
            move = 1
            return move
        else:
            return move

    def attacker(self, otherpokemon, attacker):
        i = 0
        while i == 0:
            
            print(f"\n{attacker.title()}, what would you like to do?")
            command = input()
            if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                choose_move = input(f"\n{self.tell_my_moves()}\nWhat move will {self.name} use: ")
                choose_move = battles.check_pp(self, choose_move)
                choose_move = battles.check_status(self, choose_move)
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
                elif choose_move == 0:
                    print("Choose another move!")
                elif choose_move == 1:
                    print("your pokemon can't move!")
                    i += 1
                else:
                    print("wrong command")
            else:
                print("wrong command")


    def defender(self, otherpokemon, defender):
        o = 0
        while o == 0:
            
            print(f"\n{defender.title()}, what would you like to do?")
            command = input()
            if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                choose_move = input(f"\n{otherpokemon.tell_my_moves()}\nWhat move will {otherpokemon.name} use: ")
                choose_move = battles.check_pp(otherpokemon, choose_move)
                choose_move = battles.check_status(otherpokemon, choose_move)
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
                elif choose_move == 0:
                    print("Choose another move!")
                elif choose_move == 1:
                    print("your pokemon can't move!")
                    o += 1
                else:
                    print("wrong command")
            else:
                print("wrong command")


    def start_battle_1v1(self, otherpokemon):
        turn = Watcher(1)
        attacker = input("tell me your name, attacker: ")
        defender = input("tell me your name, defender: ")
        print(f"{self.name} is attacking {otherpokemon.name}!")
        if self.speed > otherpokemon.speed:
            # empieza el atacante
            while (self.hp != 0) or (otherpokemon.hp != 0):
                battles.attacker(self, otherpokemon, attacker)
                battles.defender(self, otherpokemon, defender)
                if self.hp <= 0:
                    print(f"\n{self.name} fainted!")
                    print(f"End of the battle! winner: {defender.title()}!")
                    return turn.variable
                elif otherpokemon.hp <= 0:
                    print(f"\n{otherpokemon.name} fainted!")
                    print(f"End of the battle! winner: {attacker.title()}!")
                    return turn.variable
                turn.set_value(turn.variable +1, self, otherpokemon)
        else:
            #empieza el defensor
            while (self.hp != 0) or (otherpokemon.hp != 0):
                battles.defender(self, otherpokemon, attacker)
                battles.attacker(self, otherpokemon, defender)
                if self.hp <= 0:
                    print(f"\n{self.name} fainted!")
                    print(f"End of the battle! winner: {defender.title()}!")
                    return turn.variable
                elif otherpokemon.hp <= 0:
                    print(f"\n{otherpokemon.name} fainted!")
                    print(f"End of the battle! winner: {attacker.title()}!")
                    return turn.variable
                turn.set_value(turn.variable+1)


class moveset:     #to create moves

    def __init__(self, name, attack_type, type, power, pp, accuracy, effect):
        self.name = name
        self.attack_type = attack_type
        self.move_type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect



# move list
razorleaf = moveset("Razor Leaf", "physical", "grass", 55, 25, 95, "none")
flamethrower = moveset("Flamethrower", "special", "fire", 90, 24, 100, "none")
water_pulse = moveset("Water pulse", "special", "water", 60, 20, 100, "none")
tackle = moveset("Tackle", "physical", "normal", 40, 35, 100, "none")
scratch = moveset("Scratch", "physical", "normal", 40, 35, 100, "none")
dragon_pulse = moveset("Dragon Pulse", "special", "dragon", 85, 16, 100, "none")
sing = moveset("Sing", "status", "normal", 0, 16, 55, "sleep")

#character list
bulbasaur = pokemon("Bulbasaur", 5, 21, 11, 11, 13, 13, 11, "grass", "none", tackle, razorleaf, razorleaf, razorleaf)
charmander = pokemon("Charmander", 5, 20, 11, 10, 12, 11, 13, "fire", "none", scratch, flamethrower, scratch, flamethrower)
squirtle = pokemon("Squirtle", 5, 20, 11, 13, 11, 12, 10, "water", "none", sing, tackle, tackle, tackle)
dragapult = pokemon("Dragapult", 5, 25, 17, 14, 16, 14, 20, "dragon", "ghost", dragon_pulse, dragon_pulse, dragon_pulse, dragon_pulse)

battles.start_battle_1v1(charmander, squirtle)
