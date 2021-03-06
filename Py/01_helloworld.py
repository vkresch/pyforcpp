####################################################################################
# Simple way run script
print("Hello World")

####################################################################################
# Proper way to run script (inspired by C++)
# No code execution when importing functions
# Python use indentation and new lines
def main():
    print("Hello World 2")

if __name__ == "__main__":
    main()
    
####################################################################################
# Pass arguments to main
import sys

def main(argv):
    print(f"Hello {argv[1]}")

if __name__ == "__main__":
    main(sys.argv)
