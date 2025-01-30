import zipfile
import os
import re


# Good work on unzipping the file!
# You should now see 5 folders, each with a lot of random .txt files.
# Within one of these text files is a telephone number formated ###-###-####
# Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
# Good luck!

zip_obj = zipfile.ZipFile('res\\unzip_me_for_instructions.zip', 'r')
zip_obj.extractall()

all_matches = []

for folder, sub_folders, files in os.walk("extracted_content"):
    for f in files:
        file_obj = open(folder + '\\' + f, 'r')
        all_matches.extend(re.findall(r"\d{3}-\d{3}-\d{4}", file_obj.read()))
        file_obj.close()

print(all_matches)