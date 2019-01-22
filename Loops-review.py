def main():
    #Exercise1()
    #Exercise2()
        Exercise3()
#Exercise 1:
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Hint: Use 'continue' statement.
#Expected Output : 0 1 2 4 5

def Exercise1():
    for i in range(0,7):
        if (i ==3 or i==6):
            continue
        print(i, end="")
    print("")

#Exercise 2:
#Write a Python program to count the number of even and odd numbers from a series of numbers.
#Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4
def Exercise2():
    nums = [1,2,3,4,5,6,7,8,9,10]
    count_odd=0
    count_even=0
    for x in nums:
        if not x % 2:
            count_even+=1
        else:
            count_odd+=1
    print("Number of even numbers is:", count_even)
    print("Number of odd numbers is:", count_odd)

#Exercise 3:
#Write a Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output after User enters a blank line to end.
#Do not use an array to hold the lines of text
#Hints: You can use "\n" if you want to add a line break between sentences

def Exercise3():
    while (True):

        strings=input("Type a sentence. Enter a blank line when finished")


        if (strings == "__"):
            break
        ','.join(strings)






























if __name__ == '__main__':
     main()