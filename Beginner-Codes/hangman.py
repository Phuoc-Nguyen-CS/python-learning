import random

def hang_man():

    game_over = False

    hangman_words = ["abruptly", "absurd", "abyss", "affix", "haiku", "haphazard",
                    "hyphen", "spritz"]
    
    word = []
    word.append(random.choice(hangman_words))
    guess = 0

    # Map Syntax:
    #           map(function, iterator)
    map_word = list(map(list, word))

    print(map_word)

    user_visual = []

    # Creates the blank look for users to see
    for index in range(len(word[0])):
        user_visual.append('_')

    while game_over == False:

        # User interactions
        print(f"Please enter a letter >> \n{user_visual}")
        user_input = input().lower()

        # Map_word is a list of strings
        # Check if the user_input is within the word and if so
        # Append the word to the user_visual
        if user_input in map_word[0]:
            for index in range(len(map_word[0])):
                if user_input == map_word[0][index]:
                    user_visual[index] = user_input

        guess += 1
        
        if user_visual == map_word[0]:
                game_over = True
                print(f"{user_visual}\nWas Correct!")
        elif guess > 6:
            game_over = True

hang_man()



    


