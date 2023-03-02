text_file = open("origin.txt", "r")
lines = text_file.read()
data_into_list = lines.split("\n")
#lines = (text_file.readlines())
print(lines)
print(len(lines))
text_file.close()

for i to

'''import pandas as pd

falta = open('origin.txt', 'rb')
todo = open('after.txt', 'rb')

df1 = falta.readlines()
df2 = todo.readlines()

df2.set_index("Variant_ID", inplace=True)
df3 = df2.merge(df1, left_index=True, right_on="N_Casos_LCR", how='left')
df3.reset_index(inplace=True, drop=True)
'''
'''
f = open('origin.txt', 'r+')
my_file_data = f.read()
print(my_file_data)
f.close()
'''
'''import pandas as pd

def file_to_list(file):
    rtn: object = []
    file_object: object = open(file, "r")
    rtn: object = file_object.read().splitlines()
    file_object.close()
    return list(filter(None, pd.unique(rtn).tolist()))  # Remove Empty/Duplicates Values
    pass


file_to_list("/origin.txt")

# Example #
data_from_file: object = file_to_list('filename.txt')'''
'''import difflib

with open('origin.txt') as file_1:
    file_1_text = file_1.readlines()

with open('after.txt') as file_2:
    file_2_text = file_2.readlines()

    print()

# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='origin.txt',
        tofile='after.txt', lineterm=''):
    print(line)'''
'''
 def txt_to_lst(file_path):

    try:
        stopword=open(file_path,"r")
        lines = stopword.read().split('\n')
        print(lines)

    except Exception as e:
        print(e)

file1 = open ('origin.txt')'''


'''
file1 = open('origin.txt', 'r')
file2 = open('after.txt', 'r')
FO = open('output_file.txt', 'w')

for line1 in file1:
    print(line1)
    for line2 in file2:
        if line1 == line2:
           FO.write("%s\n" % (line1,))


FO.close()
file1.close()
file2.close()
'''


'''f = open('origin.txt') # Open file on read mode
lines = f.read().splitlines() # List with stripped line-breaks
print(lines)
f.close() # Close file'''

'''file1 = open("origin.txt", 'r')
file2 = open("after.txt", 'r')
while True:
    next_line = file1.readline()

    if not next_line:
        break;
    print(next_line.strip())

file1.close()
file2.close()'''

# Importing diffli test
