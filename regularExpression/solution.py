def matchRegularExpressions(exp, string):
    
    if string == "":
        return exp == ""

    if exp == "" or exp == "*":
        return string == ""

    if (exp[0] == "." or exp[0] == string[0]):
       return matchRegularExpressions(exp[1:], string[1:])
    elif (exp[0] == "*"):
        return matchRegularExpressions(exp[1:], string[1:]) or matchRegularExpressions(exp, string[1:])
    else:
        return False


if __name__ == "__main__":
    print(matchRegularExpressions(".*at","chat"))
    print(matchRegularExpressions(".*at","chats"))
        
        