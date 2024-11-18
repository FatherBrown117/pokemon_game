# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jack Hawkins
#               Levi Brown
#               Ajith Bandlapalli
# Section:      209
# Assignment:   Team Lab 13
# Date:         11 / 15 / 2024

from random import *
import os

def option(num_options):
   val = input("Select an option: ")


   valid=False
   while not valid:
       for i in range(num_options):
           if(val==str(i+1)):
               valid=True
       if valid:
           return (val)
       val = input("Invalid input! Try again: ")




def player_select():
   print("--------------------------- PLAYER SELECT ---------------------------\n1.Create new profile\n2.Open existing profile")
   val=option(2)
   name = input("Enter player name: ")
   if(val=="1"):
       game_file=open(f"{name}.txt", "w")
       game_file.write('candy: \npotions: \n')
       game_file.write("1 Pokemon: ")
       poke_num=randint(1,151)
       for pokemon in poke_list:
           if pokemon[0]==str(poke_num): #format of storage ex: 1 Pokemon: Name Lvl. CP.
               game_file.write(f"{pokemon[1]} 1 ")
               game_file.write(f'{pokemon[2]}\n')
       game_file.close()
       return name
   elif(val=='2'):


       return name


def display_pokemon():
    '''Displays current player's list of Pokemon
    Input: none
    Output: none
    '''
    global name

    poke_list = []
    game_file_holder = open(f"{name}.txt", "r")
    game_file_holder.readline()
    game_file_holder.readline()
    game_file = game_file_holder.readlines()
    print('''--------------------------- MAIN MENU ---------------------------
    Index | Pokemon | level | combat power''')
    for line in game_file:
        line = line.strip().split()
        if line[1] == 'Pokemon:':
            print(f'    {line[0]:^6} {line[2]:^9} {line[3]:^7} {line[4]:^13}\n')
            poke_list.append(line)

    print('\nType 1 to select a Pokemon. Type 2 to exit this menu.')
    val = option(2)
    if val == '1':
        print('\nType the index of the Pokemon to be selected.')
        val2 = option(len(poke_list))

        for line in poke_list:
            pass

    else:
        main_menu()


def main_menu():
   print("--------------------------- MAIN MENU ---------------------------\n1. View current Pokemon\n2. Catch a new Pokemon\n3. Player select")
   val = option(3)

   if val == '1':
       display_pokemon()

#Program starts running here
os.system('cls')
poke_file=open("PokeList_v3.csv", "r")
poke_file.readline()
poke_list=poke_file.readlines()

for i in range(len(poke_list)):
   poke_list[i]=poke_list[i].strip().split(",")

name = player_select()
main_menu()


