import re

def check_password_strength(password):
  
    length_rule = len(password) >= 8
    lowercase_rule = re.search(r'[a-z]', password) is not None
    uppercase_rule = re.search(r'[A-Z]', password) is not None
    digit_rule = re.search(r'\d', password) is not None
    special_char_rule = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    strength_score = sum([length_rule, lowercase_rule, uppercase_rule, digit_rule, special_char_rule])


    if strength_score == 5:
        return "✅ Strong password!"
    elif strength_score >= 3:
        return "🟡 Medium password. Consider making it stronger."
    else:
        return "🔴 Weak password. Try using a mix of letters, digits, and symbols."

def main():
    password = input("Enter your password to check its strength: ")
    result = check_password_strength(password)
    print(result)

main()

#Enter your password to check its strength: Test123
#🟡 Medium password. Consider making it stronger.
#Enter your password to check its strength: Test@1234
#✅ Strong password!
