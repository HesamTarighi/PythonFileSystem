# 1 __ Without Controller
# file = open('./files/1.txt', 'w')
# file.write('Hello Python')

# 2 __ With Controller

# write file
with open('./files/1.txt', 'w') as file :
    file.write('123456aa')
    
# read file
with open('./files/1.txt', 'r') as file :
    print(file.read())
    
# append file
with open('./files/1.txt', 'a') as file :
    file.write('\n1234')
    
# create file
with open('./files/2.txt', 'x') as file :
    file.write('123456aa')
