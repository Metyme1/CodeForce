def can_say_hello(s):
    target = "hello"
    # Start an index for target
    target_index = 0
    # Iterate over each character in the string s
    for char in s:

        if char == target[target_index]:

            target_index += 1
            if target_index == len(target):
                return "YES"
    return "NO"


input_word = input()
print(can_say_hello(input_word))  # Output should be YES
