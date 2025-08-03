import re

def is_valid_email(email):
 
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    email_input = input("Enter an email address: ")
    if is_valid_email(email_input):
        print("Valid email address ")
    else:
        print("Invalid email address ")

main()



#Enter an email address: john.doe@example.com
#Valid email address 
#Enter an email address: hello@world
#Invalid email address 

