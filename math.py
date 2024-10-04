
import random
import sys, os
import getopt
import pdb
import time

userName = "Katherine"
messageCorrect = f'Bravo {userName}  :-) :-) :-) :-) :-) :-) :-) :-)  Bon reponse'

def executeSumGame(min=0, max=100, iter=5, waitTime=5):
    print("\n")
    print("Bienvenue au jou de Addition !")
    print(f"Tu vas faire des additions de nombres entre {_min} and {_max}")
    print("Bonne chance !")
    print("")

    cntSuccess = 0
    for i in range(0, iter):
        a = random.randrange(min, max)
        b = random.randrange(0, 11)
        if a + b > max:
            b = max - a
        
        print("\n")
        print("---------------------------------------------------")
        print("\n")
        
        userRes = -1
        correctRes = a + b
        numOfTries = [1, 2, 3]
        for _try in numOfTries:
            print(f"{a} + {b} = ", end='')
            userInput = input()
            userRes = -1
            try:
                userRes = int(userInput)
            except:
                pass
            if userRes == correctRes:
                print(messageCorrect)
                cntSuccess += 1
                time.sleep(waitTime)
                break
            else:
                print(f"Le reponse ne est pas correct :-(")
                print(f"{a} + {b} != {userInput}")
                if _try < len(numOfTries):
                    print(f"essay encore, il rest {len(numOfTries) - _try} de {len(numOfTries)}")
                print("")
        
        if userRes != correctRes:
            print(f"hmm... let me help you, correct answer: {a} + {b} = {correctRes}")
            print("plus de chance la prochaine fois")
            time.sleep(waitTime)

    print("")
    print(f"Bravo, t'as fini ce jou, t'as reussi {cntSuccess} fois de {iter} ")
    print("Merci pour jouer avec moi :-) ")

def executeNextGame(min=0, max=99, iter=5, waitTime=5):
    print("\n")
    print("Bienvenue au jou de Avant/Apres !")
    print("Tu vas trouver le numero suivant/precendant entre {_min} and {_max}")
    print("Bonne chance !")
    print("")

    cntSuccess = 0
    for i in range(0, iter):
        a = random.randrange(min, max)
        
        print("\n")
        print("---------------------------------------------------")
        print("\n")
        
        addArr = [-1, 1]
        addInd = random.randrange(0, 2)
        add = addArr[addInd]
        
        userRes = -1
        correctRes = a + add
        numOfTries = [1, 2, 3]
        for _try in numOfTries:
            print(f"le numero est: {a}")
            if add == -1:
                print(f"quel numero vient AVANT {a}: ", end='')
            else:
                print(f"quel numero vient APRES {a}: ", end='')
 
            userInput = input()
            userRes = -2
            try:
                userRes = int(userInput)
            except:
                pass
            if userRes == correctRes:
                print(messageCorrect)
                cntSuccess += 1
                time.sleep(waitTime)
                break
            else:
                print(f"Wrong answer :-(")
                if add == -1:
                    print(f"{userInput} ne vient pas AVANT {a}")
                else:
                    print(f"{userInput} ne vient pas APRES {a}")

                retriesLeft = len(numOfTries) - _try
                if retriesLeft > 0:
                    print(f"essay encore, il rest {len(numOfTries) - _try} de {len(numOfTries)}")
                print("")
                time.sleep(waitTime)
        
        if userRes != correctRes:
            print(f"hmm... laisse-moi t'aider, bonne réponse est: {correctRes}")
            if add == -1:
                print(f"{correctRes} vient AVANT {a}")
            else:
                print(f"{correctRes} vient APRES {a}")
            print("plus de chance la prochaine fois")
            time.sleep(waitTime)

    print("")
    print(f"Bravo, t'as fini ce jou, t'as reussi {cntSuccess} fois de {iter} ")
    print("Merci pour jouer avec moi :-) ")




def executeEntreGame(min=1, max=98, iter=5, waitTime=5):
    print("\n")
    print("Bienvenue au jou de Entre !")
    print(f"Tu vas trouver un numero entre deau numeros")
    print("Bonne chance !")
    print("")

    cntSuccess = 0
    for i in range(0, iter):
        correctRes = random.randrange(min, max)
        a, b = correctRes - 1, correctRes + 1
        
        print("\n")
        print("---------------------------------------------------")
        print("\n")
        
        userRes = -1
        numOfTries = [1, 2, 3]
        for _try in numOfTries:
            print(f"Quel numero se trouve entre les {a} et {b}   : ", end='')
            userInput = input()
            userRes = -1
            try:
                userRes = int(userInput)
            except:
                pass
            if userRes == correctRes:
                print(messageCorrect)
                cntSuccess += 1
                time.sleep(waitTime)
                break
            else:
                print(f"Le reponse ne est pas correct :-(")
                print(f"{userInput} ne se trouve pas entre les {a} et {b}")
                if _try < len(numOfTries):
                    print(f"essay encore, il rest {len(numOfTries) - _try} de {len(numOfTries)}")
                print("")
        
        if userRes != correctRes:
            print(f"hmm... laisse-moi t'aider, bonne réponse est: {correctRes}")
            print(f"order correct est {a}, {correctRes}, {b}")
            print("plus de chance la prochaine fois")
            time.sleep(waitTime)

    print("")
    print(f"Bravo, t'as fini ce jou, t'as reussi {cntSuccess} fois de {iter} ")
    print("Merci pour jouer avec moi :-) ")

def executeGreaterGame(min=1, max=98, iter=5, waitTime=5):
    print("\n")
    print("Bienvenue au jou de comparison !")
    print(f"Tu vas trouver le numero plus grand entre deau numeros")
    print("Bonne chance !")
    print("")

    cntSuccess = 0
    for i in range(0, iter):
        a, b = random.randrange(min, max), random.randrange(min, max)
        correctRes = a if a > b else b
        
        print("\n")
        print("---------------------------------------------------")
        print("\n")
        
        userRes = -1
        numOfTries = [1, 2, 3]
        for _try in numOfTries:
            print(f"Quel numero est plus grand entre les {a} et {b}   : ", end='')
            userInput = input()
            userRes = -1
            try:
                userRes = int(userInput)
            except:
                pass
            if userRes == correctRes:
                print(messageCorrect)
                cntSuccess += 1
                time.sleep(waitTime)
                break
            else:
                print(f"Le reponse ne est pas correct :-(")
                print(f"{userInput} n'est pas plus grand entre les {a} et {b}")
                if _try < len(numOfTries):
                    print(f"essay encore, il rest {len(numOfTries) - _try} de {len(numOfTries)}")
                print("")
        
        if userRes != correctRes:
            print(f"hmm... laisse-moi t'aider, bonne réponse est: {correctRes}")
            print(f"le numero plus grand entre {a}, {b} est {correctRes}")
            print("plus de chance la prochaine fois")
            time.sleep(waitTime)

    print("")
    print(f"Bravo, t'as fini ce jou, t'as reussi {cntSuccess} fois de {iter} ")
    print("Merci pour jouer avec moi :-) ")

def usage():
    print("")
    print("--game [sum|next|entre|greater] --min [0] --max [100] --iter [5] --wait [5] --name [Katherine]")
    print("")

if __name__ == "__main__":
    options, args = getopt.getopt(sys.argv[1:], "g:s:b:i:w:n:h",
                               ["game=",
                                "min=",
                                "max=",
                                "iter=",
                                "wait=",
                                "name=",
                                "help"])
    game = ''
    _min, _max = 0, 100
    _iter = 5
    waitTime = 5
    for opt, arg in options:
        print(f"opt: {opt}, arg: {arg}")
        if opt in ['-g', '--game']:
            game = arg
        elif opt in ['-s', '--min']:
            _min = int(arg)
        elif opt in ['-b', '--max']:
            _max = int(arg)
        elif opt in ['-i', '--iter']:
            _iter = int(arg)
        elif opt in ['-i', '--wait']:
            waitTime = int(arg)
        elif opt in ['-n', '--name']:
            userName = arg
            messageCorrect = f'Bravo {userName}  :-) :-) :-) :-) :-) :-) :-) :-)  Bon reponse'
        elif opt in ['-h', '--help']:
            usage()
            exit(0)
        else:
            raise Exception(f"unexpected argument: {opt}")
    
    if game == 'sum':
        executeSumGame(_min, _max, _iter, waitTime)
    elif game == 'next':
        executeNextGame(_min, _max, _iter, waitTime)
    elif game == 'entre':
        executeEntreGame(_min, _max, _iter, waitTime)
    elif game == 'greater':
        executeGreaterGame(_min, _max, _iter, waitTime)
    else:
        print("no game was specified, try --game sum")






















