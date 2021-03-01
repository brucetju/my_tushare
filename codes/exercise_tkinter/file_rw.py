file_path = 'basic_ctls.py'

print('Read whole:')
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('Read line by line:')
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)

with open('.temp','a') as file_object:
    file_object.write('writing')