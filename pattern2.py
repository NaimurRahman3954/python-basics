'''
pattern-2
   *
  **
 ***
****
'''
print("Enter the number of rows")
rowStr = input()
row = int(rowStr)

for i in range(1, row+1):
    print(" "*(row-i)+"*"*i)
    i += 1
