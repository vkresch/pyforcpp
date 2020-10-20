####################################################################################
# Simple way run script
print("Hello World")

####################################################################################
# Proper way to run script (inspired by C++)
# No code execution when importing functions
def main():
    print("Hello World")

if __name__ == "__main__":
    main()
    
####################################################################################
# Pass arguments to main
import sys

def main(argv):
    print(f"Hello {argv[1]}")

if __name__ == "__main__":
    main(sys.argv)



