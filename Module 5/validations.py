def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False

    return True


#validate_user('', -1)
#validate_user('', 1)
#print(validate_user('user', 1))
#print(validate_user(1234, 1))
#print(validate_user([], 1))
#print(validate_user(['user'], 1))
#print(validate_user([123], 1))