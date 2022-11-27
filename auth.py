#dictionary of users
users ={
    'user1':{'firstName':"Vaibhav", 'lastName':"Malik", 'email':"vaibhav-malik@live.com",'password':"123@mail"},
    'user2':{'firstName':"Dallas", 'lastName':"Singh", 'email':"dallas@gmail.com",'password':"456@mail"},
    'user3':{'firstName':"Casey", 'lastName':"Mane", 'email':"casey@aol.com",'password':"789@mail"},
    'user4':{'firstName':"Kadu", 'lastName':"Singh", 'email':"kadu@outlook.com",'password':"910@mail"}
}

#recursive function checks if users exists to welcome them. if not it will ask for login again
def welcomeUser():
    userEmail = str(input("Please enter your email address."))
    userPassword = str(input("Please enter your password"))
    
    for i,j in users.items():
        if (j['email'] == userEmail) and (j['password'] == userPassword):
            print("Hello,",j['firstName'],j['lastName'],"you have successfully logged in")
            return
    print("wrong info")
    welcomeUser()


#calling the function
welcomeUser()






welcomeUser()