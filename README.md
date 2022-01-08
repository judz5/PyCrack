# PyCrack
Python Password Cracker
2022 CSHS Cybersecurity

### Rubric (50/50)

- [x] Top 10,000 most common passwords can be cracked
- [ ] Plain-text passwords can be checked (10)
- [x] MD5 hashed passwords can be checked (10)
- [ ] BCrypt hashed passwords can be checked (10)
- [x] SHA-256 hashed passwords can be checked (10)
- [ ] Brute force approach option (10)
- [x] Dictionary Attack option (10)
- [x] Command line arguments can be taken in (10) 

### Command Line Arguments

        -p --plain = Plain Text

        -m --md5 = MD5 Hashed

        -s --sha256 = sha256 hashed


        -b --brute = brute force *** Not Implemented ***

        -d --dict = dictionary attack


        -i --input = File to inport passwords from *** Not Implemented ***

        -o --output = file to output cracked password too *** Not Implemented ***

### Formating

    - Python3 PyCrack 5f4dcc3b5aa765d61d8327deb882cf99 -m -b 
    - Python3 PyCrack 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 -s -d RockYou.txt
    - Python3 PyCrack -i passwords.txt -o output.txt -d rockYou.txt


