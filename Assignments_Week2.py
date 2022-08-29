s_code1 = "NATO"
s_code2 = "EU"

answer = input("What is the secret code? ")
if answer == s_code1:
    print("Correct")
elif answer == s_code2:
    print("Also correct")
    s_number = int(input("What is the secret number? "))
    if s_number % 4 == 0:
        print("You are lucky!")
    else:
        print("You are not lucky.")
elif answer == "TOPSECRET":
    print("You got it!!")
else:
    print("Incorrect")




#phase 1

#zander = float(input("Enter the length of a zander you just caught: "))

#if zander >= 42:
#    print("Good job, you can eat today.")
#else:
#   print("Unfortunately the zander is ?? cm under size limit, you'll have to release it. ")