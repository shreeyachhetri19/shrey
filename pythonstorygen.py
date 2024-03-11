import random
def adventure():
    Starter=["In the realm of Eldoria",
             "In a quaint village nestled at the edge of an enchanted forest, lived two unlikely friends",
             "In the bustling port town of Seabrook, two friends,",
             "In the ancient kingdom of Arantha, nestled amidst misty mountains and whispering forests,",
             "In the bustling city of Arcadia,"]
    characters=[" Aria, an elven warrior, and Finn, a mischievous gnome",
                "Lena, a bold mage, and Milo, her cautious alchemist friend,",
                "Emma, a skilled navigator, and Lucas, a charismatic sailor,",
                "two companions, Eira, a skilled swordswoman, and Kael, a cunning rogue,",
                "two friends, Maya, a talented inventor, and Liam, a skilled locksmith"]
    plot=["set out to uncover the legendary Crystal Cavern,they faced perilous forests and treacherous mountains, forging a bond as they journeyed",
          " ventured into the enchanted forest in search of a fabled artifact",
          "rumors whispered of a lost treasure hidden on a remote island, guarded by ancient secrets and treacherous waters known as the ONE PIECE",
          "ventured into the Labyrinth of Shadows in search of treasure",
          "they embarked on a quest to unlock the mysteries of an ancient clock tower rumored to hold a powerful artifact,"]
    journey=[" where they confronted mystical guardians and cunning traps",
             "they braved treacherous paths and ancient ruins,",
             "they set sail aboard their trusty ship named as the Going Merry,",
             "their journey began when whispers of a hidden treasure led them to the mysterious Labyrinth of Shadows ",
             "they journeyed through the city's labyrinthine streets to reach the tower,"]
    action=["they encountered a fearsome dragon. With courage and skill, they defeated the beast",
            "with wit and courage overcoming trials set by the forest guardian",
            " a rival crew, led by the notorious Captain Blackbeard, sought to claim the treasure for themselves",
            "they faced deadly traps and spectral foes",
            "they encountered intricate mechanisms and cunning puzzles, each designed to guard the tower's secrets"]
    plot_twist=["they realized that their greatest treasure was their friendship",
                "they proved their worth and were rewarded with the Heartstone, a powerful crystal",
                "in a heart-pounding showdown,they outsmarted their adversaries, emerging victorious",
                "they confronted a malevolent sorcerer",
                " they finally unlocked the artifact, unleashing its power to restore hope to the city."]
    end=["With hearts full of triumph, they ventured forth, ready for new adventures together.",
         "with the sun setting behind them, casting a golden glow upon the endless sea, they sailed into the horizon, ready to write the next chapter of their epic journey.",
         "so they again set out to face whatever challenges awaited them, ready to write their own destiny.",
         "they realized that sometimes, the greatest treasures are found not in riches, but in the bonds of friendship."]
    print(random.choice(Starter)+" "+random.choice(characters)+" "+random.choice(plot)+" "+random.choice(journey)+" "+random.choice(action)+" "+random.choice(plot_twist)+" "+random.choice(end))

def romance():
    starter=["Long time ago,",
             "Once upon a time",
             "On a sunday afternoon,"]
    place=["in a crowded subway train",
           "in a bustling cafè",
           "caught in a sudden downpour",
           "in a quiet library",
           "in a quiet park"]
    bond=["initially quiet,out of boredom",
          "hailing from different places",
          "with time to spare",
          "initially focused on themselves"]
    connection=["there were two strangers who connected through their interest in reading",
                "there were two aspiring artists who found themselves drawn to each other",
                "there were two childhood swearthearts who connected in no time"]
    moment=["and amidst laughters and silly talks",
            "and sharing old stories and laughters",
            "with sharing of laughters,music and quiet moment of reflections",
            "and with the desire to connect more and more"]
    more=["they discovered a surprsing chemistry",
          "created a bond that withstands every hurdle",
          "they nurtured a growing affection for each other",
          "layed the foundation of a budding romance"]
    ending=["and discovered that love can be found in the most graceful moments.",
            "and they realised the greatest adventure of all is falling in love.",
            "and they realised that love comes when you least expect it."]
    print(random.choice(starter)+" "+random.choice(place)+" "+random.choice(bond)+" "+random.choice(connection)+" "+random.choice(moment)+" " +random.choice(more)+" "+random.choice(ending))
   
def horror():
    Starter=["In the depths of the forest stood an old mansion, abandoned and cursed.",
             "For years, the townsfolk whispered tales of the mansion being haunted by the ghost of a young girl who had tragically perished within its walls.",
             "In the heart of the Appalachian Mountains, there was a secluded valley shrouded in mist and mystery.",
             "In a remote village",
             "In the depths of the forest",
             " As the mansion came closer , its looming silhouette seemed to mock them, its windows like empty eyes peering into their souls.",
             ]
    Characters=[ " a group of six friends set out for a retreat at the lodge, seeking solace from the stresses of modern life.",
                " a group of friends sets up camp for the night, unaware of the ancient curse that haunts the woods.",
                " a young woman finds an old journal hidden beneath the floorboards, who then shows them to her friends",
                " a group of five friends—Alex, Sarah, Matt, Emily, and Jake—decided to spend a weekend exploring the abandoned estate.",]
    plot=[" Whispers drifted through the halls of the lodge, faint and indistinct, like echoes from a distant past.",
          " As darkness falls, strange noises echo through the trees, and a sense of dread settles over the campsite",
          "In the center of the room lay a mirror, its surface warped and twisted like a window into madness"]
    scare=[" One by one, they began to experience vivid nightmares—dreams filled with darkness and despair, where malevolent forces lurked just beyond the edge of consciousness. ",
           " One by one, the friends vanish into the night, leaving behind only whispers of their fate.",
           " Strange occurrences soon plagued their stay—whispers echoed through the halls, shadows danced in the corners of their vision, and the air grew heavy with dread",
           " The sound of footsteps echoing through the empty corridors, growing louder with each passing moment."]
    end=[" Unaware of the horrors that await them in the depths of the haunted house.",
         " The realization hits too late that the past is not as distant as it seems, and that it holds secrets that refuse to stay buried.",
         " falling prey to the vengeful spirits, their screams echoed throughout the area as they were dragged into the darkness."]
    print (random.choice(Starter)+" "+random.choice(Characters)+" "+random.choice(plot)+" "+random.choice(scare)+" "+random.choice(end))

def mystery():
    starter=["The small town of Millfield was in a state of shock",
             "The old bookstore on Elm Street held a peculiar allure",
             "The abandoned amusement park had always been a place of joy",
             "The vintage typewriter, clacking away in the corner of the dimly lit antique shop, seemed to be crafting its own mysterious narrative",]
    char=["as Detective Reynolds cautiously stepped through the rusty turnstile as he investigate",
          "As Detective Alex Mercer inquired",
          "Detective Olivia Turner stood before the dilapidated mansion",
          "Detective Thomas Barnes, a seasoned investigator with a keen eye for detail.",]
    plot=["The townsfolk wary of the silence share only whispers about a long-forgotten legend that might hold the key to the disappearance",
          "On the eve of a grand exhibition showcasting, the professor is found dead in his workshop, and the prized invention is missing",
          "The great novelist is found murdered in his study under peculiar circumstances. The room is locked from the inside, and the only clue is a cryptic message scrawled in invisible ink.",
          "The Willowbrook Emerald, disappears from its display case in the town's museum. The emerald, said to be imbued with mystical powers",]
    clues = ["A torn piece of a mysterious letter","a blood-stained glove", "a hidden trapdoor","a cryptic message on the wall"]
    end_plot=["with the help of the clue gathered by the detective,he was able to summarize the culprit as Mr.White",
              "as all the clues fell into place the detective found Mr.Brown's alibi a bit suspicious.He was then interrogated and was found guilty of the charges",
              "there was nothing more to be said as the culprit came up and confessed about his wrong doings",
              "the detective himself was the culprit and he never let anyone find it out with the help of his high intellect",
              "the detective was actually a quack and never found out who the culprit was but ate all the money that came from it.",
              "the detective could tell just from the first look that the victim was just faking their crime.",
              "there was a huge plot twist as the detective found out that the victim was not the actual identity of the victim and it was the culprit who was posing as the victim's family members who was later found dead in the forest"]
    print(random.choice(starter)+" "+random.choice(char)+" "+random.choice(plot)+" "+random.choice(clues)+" "+random.choice(end_plot))

print("Select a genre for your story")
while(True):
    print("1.Horror\n2.Romance\n3.Adventure\n4.Mystery\n5.To exit enter 5")
    user=int(input("Enter number here"))
    if user==1:
        horror()
    elif user==2:
        romance()
    elif user==3:
        adventure()
    elif user==4:
        mystery()
    elif(user==5):
        exit(0)
    else:
        print("Invalid Input!!!")