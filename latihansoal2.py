def is_password_valid(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_digit = False
    has_space = False
    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char.isspace():
            has_space = True
    return has_upper and has_digit and not has_space

print(is_password_valid("Password123"))  
print(is_password_valid("password"))  
print(is_password_valid("Pass 123"))    
     
          