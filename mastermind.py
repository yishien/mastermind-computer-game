def start():
    import random
    list_colours = ['R', 'O', 'Y', 'B', 'G', 'V']
    attempt = 0
    
    play = True
    while play == True:
        
        # to generate 4 random colours from the colours in the list
        colour = random.choices (list_colours, k = 4)
        print()
        
        while play == True:

            temporary_input = []
            temporary_colour = []

            correct_colour_correct_place = 0
            correct_colour_wrong_place = 0

            # to allow the user to input their guess
            enter = input('Enter your guess: ').upper()
            print()
            attempt = attempt + 1

            # to check whether the input is (4 letters & ROYBGV)
            if len(enter) != len(colour):
                print('You can only type 4 letters from R,O,Y,B,G,V.')
                continue
            
            for i in range(4):
                if enter[i] not in list_colours:
                    print('Your alphabet in position' , i+1, 'is not R/O/Y/B/G/V.')
                    continue
                
            # to compare the input and the answer (correct colour but in the wrong place)
            for i in range(4):
                if enter[i] in colour and enter[i] != colour[i]:
                    temporary_colour.append(colour[i])
                    temporary_input.append(enter[i])

            for i in range(len(temporary_colour)):
                if temporary_input[i] in temporary_colour and enter[i] != temporary_colour[i]:
                    correct_colour_wrong_place = correct_colour_wrong_place + 1

            # to compare the input and the answer (correct colour in the correct place)
            for i in range(4):
                if enter[i] == colour[i]:
                    correct_colour_correct_place = correct_colour_correct_place + 1

            # to check whether the user wins or need to try again
            if correct_colour_correct_place == 4:
                print('Congrats, '+ str(username)+ '! You took ' + str(attempt) + ' attempt(s).')
                play = False
                quit()

            else:
                print()
                print('Correct colour in the correct place: ', correct_colour_correct_place)
                print('Correct colour but in the wrong place: ', correct_colour_wrong_place)
                print()
                print('Try again, ' + str(username) + '. Dont give up!')
                print()           
                
print()
print('========================================================================')                              
print()
print('                                              WELCOME TO MASTER MIND GAME')
print()
print('========================================================================')                              
print()
username = str(input('                                          Enter your username to start: ')).capitalize()
print()
# The instruction of the game
print('-----------------------------------------HOW TO PLAY-----------------------------------------')
print()    
print('1) There are 6 colours available which are RED, ORANGE, YELLOW, BLUE, GREEN and VIOLET. ')
print('2) Enter the starting letter to represent the colour. ')
print('    R = RED   O= ORANGE   Y= YELLOW   B = BLUE   G = GREEN   V = VIOLET')
print('3) You have to guess the 4 colours (randomly selected) in a correct order. ')
print('    For example,  Enter your guess: ROYB')
print('4) The colours can be duplicated. For example,  Enter your guess: RRRB ')
print('5) It will display how many correct colour but in the wrong place & correct colour in the correct place until ')
print('     you able to guess it correctly.')  
print('6) Lastly, enjoy the game! All the best, '+ str(username)+ '! ')
# to start the game
start()
