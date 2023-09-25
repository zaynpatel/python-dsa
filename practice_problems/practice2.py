# Stacks practice problem - browser history

class Browser:
    def __init__(self):
        self.track_forward = []
        self.track_backward = []
        self.current_page = None # added this method because I observed we're going to be updating it frequently and it's better to have this as an object I can use for updates later on
    
    # I got asked a good question about the requirements
    # Everytime we open a new webpage shouldn't it be added to the "Back" stack? The answer is yes so my earlier implementation where I was checking `if self.forward` was incorrect. 
    def new_webpage(self, webpage):
        if self.current_page is not None:
            self.track_backward.append(self.current_page)
            self.track_forward.clear()
        self.current_page = webpage
            

    def go_back(self):
        # check the items to make sure I can "go back"
        if len(self.track_backward) > 1:
            # if I can go back, push the current page to forward stack
            pop = self.track_backward.pop()
            self.track_forward.append(self.current_page)
            # current page is equal to the last item in backward
            self.current_page = pop
        else:
            self.check_navigation()
            
        
    def go_forward(self):
        # only need to check if there's at least one page to navigate too
        if self.track_forward:
            self.track_backward.append(self.current_page) # first append current page to track backward
            pop = self.track_forward.pop() 
            self.current_page = pop
        else:
            self.check_navigation() # because everything is in a class there's no need to worry about scope or getter/setter methods, just use self.[function name]
    
    def check_navigation(self):
        # use len() to see whether a list is empty or not and use two separate if statements since if/elif/else assumes above are true and will evaluate as such
        if len(self.track_forward) == 0:
            print(f"There is no movement in forward direction")
        if len(self.track_backward) == 0:
            print(f"There is no movement in backward direction.")
        