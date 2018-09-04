import  re
str = "0211234567"

print(re.match("\d{3,4}-?\d{7,8}", str).group())