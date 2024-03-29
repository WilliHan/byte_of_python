import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows :
# source = ['"C:\\My Documents"', 'C:\\Code']
source = [ '/mnt/d/WORK/Git-Hub/py10' ]
# Example on Mac OS X and Linux:
# source = ['/User/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir= 'E:\\Backup'
# target_dir= 'E:\\Backup'
target_dir='/mnt/e/temp/Git_Backup'
# Example on Mac OS X and Linux:
# target_dir= '/Users/swa/backup'
# Remember to change this to which folder you will be usingo

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + \
        time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target,  ' '.join(source))

# Run the backup
print("Zip command is:", zip_command)
print("Running:")
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

zip_file_name=str(source)+".zip"
ls_command = "ls -l {0}".format(target,  ' '.join(zip_file_name))
# print("LS_COMMAND : ", ls_command)

if os.system(ls_command) == 0:
    print('Successful check to', target)
else:
    print('Checked FAILED', ls_command)
