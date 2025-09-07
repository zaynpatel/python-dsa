import re

# Learning 1: Inner loop to define parsing logic, break once first match, keep outer loop to iterate through entire file.
# Learning 6: Python evaluates and before or so this expression. 

#TODO: Figure out how adding the class changes the input of line -> this will be connected to the read_mardown function
class HTMLParser:
    def __init__(self):
        self.list_of_dictionaries = []
        self.markdown_handlers = {
        # Online suggested using the lambda functions because we can pass the line and level now, evaluate simpler than before
        '# ' : lambda line: self.handle_heading(line, 1), 
        '## ' : lambda line: self.handle_heading(line, 2), 
        '### ' : lambda line : self.handle_heading(line, 3), 
        '#### ' : lambda line: self.handle_heading(line, 4), 
        '##### ' : lambda line: self.handle_heading(line, 5),
        '###### ' : lambda line: self.handle_heading(line, 6),
        '``' : self.handle_inline_block,  
        '```' : self.handle_code_block, # this is state-based (hard)
        '- ' : self.handle_ullist_block, # this is state-based (hard and review this because there are multiple symbols we can use to define an ul list, also look at ol list syntax)
        '![' : self.handle_image, 
        '> ' : self.handle_blockquote,
        '**' : self.handle_bold, # this is state-based
        '*' : self.handle_italic,
        '[' : self.handle_links
    }

    # Refactored the read_markdown and created a new process_line function
    def read_markdown(self, file : str):
        with open(file, 'r') as md:
            for line in md:
                self.process_line(line.strip())
    
    def process_line(self, line):
        for pattern, handler in self.markdown_handlers.items():
            if line.startswith(pattern):
                handler(line)
                break
    
    # Rewrite handle_heading function to accomodate all heading types in one function
    def handle_heading(self, line, level):
        if level <= 6:
            stripped_line = line.lstrip('#' * level).strip() # depending on the level passed into the function/what's recognized
            self.list_of_dictionaries.append({'type' : f'heading{level}', 'content' : stripped_line}) # have to get better at thinking about this
        else: raise ValueError ("More than acceptable pound signs")
    
    def handle_blockquote(self, line):
        self.list_of_dictionaries.append({
            'type' : 'blockquote',
            'content' : line.lstrip('> ').strip()
        })

    def handle_links(self, line):
        # We need to introduce control flow because there's a limited amount we can do with dictionaries and custom strings
        # So, anything that matches '[' will be "flagged" as a link. We want to check if this is actually a link or not so we evaluate using if.
        # if http or https is in the line, evaluate it like a link 
        # recall that commands for re.search(expression, applied to what)
        if re.search(r'(http[s]?:\/\/[^\)]+)\)', line): # r here means raw strings
            pattern = re.findall(r'\[([^\]]+)\]\((http[s]?:\/\/[^\)]+)\)', line) # I originally used .search() but changed to .findall() in the case there are multiple links in a given line.  
            for link_text, url in pattern: # iterate as a method to unpack tuple created in pattern
                self.list_of_dictionaries.append({
                    'type' : 'link', 
                    'content' : {'link text' : link_text, 'url' : url}
                })

    def handle_image(self, line):
        # I want to search the string to see if I can find any image file types
        # Learning 5: Turns out we cannot add lists to regex, have to use the or operator instead.
        if re.search(r'(https?:\/\/[^\s]+?(?:\.png|\.jpg|\.jpeg|\.gif|\.bmp|\.tiff|\.svg))\)', line):
            match = re.findall(r'!\[([^\]]*)\]\((https?:\/\/[^\s]+?(?:\.png|\.jpg|\.jpeg|\.gif|\.bmp|\.tiff|\.svg))\)', line) # designed to work with the alt text and image syntax, this is why we're looping with two variables
            for alt_text, image_url in match:
                self.list_of_dictionaries.append({
                    'type' : 'image',
                    'content' : {'alt text' : alt_text, 'image url' : image_url}
                })        

    # Needed help/review for this function. State managing was tricky. 
    def handle_italic(self, line):
        in_italic = False # set the state to False because we haven't encountered asterik yet
        holding_string = "" # this is the string that gets appended to dictionary
        for text in line:
            if text in ["*", "_"]: # just evaluating begin and end and I think this eliminats the == * which looks at one symbol
                in_italic = not in_italic # we toggle because we don't know if this is the beginning symbol or ending symbol. but we do know what state we've set it too
                if not in_italic and holding_string:
                    self.list_of_dictionaries.append({
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
            self.list_of_dictionaries.append({
                'type' : 'italic',
                'content' : holding_string
            })
        
        holding_string = "" # confirm that this is needed, I thought the reset happens in above code

    # Needed help/review of how to use regex backticking and search for this function implementation
    def handle_inline_block(self, line):
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
                        self.list_of_dictionaries.append({
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