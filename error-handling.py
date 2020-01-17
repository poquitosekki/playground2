# ERROR HANDLING IN PYTHON

# try:
# 	pass
# except Exception:
# 	pass
# else:
# 	pass
# finally:
# 	pass

# the file spelled wrong instead of test we said test
# instead of printing a long error message we print a friendly error message

# try:
# 	f = open('tes.txt')
# except Exception:
# 	print("Sorry this file does not exist !")

# Catch different exceptions (not being vague)
# try:
# 	f = open('test.txt')
# 	var = bad_var
# except FileNotFoundError as e:
# 	print(e)
# except Exception as e:
# 	print(e)

# ELSE :
# runs if our exception does not catch any error

# try:
# 	f = open('test.txt')
# except FileNotFoundError as e:
# 	print(e)
# except Exception as e:
# 	print(e)
# else:
# 	print(f.read())
# 	f.close()

# FINALLY :
# this code block runs no matter what happens
# whether the code is successufl or throw an exceptions

# try:
# 	f = open('test.txt')
# except FileNotFoundError as e:
# 	print(e)
# except Exception as e:
# 	print(e)
# else:
# 	print(f.read())
# 	f.close()
# finally:
# 	print("Executing our Finally statement ...")


# GENERAL
# you can also raise exceptions of your own (not only the ones that python throws)
try:
	open('test.txt')
	if f.name == "test.txt":
		raise Exception
except Exception as e:
	print("ERROR !")
