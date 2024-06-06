from datetime import datetime
from datetime import date


def inputsuser():
    # Register
        first_name = input("Enter your first name:    ")
        last_name = input("Enter your last name:     ")

        email = input("Enter your email:      ")
        while validate_email(email) == False:
            email = input("please enter valid email: ")
            
        password = input("Enter your password: ")    
        while Validate_password(password) == False:
            password = input("please enter valid password: ")
            
        mobile_phone = input("Enter your mobile phone: ")            
        while Validate_phone_number(mobile_phone) == False:
            mobile_phone = input("please enter valid phone number: ")
        
        user = User(first_name, last_name, email, password, mobile_phone)   
        if validate_user_data(email, password, mobile_phone):
            user.register()
            print("Registration successful!") 



class User:
    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone
        self.is_activated = False

    def register(self):
        with open("dataFile.txt", "a") as file:
            file.write(f"{self.first_name},{self.last_name},{self.email},{self.password},{self.mobile_phone}\n")
        
                            
 
                 
def login(email, password,Name):
    with open("dataFile.txt", "r") as file:
        for line in file:
            user_data = line.strip().split(",")
            if len(user_data) >= 4 and user_data[2] == email and user_data[3] == password and user_data[0] == Name:
                print("Login successful!")
                return True
        print("Username or password is incorrect")
        return False       

        
def Validate_phone_number( mobile_phone):
    if len(mobile_phone) != 11 or mobile_phone[:3] not in ['010', '011', '012']:
        print("Invalid phone number. Please try again.")
        return False
    return True


def validate_email(email):
    with open("dataFile.txt", "r") as file:
        for line in file:
            user_data = line.strip().split(",")
            if len(user_data) >= 3 and user_data[2] == email:
                print("Email already exists.")
                return False

    if "@" not in email or "." not in email:
        print("Invalid email. Please try again.")
        return False

    return True
    
    
    
def Validate_password(password):
    if len(password) < 8:
        print("Invalid password. Please try again.")
        return False
    return True




def validate_user_data(email, password, mobile_phone):
    valid = True

    if not validate_email(email):
        valid = False
    
    if not Validate_password(password):
        valid = False
        
    if not Validate_phone_number(mobile_phone):
        valid = False
                
    return valid 












def is_valid_date(date_text, date_format='%Y-%m-%d'):
    try:
        datetime.strptime(date_text, date_format)
        return True
    except ValueError:
        return False


def list_projects():
        filepath = "project.txt"
        with open(filepath, 'r') as file3:
            # Read the entire content of the file
            file_content = file3.read()
            print(file_content)

def printlist():
    print("- - - - the all project in system : --  - - - - - - - -  - \n")
    list_projects()
    print("- - - - the all project in system : --  - - - - - - - -  -\n")
    print("##################################################\n")



def delfun(Name):
    with open('project.txt', 'r') as file:
        lines = file.readlines()
    delword = input("please enter title that your are want to delete :  ")
    new_lines = []
    for line in lines:
        values = line.strip().split(',')
        if values[1] != delword or values[0] != Name:
            new_lines.append(line)

    with open('project.txt', 'w') as file:
        file.writelines(new_lines)
    
    printlist()



def inputs(Name):
    title = input("Enter title:    ")
    details= input("Enter details:    ")
    while True:
        total_target = input("Enter total_target:    ")
        if not total_target.isdigit():
            print("this is not number please enter number :   ")
            continue
        start_time = input("Enter a date (YYYY-MM-DD) :   ")
        end_date=input("Enter end_date: (YYYY-MM-DD) :    ") 
        if is_valid_date(start_time) and is_valid_date(end_date) and start_time < end_date:
            print(f"The date of start and end is valiedis valid.\n")
            break
        else:
            print(f"The date {start_time} or {end_date} or start date greater than end dateis not valid. Please try again.")
    
    project=Project(title,details,total_target,start_time,end_date)
    project.create_project(Name)
    print("##################################################")



def update_word_in_file(Name):
    printlist()
    delfun(Name)
    print("Enter new information of updated project :   \n")
    inputs(Name)
    printlist()    





def upfdatemony(projectName, money,Name):
    with open('project.txt', 'r') as file:
        lines = file.readlines()
    new_lines = []
    for line in lines:
        values = line.strip().split(',')
        if projectName == values[1] and values[0] == Name:
            # Split the line into individual values         
            if values[3] != "0":

                if  int(values[3]) > money:
                    # Update the money value
                    money=int(values[3])-money
                    values[3] = str(money)
                    # Join the updated values back into a line
                    new_line = ','.join(values) + '\n'
                    new_lines.append(new_line)
                else:
                    print(f"we take only {values[3]} to finsh project Thank you  : ")
            else:
                print("this project is completed and not need more mony :   \n")
        else:
            new_lines.append(line)

    with open('project.txt', 'w') as file:
        file.writelines(new_lines)

    printlist()

class Project:
    def __init__(self, title, details, total_target, start_time, end_time):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time


    def create_project(self,Name):
        # Implement project creation logic here
        with open("project.txt", "a") as file2:
            file2.write(f"{Name},{self.title},{self.details},{self.total_target},{self.start_time},{self.end_time}\n")
    







def delfundate():
    with open('project.txt', 'r') as file:
        lines = file.readlines()
    current_date = date.today()
    new_lines = []
    for line in lines:
        values = line.strip().split(',')
        if values[5] > str(current_date):
            new_lines.append(line)

    with open('project.txt', 'w') as file:
        file.writelines(new_lines)
    


def main():

    delfundate()

    while True:
        print("Welcome to the Console Home!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("------------------------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":

            inputsuser()

        elif choice == "2":

            email = input("Enter your email:    ")
            password = input("Enter your password:    ")
            Name=input("please Ener Your Frist name   : ")
            while login(email,password,Name) == False:
                email = input("Enter your email:   ")
                password = input("Enter your password:   ")
                Name=input("please Ener Your Frist name   : ")
                login(email,password,Name)

            print(Name)
            # Login
            # Implement login logic here
            print(f"Welcome  {Name}  to the project!")
            print("1. create project :")
            print("2. list all project :")
            print("3. update :  ")
            print("4. delete :   ")
            print("5. I want to give mony :   \n")


            
            choiceProject  =input(" Enter what are you want :")
            print("------------------------------------------------")


            if choiceProject == "1" :
                inputs(Name)
                delfundate()
            elif choiceProject == "2" :
                print("this is all alist that you are searched for : \n")
                printlist()
            elif choiceProject == "3" :
                print("this is option to update list : \n")
                update_word_in_file(Name)
            elif choiceProject == "4" :
               print("this is option To delete List list : \n")
               delfun(Name)
            elif choiceProject == "5" :
                printlist()
                projectName=input("please Enter title of project name  :   \n")
                money=int(input("Enter mony please :   \n"))
                upfdatemony(projectName,money,Name)

                

        elif choice == "3":
            # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



    def main():
        # Implement the main console app loop here
        pass


    if __name__ == "__main__":
        main()







