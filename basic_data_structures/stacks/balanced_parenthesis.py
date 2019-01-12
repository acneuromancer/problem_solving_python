from Stack import Stack

def parenthesis_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    return balanced and s.is_empty()


print(parenthesis_checker("((())))"))
print(parenthesis_checker("((()))"))
