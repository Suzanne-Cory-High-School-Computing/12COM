class Password_manager:
    def __init__(self):
        self.old_passwords = [] # initialise the list when the constructor is called
        print('The list has been initialised to: ',self.old_passwords)

    def get_password(self):
        if len(self.old_passwords) > 0:
            current_password = self.old_passwords[-1]
        else:
            current_password = ""
        return (current_password)
    
    def set_password(self,new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
        else:
            print('You cannot re-use old passwords.  Please try again.')
        print('The list has been set to: ',self.old_passwords)

    def is_correct(self,curr_password):
        if curr_password == self.old_passwords[-1]:
            return True
        else:
            return False
        print('The list contains: ',self.old_passwords)

my_object = Password_manager() # constructor creates new object

choice = int(input('Would you like to \n1 - get your current password\n2 - set a new password\n3 - enter your current password\n4 - exit: '))
while (True):
    if choice == 1: # get the current password
        print('Your current password is',my_object.get_password())
    elif choice == 2: # set a new password
        new_password = input('Enter a new password: ')
        my_object.set_password(new_password)
    elif choice == 3: # verify the password
        entered_password = input('Enter your current password: ')
        print(my_object.is_correct(entered_password))
    else:
        quit()
    choice = int(input('Would you like to \n1 - get your current password\n2 - set a new password\n3 - enter your current password\n4 - exit: '))