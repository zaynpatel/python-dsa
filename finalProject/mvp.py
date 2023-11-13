import re

# Learning 1: Inner loop to define parsing logic, break once first match, keep outer loop to iterate through entire file.
# Learning 6: Python evaluates and before or so this expression. 


# Context manager to read lines
def read_markdown(file):
    with open(file, 'r') as md:
        markdownFile = md.readlines()
        for text in markdownFile:
            for pattern, function in markdown_handlers.items():
                if text.startswith(pattern):
                    function(text)

# need to think more about what to add here and how this relates to parsing and markdown_handlers dictionary (what fcn calling across file looks like too.) 
list_of_dictionaries = [] # this becomes the immediate representation which I'll pass into my HTML function

# Input to this is one line - where is line in file? Need to write this so it's available and can be parsed. 
def handle_heading1(line):
    list_of_dictionaries.append({
        'type' : 'heading1',
        'content' : line.lstrip('# ').strip()
    })

def handle_heading2(line):
    list_of_dictionaries.append({
        'type' : 'heading2',
        'content' : line.lstrip('## ').strip() # why do we need two .strip() - one for heading/one for whitespace after text?
    })

def handle_heading3(line):
    list_of_dictionaries.append({
        'type' : 'heading3',
        'content' : line.lstrip('### ').strip() 
    })

def handle_heading4(line):
    list_of_dictionaries.append({
        'type' : 'heading4',
        'content' : line.lstrip('#### ').strip() 
    })

def handle_heading5(line):
    list_of_dictionaries.append({
        'type' : 'heading5',
        'content' : line.lstrip('##### ').strip() 
    })

def handle_heading6(line):
    list_of_dictionaries.append({
        'type' : 'heading6',
        'content' : line.lstrip('###### ').strip() 
    })

def handle_blockquote(line):
    list_of_dictionaries.append({
        'type' : 'blockquote',
        'content' : line.lstrip('> ').strip()
    })

def handle_links(line):
    # We need to introduce control flow because there's a limited amount we can do with dictionaries and custom strings
    # So, anything that matches '[' will be "flagged" as a link. We want to check if this is actually a link or not so we evaluate using if.
    # if http or https is in the line, evaluate it like a link 
    # recall that commands for re.search(expression, applied to what)
    if re.search(r'(http[s]?:\/\/[^\)]+)\)', line): # r here means raw strings
        pattern = re.findall(r'\[([^\]]+)\]\((http[s]?:\/\/[^\)]+)\)', line) # I originally used .search() but changed to .findall() in the case there are multiple links in a given line.  
        for link_text, url in pattern: # iterate as a method to unpack tuple created in pattern
            list_of_dictionaries.append({
                'type' : 'link', 
                'content' : {'link text' : link_text, 'url' : url}
            })

def handle_image(line):
    # I want to search the string to see if I can find any image file types
    # Learning 5: Turns out we cannot add lists to regex, have to use the or operator instead.
    if re.search(r'(https?:\/\/[^\s]+?(?:\.png|\.jpg|\.jpeg|\.gif|\.bmp|\.tiff|\.svg))\)', line):
        match = re.findall(r'!\[([^\]]*)\]\((https?:\/\/[^\s]+?(?:\.png|\.jpg|\.jpeg|\.gif|\.bmp|\.tiff|\.svg))\)', line)
        for alt_text, image_url in match:
            list_of_dictionaries.append({
                'type' : 'image',
                'content' : {'alt text' : alt_text, 'image url' : image_url}
            })        

# Needed help/review for this function. State managing was tricky. 
def handle_italic(line):
    in_italic = False # set the state to False because we haven't encountered asterik yet
    holding_string = "" # this is the string that gets appended to dictionary
    for text in line:
        if text in ["*", "_"]: # just evaluating begin and end and I think this eliminats the == * which looks at one symbol
            in_italic = not in_italic # we toggle because we don't know if this is the beginning symbol or ending symbol. but we do know what state we've set it too
            if not in_italic and holding_string:
                list_of_dictionaries.append({
                    'type' : 'italic',
                    'content' : holding_string
                })
                holding_string = ""
            continue # add this to ensure that the markers aren't appended. without this, the 
        # if we are in block, just keep adding text!
        if in_italic:
            holding_string += text

    # keep this here for text that's still italic when we reach the end of the line
    if in_italic and holding_string:
        list_of_dictionaries.append({
            'type' : 'italic',
            'content' : holding_string
        })
    
    holding_string = "" # confirm that this is needed, I thought the reset happens in above code

# Needed help/review of how to use regex backticking and search for this function implementation
def handle_inline_block(line):
    # first step is to define the state
    in_inline = False 
    holding_string = "" # figure out why the previous one wasn't persisting
    collected_inline = ""
    index = 0

    # just as before we need to figure out if it's a real or unreal inline code block but isn't this why we have the count between opening and closing?

    while index < len(line):
        char = line[index]

        if char == '`':
            backtick_count = 1
            while index + backtick_count < len(line) and line[index + backtick_count] == '`':
                backtick_count += 1
        
            if not in_inline:
                in_inline = True
                opening_backtick_count = backtick_count
        
            else:
                if backtick_count == opening_backtick_count:
                    in_inline = False
                    collected_inline += holding_string
                    list_of_dictionaries.append({
                        'type' : 'inline code',
                        'content' : collected_inline
                    })
                
                    holding_string = ""
                else:
                    holding_string += '`' * backtick_count
        
            index += backtick_count - 1 # confirm 

        elif in_inline:
            holding_string += char
    
    index += 1


# Learning 3: Because a dictionary needs to be hashable and immutable, it can only contain static values (strings, numbers, etc)
# So, re isn't allowed because it's dynamic (pattern matching against multiple strings)

# How do we handle just text, lol?
markdown_handlers = {
    '# ' : handle_heading1, 
    '## ' : handle_heading2, 
    '### ' : handle_heading3, 
    '#### ' : handle_heading4, 
    '##### ' : handle_heading5,
    '###### ' : handle_heading6,
    '``' : handle_inline_block,  
    '```' : handle_code_block, # this is state-based (hard)
    '- ' : handle_ullist_block, # this is state-based (hard and review this because there are multiple symbols we can use to define an ul list, also look at ol list syntax)
    '![' : handle_image, 
    '> ' : handle_blockquote,
    '**' : handle_bold, # this is state-based
    '*' : handle_italic,
    '[' : handle_links
}

# Need a central loop or parsing function to work with handle_image v. handle_links
# Iterator is going to be down here and I need to think about what to handle plain text with.