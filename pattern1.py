'''
pattern-1
   *
  ***
 *****
*******
'''

print("Enter the number of rows")
rowStr = input()
row = int(rowStr)

for i in range(1, row+1):
    print(" "*(row-i)+"*"*(2*i-1))
    i += 1
