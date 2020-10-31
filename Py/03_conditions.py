def main():
    a = 4
    message = ""

    if a > 5:
        message = "Greater than 5"
    elif a == 4:
        message = "Equals to 4"
    else:
        message = "Not Greater than 5 and not equal to 4"

    print(message)

    # Similar Tenary Operators in C++ (simple)
    # Example for two statements
    message = "Greater than 5" if a > 5 else "Not Greater than 5"
    print(message)

    # Example for three statements
    message = "Greater than 5" if a > 5 else ("Equals to 4" if a == 4 else "Not Greater than 5 and not equal to 4")
    print(message)

    
# Switch does not exist in Python
# Use python dictionary
def numbers_to_strings(argument):
    # Similar Hash table
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    main()
