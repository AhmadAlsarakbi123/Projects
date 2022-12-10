# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def listSkills(val, list=[]):
    list.append(val)
    return list

def func1(c, k):
    c.test = c.test + 1
    k = k + 1

class plus:
    def __init__(self):
        self.test = 0
class Welcome:
    def __init__(self,name):
        self.name = name

    def __add__(self, other):
        skills = self.name + other.name
        print("i am here")
        return Welcome(skills)

    def __str__(self):
        print("ss")
        return "test"

    def say(self):
        print('welcome', self.name)


def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

def convert_sources_into_array ():
    original = open('bestiary-complete.json', 'r')
    d = json.load(original)
    monsters = []

    for source in d:
        for monster in source['monster']:
            if 'ac' in monster:
                if len(monster) == 2:
                    temp = monster['ac'][0]
                    monster['ac'][0] = monster['ac'][1]
                    monster['ac'][1] = temp
                    monsters.append(monster)
                elif isinstance(monster['ac'][0], dict):
                    if 'special' in monster['ac'][0]:
                        print(monster['ac'][0])
                    else:
                        monsters.append(monster)
                elif isinstance(monster['ac'][0], str):
                    monster['ac'][0] = {'ac': monster['ac'][0], 'from': ['natural armor']}
                    monsters.append(monster)
                elif isinstance(monster['ac'][0], int):
                    monster['ac'][0] = {'ac': monster['ac'][0], 'from': ['natural armor']}
                    monsters.append(monster)
    for index, monster in enumerate(monsters):
        if 'cr' in monster:
            if isinstance(monster['cr'], dict):
                print(monster['cr'])
                monsters[index]['cr'] = monster['cr']['cr']
    destination = open('bestiary-complete-only-monsters.json', 'w')
    json.dump(monsters, destination)

def count_monsters():
    original = open('bestiary-complete-only-monsters.json', 'r')
    d = json.load(original)
    return len(d)

def get_monsters():
    original = open('bestiary-complete-only-monsters.json', 'r')
    return original

def calculate_modifier_from_ab_score(score):
    return (score - 10) / 3

if __name__ == '__main__':
    df = pd.read_json(get_monsters())
    print(df.info())
    total_bonus = 0
    count = 0
    for index, row in df.iterrows():
        if row['cr'] == '3':
            bonus = 0
            bonus += calculate_modifier_from_ab_score(row['str']) if row['str'] > 5 else 0
            bonus += calculate_modifier_from_ab_score(row['dex']) if row['dex'] > 5 else 0
            bonus += calculate_modifier_from_ab_score(row['con']) if row['con'] > 5 else 0
            bonus += calculate_modifier_from_ab_score(row['int']) if row['int'] > 5 else 0
            bonus += calculate_modifier_from_ab_score(row['wis']) if row['wis'] > 5 else 0
            bonus += calculate_modifier_from_ab_score(row['cha']) if row['cha'] > 5 else 0
            total_bonus += bonus
            count += 1
            if bonus > 6:
                print(str(bonus) + "larger than 6")
                print(row['str'])
                print(row['dex'])
                print(row['con'])
                print(row['int'])
                print(row['wis'])
                print(row['cha'])
            if bonus < 4:
                print(str(bonus) + "smaller than 4")
                print(row['str'])
                print(row['dex'])
                print(row['con'])
                print(row['int'])
                print(row['wis'])
                print(row['cha'])
    print(total_bonus / count)
    print(count)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
