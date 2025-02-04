userpwd = "r9nd0m_"
guess = input("What is your password? ")
attempts = 0
while (attempts < 4):
    if (userpwd != guess):
        guess = input("Password incorrect.  What is your password? ")
        attempts += 1
    else:
        print("You have been logged in.  Welcome!")
        quit()
print("Too many attempts.  You have been kicked off of the system.")