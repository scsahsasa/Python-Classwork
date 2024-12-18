#String related methods

strmsg="helLOWorld!!!"

#converting data to lowercase

new_msg=strmsg.lower()

print("The lower case string is:",new_msg)

#converting data to uppercase

upp_msg=strmsg.upper()
print("The upper case string is:",upp_msg)

name="      Atharva       "
final_name=name.strip()
print("The final input is",final_name)

#removing left space and Right space
lspace=name.lstrip()
print("The leftspace removed",lspace)


rspace=name.rstrip()
print("The rightspace removed",rspace)

#str.replace(old, new): This method replaces all occurrences of the "old" substring
#with the "new" substring in the string.

sentence = "I like apples, and I like pineapple."
new_sentence = sentence.replace("like", "love")
print(new_sentence)
