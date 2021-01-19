class Bot:
    first_name = (
        "Super", "stuipid", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy",
        "Masked", "Unusual", "American", "Lego", "MLG", "Mlg", "lil", "Lil")

    last_name = (
        "Coder", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman",
        "Programmer",
        "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper",
        "Quickscoper")  # where I'd get the random name for my bot

    def __init__(self, bot_name):
        self.___bot_name = bot_name  # stores the Bot's name into an instance variable

    def __str__(self):
        Information = " The Bot's name is %s %s." % self.___bot_name
        return Information
        # returns information about the Robot(Robot's name)

    # print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")

    def initial_greeting(self, player_name):
        print(
            "Hello my name is %s! your random bot assigned Welcome to the word guessing game %s would you like to begin?" % (
            self.___bot_name, player_name))  # greets the player display this to the terminal

    def draw_Bot(self):
        print("=====================")
        print("* * * * *")
        print("*  @  @ *")
        print("*  @  @ *")
        print("* @  $ @ *")
        print("*  @  @ *")
        print("*  @  @ *")
        print("*       *")
        print("*       *")
        print("*_______*")
        print("/       *")
        print("* * * * *")
        print("=====================")
        print("\n")

    def get_name(self):
        # print("getter method has been called")   # test to see if the getter works
        return self.___bot_name
        # returns the Bot's name

    def set_fileName(self, new_name):
        # print("Setter method has been called ")
        self.name = new_name
        # updates the Bot's name, if a new name is given


class bot1(Bot):
    key_counter = 1  # bot1.key_counter
    value_counter = 0  # bot1.value_counter
    bot_score = 0  # bot1.bot_score
    user_score = 0  # bot1.user_score
    words_guessed = 0  # counter for words guessed

    def __init__(self, nickname, Dict1):
        super().__init__(nickname)
        self.words = []  # list with words to guess
        self.Dict = Dict1  # stores the Dictionary into an instance variable
        for keys in self.Dict:
            self.words.append(keys)  # a loop to loop through and add it to the dictioary
        self.move_word = self.words[0]
        self.clues = self.Dict[self.move_word]  # stores all the values associated with the word into a variable list
        self.answer = True
        self.games_played = 0  # counter for amount of games played

    def draw_Bot(self):
        print("=====================")
        print("* * * * *")
        print("*  @  @ *")
        print("*       *")
        print("*       *")
        print("*_______*")
        print("/       *")
        print("* * * * *")
        print("=====================")
        print("\n")

    def initial_greeting(self, player_name):
        super().initial_greeting(player_name)
        user_input = input(" Please type YES if you want to play or else type NO if you dont wish to play: ").lower()  # asks player if they want to play
        return user_input  # returns the player's input into the program
        # "\033[1;32;40m Bright Green  \n"

    def respond_to_gameplay(self, response):
        # print("this method has been called play method !!!!!").  for testing purposes
        if response == "yes" or response == "y":
            print(
                "========================== \nCHatbotguessing game will now commence I will present you with clues to words and you have to guess what the words are! you will have a couple of chances to guess the right word  \n==================")
            if self.games_played > 0:
                print("You have been through this before you already know how it works")
                return
        elif response == "no" or response == "n":
            print("============== \n Maybe next time" "\N{slightly smiling face}")
            # check to see if the emoji prints to the screen!!!!!!
        else:
            print("ERROR 404")
            # ERROR 404 INVALID INPUT

    def clue(self):
        if bot1.value_counter == 0:
            print("Please Guess this word!", "\n", " Here is your very first clue...")
            #print(self.move_word)  was testing to figure out issues with code
            return self.clues[
                bot1.value_counter]  #  must start at the indentations + 1 beacuse list counter begin at 0!!!!!
        else:  # we move onto the next clue !!!!
            print("here is your next clue: ")
            bot1.words_guessed += 1
            return self.clues[bot1.value_counter]

    def guess(self, word_guess):
        if word_guess == self.move_word:
            print("\033[1;32;40m You have successfully guessed the right word  \033 [m")
            # \033[1;32;40m You have successfully guessed the right word  \n
            print("\033[44;33m If you want to change the Robot Score Type SCORE into the input \033[m")
            bot1.words_guessed += 1  # correct wordsss counter
            bot1.user_score += 1  # everytime the user guesses the right word their score goes up by one
            self.answer = True  # if the user's guess is equal to the first chosen word the answer is True
            print("\033[1;32;40m Your score is: \033[m",
                  bot1.words_guessed)  # checks to see whether the guessed word was correct
            print("\033[44;33m The user score  is: \033[m ", bot1.user_score)
            print("\033[1;32;40m The Robot's score is: \033[m", bot1.bot_score)
            # "\033[44;33m The Robot's score is: \033[m
            return bot1.words_guessed

        elif word_guess == "score":
            print("The Bot's score criteria has been now changed.")


        elif word_guess == "new":
            print("You have requested a word change. You now need to specify a new range so I can select new words.")

        else:
            print("Your answer is wrong!")
            self.answer = False  # if the user's guess is NOT equal to the chosen word or the chosen word in upper case, the answer is False
            bot1.bot_score += 1
            bot1.words_guessed += 1
            return bot1.words_guessed, bot1.bot_score, bot1.words_guessed

    def Get_Answer(self):
        return self.answer  # Getter for the answer to avoid accidentally overriding it outside of the class

    def next_clue(self):
        while bot1.value_counter < len(self.clues):  # only returns next clue while there are clues available
            self.Clue = self.clues[:bot1.value_counter]  # stores the word in the next position as the next clue
            bot1.value_counter += 1  # increments the clue counter by 1   i.e the value side of the dictionary!!!
            return self.Clue, bot1.value_counter  # returns the next clue and the clue counter

    def next_word(self):
        bot1.value_counter = 0  # we reset the counter now back to 0 as we moved onto a new word
        #print(self.move_word)   was testing to figure out issues with code
        while bot1.key_counter < len(self.words):  # only returns next word while there are words available
          #  print(self.move_word)  was testing to figure out issues with code
            self.move_word = self.words[
                bot1.key_counter]  # stores the word in the next position as the next word ##### the problems seems to happen here
          #  print(self.move_word)   was testing to figure out issues with code
            self.clues = self.Dict[self.move_word]  # updates the clues associated with the next word
            # print(self.move_word)   was testing to figure out issues with code
            bot1.key_counter += 1  # increments the word counter  by 1
            # print(self.move_word)   was testing to figure out issues with code
            # sets clue counter back to 0 this is the value side of the dictionary
            bot1.draw_Bot(self)
        #  print(self.move_word)  # returns the next word

    def add_score(self):
        bot1.bot_score += 1  # increments the bot score counter by one when the method is called
        bot1.draw_Bot(self)
        return bot1.bot_score

    def change_score(self):  # additonal feature
        if bot1.bot_score <= 3:
            bot1.bot_score += 1
        if bot1.bot_score > 3 and bot1.bot_score <= 5:
            bot1.bot_score += 2
        if bot1.bot_score > 5:
            bot1.bot_score += 3
        bot1.draw_Bot(self)
        return bot1.bot_score

    def display_winner(self):
        if bot1.bot_score > bot1.words_guessed:
            bot1.draw_Bot(self)
            print("Game has ended")
            print("The game is over. The Robot has won!")
            print("You have lost the game !!!!!!!!!!!!!!!!")
            print("You have scored", bot1.user_score, "\n", "\U0001F644")

        if bot1.bot_score < bot1.words_guessed:
            print("WOOHOO You beat me well done not many people do!!!!!! ", "\n", "\U0001F606")
            bot1.draw_Bot(self)
            bot1.play_again(self)

        else:
            print("The game is over. You and the Robot drew!")

    def Get_Closing_Greeting(self):
        return self.Closing_Greeting  # returns the Closing Greeting sentence

    def Set_Closing_Greeting(self, string):
        self.Closing_Greeting = string  # sets the Closing Greeting sentence

    def play_again(self):
        user = input("Would you like to play again?").lower()
        if user == "yes":
            self.games_played += 1
            response = "yes"
            bot1.value_counter = 0
            bot1.key_counter = 1
            bot1.bot_score = 0  # with lines 200-203 all we want to do is reset everything back to 0 for the purpose of reseting the game and starting again
            bot1.user_score = 0
            bot1.draw_Bot(self)
            bot1.respond_to_gameplay(self, response)
        else:
            quit()
