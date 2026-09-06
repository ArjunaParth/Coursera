x=input('whats x?')
y=input('whats y?') 
input1=input('what do you want to do?')
if input1=="add" or input1=="Add" or input1=="ADD":
  print('x+y=',int(x)+int(y))
if input1=="subtract" or input1=="Subtract" or input1=="SUBTRACT":
  print('x-y=',int(x)-int(y))
if input1=="multiply" or input1=="Multiply" or input1=="MULTIPLY":
  print('x*y=',int(x)*int(y))
if input1=="divide" or input1=="Divide" or input1=="DIVIDE":
  print('x/y=',int(x)/int(y))
if input1=="floor divide" or input1=="Floor Divide" or input1=="FLOOR DIVIDE":
  print('x//y=',int(x)//int(y))
if input1=="modulo" or input1=="Modulo" or input1=="MODULO":
  print('x%y=',int(x)%int(y))
if input1=="power" or input1=="Power" or input1=="POWER":
    for i in range(1,11):
      print ('x*',i,'=',int(x)*i)