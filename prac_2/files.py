name_file = open('name.txt', 'w')
name = input("What is your name?: ")
name_file.write(name)
name_file.close()

open_file = open('name.txt', 'r')
open_file.read().strip()
print ("Your name is",name)
open_file.close()

out_file = open('numbers.txt', 'r')
num_one = int(out_file.readline())
num_two = int(out_file.readline())

print(num_one + num_two)
out_file.close()