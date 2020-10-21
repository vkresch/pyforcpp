####################################################################################
# Simple function definiton
def say_hello():
    print("Hello world!")

# Explicit type definition
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

def mean_manual(seq):
    n = 0.0
    for x in seq:
        n += x
    return n/len(seq)

def mean_builtin(seq):
    return sum(seq)/len(seq)

# Prototyping is not needed

####################################################################################
# Call by reference/value example in python only with objects possible

####################################################################################
# Pass function address and run
other_mean_name = mean_manual

def ForEach(values, func):
    for value in values:
        func(value)


####################################################################################
# Python decorators

####################################################################################
# Return multiple values
def multiple_values(a, b):
    return a, b

####################################################################################
# Templates in python are implicit and builtin
# Means calculation of float or int are already considered

####################################################################################
# Lambda functions
mean = lambda seq: sum(seq) / len(seq)

####################################################################################
# main function
def main():
    rvec = [1, 2, 3, 4, 5]
    print(mean_manual(rvec))
    c, d = multiple_values(1, 2)

if __name__=="__main__":
    main()