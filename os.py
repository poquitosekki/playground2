import os
from datetime import datetime

# Show all the attributes and methods that we can use in this module
# print(dir(os))

# DIRECTORYS
# get current working directory
# print(os.getcwd())
# Change the working directory
# os.chdir('/Users/poquito/Desktop/')
# print(os.getcwd())
# List all the file and directorys in the current folder (which is Desktop in this case)
# returns a list
# print(os.listdir())
#
# # CREATING
# # makes only the top level directory
# os.mkdir('mkdir-func')
# # we can make dirs with multiple levels unlike the mkdir
# os.makedirs('makedirs-func/sublevel')
#
# # REMOVING
# os.rmdir("mkdir-func")
# os.removedirs("makedirs-func/sublevel")
#
# # RENAMING
# os.rename('test.txt', 'demo.txt')
# print(os.listdir())
#
# # print all the information about file
# print(os.stat('demo.txt'))
# # get just the size of the file
# print(os.stat('demo.txt').st_size)
# # Time run
# mod_time = os.stat('demo.txt'.st_mtime)
# Change it to human readable format
# print(datetime.fromtimestamp(mod_time))

# os.chdir("/Users/poquito/Desktop")
# for dirpath, dirname, filename in os.walk("/Users/poquito/Desktop"):
#     print(dirpath, dirname, filename)

# return the environment : /Users/poquito
# print(os.environ.get('HOME'))
# # do the work for you instead of worying about / , it concatenates
# file_path = os.path.join(os.environ.get("HOME"), "test.txt")
# print(file_path)

# return the basename : test.txt
# print(os.path.basename("/tmp/test.txt"))
# # return the dirname : /tmp
# print(os.path.dirname("/tmp/test.txt"))
# # return both
# print(os.path.split("/tmp/test.txt"))
# # if you want to check the existence : False
# print(os.path.exists("/tmp/test.txt"))
# # check if it's directory : False (not dir)
# print(os.path.isdir("/tmp/blabla"))
# # check if it's a file : False (not file)
# print(os.path.isfile("/tmp/blabla"))
#
# # THIS IS REALLY IMPORTANT IT SPLITES THE ROOT AND THE EXTENSION
# # return them in a tuple
# print(os.path.splitext("/tmp/test.txt"))
