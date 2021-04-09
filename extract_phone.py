

# importing the module
import re

# extracting the mobile number
# ([A-Z])\w+

with open('input.txt') as f:
    lines = f.readlines()
    for mobile in lines:
        m = re.findall('([0-9]{5}-[0-9]{6})', mobile)
        n = re.findall('([0-9]{5} [0-9]{6})', mobile)
        o = re.findall('([0-9]{5}[0-9]{6})', mobile)

        for i in m:
            x = i.replace('-', '')
            with open('output.txt', 'a') as f:
                f.writelines(x)
                f.writelines("\n")
            print(x)

        for j in n:
            y = j.replace(' ', '')
            with open('output.txt', 'a') as f:
                f.writelines(y)
                f.writelines("\n")
            print(y)

        for k in o:
            with open('output.txt', 'a') as f:
                f.writelines(k)
                f.writelines("\n")
            print(k)

    f.close()
    with open('output.txt') as f:
        lines = f.readlines()
        count_lines = len(lines)
        print('total number:', count_lines)
