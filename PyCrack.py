import getopt, sys

mode = ""
attack = ""

dictFile = ""

def setMode(modeSet):
    global mode
    mode = modeSet
    print("Mode Set To : %s" % mode)

def setAttack(attackSet, file):
    global attack, dictFile
    attack = attackSet
    print("Method Set to : %s" % attackSet)
    if(attack == "Dictionary"):
        dictFile = file
        print("Dictionary File : %s" % dictFile)

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
# Options
options = "pmcsbd:"
long_options = ["plain", "md5", "crypt", "sha256", 'brute', 'dict']
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-p", "--plain"):
            setMode("PlainText")
             
        elif currentArgument in ("-m", "--md5"):
            setMode("MD5")
             
        elif currentArgument in ("-c", "--crypt"):
            setMode("BCrypt")
        
        elif currentArgument in ("-s", "--sha256"):
            setMode("SHA-256")

        elif currentArgument in ("-b", "--brute"):
            setAttack("Brute Force", "")

        elif currentArgument in ("-d", "--dict"):
            #print ("Dictionary file Name: ", sys.argv[sys.argv.index("-d")+1])  
            setAttack("Dictionary", sys.argv[sys.argv.index("-d")+1])
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

if not(len(mode)>0):
    print("***** No Mode Detected, Please Retry And Enter a Mode Argument ******")
    quit()

print("why am i here")
    