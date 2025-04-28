def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1, n2):
    return n1/n2

operations = {
"+" : add,
"-" : sub,
"*" : mul,
"/" : div,
}

def calculator():
    from art import logo
    print(logo)
    user_input_1 = float(input("Enter the first number:\n"))
    continue_working = True
    while continue_working:

        for symbols in operations:
            print(symbols)
        operator_choice = input("Choose the operator:\n")
        user_input_2 = float(input("Enter next number :\n"))
        answer = operations[operator_choice](user_input_1, user_input_2)
        print(f"{user_input_1} {operator_choice} {user_input_2} = {answer}")

        choice = input(f"Type Y continue working with {answer} or N to start new calculation:\n").upper()
        if choice == "Y":
            user_input_1 = answer
        else:
            continue_working = False
            print("\n" * 20)
            calculator()    #recursion is happening here, calling a function in itself

calculator()
