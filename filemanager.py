class FileManager:
    checker = True  # checker to see if requirements are met !!!!!
    empty_string_1 = ""  # will be called in methods below
    empty_list = []                 # we creating an empty list to add the words to it
    dict_return = {}                   # we created an empty dictionary to add the keys i.e words to guess  and values i.e the clues to it
    counter = 0                 #just an counter to keep track of everything

    def __init__(self, filename):
        self.__filename = filename  # stores filename into an instance variable
        file_1 = open(self.__filename)  # opens the file
        self.file_length = 0  # the file length counter being instialised
        for x in file_1:  #  i want get loop through all the lines in the text file
            x = ''
            self.file_length += 1  # incrementing the legnth of the file for each new line there is
        file_1.close()  # closing a file after opening it is very key

    def get_line_number(self, num_loop):
        file_1 = open(self.__filename)  # were just opening the file
        if num_loop in range(0, ( self.file_length + 1)):  # remmber the lenght of the text file!!!!  making sure it is in range
            lines = file_1.readlines()  # i want to read the lines in the string
            FileManager.empty_string_1 = lines[ num_loop - 1]  # we defined the empty string variable at the begining of our variable
            file_1.close()  # . it is very important to always close the file when your are done with it
            return FileManager.empty_string_1  # returns the line for that number
        else:
            print(
                "\033[44;33mERROR 409 INPUT IS OUT OF RANGE........ PLEASE TRY AGAIN \033[m")  # we want to highlight thathe user went wrong somewhere

    def get_filename(self):
        return self.__filename  # returns the file name

    def set_filename(self, update_name):
        self.__filename = update_name  # sets a new file name if a new name is given

    NewFile = property(get_filename,
                       set_filename)  # we use the property fucntion to acheive the behaviours set out in the getter and setter methods

    def get_length(self):
        ####  print("test")
        return self.file_length  # we just want to return the legnth of the file

    def read_file(self):
        file_1 = open(self.__filename)  # we must open the file to access its contexts
        lines = file_1.readlines()  # reads the lines in the file
        display_string = FileManager.empty_string_1.join(lines)  # turns list into string
        file_1.close()
        return display_string  # returns the file as a string

    def read_line_range(self, ran):
        if len(ran) == 2  and ran[0] < self.file_length and ran[1] < self.file_length:  # checks if the entered range is in the right format (has exactly 2 values, first value isn't bigger than the second, the values are positive, the values are valid line numbers
            file_1 = open(self.__filename)
            lines = file_1.readlines()
            slicing = lines[ran[0]:ran[1] + 1]
            update_string = FileManager.empty_string_1.join(slicing)  # here were only converting the list to the string
            file_1.close()  # it  is always good to close the file after done using it in an method/function
            return update_string  # returns the string
        else:
            print("\033[44;33mERROR 409 INPUT IS OUT OF RANGE........ PLEASE TRY AGAIN \033[")
            return FileManager.empty_string_1


class BotFileManager(FileManager):  # HERE WE CREATED THE CHILD CLASS

    def __init__(self, filename):
        super().__init__(filename)  # inherits the filename of the parent class
        self.dict = {}  # empty dictionary stored into an instance variable

    def __str__(self):
        Information = "The list is %s lines long. The dictionary with words to guess is: %s" % (
        self.file_length, self.dict)
        return Information  # returns Information about the BotFileManager class

    def all_words(self):
        self.dict = {}  # here we created an empty string!!!
        update_string = self.read_file()  # we want to read the file and its contexts
        split_string = update_string.split(",")  # we want to do a new line
        position_counter = 0
        while position_counter < self.file_length:  # obviosly this continues as long as the position counter is less than the legnth
            list1 = split_string[position_counter]  # stores each line into the variable list1
            split_lines = list1.split(",")  #  this was missing from my other assignments
            self.dict[split_lines[0]] = split_lines[1:]  #  with this numbers im keeping the string in range
            position_counter += 1  # im iterated the position counter eveerytime it goes past
        return self.dict  # returns the dictionary

    def dictionary_from_range(self, ran):
        self.dict = {}  # resets the variable to an empty dictionary if called
        Range = self.read_line_range(ran)  # were are taking it from the parent class
        if len(ran) == 2  and ran[0] < self.file_length and ran[1] < self.file_length: # checks if the entered range is in the right format (has exactly 2 values, first value isn't bigger than the second, the values are positive, the values are valid line numbers)
            split_lines = Range.split(",")  # splits the string where there is a new line
            position_counter = ran[0]  # counter starts at the the position of the first entered value
            m_list = 0  # counter starts at position 0 of the list
            while position_counter in range(ran[0], ran[1] + 1):  # while loop continues until the counter is no longer in the specified range
                list_as_string = split_lines[m_list]  # stores each line into list1
                if m_list == 0:  # making sure the position of word is equal to 0
                    list1 = list_as_string  # if it is, then the string stays the same
                else:
                    list1 = list_as_string[1:]  # if it isn't at position 0 then the new string becomes the old string without the empty space in front of the first word
                L1 = list1.split(",")  # splits the line where there is a comma
                self.dict[L1[0]] = L1[1:]  # adds the first word of the line as a key to the dictionary and the other 5 words as the values
                position_counter += 1  # increments the counter
                m_list += 1  # increments the position counter
            return self.dict  # returns the dictionary
        else:
            print("\033[44;33mThe user inputted range is not in the right format therefore we have returned an empty list for you \033[m")
            return FileManager.empty_list

    def line_as_dictionary(self, no):
        self.dict = {}  # resets the variable to an empty dictionary if called
        Line = self.get_line_number(no)  # inherits the get_line_number method from the parent class
        if no in range(0, (self.file_length + 1)):  # checks if the number entered is a valid line number
            L1 = Line.split(",")  # splits the line where there is a comma
            self.dict[L1[0]] = L1[1:]  # adds the first word of the line as a key to the dictionary and the other 5 words as the values
            return self.dict  # returns the dictionary
        else:
            print( "\033[44;33mThe user inputted range is not in the right format therefore we have returned -1  for you \033[m")
            return -1  # if the entered number is out of range, the method returns -1

    def new_words(self):
        self.dict = {}  # an empty string to put our values and keys into, you can have this at the very start of the parent class aswelll
        new_list = []  # empty list i created
        start = input("Please enter your starting range line for the dictionary: ")
        stop = input("Please enter your ending range line for the dictionary: (has to be larger than your input) ")
        new_list.append(int(start))  # here i want to add the start and stopping ranges to the empyt list that instaitiated above
        new_list.append(int(stop))
        new_lines = self.read_line_range(new_list)
        split_lines = new_lines.split("\n")
        position_counter = new_list[0]  # counter starts at the the position of the first entered value
        counter_list = 0  # counter starts at position 0 of the list
        if stop > start:
            while position_counter in range(new_list[0], new_list[ 1] + 1):  # while loop continues until the counter is no longer in the specified range
                list_as_string = split_lines[counter_list]  # stores each line into list1
                if counter_list == 0:  # if the counter list is at 0 we do not give the old list a new value
                    old_list = list_as_string  # i.e it stays the same
                else:
                    old_list = list_as_string[1:]
                format_lines = old_list.split(",")  # here we want to split the line evertime there is is a comma from the text file
                self.dict[format_lines[0]] = format_lines[1:]  # adds the first word of the line as a key to the dictionary and the other 5 words as the values
                position_counter += 1  # increments the counter
                counter_list += 1  # increments the position counter of the counter list
                return self.dict
        else:
            print("OUT OF RANGE..... -1", "\n", "Your stopping range is rather to large")
