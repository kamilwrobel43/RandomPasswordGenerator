import random
def passwordgenerator(length,list,digitdec,specialchardec,keywordchange):
    sletflag = False
    bletflag = False
    specflag = False
    digitflag = False

    password = []
    while sletflag==False or bletflag==False or digitflag==False or specflag==False:
        sletflag = False
        bletflag = False
        specflag = False
        digitflag = False
        if keywordchange=="N":
            sletflag=True
            bletflag=True
        if digitdec == "N":
            digitflag = True
        if specialchardec == "N":
            specflag = True
        password.clear()
        options=["sLetter","bLetter"]
        newlist=[]
        if keywordchange=="N":
            newkeyword = "".join(list)
            password.append(newkeyword)
        else:
            if len(list)>0:
                for letter in list:
                    if letter.isalpha()==False:
                        newlist.append(letter)
                        if letter.isdigit():
                            continue
                        else:
                            continue
                    else:
                        rand=random.choice(options)
                        if rand=="sLetter":
                            newlist.append(letter.lower())
                            sletflag=True
                        else:
                            bletflag=True
                            newlist.append(letter.upper())
            newkeyword="".join(newlist)
            password.append(newkeyword)
        if digitdec=="Y":
            options.append("digit")
        if specialchardec=="Y":
            options.append("special")
        for i in range(length-len(newkeyword)):
            rand=random.choice(options)
            if rand=="digit":
                password.append(chr(random.randint(48,57)))
                digitflag=True
            if rand=="sLetter":
                sletflag=True
                password.append(chr(random.randint(97,122)))
            if rand=="bLetter":
                bletflag=True
                password.append(chr(random.randint(65,90)))
            if rand=="special":
                specflag=True
                diffranges=[chr(random.randint(33,47)),chr(random.randint(58,64)),chr(random.randint(91,96)),chr(random.randint(123,125))]
                password.append(random.choice(diffranges))
    random.shuffle(password)
    newpassword="".join(password)
    return newpassword


nextdecision="Y"
while nextdecision=="Y":
    length=(input("Type length of the password: "))
    while length.isnumeric()==False or int(length)<=0:
        length = (input("Type length of the password: "))
    length=int(length)
    keywordchangedecision="N"
    keyword=""
    keyworddecision=input("Do you want to use keyword in your password?(Y/N): ").upper()
    while keyworddecision not in ["Y","N"]:
        keyworddecision = input("Do you want to use keyword in your password?(Y/N): ").upper()
    if keyworddecision=="Y":
        keyword=input("Type keyword: ")
        keywordchangedecision=input("Do you want your keyword to be modified (mixed big and small letters)?").upper()
        while keywordchangedecision not in ["Y","N"]:
            keywordchangedecision = input("Do you want your keyword to be modified (mixed big and small letters)?").upper()
    digitdecision=input("Do you want to have extra digit in your password?(Y/N): ").upper()
    while digitdecision not in ["Y","N"]:
        digitdecision = input("Do you want to have extra digit in your password?(Y/N): ").upper()
    specialchardecision=input("Do you want to have extra special characters in your password?(Y/N): ").upper()
    while specialchardecision not in ["Y","N"]:
        specialchardecision = input("Do you want to have extra special characters in your password?(Y/N): ").upper()
    while (length<len(keyword)+2 and specialchardecision=="Y" and digitdecision=="Y") or (length<len(keyword)+1
    and(specialchardecision=="Y" or digitdecision=="Y")) or length<len(keyword):
        print("The length of your password must be longer or at least equal to the length of keyword you typed and have 1 or 2 extra length for digit or/and special character!")
        length = (input("Type length of the password: "))
        while length.isnumeric() == False or int(length) <= 0:
            length = (input("Type length of the password: "))
        length = int(length)

        keyword = ""
        keyworddecision = input("Do you want to use keyword in your password?(Y/N): ").upper()
        while keyworddecision not in ["Y", "N"]:
            keyworddecision = input("Do you want to use keyword in your password?(Y/N): ").upper()
        if keyworddecision == "Y":
            keyword = input("Type keyword: ")
            keywordchangedecision = input("Do you want your keyword to be modified (mixed big and small letters)?").upper()
            while keywordchangedecision not in ["Y", "N"]:
                keywordchangedecision = input("Do you want your keyword to be modified (mixed big and small letters)?").upper()
        digitdecision = input("Do you want to have extra digit in your password?(Y/N): ").upper()
        while digitdecision not in ["Y", "N"]:
            digitdecision = input("Do you want to have extra digit in your password?(Y/N): ").upper()
        specialchardecision = input("Do you want to have extra special characters in your password?(Y/N): ").upper()
        while specialchardecision not in ["Y", "N"]:
            specialchardecision = input("Do you want to have extra special characters in your password?(Y/N): ").upper()

    listofletterskeyword=list(keyword)

    print("Your password: ")
    password=passwordgenerator(length,listofletterskeyword,digitdecision,specialchardecision,keywordchangedecision)
    print(password)

    filedecision=input("Do you want to save it in file?(Y/N)").upper()
    while filedecision not in ["Y","N"]:
        filedecision = input("Do you want to save it in file?(Y/N)").upper()
    if filedecision=="Y":
        filename=input("Type path and file name : ")
        name=input("What is this password to?: ")
        with open(filename,"a") as file:
            file.write(str(name)+": "+password+"\n")
    nextdecision=input("Do you want to create another password?(Y/N)?: ").upper()
    while nextdecision not in ["Y","N"]:
        nextdecision = input("Do you want to create another password?(Y/N)?: ").upper()
print("Thank you, Bye!")





