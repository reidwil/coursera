from random import randrange

def name_to_number(name):

    """
    takes in a name input and translates it to it's corresponding number
    valid names = rock, Spock, paper, lizard, scissors
    returns name's number or error message
    """
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "invalid input"

def number_to_name(number):
    """
    takes in a number and returns it's corresponding name
    returns name
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "invalid input"
    
def rpsls(name):
    """
    main method that calls all the others and plays you in rpsls
    prints if input won or not
    """
    print("\n")
    player_number = name_to_number(name)
    comp_number   = randrange(0,5) # get random number for computer between 0 and 4
    comp_name     = number_to_name(comp_number)
    deciding_num  = (player_number - comp_number) % 5

    if deciding_num == 0:
        print(f"Player chooses {name} \nComputer chooses {comp_name}\nPlayer and computer tie!")
    elif deciding_num >= 2:
        print(f"Player chooses {name} \nComputer chooses {comp_name}\nComputer wins!")
    else:
        print(f"Player chooses {name} \nComputer chooses {comp_name}\nPlayer wins!")
