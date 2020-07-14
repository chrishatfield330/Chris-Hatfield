import random
import time

#arrange responses in a list
eight_ball= ['As I see it, yes.',
 'Ask again later.',
 'Better not tell you now.',
 'Cannot predict now.',
 'Concentrate and ask again.',
 'Don’t count on it.',
 'It is certain.',
 'It is decidedly so.',
 'Most likely.',
 'My reply is no.',
 'My sources say no.',
 'Outlook not so good.',
 'Outlook good.',
 'Reply hazy, try again.',
 'Signs point to yes.',
 'Very doubtful.',
 'Without a doubt.',
 'Yes.',
 'Yes definitely.',
 'You may rely on it.']


#question prompt
def question():
    question = input('Please ask me a question.   ')

#this will check if meaning of life is in the question
    if 'meaning of life' in question:
        print('Hmmmm...')
        time.sleep(2)
        print('The answer you seek is 42.')
    else:

#2 second pause for thinking.
        print('Let me think.')
        time.sleep(2)

    
    
        print ('The magic 8 ball says: ') 
        print (random.choice(eight_ball))
    

   

while True:
    question() 
    repeat = input('Would you like to ask another question? (Y/N)')
    if not (repeat == 'y' or repeat == 'Y'):
        print ('Come back when you have a question for the great and powerfull 8 ball.')
        time.sleep(4)
        input('Press ENTER to exit.')
        break

