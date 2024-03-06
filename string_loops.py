''' Task: Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated 
strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.
Input Format: The first line contains an integer, T (the number of test
cases).

Sample Input
2
Hacker
Rank
Sample Output
Hce akr
Rn ak
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Read the number of test cases
t = int(sys.stdin.readline())

# Loop through each test case
for _ in range(t):
    # Read the input string
    s = sys.stdin.readline().strip()
    
    # Get the even-indexed characters
    even_chars = s[::2]
    
    # Get the odd-indexed characters
    odd_chars = s[1::2]
    
    # Print the even and odd indexed characters separated by a space
    print(even_chars, odd_chars)


               

