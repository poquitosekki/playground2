def main():
    # print("First Module's Name : {}".format(__name__))
    pass

# check if this file is run directly by python or being imported
# this code does not run if we imported that file as a module for other files
if __name__ == '__main__':
    print("Run directly")
else:
    print("Run from import")

# This prints MAIN
# before python runs any file or code
# it sets a few special variable eg : name
# it sets the name var to MAIN
# Whenever we add a module it sets the name to that module
# print("First Module's Name : {}".format(__name__))
