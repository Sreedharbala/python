import two

print("top level in three.py")

two.func()
if __name__ == "__main__":
    print("three.py is being run directly")

else:
    print("three.py has been imported")