# PyCrack
Python Password Cracker

Top 10,000 most common passwords can be cracked
    Plain-text passwords can be checked (10)
    MD5 hashed passwords can be checked (10)
    BCrypt hashed passwords can be checked (10)
    SHA-256 hashed passwords can be checked (10)
Brute force approach option (10)
Dictionary Attack option (10)
Command line arguments can be taken in (10)


-p --plain = Plain Text
-m --md5 = MD5 Hashed
-c --crypt = BCrypt Hashed
-s --sha256 = sha256 hashed

-b --brute = brute force
-d --dict = dictionary attack

-i --input = File to inport passwords from
-o --output = file to output cracked password too

formating -----
    Python3 PyCrack someMd5 -m -b (Brute Force it)
    Python3 PyCrack SomeCrypt -c -d RockYou.txt
    Python3 PyCrack -i someList -o output.txt -d rockYou.txt

what we gotta do -----

make function that can create hash quickly for the dictionary word depending on what their choice was
(I.e if they said sha256 then it should know to convert each thing to sha256 vise versa)

take the file given after -d, store this file somehow
loop thru the file, encrypt the word to the correct hash, compare it to the hash we have, if it is the same return the unhashed word, if its not cont.
