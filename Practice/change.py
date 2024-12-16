a="2a2b2c"
output=" "
var=""
for char in a:
    if char.isalpha():
        var=char
        output=output+(var*num)
    else:
        num=int(char)
        
print(output)            
            