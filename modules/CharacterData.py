import json
import os

#random notes
#in data folder (beside main.py):
#    - characters folder:
#        - characterjson
#        - character icon



#-----------
#PLEASE REDO THIS
#simplify all this
#just have a json of 
#- particulars
#- attributes array
#- skills
#- strength array
#- reflex array
#- intelligence array
JUST STREAMLINE THIS. THIS IS TOO COMPLICATED
#-----------



#this class handles all character data related things
#get correct amount of rolls
class CharacterData:
    def __init__(self):
        #create a dictionary of dictionaries, containing all character jsons
        self.list_of_characters = {}

    def load_characters(self):
        #this func loads list_of_characters from data directory

        #get list of character names
        list_of_character_names = []
        list_of_character_directories = [x[0] for x in os.walk('../data/characters/')]
        for i in list_of_character_directories:
            dir_split = i.split('/')
            list_of_character_names.append(dir_split[len(dir_split)-1])
        list_of_character_names.pop(0) #remove first element of list

        #create dictionary keys for each character name
        for i in list_of_character_names:
            self.list_of_characters[i] = ""

        #for every character load their json
        for character in self.list_of_characters:
            #load json
            file = open('../data/characters/' + character + '/' + character + ".json")
            loaded_json = json.load(file)
            file.close()
            #append json to list_of_characters
            self.list_of_characters[character] = loaded_json

    def get_amount_of_dice(character_name, roll_name):
        #get approriate data dict
        curr_dict = list_of_characters[character_name]
        roll_count = 0
        #get raw dicegcount
        #add root attribute dice count
        #add base dice
        return roll_count
        pass


temp = CharacterData()
temp.load_characters()
print(temp.list_of_characters)
