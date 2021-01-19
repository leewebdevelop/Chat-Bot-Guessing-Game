import random  # used for generating a random bot name
import pygame  # must import the pygame libraries
from bot import Bot, bot1  # imports the Bot class and bot1 class from bot.py
from filemanager import BotFileManager  # imports the BotFileManager class from filemanager.py

pygame.init()               # were just initialisin the pygame to get it to run

Display_Width = 800  # the ideal width and height for repl
Display_Height = 600

display_size = [Display_Width,Display_Height]  # put them in named variables !!! ideall the aspect ratio should be 800 600 for repl
display = pygame.display.set_mode(display_size)  # setting the display window in the specified size

Bot_image = pygame.image.load( "bot_image.bmp")  # loading the robot image  for pycharm for some reason only images in bmp fornat work
Bot_position = [144, 79]  # precisely stating the postion of the robot
Bot_size = [400, 400]  # defining the size of the Robot to 400 pixels wide and 400 pixels high
Bot_scaled = pygame.transform.scale(Bot_image, Bot_size)  # scaling the size
white = [240, 240, 0]  # here we make the background display whitw
display.fill(white)
display.blit(Bot_scaled, Bot_position)  # . we can move the position of the robot here to wherever we want !!!!

pygame.display.update()  # updates the screen to display everything

FileManager_1 = BotFileManager("botfilemanager.txt")  # creates an instance of the BotFileManager class

tester_dict = {"testing": ["1", "2", "3", "4", "5"]}

r = random.sample(Bot.first_name,2)  # Bot.first_name is the population and 2 is the number we want to take from the population first word being for first name and second name is last name
name_bot = [str(x) for x in r]  # the random sample returns the random names as a list I want to then convert that to a string

for event in pygame.event.get():
    if event.type == pygame.QUIT:  # if users clicks x out of it the pygame will stop running
        run_game = False  # we chane the conditiond to false to let this happen

Bot_image = Bot(name_bot)  # creating an instance of the Bot class

Bot_defined = bot1(name_bot, tester_dict)  # here were only defining the bots's namme

Bot_defined.draw_Bot()  # prints the robot to the screen

"\n"
closing_message = "Thank you for playing."  # here we are defining the closing message want to emphasis it aswell using colours
# \032[1;32;40m Thank you for playing.   \n"
"\n"

Bot_defined.Set_Closing_Greeting(closing_message)  # setting the closing message

name = input("Please enter your name: ").upper()  # stores the user's name into a variable NOTICE HOW WE ALSO CHANGE IT TO ALL CAPS ASWELL FOR VISUAL PURPOSES

Bot_defined.draw_Bot()  # prints the robot to the screen

player_answer = Bot_defined.initial_greeting(
    name)  # passes in the player's name and asks the user if they want to play, then stores their answer into a variable

Bot_defined.draw_Bot()  # WE CALL THE DRAW BOT FUNCTION ALOT OF THE TIME AS WE WANT TO IT TO APPEAR IT EVERYTIME IS DONE IN THE GAME

Bot_defined.respond_to_gameplay(player_answer)  # passes in the player's response and outputs the corresponding message

clock = pygame.time.Clock()

if player_answer == "yes":  # only if the player agrees to playing, the game will continue
    print("We need a range from (from 1 - %i), so I can provide you with words." % (FileManager_1.get_length() - 1))

    # asks the player to specifiy a range to create the dictionary of words

    # could poentially make it error if users types in 0 not sure yet

    words = FileManager_1.new_words()  # calls the method and attributes it to the variable "word"

    "\n"
    "\n"

    Bot_defined = bot1(name_bot, words)  # creates an instance of the GuessingBot class with the specified dictionary

    print(Bot_defined.clue())  # prints the very  first clue to the display

    word_guess = input(
        "Enter your guess here:  ").lower()  # asks player to guess the word we change the word to all lowercase as it makes it easier for the user!! shooudlnt matter in the chatbot guessing game

    Bot_defined.draw_Bot()  # calling the draw method to print the robot to the screen

    Bot_defined.guess(word_guess)  # checks to see what the player has entered

    print("Your score is now:", Bot_defined.user_score, "\n", "The Bot's score is now:", Bot_defined.bot_score)

    if word_guess == "score":  # adding the addiotnal feature to our program..... if user types score into where they input their guess
        print("The Bot's score is now: ",
              Bot_defined.change_score())  # changes the bot's score when the player enters "score"
        print("Your score is now:",Bot_defined.user_score, "\n","The Bot's score is now:", Bot_defined.bot_score)    # all we want to do is print the user score and bot score to the screen

    if word_guess == "new":  # we want to use an elif statement as we want to tell python if all the other conditions wernt meant this will conditions will follow through
        new_dict = FileManager_1.new_words()  # stores the new dicitionary into a variable called new_dict
        bot_score = Bot_defined.bot_score  # stores the Bots score into a variable so we can fetch it out later
        Words_Guessed = Bot_defined.words_guessed  # stors the player's score into a variable
        Bot_defined = bot1(name_bot,new_dict)  # creates a new instance of the Bot, passing in the new dictionary of words
        Bot_defined.bot_score = bot_score  # stores the previous Robot score into the new instance
        Bot_defined.words_guessed = Words_Guessed  # stores the previous player score into the new instance

    while Bot_defined.key_counter < len(Bot_defined.words):

        if Bot_defined.Get_Answer() == True:
            Bot_defined.next_word()  # updates the next word
            "\n"
            print(Bot_defined.clue())  # prints the first clue
            "\n"
            word_guess = input("Can you guess the word? ").lower()  # asks player to guess the word
            Bot_defined.draw_Bot()  # calling the draw method to print the robot to the screen
            Bot_defined.guess(word_guess)

            if word_guess == "score":
                print("The Bot's score is now: ",
                      Bot_defined.change_score())  # changes the bot's score when the player enters "score"
                print("Your score is now:",Bot_defined.user_score, "\n","The Bot's score is now:", Bot_defined.bot_score)  # we want to display the new score to the user to the screen
            if word_guess == "new":
                new_dict = FileManager_1.new_words()
                bot_score = Bot_defined.bot_score
                Words_Guessed = Bot_defined.words_guessed
                Bot_defined = bot1(name_bot, new_dict)                         #e want to retrieve the new empty dictionary to add the new words to it
                Bot_defined.bot_score = bot_score
                Bot_defined.words_guessed = Words_Guessed


        if Bot_defined.Get_Answer() == False:
            while Bot_defined.value_counter < (len(Bot_defined.clues)) - 1 and Bot_defined.value_counter < len(
                    Bot_defined.words):  # loop continues as long as there are words and clues left
                if Bot_defined.answer == True:
                    Bot_defined.next_word()  # updates the next word
                    print(Bot_defined.clue())  # prints the first clue
                    word_guess = input("Can you guess the word? ")  # asks player to guess the word
                    Bot_defined.draw_Bot()  # calling the draw method to print the robot to the screen
                    Bot_defined.guess(word_guess)

                    if word_guess == "score":
                        print("you have now changed the bot score The Bot's score is now: ",
                              Bot_defined.change_score())  # changes the bot's score when the player enters "score"
                        print("Your score is now:",Bot_defined.user_score, "\n","The Bot's score is now:", Bot_defined.bot_score)

                    if word_guess == "new":
                        new_dict = FileManager_1.new_words()
                        bot_score = Bot_defined.bot_score
                        Words_Guessed = Bot_defined.words_guessed
                        Bot_defined = bot1(name_bot, new_dict)                   # we want to retrieve the new empty dictionary to add the new words to
                        Bot_defined.bot_score = bot_score
                        Bot_defined.words_guessed = Words_Guessed


                if Bot_defined.Get_Answer() == False:
                    "\n"
                    "\n"
                    Bot_defined.next_clue()  # moves on to the next clue
                    print(Bot_defined.clue())  # prints the next clue
                    word_guess = input("Enter your guess here  ").lower()  # asks player to guess the word
                    Bot_defined.draw_Bot()  # calling the draw method to print the robot to the screen
                    Bot_defined.guess(word_guess)

                    if word_guess == "score":
                        print("The Bot's score is now: ",
                              Bot_defined.change_score())  # changes the bot's score when the player enters "score"
                        print("Your score is now:", Bot_defined.user_score, "\n", "The Bot's score is now:",Bot_defined.bot_score)
                    if word_guess == "new":
                        new_dict = FileManager_1.new_words()
                        bot_score = Bot_defined.bot_score
                        Words_Guessed = Bot_defined.words_guessed
                        Bot_defined = bot1(name_bot, new_dict)    # we want to retrieve the new empty dictionary to add the new words to it
                        Bot_defined.bot_score = bot_score         # here were only retrieving the new bot score
                        Bot_defined.words_guessed = Words_Guessed  # were just updating the words guess

            # we want to retrieve the new empty dictionary to add the new words to it
            # here were only retrieving the new bot score
            # were just updating the words guess
            else:
                if Bot_defined.key_counter < len(Bot_defined.words):
                    print("The word was %s" % Bot_defined.next_word, "\n", "The Robot's score is: ",
                          Bot_defined.add_score(), "\n", "Your score is: ",
                          Bot_defined.words_guessed)  # tells the player what the word was
                    # prints the Robot's score to the screen
                    # tells the player their score
                    Bot_defined.answer = True  # eventually when user uses up all their guesses the bot will move onto the next word

    else:
        if Bot_defined.Get_Answer() == True:
            Bot_defined.display_winner()
            Bot_defined.Set_Closing_Greeting(closing_message)
            print(Bot_defined.Get_Closing_Greeting())  # when we run of words then this will be printed to the screen
        if Bot_defined.Get_Answer() == False:
            while Bot_defined.value_counter < (
                    len(Bot_defined.clues)) - 1:  # loop continues as long as there are clues left
                if Bot_defined.answer == True:
                    Bot_defined.value_counter = (len(
                        Bot_defined.clues)) - 1  # breaks the while loop and termintes the game
                if Bot_defined.Get_Answer() == False:
                    "\n"
                    Bot_defined.next_clue()  # moves on to the next clue
                    print(Bot_defined.clue())  # prints the next clue
                    "\n"
                    word_guess = input("Can you guess the word? ").lower  # asks player to guess the word
                    Bot_defined.draw_Bot()  # calling the draw method to print the robot to the screen
                    Bot_defined.guess(word_guess)
                    "\n"
                    if word_guess == "score":
                        print("The Bot's score is now: ",
                              Bot_defined.change_score())  # changes the bot's score when the player enters "score"
                        print("Your score is now:",Bot_defined.user_score, "\n","The Bot's score is now:", Bot_defined.bot_score)
                    if word_guess == "new":   # ths is an trigger if the user types new into as yuou notice were reoeating this codfe  alot
                        new_dict = FileManager_1.new_words()
                        Bot_score = Bot_defined.bot_score
                        Words_Guessed = Bot_defined.words_guessed
                        Bot_defined = bot1(name_bot, new_dict)
                        Bot_defined.bot_score = Bot_score
                        Bot_defined.words_guessed = Words_Guessed

            else: #  the while just check ifr there any clues left
                # prints when no more clues and words are left
                if Bot_defined.Get_Answer() == True:
                    Bot_defined.display_winner()  # we want to display the winner of the game to the screen
                    Bot_defined.Set_Closing_Greeting(closing_message)  # setting the closing message
                    print(Bot_defined.Get_Closing_Greeting())  # tells the player that the game is over and displays the closing greeting
                if Bot_defined.Get_Answer() == False:  # elif statement was used as we want to tell python if the prior statements werent true could used other methods aswell
                    print("The word was %s" % Bot_defined.move_word, "\n", "The Bots score is: ",
                          Bot_defined.add_score(), "\n", "Your score is: ",
                          Bot_defined.words_guessed)  # printing what the word was, bots score  and the amount of words guessed to the screen
                    Bot_defined.display_winner()  # we want to the display the winner to the screen
                    Bot_defined.Set_Closing_Greeting(closing_message)  # were just setting setting closing message for the program



    clock.tick(120)  # we opted for 120 frames per second for this partucular program
pygame.quit()
quit()
