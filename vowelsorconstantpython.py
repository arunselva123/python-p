l = input("Input a letter of the alphabet: ")
https://www.onlinegdb.com/online_python_compiler#editor_1
if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 
