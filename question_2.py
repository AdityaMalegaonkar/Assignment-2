# Assignment - 2

# 2. Write a Python program to print a dictionary whose keys should be the alphabet from a-z and
# the value should be corresponding ASCII values

alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ascii_list = []

for i in range(97 , 97 + 26):       # ascii value of "a" is 97 and there are total 26 alphabets
    ascii_list.append(i)

final_dict = dict(zip(alphabet_list , ascii_list))
print(final_dict)