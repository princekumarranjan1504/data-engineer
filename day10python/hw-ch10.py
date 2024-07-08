# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score.
# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.
# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file.
# 5. Repeat program 4 for a list of such words to be censored.
# 6. Write a program to mine a log file and find out whether it contains ‘python’.
# 7. Write a program to find out the line number where python is present from ques 6.
# 8. Write a program to make a copy of a text file “this. txt”
# 9. Write a program to find out whether a file is identical & matches the content of another file.
# 10. Write a program to wipe out the content of a file using python.
# 11. Write a python program to rename a file to “renamed_by_ python.txt.

# q1
with open('poem.txt') as f:
    poem = f.read()

if('twinkle' in poem):
    print("present")
else:
    print("not present")

# # q2
import random

def game():
    print("your are playing the game")
    score = random.randint(1,50)
    # featching the hiscore
    with open('hiscore.txt') as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score


# q3
def genrateTable(n):
    table = ""
    for i in range(1, 11):
        table += f'{n}X{i}={n*i}\n'

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    genrateTable(i)

# q4
word = "Donkey"

with open("/home/prince/python/data-engineer/day10python/file1.txt","r") as f:
    content = f.read()
contentNew = content.replace(word, "######")

with open("/home/prince/python/data-engineer/day10python/file1.txt","w") as f:
    f.write(content)

# q5
words = ["Donkey",'bad','ganda']

with open("file1.txt","r") as f:
    content = f.read()

for word in words:
    contentNew = content.replace(word, "#"*len(word))

with open("file1.txt","w") as f:
    f.write(content)

# q6
with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("present")
else:
    print("not present")

# q7
with open("log.txt") as f:
    lines = f.readline()

lineno = 1
for lie in lines:
    if("python" in lines):
        print(f"present in line no. {lineno}")
        break
    lineno += 1 
else:
    print("not present")

# q8
with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt") as f:
    content = f.write(content)

# q9
with open("file1.txt") as f:
    content1 = f.read()

with open("poem.txt") as f:
    content2 = f.read()

if(content1==content2):
    print("identical")
else:
    print("not identical")

# q10
with open("poem.txt") as f:
    f.write("")

# q11
with open("poem.txt") as f:
    content = f.read()

with open("remane_by_python.txt") as f:
    f.write(content)