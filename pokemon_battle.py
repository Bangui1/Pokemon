from random import randint
from time import sleep as ts
from sys import stdout as systd
from pandas import read_csv as pd
from pygame import mixer


typechart = pd(r'.\pokemon_battle\test_chart.csv',index_col="att/def") #cambiar el string por el path en donde tienen el type_chart.csv

def print_slow(str):
    for letter in str:
        systd.write(letter)
        systd.flush()
        ts(0.01)

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
        move_number = moveset.move_used(self, move_number)
        
        move_number = pokemon_move

    def tell_my_moves(self):   #movelist
        return f"Your moves are:\n\n\t1.-{self.move_1.name}\n\t2.-{self.move_2.name}\n\t3.-{self.move_3.name}\n\t4.-{self.move_4.name}"

    def nickname(self, new_name): 
        self.name = new_name

    def pkmn_stats(self):     #prints desired pokemon's stats
      if self.type_2 != "none":
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntypes:\n\t{self.type_1}\n\t{self.type_2}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2.name}\n\t{self.move_3.name}\n\t{self.move_4.name}\n")
      else:
        print (f"name: {self.name} \nlevel: {self.lvl} \nhp: {self.hp} \nattack: {self.attack}\ndefense: {self.defense} \nspeed: {self.speed}\ntypes:\n\t{self.type_1}\nmoves: \n\t{self.move_1.name}\n\t{self.move_2.name}\n\t{self.move_3.name}\n\t{self.move_4.name}\n")

class battles(pokemon):
    
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
        move_number = moveset.move_used(self, move_number)
         
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
        
        move_number = moveset.move_used(self, move_number)
        
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
            print_slow(f"{otherpokemon.name} has {otherpokemon.hp} hp left!\n")
            return otherpokemon.hp
        else:
            print_slow(f"{self.name} missed!")
            return ""      
        
    def status_move(self, move_number, otherpokemon):
        if otherpokemon.status_time <= 0:
            # tiene que existir una funcion para los status moves que son acumulables, ej: "Growl"
            if move_number.effect == "sleep":
                affected_time = randint(1, 7)
                otherpokemon.status_time = affected_time
                otherpokemon.status_effect = "sleep"
                print_slow(f"{otherpokemon.name} is affected with {otherpokemon.status_effect}!")
                return 0
            else:
                return 0
        else:
            #tiene que existir una funcion para los status moves que son acumulables, ej: "Growl"
            if move_number.effect == "sleep":
                print_slow(f"{otherpokemon.name} has been already affected with something!")
                return 0
            else:
                return 0
            
        

    def check_pp(self, move):
        if move in range(1,5):

            move_used = moveset.move_used(self, move)

            if move == 0 or move == 1:
                return move
            elif move_used.pp > 0:
                return move
            elif move_used.pp <= 0: 
                print_slow(f"{move_used.name} has no pp left")
                move = 0
                return move
        else:
            return move

    def check_status(self, move):
        if move == 0:
            move = 0
            return move

        if self.status_effect == "sleep":
            ts(1)
            print_slow(f"{self.name} is sleeping!")
            move = 1
            return move
        else:
            return move

    def attack(self, otherpokemon, attacker):
        i = 0
        while i == 0:
            
            print(f"\n{attacker.title()}, what would you like to do?\na.- Attack\nb.- Bag(not working)\nr.- Run(not working)\np.- Pokemon(not working)")
            command = input()
            if ((command.lower()) == "a") or ((command.lower()) == "attack"):
                choose_move = input(f"\n{self.tell_my_moves()}\nWhat move will {self.name} use: ")
                choose_move = battles.check_pp(self, choose_move)
                choose_move = battles.check_status(self, choose_move)
                if choose_move == "1":
                    print_slow(f"{self.name} used {self.move_1.name}! {battles.effectiveness(self, otherpokemon, 1)}\n")
                    ts(1)
                    battles.attack_damage(self, otherpokemon, 1)
                    ts(1)
                    i += 1
                elif choose_move == "2":
                    print_slow(f"{self.name} used {self.move_2.name}! {battles.effectiveness(self, otherpokemon, 2)}\n")
                    ts(1)
                    battles.attack_damage(self, otherpokemon, 2)
                    ts(1)
                    i += 1
                elif choose_move == "3":
                    print_slow(f"{self.name} used {self.move_3.name}! {battles.effectiveness(self, otherpokemon, 3)}\n")
                    ts(1)
                    battles.attack_damage(self, otherpokemon, 3)
                    ts(1)
                    i += 1
                elif choose_move == "4":
                    print_slow(f"{self.name} used {self.move_4.name}! {battles.effectiveness(self, otherpokemon, 4)}\n")
                    ts(1)
                    battles.attack_damage(self, otherpokemon, 4)
                    ts(1)
                    i += 1
                elif choose_move == 0:
                    print_slow("Choose another move!")
                    ts(0.5)
                elif choose_move == 1:
                    print_slow("your pokemon can't move!")
                    ts(1)
                    i += 1
                else:
                    print("wrong command")
                    continue
            else:
                print("wrong command")


    def start_battle_1v1(self, otherpokemon):
        turn = Watcher(1)
        attacker = input("tell me your name, attacker: ")
        defender = input("tell me your name, defender: ")
        print(f"{self.name} is attacking {otherpokemon.name}!")
        mixer.pre_init(44100, 32, 2, 4096)
        mixer.init()
        mixer.music.load(r'.\pokemon_battle\battle_theme.mp3') #add music file path
        mixer.music.play()
        if self.speed > otherpokemon.speed:
            # empieza el atacante
            while (self.hp != 0) or (otherpokemon.hp != 0):
                battles.attack(self, otherpokemon, attacker)
                if otherpokemon.hp <= 0:
                    print_slow(f"\n{otherpokemon.name} fainted!")
                    print_slow(f"End of the battle! winner: {attacker.title()}!")
                    battles.victory_music(self)
                    return turn.variable
                elif self.hp <= 0:
                    print_slow(f"\n{self.name} fainted!")
                    print_slow(f"End of the battle! winner: {defender.title()}!")
                    battles.victory_music(self)
                    return turn.variable
                battles.attack(otherpokemon, self, defender)
                if self.hp <= 0:
                    print_slow(f"\n{self.name} fainted!")
                    print_slow(f"End of the battle! winner: {defender.title()}!")
                    battles.victory_music(self)
                    return turn.variable
                elif otherpokemon.hp <= 0:
                    print_slow(f"\n{otherpokemon.name} fainted!")
                    print_slow(f"End of the battle! winner: {attacker.title()}!")
                    battles.victory_music(self)
                    return turn.variable
                turn.set_value(turn.variable +1, self, otherpokemon)

        else:
            #empieza el defensor
            while (self.hp != 0) or (otherpokemon.hp != 0):
                battles.attack(otherpokemon, self, attacker)
                if otherpokemon.hp <= 0:
                    print_slow(f"\n{otherpokemon.name} fainted!")
                    print_slow(f"\nEnd of the battle! winner: {attacker.title()}!\n")
                    return turn.variable
                elif self.hp <= 0:
                    print_slow(f"\n{self.name} fainted!")
                    print_slow(f"\nEnd of the battle! winner: {defender.title()}!\n")
                    return turn.variable
                battles.attack(self, otherpokemon, defender)
                if self.hp <= 0:
                    print_slow(f"\n{self.name} fainted!")
                    print_slow(f"\nEnd of the battle! winner: {defender.title()}!\n")
                    return turn.variable
                elif otherpokemon.hp <= 0:
                    print_slow(f"\n{otherpokemon.name} fainted!")
                    print_slow(f"\nEnd of the battle! winner: {attacker.title()}!\n")
                    return turn.variable
                turn.set_value(turn.variable+1)

    def choose_pkmn(self, number):
        if number == 1:
            number = charmander
        elif number == 2:
            number = squirtle
        elif number == 3:
            number = bulbasaur
        return number

    def cpu_attack(self, p_pkmn):
        move_chosen = str(randint(1,4))
        move_chosen = battles.check_pp(self, move_chosen)
        move_chosen = battles.check_status(self, move_chosen)
        if move_chosen == "1":
            print_slow(f"Enemy {self.name} used {self.move_1.name}! {battles.effectiveness(self, p_pkmn, 1)}\n")
            ts(1)
            battles.attack_damage(self, p_pkmn, 1)
            ts(1)
            # i += 1
        elif move_chosen == "2":
            print_slow(f"Enemy {self.name} used {self.move_2.name}! {battles.effectiveness(self, p_pkmn, 2)}\n")
            ts(1)
            battles.attack_damage(self, p_pkmn, 2)
            ts(1)
            # i += 1
        elif move_chosen == "3":
            print_slow(f"Enemy {self.name} used {self.move_3.name}! {battles.effectiveness(self, p_pkmn, 3)}\n")
            ts(1)
            battles.attack_damage(self, p_pkmn, 3)
            ts(1)
            # i += 1
        elif move_chosen == "4":
            print_slow(f"Enemy {self.name} used {self.move_4.name}! {battles.effectiveness(self, p_pkmn, 4)}\n")
            ts(1)
            battles.attack_damage(self, p_pkmn, 4)
            ts(1)
            # i += 1
        elif move_chosen == 0:
            print_slow("Choose another move!")
            ts(0.5)
        elif move_chosen == 1:
            print_slow("your pokemon can't move!")
            ts(1)
            # i += 1
        else:
            print("wrong command")
#cambiar ifs por funcion

    def battle_vs_cpu(self):
        turn = Watcher(1)
        player = (input(f'Enter your name, trainer: '))
        print_slow(f'\n1.- Charmander (fire)\n2.- Squirtle (water)\n3.- Bulbasaur (grass)\n')
        pokemon = int(input('Choose your pokemon (enter number): '))
        player_pkmn = battles.choose_pkmn(self, pokemon)
        enemy_pkmn = battles.choose_pkmn(self, randint(1,3))
        print_slow(f'Battle started: {player_pkmn.name} vs {enemy_pkmn.name}')
        mixer.pre_init(44100, 32, 2, 4096)
        mixer.init()
        mixer.music.load(r'.\pokemon_battle\battle_theme.mp3') #add music file path
        mixer.music.play()
        if player_pkmn.speed >= enemy_pkmn.speed:
            while (player_pkmn.hp != 0) and (enemy_pkmn.hp != 0):
                battles.attack(player_pkmn, enemy_pkmn, player)
                if enemy_pkmn.hp <= 0:
                    print_slow(f'\nEnemy {enemy_pkmn.name} fainted!')
                    mixer.music.stop()
                    mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
                    mixer.music.play()
                    print_slow(f'End of the battle! Winner: {player.title()}')
                    ts(11)
                    return turn.variable
                elif player_pkmn.hp <= 0:
                    print_slow(f"\nYour {player_pkmn.name} fainted!")
                    mixer.music.stop()
                    mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
                    mixer.music.play()
                    print_slow(f"End of the battle! winner: {enemy_pkmn.name}!")
                    ts(11)
                    return turn.variable
                battles.cpu_attack(enemy_pkmn, player_pkmn)
                if player_pkmn.hp <= 0:
                    print_slow(f"\nYour {player_pkmn.name} fainted!")
                    mixer.music.stop()
                    mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
                    mixer.music.play()
                    print_slow(f"End of the battle! winner: {enemy_pkmn.name}!")
                    ts(11)
                    return turn.variable
                elif enemy_pkmn.hp <= 0:
                    print_slow(f"\nEnemy {enemy_pkmn.name} fainted!")
                    mixer.music.stop()
                    mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
                    mixer.music.play()
                    print_slow(f"End of the battle! winner: {player.title()}!")
                    ts(11)
                    return turn.variable
                turn.set_value(turn.variable +1, player_pkmn, enemy_pkmn)
        else:
            while (player_pkmn.hp != 0) or (player_pkmn.hp != 0):
                battles.cpu_attack(enemy_pkmn,player_pkmn)
                if enemy_pkmn.hp <= 0:
                    print_slow(f"\nEnemy {enemy_pkmn.name} fainted!")
                    mixer.music.stop()
                    mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
                    mixer.music.play()
                    print_slow(f"\nEnd of the battle! winner: {enemy_pkmn.name}!\n")
                    ts(11)
                    return turn.variable
                elif player_pkmn.hp <= 0:
                    print_slow(f"\nYour {player_pkmn.name} fainted!")
                    mixer.music.stop()
                    mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
                    mixer.music.play()
                    print_slow(f"End of the battle! winner: {enemy_pkmn.name}!")
                    ts(11)
                    return turn.variable
                battles.attack(player_pkmn, enemy_pkmn, player)
                if player_pkmn.hp <= 0:
                    print_slow(f"\nYour {player_pkmn.name} fainted!")
                    print_slow(f"End of the battle! winner: {enemy_pkmn.name}!")
                    return turn.variable
                elif enemy_pkmn.hp <= 0:
                    print_slow(f"\nEnemy {enemy_pkmn.name} fainted!")
                    print_slow(f"End of the battle! winner: {player.title()}!")
                    return turn.variable
                turn.set_value(turn.variable +1)
        
    def victory_music(self):
        mixer.music.stop()
        mixer.music.load(r'.\pokemon_battle\victory_theme.mp3')
        mixer.music.play()
        ts(15)

class moveset:     #to create moves

    def __init__(self, name, attack_type, type, power, pp, accuracy, effect):
        self.name = name
        self.attack_type = attack_type
        self.move_type = type
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect

    def move_used(self, move_num):
        move_num = int(move_num)
        move_number = move_num
        if move_num < 1 and move_num > 4:
            move_number = str(move_num)

        if move_num == 1:
            move_number = self.move_1
        elif move_num == 2:
            move_number = self.move_2
        elif move_num == 3:
            move_number = self.move_3
        elif move_num == 4:
            move_number = self.move_4
        return move_number


# move list
razorleaf = moveset("Razor Leaf", "physical", "grass", 55, 25, 95, "none")
flamethrower = moveset("Flamethrower", "special", "fire", 90, 24, 100, "none")
water_pulse = moveset("Water pulse", "special", "water", 60, 20, 100, "none")
tackle = moveset("Tackle", "physical", "normal", 40, 35, 100, "none")
scratch = moveset("Scratch", "physical", "normal", 40, 0, 100, "none")
dragon_pulse = moveset("Dragon Pulse", "special", "dragon", 85, 16, 100, "none")
sing = moveset("Sing", "status", "normal", 0, 16, 55, "sleep")
ember = moveset("Ember", "special", "fire", 40, 25, 100, "none")
slash = moveset("Slash", "physical", "normal", 70, 20, 100, "none")
bubble = moveset("Bubble", "special", "water", 40, 30, 100, "none")

#character list
bulbasaur = pokemon("Bulbasaur", 5, 21, 11, 11, 13, 13, 11, "grass", "none", tackle, razorleaf, razorleaf, razorleaf)
charmander = pokemon("Charmander", 5, 20, 11, 10, 12, 11, 13, "fire", "none", scratch, flamethrower, ember, slash)
squirtle = pokemon("Squirtle", 5, 20, 11, 13, 11, 12, 10, "water", "none", scratch, bubble, water_pulse, tackle)
dragapult = pokemon("Dragapult", 5, 25, 17, 14, 16, 14, 20, "dragon", "ghost", dragon_pulse, dragon_pulse, dragon_pulse, dragon_pulse)



battles.start_battle_1v1(charmander, squirtle)
# battles.start_battle_1v1(dragapult, bulbasaur)
# battles.battle_vs_cpu()
