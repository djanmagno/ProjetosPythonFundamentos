# -*- coding: utf-8 -*-

#Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (Tabuleiro)

board = [
'''

>>>>>>>>>> Forca <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========='''
]

# Class
class Hangman:

    # Constructor Method
    def __init__(self,word):
        self.word = word
        self.wrong_letter = []
        self.correct_letter = []
        #
    # Method to find the letter
    def guess(self,letter):
        if letter in self.word and letter not in self.correct_letter:
            self.correct_letter.append(letter)
        elif letter not in self.word and letter not in self.wrong_letter:
            self.wrong_letter.append(letter)
        else:
            return False
        return True

    # Method to verify if the game has finished
    def hangman_over(self):
        return self.hangman_won() or (len(self.wrong_letter) == 6)

    # Method to verify if the game has finished
    def hangman_won(self):
        if "_" not in self.hide_word():
            return True
        return False

    # Method to hide the letter of the board
    def hide_word(self):
        rturn = ""
        for letter in self.word:
            if letter not in self.correct_letter:
                rturn = rturn + "_"
            else:
                rturn = rturn + letter
        return rturn

    # Method to check the game status and print it on the screen board
    def print_game_status(self):
        print(board[len(self.wrong_letter)])
        print("\nWord: " + self.hide_word())
        print("\nWrong Letters: ",)
        for letter in self.wrong_letter:
            print(letter,)
        print()
        print("Correct Letters: ",)
        for letter in self.correct_letter:
            print(letter,)
        print()

# Function to read a word from the palavras.txt file on a rondom way
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

# Main Function - Execution of the program
def main():

    # Object
    game = Hangman(rand_word())

    # While the game still running, print the status and ask for another letter after that read the new character
    while not game.hangman_over():
        game.print_game_status()
        user_input = input("\nType a letter: ")
        game.guess(user_input)

    # Verify the game status
    game.print_game_status()

    # According with the status, print a message on the screen for the user
    if game.hangman_won():
        print("\nCongratulations! You have won!")
    else:
        print("\nGame Over! You have lost")
        print("The word was" + game.word)

    print("\nNice to play with you! Back another time to play again!\n")

# Execute the program
if __name__ == "__main__":
	main()


