# AM Automate Tools

## Extract Email From Text File

Extract email list from any text file. There are few options including sorting and output as any file format.

**File name:**

[extract_email_from_text.py](extract_email_from_text.py)

*Run the command with any file, for example file name is list_of_email.txt, and output file will be extract_email.txt*

`python extract_email_from_text.py list_of_email.txt > extract_email.text`

*To sort and unique email Run the command with any file, for example file name is list_of_email.txt, and output file will be extract_email.txt*

`python extract_email_from_text.py list_of_email.txt | sort | uniq > extract_email.text`