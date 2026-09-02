target = int(input("What is the target? "))

if not (-10**9 <= target <= 10**9):
    print("Write correct target")
else:
    length = int(input("What's the length of array? "))

    nums = []
    i = 0

    while i < length:
        nums.append(int(input("Write the entry to array: ")))
        i += 1

    nums.sort()

    found = False

    for i in range(length):
        for j in range(i):
            if nums[i] + nums[j] == target:
                print("The required numbers are", nums[i], "and", nums[j])
                found = True

    if not found:
        print("No pair found.")