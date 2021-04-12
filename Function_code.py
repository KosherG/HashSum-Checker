import time, os, tkinter
from tkinter import filedialog

root =tkinter.Tk()
root.withdraw()

input('#######Welcome to Hash Checker####### \nPress Enter to begin')
print('Choose file:\n.......')
time.sleep(2)

filePath = filedialog.askopenfilename()
user_hash_id = input('Original Hash:  ')

hashType = input('\nHash Type:  ')
print('\n')

cmd = 'cmd /c certutil -hashfile %s > hash_key.txt'%(filePath) 

os.system(cmd)


hash_file = open('hash_key.txt')
hash_lines = hash_file.readlines()
prog_hash_id = hash_lines[1]
prog_hash_id = prog_hash_id[:-1]
answer = prog_hash_id == user_hash_id
if answer is True:
    print('Hashes are the same: ', prog_hash_id == user_hash_id)
if answer is False:
    print('Hashes are not the same: \n')
print('Length of Program Hash is:  ',len(prog_hash_id))
print('Length of User Hash is:  ',len(user_hash_id))

input('\nPress Enter To exit')
