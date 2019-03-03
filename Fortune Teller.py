import random
answers = ['It will happen for you!',

'It is decidedly so', 'For sure!!!', 'Yes – definitely',

'You can bet your bottom dollar', 'As I can see it, YES', 'Most likely',

'Future looks good', 'Yes Signs point to yes', 'Hmmm not sure', 'Try Again',

'Ask again later', 'Better not tell you that right now', 'Cant predict that now',

'Concentrate and ask again', 'Dont count on it', 'My Guess is no', 'My sources say no',

'Future is not so good', 'Very doubtful'] # List of random responses

print('Hello Traveler, I am Randini the Great, What is your name?') # Introduction for Fortune Teller
name = input("Enter your name here my friend: ") # Asking for User to input their name
print('Hello: ' + name)


def Randini():
    print('Ask me any question.') # Asking for User to input a random question
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    print('I hope that helped!')
    Replay()


def Replay():
    print ('Do you have another question? [Y/N] ') # Asking for User to input another random question
    reply = input()
    if reply == 'Y':
        Randini()
    elif reply == 'N':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()


Randini()
