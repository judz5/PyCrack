import getopt, sys, hashlib

mode = ""
attack = ""

dictFile = ""

longEnabled = False

def setMode(modeSet):
    global mode
    mode = modeSet
    print("Mode Set To : %s" % mode)

def setAttack(attackSet, file):
    global attack, dictFile
    attack = attackSet
    print("Attack Method Set to : %s" % attackSet)
    if(attack == "Dictionary"):
        dictFile = file
        print("Dictionary File : %s" % dictFile)

def checkMode(test):
    global mode
    if test == mode:
        return True
    else:
        return False

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[2:]

options = "pmsbd:l"

pw = sys.argv[1]
if pw in ['-p','-m','-s', '-b', '-d', '-l']:
    print("No Password Given To Crack!")
    quit()

print("Attemping to Crack : %s" % pw)

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

if(attack == "Dictionary"):
    with open(dictFile) as pwList:
        for line in pwList:
            l = line.rstrip().encode('utf-8')
        
            if checkMode("MD5"):
                hashLine = hashlib.md5(l)
            elif checkMode("SHA-256"):
                hashLine = hashlib.sha256(l)
            
            if(longEnabled):
                print("Currently Checking : %s" % line.rstrip())

            if(hashLine.hexdigest() == pw):
                print("\nCracked! Password is : %s" % line)
                quit()


    
