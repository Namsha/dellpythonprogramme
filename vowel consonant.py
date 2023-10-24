# Python code to find character is vowels or consonants

# inputs from the user
c = input('Enter a Characters: ')

# find vowel or constant and display result
if(c=='A' or c=='a' or c=='E' or c =='e'
            or c=='I' or c=='i' or c=='O'
              or c=='o' or c=='U' or c=='u'):
    print(c, "is a Vowels.")
else:
    print(c, "is a Consonants.")