strength = ["Abaddon", "Alchemist", "Axe", "Beastmaster",
           "Brewmaster", "Bristleback", "Centaur Warrunner", "Chaos Knight",
           "Clockwerk", "Doom", "Dragon Knight", "Earth Spirit",
           "Earthshaker", "Elder Titan", "Huskar", "Io",
           "Kunkka", "Legion Commander", "Lifestealer", "Lycan",
           "Magnus", "Mars", "Night Stalker", "OmniKnight",
           "Phoenix", "Pudge", "Sand King", "Slardar",
           "Snapfire", "Spirit Breaker", "Sven", "Tidehunder",
           "Timbersaw", "Tiny", "Treant Protector", "Tusk",
           "Underlord", "Undying", "Wraith King"]

agility = ["Anti-Mage", "Arc Warden", "Bloodseeker", "Bounty Hunter",
           "Broodmother", "Clinkz", "Drow Ranger", "Ember", "Faceless Void",
           "Gyrocopter", "Juggernaut", "Lone Druid", "Luna",
           "Medusa", "Meepo", "Mirana", "Monkey King",
           "Morphling", "Naga Siren", "Nyx Assassin", "Pangolier",
           "Phantom Assasin", "Phantom Lancer", "Razor", "Riki",
           "Shadow Fiend", "Slark", "Sniper", "Spectre",
           "Templar Assasin", "Terrorblade", "Troll Warlord", "Ursa",
           "Vengeful Spirit", "Venomancer", "Viper", "Weaver"]

intelligence = ["Ancient Apparition", "Bane", "Batrider", "Chen",
                "Crystal Maiden", "Dark Seer", "Dark Willow", "Dazzle",
                "Death Propthet", "Disruptor", "Enchantress", "Enigma",
                "Grimstroke", "Invoker", "Jakiro", "Keeper of the light",
                "Leshrac", "Lich", "Lina", "Lion",
                "Nature's Prohet", "Necrophos", "Ogre Magi", "Oracle",
                "Outworld Devourer", "Puck", "Pugna", "Queen Of Pain",
                "Rubick", "Shadow Demon", "Shadow Shanam", "Silencer",
                "Skywrath Mage", "Storm Spirit", "Techies", "Tinker",
                "Visage", "Void Spirit", "Warlock", "Windranger",
                "Winter Wyvern", "Witch Doctor", "Zeus"]


import random
from random import *

print("It's my programm for Dota 2")
print("")

while (True):
    print(" Interface:")
    print("   1 - single draft")
    print("   2 - all random")
    print("")
    tmp = int(input(" Input number:"))
    print("") 
    if (tmp == 1):
        s = choice(strength)
        a = choice(agility)
        i = choice(intelligence)
        print("  strength: ", s)
        print("  agility: ", a)
        print("  intelligence: ", i)
    if (tmp == 2):
        s = choice(strength)
        a = choice(agility)
        i = choice(intelligence)
        print("  your hero: ", choice([s, a, i]))
    print("")
    print("") 
    print("**********************************")
    print("")
    print("") 

print("strength: ", s)
print("agility: ", a)
print("intelligence: ", i)
