import os
import pyttsx3
print("**********************************Welcome To My ChatBox***************************************")
pyttsx3.speak("\n\n\n\n\n\n  Welcome To My ChatBox \n\n\n")

print()
while True:   
    print("Hii... what you want to run \t\t" ,end='')
    pyttsx3.speak("Hii... what you want to run ")
    p = input()
    if("run" in p) and ("chrome" in p) :
        print("Opening a Chrome Browser.....")
        os.system("chrome")

    elif("run" in p) and ("vlc" in p):
        print("Opening vlc.....")
        os.system("vlc")

    elif("run" in p) and (("notepad" in p)or("editor" in p)):
        print("Opening Text Editor.... ")
        os.system("notepad")

    elif("calculator" in p):
        print("Opening Calculator.....")
        os.system("calc") 
   
    elif("run" in p) and (("jupyter" in p)or("IDE" in p)):
        print("Opening Jupyter IDE.....")
        os.system("jupyter notebook")

    elif("run" in p) and (("paint" in p) or ("drawing software" in p)):
        print("Opening Paint Software!")
        os.system("mspaint")

    elif("run" in p) and ("youtube" in p):
        print("Opening YouTube")
        os.system("chrome ")

    elif ("linkedin" in p):
        print("Opening Linkedin")
        os.system("chrome https://www.linkedin.com/in/shalini-rana-b1771218a/")

    elif  ("twitter" in p):
        print("Opening Twitter")
        os.system("chrome https://twitter.com/_Shalini_Rana_")

    elif  ("gmail" in p):
        print("Opening Gmail.....")
        os.system("chrome www.gmail.com")

    elif ("whatsapp" in p):
        print("Opening Whatsapp.....")
        os.system("chrome web.whatsapp.com")

    elif ("facebook" in p):
        print("Opening Facebook.....")
        os.system("chrome https://www.facebook.com/avantika.rana.562/")

     elif ("instagram" in p):
        print("Opening Instagram.....")
        os.system("chrome https://www.instagram.com/shalinirana___/")

    elif ("amazon" in p):
        print("Opening Amazon......")
        os.system("chrome www.amazon.in") 
 
    elif ("flipkart" in p):
        print("Opening Flipkart.....")
        os.system("chrome www.flipkart.com")

    elif ("teamviewer" in p): 
        print("Opening TeamViewer")
        os.system("teamviewer")

    elif(("show" in p)or("listout" in p))and("directory" in p):  
        print("Here show all the directories...")
        os.system("dir") 
 
    elif("clear" in p)and("screen" in p):
        os.system("cls")  
   
    elif("exit" in p):
        pyttsx3.speak("Hope You Like chatbox!!!!!!!!!")
        print("________________________________________________________________________________________________________________________")
        os.system(exit())
        break
    else:
        print("I am sorry, This service is not available")
        pyttsx3.speak("I am sorry, this service is not available")
        
