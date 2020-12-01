import random
import math as m
#
#
def isPrime(n1):
  for x in range(2,n1):
    if n1%x==0:
      return False
  return True
#
#
def findN(mins,maxs):
  primes = []
  for i in range(mins,maxs):
    if isPrime(i)==True:
      primes.append(i)
  if len(primes)<=3:
    return "X"
  p = random.choice(primes)
  q=p
  while p==q:
    q = random.choice(primes)
  n = p*q
  return n,p,q
#
#
def eulerT(n1,p=0,q=0):
  if (p!=0) and (q!=0):
    return (p-1)*(q-1)
  liste=[]
  for x in range(1,n1):
    temp=m.gcd(n1,x)
    if temp==1:
      liste.append(x)
  return len(liste)
#
#
def findKeys(n,p=0,q=0):
  if p!=0 and q!=0:
    et=(p-1)*(q-1)
  else:
    et=eulerT(n)
  options=[]
  for item in range(1,et):
    if m.gcd(item,et)==1:
      options.append(item)
  print("some possible values for e:")
  listeo=[]
  check=False
  while check==False:
    k=0
    while k<10:
      c=random.choice(options)
      listeo.append(c)
      k+=1
    for option in listeo:
      print(option, end=" ")
    checkr=input("\nAre these values Satisfactory? ")
    if checkr=="y" or checkr=="yes" or checkr=="Yes" or checkr=="Y" or checkr=="true":
      check=True
    else:
      check=False
    listeo=[]
  q=1
  while q==1:
    q=0
    try:
      e=int(input("\nwhich option do you want to have as e? "))
    except ValueError:
      q=1
      print("not a number.")
    if (e in options)==False:
      q=1
      print("Please try again.")
  print()
  d=0
  for item in options:
    test=e*item
    if test%et==1:
      d=item
  return e,d,et
#
#
def provideKeys(minns,maxxs):
  ne=findN(minns,maxxs)
  if ne=="X":
    print("The bounds are too small. Sorry!")
    return
  ke=findKeys(ne[0],ne[1],ne[2])
  pubk=(ne[0],ke[0])
  prik=(ne[0],ke[1])
  print("private key:",prik,"\npublic key:",pubk)
  return prik,pubk
#
#
def convert1(str1):
  list1=[]
  for i in range(len(str1)):
    list1.append(str1[i])
  list2=[]
  for chara in list1:
    temp=ord(chara)
    list2.append(temp)
  return list2
#
#
def convert2(list1):
  list2=[]
  for chara in list1:
    temp=chr(chara)
    print(temp,end="")
    list2.append(temp)
  print()
  return list2
#
#
def convert3(list1,n,key):
  list2=[]
  for pt in list1:
    temp=pt**key
    temp=temp%n
    list2.append(temp)
  return list2
#
#
def convert4a(list1,n1,key1,n2,key2,list2,marker=4):
  list2a=[]
  list3=[]
  for pt in list2:
    temp=pt**key2
    temp=temp%n2
    list2a.append(temp)
  list1.append(marker)
  for add in list2a:
    list1.append(add)
  for pt in list1:
    temp=pt**key1
    temp=temp%n1
    list3.append(temp)
  return list3
#
#
def convert4b(list1,n1,key1,n2,key2,marker=4):
  list1a=[]
  list2a=[]
  for pt in list1:
    temp=pt**key1
    temp=temp%n1
    list1a.append(temp)
  for check in range(len(list1a)):
    if (list1a[check]==marker):
      split=check
      break
  list2=list1a[(split+1):]
  list1a=list1a[:split]
  for pt in list2:
    temp=pt**key2
    temp=temp%n2
    list2a.append(temp)
  list3=list1a+list2a
  return list3
#
#
def take_Key():
  knock=True
  while (knock==True):
    try:
      n=int(input("what is the first value of the key? "))
      e=int(input("what is the second value of the key? "))
      key=(n,e)
      print("\n"+str(key))
      checkr=input("Are these values correct? ")
      if checkr.upper()=="Y" or checkr.upper()=="YES" or checkr.upper()=="TRUE":
        knock=False
    except ValueError:
      print("not a number. The key is always two numbers.")
  return key
#
#
def tabulaRecta(str1,toggle):
  alphabet="abcdefghijklmnopqrstuvwxyz,./;'[]\`1234567890-= ~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
  list1=list(str1)
  list2=[]
  list3=[]
  list4=[]
  x=0
  for letter in alphabet:
    x+=1
    list2.append([letter,x])
  x=0
  for pt in list1:
    for letter in list2:
      if letter[0]==pt:
        if toggle==True:
          ct=letter[1]+x
        elif toggle==False:
          ct=letter[1]-x
        ct=ct%len(list2)
        list3.append(ct)
    x+=1
    x=x%len(list2)
  for ct in list3:
    for letter in list2:
      if letter[1]==ct:
        list4.append(letter[0])
  str2="".join(list4)
  return str2
#
#
