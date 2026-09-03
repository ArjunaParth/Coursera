import re
filename = "/Users/arjunaparth/Desktop/regex_sum_2437009.txt"
with open(filename, "r") as file:
    content = file.read()
numbers = re.findall("[0-9]+", content)
total_sum = sum(int(num) for num in numbers)
print(f"Total numbers found: {len(numbers)}")
print(f"Sum: {total_sum}")
