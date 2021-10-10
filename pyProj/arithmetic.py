rightAns = int(4*100-54)
print("Can YOU solve this:\n4 * 100 -54")
userAns = int(input("Write your answer there: "))
if userAns == rightAns:
    print("Your answer is absolutely right! Right answer is  %d" % (rightAns))
else:
    print("You was wrong :(\nThe right answer is  %d\nYour answer is  %d" % (rightAns, userAns))