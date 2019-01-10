#Isaac Arthur and Tyson Vorwaller
#Crossword and trivia puzzle game
#11/18
import random
#Words and definitions
aa="Represented in 1s and 0s",
a= "binary"

bb="Get data from the \"outside world\"", 
b="input"

cc="Display the results of the program on the screen",
c="output"

dd="a person who writes computer programs in Python",
d="programmer"

ee="sequence of Python statements that have been crafted into something"
e="program"

ff="When the program will work, but is in the wrong order"
f="logicerror"

gg="A type of programming language"
g="python"

hh="A function that displays a string"
h="print"

ii="Repeats a block of code while True"
i="whileloop"

jj="A whole number"
j="integer"

score = 0
#Puzzle this is our crossword puzzle that is displayed in index's
puzzle = ("lwhileloopcotupniltrhngwofqkuoropiypbzpgehrzciigtrgtomneupua"+
          "eygaejrhomtprtgisrfmnyaynnckoeiwmtwwycnr")
#Correctness Checks to see if your awnser is actually correct or not
correct="That is correct! Now move on to the word search"
incorrect="That is not right, please try again."

question=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj]
answer=[a,b,c,d,e,f,g,h,i,j]
def word(question, anwser):
    global score
    attempts =10
    x=random.randrange(len(question))
    que=question[x]
    word = anwser[x]
    while True:
        resp= input(que)
        if  resp == word:
            score = score +attempts*10
            print(correct)
            del question[x]
            del answer[x]
            return word
        else:
            attempts -=1
            print(incorrect)
 #this is our display it displayes our questions
            
def display():
    question[0]
    question=question

#this is our attempts it keeps track of how many attempts you have and gives you a score
def search(word):
    global score
    attempts =10
    ip=""
    bw=""
    display_puzzle()
    while True:
        index=input("enter the index positions for the word seperated by a ,")
        for i in index:
            if i ==",":
                x=int(ip)
                bw = bw+puzzle[x]
                ip=""

            else:
                ip=ip +i
        if bw == word:
            score = score +attempts*10
            print ("correct")
            break
        else:
            attempts -=1
            print("wrong")
    
    
  


#this is our display format this is how our crossword displays in idle
def display_puzzle():
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:])
 #this is the main menu and how it displays    
def main():
    print("Python terms")
    print(score)
    while len(question) >0:
        x=word(question, answer)
        search(x)
    print ("you got them all")
    
main()
