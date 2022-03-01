import getopt, sys, hashlib, time, multiprocessing

mode = ""
attack = ""

dictFile = ""

longEnabled = False

def setMode(modeSet):
    global mode
    mode = modeSet
    word = ("Mode : %s" % mode)
    for w in word:
        sys.stdout.write(w)
        sys.stdout.flush()
        time.sleep(.2)
    print("")

def setAttack(attackSet, file):
    global attack, dictFile
    attack = attackSet
    word = ("Method : %s" % attackSet)
    if(attack == "Dictionary"):
        dictFile = file
        word = ("Dictionary File : %s" % dictFile)
    word = word.center(25)
    for w in word:
        sys.stdout.write(w)
        sys.stdout.flush()
        time.sleep(.2)
    print("")

def checkMode(test):
    global mode
    if test == mode:
        return True
    else:
        return False

def loading():
    global notcomplete
    animation = ["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]

    i = 0
    while True:
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        i += 1

    print("\n")
    

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[2:]

options = "pmsbd:l"

pw = sys.argv[1]
if pw in ['-p','-m','-s', '-b', '-d', '-l']:
    print("No Password Given To Crack!")
    quit()

print(""" ██▓███ ▓██   ██▓ ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
░▒ ░     ▓██ ░▒░   ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░░       ▒ ▒ ░░  ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
         ░ ░     ░ ░         ░           ░  ░░ ░      ░  ░   
         ░ ░     ░                           ░               

""")

word = ("Hash : %s" % pw)
for w in word:
    sys.stdout.write(w)
    sys.stdout.flush()
    time.sleep(.2)

print("")

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-p"):
            setMode("PlainText")
             
        elif currentArgument in ("-m"):
            setMode("MD5")
             
        elif currentArgument in ("-s"):
            setMode("SHA-256")

        elif currentArgument in ("-b"):
            setAttack("Brute Force", "")

        elif currentArgument in ("-l"):
            longEnabled = True
            print("Test Output Enabled")

        elif currentArgument in ("-d"):
            #print ("Dictionary file Name: ", sys.argv[sys.argv.index("-d")+1])  
            setAttack("Dictionary", sys.argv[sys.argv.index("-d")+1])
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

if not(len(mode)>0):
    print("***** No Mode Detected, Please Retry And Enter a Mode Argument ******")
    quit()
if not(len(attack)>0):
    print("***** No Attack Setting Detected, Defaulting to Brute Force ******")
    setAttack("Brute Force", "")

print("\n")

count = 0

start_time = time.time()

t = multiprocessing.Process(target=loading)

if(attack == "Dictionary"):
    f = open(dictFile)
    
    t.start()
    print("Loading...")
    for line in f:
        l = line.rstrip().encode('utf-8')
        
        if checkMode("MD5"):
            hashLine = hashlib.md5(l)
            check = hashLine.hexdigest()
        elif checkMode("SHA-256"):
            hashLine = hashlib.sha256(l)
            check = hashLine.hexdigest()
        elif checkMode("PlainText"):
            check = line.rstrip()
        if(longEnabled):
            print("Currently Checking : %s" % line.rstrip())

        count = count + 1
        if(check == pw):
            t.terminate()
            print("\n")
            print("--- %s Attempts ---" % count) 
            print("--- %s seconds ---" % (time.time() - start_time))
            print("--- Password is :",pw,"---")
            quit()
t.terminate()
print("\n")
print("Password Not Found in Dictionary")

