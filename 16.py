#QUESTION PAPER
from __future__ import print_function
import sys
import os;
import datetime
import time
count=0
print("\t\t***********^^WELCOME^^***********")
print("\t\t\t\t\t",datetime.datetime.now())
str=input("Enter your name:\n")
print("\n   INN Examination")
print("      Delhi,India\n")
var1=input("press Y to Continue \npress E to Exit\n")
if(var1=="y" or var1=="Y"):
    print("welcome!" +" "+str)
    print("\n\tExam will start in 30 sec\n")
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            #sys.stdout.write("\r" %(timeformat) )
            #sys.stdout.flush()
            print(timeformat, end='\r' ,flush=True)
            sys.stdout.flush()
            time.sleep(1)
            t -= 1
            #os.system('cls')
    print("\t## Instructions ##")
    print("1. Exam is of 30 min")
    print("2. There will 5 questions MCQ")
    print("3. Total Marks [25] , each question have equal marks")
    print("4. Passing Marks is [20]\n")
    print("\t**All The Best**\t\n")
    countdown(5)
    print("\nSelect the correct option")
    print("1. Modulator and demodulator as combinely  is known as –\n")
    print("A: Modulus")
    print("B: Modem")
    print("C: Mod switch")
    print("D: Mod access\n")
    #time.sleep(5)
    str2=input("\nAnswer:")
    countdown(5)
    
    if(str2=='b' or str2=='B'):
        count=count+5
    print("\n2. Which of the following network device has the slowest type of connection?\n")
    print("A: DSL")
    print("B: Router")
    print("C: Bridges")
    print("D: Dial-up modems")
    countdown(5)
    str3=input("\nAnswer:")
    if(str3=='d' or str3=='D'):
        count=count+5
    print("\n3. Which of the following is an example of Personal Area Networking?\n")
    print("A: Bluetooth")
    print("B: WAN")
    print("C: WLAN")
    print("D: All of the above")
    countdown(5)
    str4=input("\nAnswer:")
    if(str4=='a' or str4=='A'):
        count=count+5    
    print("\n")
    print("Your score is: ",count)    
elif(var1=="e" or var1=="E"):
    print("Thank you!")
else:
    print("X Invalid Input X")

