# question number 1
for a in range(0,99):
    print(f'0{a}' if 0 <= a <= 9 else a,end=', ')
print(f'99')



# question number 2
inp = str(input("please enter the pattern to be printed: "))
vowels = 'aeiouAEIOU'
if inp not in vowels:
    for a in range(0,7):
        for b in range(a):
            print(inp,end='')
        print(inp)
elif len(inp) > 1:
    print("character canot be more than 1 letter")
else:
    print("you can't add vowels")



# question number 3
org = str(input("Enter a word ->"))
if org == org[::-1]:
    print(f'the word {org} is palindrome')
else:
    print(f'the word {org} is not palindrome')



# question number 4
total_sum = 0
count_three = 0
count_five = 0

for number in range(1, 51):
    if number % 2 == 0:
        total_sum += number

        if number % 3 == 0:
            print("Three")
            count_three += 1
        elif number % 5 == 0:
            print("Five")
            count_five += 1
        else:
            print(number)

print("\nTotal Sum of Even Numbers: ", total_sum)
print("Count of numbers replaced with 'Three': ", count_three)
print("Count of numbers replaced with 'Five': ", count_five)
