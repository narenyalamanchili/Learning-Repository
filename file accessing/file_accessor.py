honda_writer = open('file accessing/honda.txt', 'w')
honda_reader = open('file accessing/honda.txt', 'r')

'''
4 things u can do in a open file function seen above:

1. r - reads the file and returns an error if said file does not exist, called with .read() function
2. w - overwrites anything in the file with whatever you decide to write into it after opening, called with .write() fucntion
3. a - appends (writes) what you want to write in the file, but is also called with .write() function
4. x - creates the file and returning an error if said file already exists. No call function necessary (doesn't need to be called cause why...?)

They will always be strings.
'''




honda_writer.write('today is the first ever written documentation released inside the honda files')

honda_writer.close()

print(honda_reader.read())

honda_appender = open('file accessing/honda.txt', 'a')

honda_appender.write(f'\n{str ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}')

honda_appender.close()

print(honda_reader.read())


'''
In order to have a variable do one specific thing, 
you need the variable to be attached to that specific thing when you open the variable using the open function.

In order to make it easier, not have to close the function, or have everything in one spot, 
you can use a with statement to pack everything together.
Since with statments have a body, 
it does not need to be closed and the functions inside will close as soon as everything in the body has finished.
'''

print('with statements:')

with open('file accessing/honda.txt', 'r') as honda:
    print(honda.readline())

#readline() function will only print the incoming line

with open('file accessing/honda.txt', 'r') as honda:
    for line in honda:
        print(line)



with open('file accessing/honda.txt', 'r') as honda:
    print(honda.read(25))
    print(honda.read())

print("exp")

print()
with open('file accessing/honda.txt', 'r') as honda:
    first_line = honda.read(len(honda.readline()))
    new_start = first_line[0:]
    print(new_start)

'''
first_line = honda.read(len(honda.readline())):
In this scenario, first_line is defined as reading the .txt file up until len(honda.readline())
This means that first_line will be equal to honda reading the entire first line

new_start = first_line[0:]:
When the line new_start = first_line[0:] is run, first_line is mentioned meaning that honda reads the next line
The [0:] means that it will set the variable new_start to the second line from index 0 to the end
'''


with open('file accessing/honda.txt', 'r') as honda:
    first_line = honda.read(len(honda.readline()))
    print(first_line)

'''
first_line is defined by honda reading the full .txt file until the given number argument (.read(index to read until))
len(honda.readline()) returns the index of which the line ends
This means that at:
first_line = honda.read(len(honda.readline()))
first_line = the first line of the .txt file

When print(first_line) is seen,
honda.read(len(honda.readline())) is called again making first_line contain the second line
'''
