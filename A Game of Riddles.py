print('Importing packages')
import time as t
t.sleep(1)
print()
print()
print()
print('Welcome to:')
t.sleep(2)
print('A Game of Riddles!')
print()
print('This game consists of a series of riddles with a numerical answer. Your answer will never be a negative number. Your answer will never be zero. Your answer will never have a decimal point. (If you enter an answer with a negative or a decimal, the game will crash, and you will lose your progress.) You will not be told when you get a question wright or wrong. To skip a question, type skip. When you get a question right, you will gain a point. When you get a question wrong, you will lose a point. The minimum score is 0. IMPORTANT! ALWAYS ANSWER AS A DIGIT! (For example, if your answer is ten, write it like this: "10", not this: "ten". There are ten questions. Enjoy!')
print()
t.sleep(5)
print('Press enter to start.')
input()
print()
print()
print()
score = 0
print(' == QUESTION ONE: St. Ives ==')
print('As I was going to St. Ives, I met a man with seven wives.')
print('Every wife had seven sacks, every sack had seven cats, and every cat had seven kits.')
print('Wives, sacks, cats, and kits, how many were going to St. Ives?')
print()

ans1 = input("Type your answer here: ")
print()
print('Processing answer...')
t.sleep(1)
print('Answer processed!')
if ans1 == 'skip':
      print('Skipped question 1! You have neither gained nor lost a point.')
elif int(ans1) == 1:
    score = score + 1
    print('Score logged')
elif int(ans1) != 1:
    score = score - 1
    print('Score logged')
    
    if score < 0:
        score == 0
print(score)

print()
print()
print()
print(' == QUESTION TWO: Even == ')
print('I am an odd number. Take away a letter (from my letter form, e.g. five) and I am even. What number am I?')
print()
ans2 = input("Type your answer here: ")
if ans2 == 'skip':
      print('Skipped question 2! You have neither gained nor lost a point.')
elif int(ans2) == 7:
    score = score + 1
    print('Score logged')
elif int(ans2) != 7:
    score = score - 1
    print('Score logged')
    
    if score < 0:
        score == 0
        print('Warning! You are bad at this game! Your score is still zero!')
print(score)        
print()
print()
print()
print('QUESTION THREE: Odd little fish')
print('In an odd little town, was an odd little stream with odd little fish in an odd little team. A stranger approached a local fisherman, and asked him how much his odd little fish weighed. The odd little man replied, "All the fish in this stream weigh exactly 1/2 of a pound plus 1/2 of a fish." Isn’t that odd? How many pounds does an odd little fish weigh?')
print()
ans3 = input("Type your answer here: ")
if ans3 == 'skip':
      print('Skipped question 3! You have neither gained nor lost a point.')
elif int(ans3) == 1:
    score = score + 1
    print('Score logged')
elif int(ans3) != 1:
    score = score - 1
    print('Score logged')
    
    if score < 0:
        score == 0
print(score)
print()
print()
print()
print('From now on, the questions get harder.')
t.sleep(1)
print(' == QUESTION FOUR: Blonde, Burnette, and Redheaded == ')
print('A man describes his daughters, saying, "They are all blonde, but two; all brunette but two; and all redheaded but two." How many daughters does he have?')
print()
ans4 = input("Type your answer here: ")
if ans4 == 'skip':
      print('Skipped question 4! You have neither gained nor lost a point.')
elif int(ans4) == 3:
    score = score + 1
    print('Score logged')
elif int(ans4) != 3:
    score = score - 1
    print('Score logged')
    
    if score < 0:
        score == 0
print('End of demo. Your score is ' + str(score) + '.')
print()
print('Made by CrazyChickenYT')
