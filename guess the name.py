# Biésów Smãtk

import random

WORDS=('Matilda', 'Grażina', 'Wioleta','Ana', 'Aleksandra', 'Agnesa', 'Ewelina', 'Katerina', 'Frédrisz', 'Tomôsz', 'Grégor', 'Karól', 'Sławòmir', 'Łukôsz', 'Adóm', 'Léna', 'Elizabeta', 'Frany') #list of names used in game


input('Wcëskôj Enter, żebë kòmpùter pòcygnął kawel i nalôzł dlô Ce miono.\n') #waiting for player to start

word = random.choice(WORDS) #seeking for random word from list
length = len(word) #checking words length
if length == 1: #informing player how long the word is
	print('Wëlosowóné miono je', length,'lëtrã dłudżé.')
elif length>1 and length<5:
	print('Wëlosowóné miono je', length,'lëtrë dłudżé.')
else:
	print('Wëlosowóné miono je', length,'lëtrów dłudżé.')

print('\nTerô môsz 5 pëtaniów, w jaczich so mòżesz spëtac, czë lëtra je w wëlosowónym mionie. Kòmpùter mòże Ce òdpòwiadac blós "jo" abò "nié".\n') #instruction for player
print('Żebë Cë bëło lżi, wzérôj na lëstã mionów:')
for j in range(len(WORDS)):
        print(WORDS[j])
print()
for i in range(5): #five questions about letters in the word
        letter = input('Je w tim mionie takô lëtra: ')
        if letter.lower() in word.lower(): #letter in word is or is not
                print('jo\n')
        else:
                print('nié\n')

print('Terô wëzgôdnij miono.') #waiting for answer
answer = input('\nTo je miono ')
if answer.lower() == word.lower():
        print('\nJes wëzgôdł!') #win
else:
        print('\nNi môsz wëzgôdłé') #failure
        print('To miono to', word)

input('\nWcëskôj Enter,' #żebë wëlosowac pòsobné słowò abò Escape,
' żebë skùńczëc.')
