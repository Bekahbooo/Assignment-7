# Row number
size = int(input("Enter the number of rows: "))
#space until numbers start
print((" " * size) + str(size))
mult = 2
# first row
print((" " * (size - 1)) + str(size - 1) + " " + str(size - 1))
size -= 2
# rows until end
for i in range(size):
    
    print((" " * size ) + str(size) + ((" " + str(size)) * mult))
    size -= 1
    mult += 1
# didn't figure out how to count down instead of up in time