import re

def calculate(s):
    print(s)
    fuhao = r'[+ \-,*,/]'
    raw_text = ''
#    raw_text = [a if a != ' ' for a in s]
#    raw_text = ''.join(raw_text)
    for a in s:
        if a != ' ':
            raw_text += a
    print(raw_text)
    num = re.split(fuhao, raw_text)
    print(num)
    num = [int(i) for i in num]
    op = re.findall(fuhao, raw_text)
    print(op)

    i = 0
    for index in range(len(op)):
        o = op[i]
        if o =='*' or o == '/':
            if o == '*':
                tmp = num[i] * num[i+1]
            if o == '/':
                tmp = num[i] // num[i+1]
            del num[i]
            del num[i]
            del op[i]
            num.insert(i, tmp)
            print(num)
            print(op)
        else:
            i += 1
        if i==len(op):break

    res = num[0]
    for i,o in enumerate(op):
        if o == '+':
            res += num[i+1]
        else:
            res -= num[i+1]
        print(res)
    print(res)


            

if __name__ == '__main__':	
    string = ' 3 + 4 * 2 + 3'
    string = '2*3*4'
    calculate(string)
