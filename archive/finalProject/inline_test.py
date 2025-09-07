# Learning 1: When we modify `index` inside a for loop, doesn't affect the next value of index in the sequence.
# Implication is, I'm going to use more variables like index to control the iteration process.
stringExample = "E `inline` inside."
in_inline = False
holding_string = ""
collected_inline = "" # used to persist the data that was not done in my previous code implementation. 
index = 0

while index < len(stringExample): 
    char = stringExample[index]
    if char == '`':
        backtick_count = 1 
        # while we are still in bounds and the character is a backtick (`), add one to count - our goal is to see consecutive
        while index + backtick_count < len(stringExample) and stringExample[index + backtick_count] == '`':
            backtick_count += 1
    
        if not in_inline:

            in_inline = True
            opening_backtick_count = backtick_count
        
        else:
            if backtick_count == opening_backtick_count: # if we find the same number of backticks at the end of the sequence as we had at the start, we're done with inline code block. 
                in_inline = False # change the state
                collected_inline += holding_string
                holding_string = ""

            else:
                holding_string += '`' * backtick_count # if they aren't equal to same, treat them as part of the code and add them to the string

        index += backtick_count - 1

    elif in_inline:
        holding_string += char
    
    index += 1