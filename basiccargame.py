user_input=input("type help to start:")
while user_input=="help":
    print('''1.)start-to start the car 2).stop-stop the car 3).quit-exit''')
    choice=input()
    if choice.upper()=="start" or choice.lower()=="start":
        print('car started lets go!')
    elif choice.upper()=="stop" or choice.lower()=="stop":
        print("car stopped!!!")
    elif choice.upper()=="quit" or choice.lower()=="quit":
        print(" car program exited ")
        break
else:
    print("i cannot understand!")
        
