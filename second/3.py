# a="How  are  you"
# print(a)

# b=a.split("  ")
# print(b)

# print(' '.join(b))

string="How are  you"
print(string)

string_lst1=string.split(" ")
print(string_lst1)

string_lst2=[s for s in string_lst1 if s!=""]
print(string_lst2)

print(' '.join(string_lst2))