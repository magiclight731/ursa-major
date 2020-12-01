import main.py as RSA
#
#
Yes=True
yes=True
true=True
y=True
n=False
no=False
No=False
false=False
stop=False
#
print("Hello and welcome to this particular RSA encryption program!")
print("here you can generate a pair of keys, or you can apply your RSA-compliant keys to a message to get your encrypted message.")
print("valid commands are:")
print("generate (0) \nencrypt (1) \ndecrypt (2) \nencrypt with signature (3) \ndecrypt with signature (4) \nExplain RSA (A)")
print("\nbut first, would you like to activate Tabula Recta Mode? \n \nTabula Recta Mode runs the Tabula Recta coding method over your inputs, scrambling the values. It needs to be on for decrypting messages encrypted with it on.")
toggle=input("Enable Tabula Recta Mode? ")
while stop==False:
   print()
   command=input("what would you like to do? ")
   print()
   if command=="generate" or command=="generate keys" or command=="0":
      w=8
      while w==8:
         w=5
         try:
            minimum=int(input("what's the lower bound of your p and q? "))
            maximum=int(input("what's the upper bound of your p and q? "))
         except ValueError:
            print("That is not a number. Please enter a number.")
            w=8
      print()
      maximum,minimum=max(minimum,maximum),min(minimum,maximum)
      try:
         RSA.provideKeys(minimum, maximum)
      except MemoryError:
         print("those Bounds are too big, sorry.")
   elif command=="encrypt" or command=="encrypt message" or command=="encode" or command=="encode message" or command=="1":
      plaintext=input("what message are you encrypting? ")
      if toggle==True:
         plaintext=RSA.tabulaRecta(plaintext,True)
      plaintext=RSA.convert1(plaintext)
      print()
      print("now, enter the encryption key:")
      key=RSA.take_Key()
      ciphertext=RSA.convert3(plaintext,key[0],key[1])
      print()
      print(ciphertext)
   elif command=="decrypt" or command=="decrypt message" or command=="decode" or command=="decode message" or command=="2":
      w=8
      while w==8:
         w=5
         try:
            ciphertext=eval(input("what message (in list form) are you decrypting? "))
         except (NameError,SyntaxError):
            print("That is not a list. Please enter a list.")
            w=8
      print()
      print("now, enter the decryption key:")
      key=RSA.take_Key()
      plaintext=RSA.convert3(ciphertext,key[0],key[1])
      print()
      plaintext=RSA.convert2(plaintext)
      if toggle==True:
         plaintext=RSA.tabulaRecta(plaintext,False)
      print(plaintext)
   elif command=="encrypt with signature" or command=="encrypt signature" or command=="encode with signature" or command=="encode signature" or command=="3":
      reassure=False
      while (reassure==False):
         plaintext=input("what message are you encrypting? ")
         plaintext=plaintext+" "
         sig=input("what is your signature? ")
         full_plaintext=plaintext+sig
         print(full_plaintext)
         reassure=eval(input("is this what you want to encrypt? "))
      print("\nenter their public key:")
      PubK=RSA.take_Key()
      print("\nenter your private key:")
      PriK=RSA.take_Key()
      if toggle==True:
         plaintext=RSA.tabulaRecta(plaintext,True)
         sig=RSA.tabulaRecta(sig,True)
      plaintext=RSA.convert1(plaintext)
      sig=RSA.convert1(sig)
      unique=eval(input("do you want to use a unique signature marker? "))
      if (unique==True):
         print("These values for your marker are invalid. Please do not choose them.")
         for item in plaintext:
            print(item,end=" ")
            if ((item % 15) == 0):
               print()
         print(pubK[0])
         w=8
         while w==8:
            w=5
            try:
               mark=int(input("what marker value would you like to use? "))
            except ValueError:
               print("That is not a number. Please enter a number.")
               w=8
         ciphertext=RSA.convert4a(plaintext,PubK[0],PubK[1],PriK[0],PriK[1],sig,mark)
      else:
         ciphertext=RSA.convert4a(plaintext,PubK[0],PubK[1],PriK[0],PriK[1],sig)
      print(ciphertext)
   elif command=="decrypt with signature" or command=="decrypt signature" or command=="decode with signature" or command=="decode signature" or command=="4":
      check=0
      unique=eval(input("is there a unique signature marker? "))
      if (unique==True):
         mark=int(input("what marker value was used? "))
         check=1
      print("\nenter their public key:")
      PubK=RSA.take_Key()
      print("\nenter your private key:")
      PriK=RSA.take_Key()
      ciphertext=eval(input("finally, what is your mesasage? "))
      if check==1:
         plaintext=RSA.convert4b(ciphertext,PriK[0],PriK[1],PubK[0],PubK[1],unique)
      else:
         plaintext=RSA.convert4b(ciphertext,PriK[0],PriK[1],PubK[0],PubK[1])
      sig=RSA.convert2(plaintext[1])
      plaintext=RSA.convert2(plaintext[0])
      if toggle==True:
         sig=RSA.tabulaRecta(plaintext[1],False)
         plaintext=RSA.tabulaRecta(plaintext[0],False)
      plaintext=plaintext+sig
      print(plaintext)
   elif command.upper()=="EXPLAIN" or command.upper()=="EXPLAIN RSA" or command.upper()=="A":
      print("RSA is an early form of Assymentric Cryptography.")
      print("Assymetic cryptography works through Key-pairs, or pairs of information that decrypt each other.")
      print("This means that, even if someone has one key, they cannot messages encrypted with that key; rather, they need the corresponding 'other' key from the keypair.")
      print("In RSA, keys are made of two numbers: the base N, and the exponent E. keys are written as (n,e).")
      print("in this code, you can generate a key pair by inputting bounds for p and q, the two factors of N. the code will then generate values for E, and ask you to choose one of these values. It will then return your Public Key and your Private Key.")
      print("Your public key may be sent to anyone you wish. It is used to encrypt messages so that only you may decrypt that message. You can also use it to decrypt certain messages, verifying the sender.")
      print("DO NOT TELL ANYONE YOUR PRIVATE KEY. it is solely for yourself. You can use it to decrypt messages meant for your eyes only, or to encrypt messages that assure people it is you who sent it.")
      print("As you can see, keys in RSA can be used to verify sender OR recipitent, exclusively. However, RSA also has a 'signature' method that does both of these.")
      print("when encrypting a message with a signature, you encrypt a part of the message with your private key. The result is then re-encrypted with the intended recipitent's public key, possibly adding some extra parts to the message.")
      print()
      print("This code also uses a Tabula Recta encryption method. Tabula Recta is an old method of encrypting messages. It makes your message be less obvious based on the frequency of certain characters. it is reccommended, but not necessary. Also, it must be on if you plan to decrypt messages that were encrypted in this code with the Tabula Recta code on.")
      print()
      print("Anyways, please be aware that this code is not incredibly high-security or user-friendly. You will need to copy down your keys when they are returned to you. It is reccommended you use large values for your p and q bounds when generating keys. You must input your encrypted lists as they were given by the function; otherwise you may have errors with the code.")
   else:
      print("That was not one of the available commands for this program. Please try again.")
   print()
   stop=eval(input("would you like to Stop? "))
#
