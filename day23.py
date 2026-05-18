'''1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********   '''
'''rows = int(input("Enter total number of lines="))
for i in range(rows):
    # Left spaces
    for j in range(rows - i - 1):
        print(" ", end="")
    # First row
    if i == 0:
        print("*")
    # Last row
    elif i == rows - 1:
        for j in range(2 * rows - 1):
            print("*", end="")
        print()
    # Middle rows
    else:
        print("*", end="")
        # Inner spaces
        for j in range(2 * i - 1):
            print(" ", end="")

        print("*")'''


'''2) Hollow Rectangle
    *********
    *          *
    *          *
    *          *
    *********  '''
'''rows = int(input("Enter total rows number="))
cols = int(input("Enter total columns number="))

for i in range(rows):

    for j in range(cols):

        # Border condition
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")

        else:
            print(" ", end="")

    print()'''

'''3) X Star Pattern
    *   *
     * *
      *
     * *
    *   * '''
'''rows = int(input("Enter total number of rows="))

for i in range(rows):

    for j in range(rows):

        if j == i or j == rows - i - 1:
            print("*", end="")

        else:
            print(" ", end="")

    print()'''

'''4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
'''
'''rows =int(input("Total number of rows=")) 

# Upper part
for i in range(rows):

    # Left spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Hollow pyramid
    if i == 0:
        print("*")

    else:
        print("*", end="")

        for j in range(2 * i - 1):
            print(" ", end="")

        print("*")

# Lower part
for i in range(rows - 2, -1, -1):

    # Left spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Hollow pyramid
    if i == 0:
        print("*")

    else:
        print("*", end="")

        for j in range(2 * i - 1):
            print(" ", end="")

        print("*")'''

'''    5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1 '''

'''rows = int(input("Enter total number of rows="))

for i in range(rows):

    # Left numbers
    for j in range(1, rows - i + 1):
        print(j, end="")

    # Stars
    for j in range(2 * i):
        print("*", end="")

    # Right numbers
    for j in range(rows - i, 0, -1):
        print(j, end="")

    print()'''

'''6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9 '''
'''rows = int(input("Enter total number of rows="))

for i in range(1, rows + 1):

    # Dashes
    for j in range(rows - i):
        print("-", end=" ")

    # Numbers
    for j in range(i):
        print(i + j, end=" ")

    print()'''

'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
'''
'''rows = int(input("Enter total number of rows="))
for i in range(rows):

    # Numbers
    for j in range(i):
        print(2 * i - j, end=" ")

    # Dashes
    for j in range(rows - i):
        print("-", end=" ")

    print()'''

'''8) Border Number Pattern
    1 2 3 4 5
    2          5
    3          5
    4          5
    5 5 5 5 5 '''

'''rows = int(input("Enter total number of rows="))
for i in range(1, rows + 1):

    for j in range(1, rows + 1):

        # First row
        if i == 1:
            print(j, end=" ")

        # Last row
        elif i == rows:
            print(rows, end=" ")

        # First column
        elif j == 1:
            print(i, end=" ")

        # Last column
        elif j == rows:
            print(rows, end=" ")

        # Inner space
        else:
            print(" ", end=" ")

    print()'''

'''9) Hollow Diamond Square
    ***********
    ****    ****
    ***      ***
    **        **
    *          *
    *          *
    **        **
    ***      ***
    ****    ****
    ***********
'''
'''rows = int(input("Enter total number of rows="))

# Upper part
for i in range(rows):

    # Left stars
    for j in range(rows - i):
        print("*", end="")

    # Middle spaces
    for j in range(2 * i + 1):
        print(" ", end="")

    # Right stars
    for j in range(rows - i):
        print("*", end="")

    print()

# Lower part
for i in range(rows):

    # Left stars
    for j in range(i + 2):
        print("*", end="")

    # Middle spaces
    for j in range(2 * (rows - i) - 3):
        print(" ", end="")

    # Right stars
    for j in range(i + 2):
        print("*", end="")

    print()'''

'''10) Slanted Star Block
    ****
     ****
      ****
       ****
'''
'''rows = int(input("Enter total number of rows="))
cols = int(input("Enter total number of columns="))

for i in range(rows):

    # Left spaces
    for j in range(i):
        print(" ", end="")

    # Stars
    for j in range(cols):
        print("*", end="")

    print()'''

'''11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1
'''
'''rows =  int(input("Enter total number of rows="))

# Upper part
for i in range(1, rows + 1):

    # Left numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Spaces
    for j in range(2 * (rows - i)):
        print(" ", end="")

    # Right numbers
    for j in range(i, 0, -1):
        print(j, end="")

    print()

# Lower part
for i in range(rows - 1, 0, -1):

    # Left numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Spaces
    for j in range(2 * (rows - i)):
        print(" ", end="")

    # Right numbers
    for j in range(i, 0, -1):
        print(j, end="")

    print()'''

'''12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
'''
'''rows = int(input("Enter total number of rows="))

# Upper part
for i in range(1, rows + 1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    # First row
    if i == 1:
        print(i)

    else:
        print(i, end="")

        # Inner spaces
        for j in range(2 * i - 3):
            print(" ", end="")

        print(i)

# Lower part
for i in range(rows - 1, 0, -1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    # First row
    if i == 1:
        print(i)

    else:
        print(i, end="")

        # Inner spaces
        for j in range(2 * i - 3):
            print(" ", end="")

        print(i)'''

'''13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5 '''
'''rows = int(input("Enter total number of rows="))

for i in range(rows):

    for j in range(rows):

        if j == i:
            print(i + 1, end="")

        elif j == rows - i - 1:
            print(rows - i, end="")

        else:
            print(" ", end="")

    print()'''

'''14) Spiral Number Square
     1   2   3   4
    12  13  14   5
    11  16  15   6
    10   9   8   7 
'''
'''n = int(input("Enter total number of rows="))
a = [[0]*n for i in range(n)]
num = 1
top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    # Left to Right
    for i in range(left, right + 1):
        a[top][i] = num
        num += 1
    top += 1

    # Top to Bottom
    for i in range(top, bottom + 1):
        a[i][right] = num
        num += 1
    right -= 1

    # Right to Left
    for i in range(right, left - 1, -1):
        a[bottom][i] = num
        num += 1
    bottom -= 1

    # Bottom to Top
    for i in range(bottom, top - 1, -1):
        a[i][left] = num
        num += 1
    left += 1

for row in a:
    for val in row:
        print(val, end=" ")
    print()'''


'''15) Zig-Zag Star
    *   *   *
      *   *
    *   *   * '''
'''for i in range(3):

    if i % 2 == 0:
        print("*   *   *")

    else:
        print("  *   *")'''

'''16) Palindrome Pyramid
            1
           121
          12321
         1234321
        123454321
'''
'''rows = int(input("Enter total number of rows="))

for i in range(1, rows + 1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()'''

'''17) Hollow Hourglass
    * * * * *
      *     *
        * *
          *
        * *
      *     *
    * * * * *
'''
'''rows =int(input("Enter total number of rows="))

# Upper part
for i in range(rows):

    # Left spaces
    for j in range(2 * i):
        print(" ", end="")

    # Stars
    for j in range(rows - i):

        if j == 0 or j == rows - i - 1 or i == 0:
            print("* ", end="")

        else:
            print("  ", end="")

    print()

# Lower part
for i in range(rows - 2, -1, -1):

    # Left spaces
    for j in range(2 * i):
        print(" ", end="")

    # Stars
    for j in range(rows - i):

        if j == 0 or j == rows - i - 1 or i == 0:
            print("* ", end="")

        else:
            print("  ", end="")

    print()'''

'''18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1'''

'''n=int(input("Enter total number of lines="))
digit=1
for i in range(1,n+1) :
	for j in range(1,i+1) :
		print(digit,end=" ")
		digit=1-digit
	print()'''

'''19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5
'''
'''rows = int(input("Enter total number of lines="))

for i in range(rows):

    for j in range(rows):

        if j == i or j == rows - i - 1:
            print(rows - i, end="")

        else:
            print(" ", end="")

    print()'''

'''20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1
'''
'''rows =  int(input("Enter total number of rows="))
num =  1

# Upper part
for i in range(1, rows + 1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    temp = num

    # Numbers
    for j in range(i):
        print(temp, end=" ")
        temp += 1

    num += i
    print()

# Lower part
for i in range(rows - 1, 0, -1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    start = i * (i - 1) // 2 + 1

    # Numbers
    for j in range(i):
        print(start + j, end=" ")

    print()'''

'''21) Hollow Pyramid (Practice)
            *
           * *
          *   *
         *     *
        *********
'''
'''rows = int(input("Enter total number of rows="))

for i in range(rows):

    # Left spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # First row
    if i == 0:
        print("*")

    # Last row
    elif i == rows - 1:
        for j in range(2 * rows - 1):
            print("*", end="")
        print()

    # Middle rows
    else:
        print("*", end="")

        # Inner spaces
        for j in range(2 * i - 1):
            print(" ", end="")

        print("*")'''

'''22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
'''
'''rows = int(input("Enter total number of rows="))

for i in range(rows):

    # Left spaces
    for j in range(i):
        print(" ", end="")

    # First row
    if i == 0:
        for j in range(2 * rows - 1):
            print("*", end="")
        print()

    # Last row
    elif i == rows - 1:
        print("*")

    # Middle rows
    else:
        print("*", end="")

        # Inner spaces
        for j in range(2 * (rows - i) - 3):
            print(" ", end="")

        print("*")'''

'''23) Plus Star Pattern
          *
          *
    *********
          *
          *
'''
'''row=int(input("Enter number of rows="))

for i in range(row) :
	for j in range(row) :
		if i==row//2 or j==row//2 :
			print("*",end=" ")
		else :
			print(" ",end=" ")
	print()'''

'''24) Hollow X Pattern
    *   *
     * *
      *
     * *
    *   *
'''
'''rows = int(input("Enter total number of rows="))
for i in range(rows):

    for j in range(rows):

        # Diagonals
        if j == i or j == rows - i - 1:
            print("*", end="")

        else:
            print(" ", end="")

    print()'''

'''25) Number Sandglass
    123454321
     1234321
      12321
       121
        1
       121
      12321
     1234321
    123454321'''
'''rows = int(input("Enter total number of rows="))
# Upper part
for i in range(rows, 0, -1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

# Lower part
for i in range(2, rows + 1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    # Increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()'''

'''26) Right Hollow Number Triangle
    1
    12
    1 3
    1   4
    12345
'''
'''rows = int(input("Enter total number of rows="))
for i in range(1, rows + 1):

    # First and last row
    if i == 1 or i == rows:

        for j in range(1, i + 1):
            print(j, end="")

    else:
        print("1", end="")

        # Inner spaces
        for j in range(i - 2):
            print(" ", end="")

        print(i, end="")

    print()'''
'''27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10
'''
'''rows = int(input("Enter number of rows="))
num = 1

for i in range(1, rows + 1):

    # Left spaces
    for j in range(rows - i):
        print(" ", end="")

    # Numbers
    for j in range(i):
        print(num, end=" ")
        num += 1

    print()'''
'''28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****
'''
'''rows = int(input("Enter total number of rows="))

for i in range(rows):

    for j in range(rows):

        # Border condition
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")

        else:
            print(" ", end="")

    print()'''

'''29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4'''
'''rows = int(input("Enter number of rows="))

for i in range(rows):

    for j in range(rows):

        if i == j:
            print(i + 1, end=" ")

        else:
            print("-", end=" ")

    print()'''
	

'''30) Extended Slanted Star Block
    ****
     ****
      ****
       ****
        ****
'''
rows = int(input("Enter number of rows="))
cols = int(input("Enter number of columns="))

for i in range(rows):

    # Left spaces
    for j in range(i):
        print(" ", end="")

    # Stars
    for j in range(cols):
        print("*", end="")

    print()