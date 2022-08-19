#!/usr/bin/env python3

# """Author: Eric Flores
#    Random Poem Generator program. This program will generate a pool of poems
#    that the user can then randomly print in teh console."""

import os
import random
from time import sleep

# Writting the poems as .txt files to be randomly selected by the program.
# Files are generated when the program is run and stored in a local directory


def poem_gen():
    # """Writes the poems and saves them in a local directory"""

    poem1_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_1.txt'
    with open(poem1_path, 'w', encoding="utf-8") as poem1:
        poem1.write(' \n')
        poem1.write('"Change carreers they said\n')
        poem1.write('It will be good for your family they said\n')
        poem1.write('Lots of money in coding they said\n')
        poem1.write('What good is it if I\'m dead"\n')
        poem1.write('  - Eric Flores')

    poem2_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_2.txt'
    with open(poem2_path, 'w', encoding="utf-8") as poem2:
        poem2.write(' \n')
        poem2.write('"There was a young fellow who thought\n')
        poem2.write('Very little but thought it a lot.\n')
        poem2.write('Then at long last he knew\n')
        poem2.write('What he wanted to do,\n')
        poem2.write('But before he could start, he forgot"\n')
        poem2.write('  - Irish Limerick')

    poem3_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_3.txt'
    with open(poem3_path, 'w', encoding="utf-8") as poem3:
        poem3.write(' \n')
        poem3.write('"I scaffolded it\n')
        poem3.write('I coded it\n')
        poem3.write('I refactored it\n')
        poem3.write('I tested it\n')
        poem3.write('I deployed it\n')
        poem3.write('I need a beer"\n')
        poem3.write('  - Stephen Belovarich')

    poem4_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_4.txt'
    with open(poem4_path, 'w', encoding="utf-8") as poem4:
        poem4.write(' \n')
        poem4.write('"You don\'t open source your code\n')
        poem4.write(' Because it makes you money.\n')
        poem4.write(' I don\'t open source my code\n')
        poem4.write(' Because it is embarrassing\n')
        poem4.write(' We are not the same"\n')
        poem4.write('  - Reddit user 4gedN5stars')

    poem5_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_5.txt'
    with open(poem5_path, 'w', encoding="utf-8") as poem5:
        poem5.write(' \n')
        poem5.write('"Beans, beans\n')
        poem5.write('The magical fruit\n')
        poem5.write('The more you eat,\n')
        poem5.write('The more you toot"\n')
        poem5.write('  - Author lost to the winds of time')

    poem6_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_6.txt'
    with open(poem6_path, 'w', encoding="utf-8") as poem6:
        poem6.write(' \n')
        poem6.write('"Do you carrot all for me?\n')
        poem6.write('My heart beets for you,\n')
        poem6.write('With your turnip nose\n')
        poem6.write('And your radish face,\n')
        poem6.write('Your are a peach.\n')
        poem6.write('If we cantaloupe,\n')
        poem6.write('Lettuce marry:\n')
        poem6.write('Weed make a swell pear."\n')
        poem6.write('  - Unknown Pun Lover probably')

    poem7_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_7.txt'
    with open(poem7_path, 'w', encoding="utf-8") as poem7:
        poem7.write(' \n')
        poem7.write('"I never saw a Purple Cow,\n')
        poem7.write('I never hope to see one;\n')
        poem7.write('But I can tell you, anyhow,\n')
        poem7.write('I\'d rather see than be one."\n')
        poem7.write('  - Gelett Burgess')

    poem8_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_8.txt'
    with open(poem8_path, 'w', encoding="utf-8") as poem8:
        poem8.write(' \n')
        poem8.write('"Larry came into my bar\n')
        poem8.write('Every day to drink two beers.\n')
        poem8.write('"My brother’s dying; one\'s for him,"\n')
        poem8.write('He said, his eyes full of tears.\n')
        poem8.write(' \n')
        poem8.write('One day he orders just one.\n')
        poem8.write('His brother\'s dead, I\'m thinking.\n')
        poem8.write('I asked him, but he replied,\n')
        poem8.write('"No, it\'s me; I\'ve given up drinking""\n')
        poem8.write('  - Joanna Fuchs')

    poem9_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_9.txt'
    with open(poem9_path, 'w', encoding="utf-8") as poem9:
        poem9.write(' \n')
        poem9.write('"Hugging a porcupine takes some practice.\n')
        poem9.write('So I\'ll start out with a cactus."\n')
        poem9.write('  - Marilyn Singer')

    poem10_path = '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems/Poem_10.txt'
    with open(poem10_path, 'w', encoding="utf-8") as poem10:
        poem10.write(' \n')
        poem10.write('"There once was a man from Peru.\n')
        poem10.write('Who dreamed he was eating his shoe.\n')
        poem10.write('He woke up at night.\n')
        poem10.write('With a terrible fright.\n')
        poem10.write('To find out his dream had come true!"\n')
        poem10.write('  - Some Dreamy Peruvian')


poem_gen()

# Welcome message with instructions for users to generate a random poem


def poem_menu():
    """Shows the welcome menu and instructions"""
    print('\nWelcome to the Random Poem Generator App!')
    first_text = input('Press "ENTER" to generate a poem!')

    # When "ENTER" is pressed a random .txt file is opened in the terminal
    if first_text == "":
        first_random_poem = random.choice(os.listdir(
            '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems'
        ))
        with open(first_random_poem, encoding="utf-8") as first_f:
            first_file_contents = first_f.read()
            sleep(.25)
            print(first_file_contents)
    # If any key other than "ENTER" is pressed, the user is reminded to press "ENTER"
    else:
        sleep(.25)
        print('\nOops! Please ONLY press "ENTER" to generate a poem!')
        poem_menu()


poem_menu()

# After the initial poem is generated, the user is asked if they want to generate another one
while True:
    sleep(.25)
    print('\nWould you like to generate another poem?\n')
    text = input('y/n').lower()

    # If the use chooses "y", another poem is generated
    if text == "y":
        random_poem = random.choice(os.listdir(
            '/Users/eflo/StudentWork/Python3/PoemGenerator/randPoems'
        ))
        with open(random_poem,  encoding="utf-8") as f:
            file_contents = f.read()
            sleep(.25)
            print(file_contents)
    # If the user presses "ENTER" a message reminds them to choose either "y" or "n"
    elif text == "":
        sleep(.25)
        print('\nUh-oh! Please only enter "y" or "n"\n')
    # If the user chooses "n" the program stops
    elif text == "n":
        break
    # If the user presses a character other than "y", "n", or "ENTER"
    # a message reminds them to choose either "y" or "n"
    else:
        print('\nUh-oh! Please only enter "y" or "n"\n')
# When the program stops, a farewell message is displayed
sleep(.25)
print('\nParting is such sweet sorrow...\n')
