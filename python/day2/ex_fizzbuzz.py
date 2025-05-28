# Write a program that:
# 1. Prints numbers from 1 to 30
# 2. For multiples of 3, print "Fizz" instead of the number
# 3. For multiples of 5, print "Buzz" instead of the number
# 4. For multiples of both 3 and 5, print "FizzBuzz"
# 5. If a number contains digit 7, print "Lucky" instead
# 6. Use continue to skip any number that is even and greater than 20
for number in range(1, 31):
    fizz_flag = False
    buzz_flag = False
    fizzbuzz_flag = False

    if number % 2 == 0 and number >= 20:
        continue

    # shi = number // 10
    # ge = number % 10
    # if shi == 7 or ge == 7:
    #     print("Lucky")
    #     continue
    # using text to deal with
    if "7" in str(number):
        print("lucky")
        continue

    if number % 3 == 0:
        fizz_flag = True
    if number % 5 == 0:
        buzz_flag = True
    if fizz_flag and buzz_flag:
        fizzbuzz_flag = True

    if fizzbuzz_flag:
        print("FizzBuzz")
        continue
    elif fizz_flag:
        print("Fizz")
        continue
    elif buzz_flag:
        print("Buzz")
        continue

    print(f"number: {number}")

# analogy:
# 1.pay attention to the priority of the continue
# 2.The and, or, not
# 3.keyword in
# 4.if-elif-else, single output, means one condition true, it will output
#   with multiple condition check, using multiple ifs
