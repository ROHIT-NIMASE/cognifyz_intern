def is_palindrome(text):
   
    cleaned_text = text.replace(" ", "").lower()
  
    return cleaned_text == cleaned_text[::-1]

def main():
    user_input = input("Enter a word or phrase: ")
    
    if is_palindrome(user_input):
        print("It's a palindrome ")
    else:
        print("Not a palindrome ")

main()
#Enter a word or phrase: Madam
#It's a palindrome 

#Enter a word or phrase: Hello
#Not a palindrome 
