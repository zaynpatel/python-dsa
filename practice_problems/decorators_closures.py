# Problem 1: Define a closure with persistent state
def make_tag_counter(tag):
    # make_tag_counter is a closure (function that remembers values from its scope even after it is done executing)
    valid_tags = ["h1", "p", "a"]
    if tag not in valid_tags:
        raise ValueError(f"Tag: {tag} not a valid tag: {valid_tags}")
    count = 0
    def hold_tag_counter():
        # We need nonlocal because we want to update a free variable `count`
        # `count` is considered a free variable because it persists after make_tag_counter scope is gone
        nonlocal count
        count += 1
        return count
    return hold_tag_counter

# Notice that we create our own tag counter for each tag. Those counters are different closures which hold the "count state" for each tag
# h1_counter = make_tag_counter("h1")
# p_counter = make_tag_counter("p")
# print(h1_counter())
# print(h1_counter())
# print(p_counter())

# Problem 2: Use `nonlocal` to modify enclosed state
def rate_limiter(max_calls):
    # We want times_called here because if it was inside track_calls each call would have its own times_called variable
    # and we want it to be managed at the rate_limiter level
    times_called = 0
    def track_calls(msg: str):
        nonlocal times_called
        if times_called >= max_calls:
            raise RuntimeError("Called too many times")
        times_called += 1
        return msg
    return track_calls

# limited_print = rate_limiter(3)
# print(limited_print("hello"))
# print(limited_print("world"))
# print(limited_print("again"))
# print(limited_print("once more"))

# Problem 3: Write a decorator that logs args and return values
# Remember that decorators are just functions that take other functions and return new functions
def debug(func):
    # It is less complex to use a decorator here because func is binded to the closure of debug and we can use it in inner_debug without needing to pass func around directly
    """A decorator that returns the function name, arguments, and return value"""
    # We want the decorator to be generic so we want it to accept any arg/kwarg
    def inner_debug(*args, **kwargs):
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        kwarg_str = ', '.join(repr((k, v)) for k, v in kwargs.items())
        arguments = f"Args: {arg_str} and kwargs: {kwarg_str}"
        result = func(*args, **kwargs)
        print(f"Calling {name} with arguments ({arguments}) and returning {result}")
        return result  # Returns the original function result preserves the behavior of the original function while also ensuring the wrapper adds debug outputs
    return inner_debug

# When we apply the decorator @debug we get something like this: `debug(multiply)`
# Note that the decorator receives the *function object* not the return value
# This means that `multiply` is replaced by `inner_debug` somewhere in the call stack and that fcn executes instead
@debug
def multiply(a: int, b: int):
    return a * b

#print(multiply(3, 4))

# Problem 4: Combine closure, nonlocal, and decorator
def count_calls(max_calls):
    def decorator(func):
        count = 0
        # The closure is built when `call_information` is created and only contains the variables the inner function references
        def call_information(*args, **kwargs):
            nonlocal count  # Recall that we need to turn count into nonlocal so we can update its value
            if count >= max_calls:
                raise RuntimeError(f"Exceed max number of calls for func: {func}")
            count += 1
            name = func.__name__
            result = func(*args, **kwargs)
            print(f"Function: {name} has been called: {count} times and returning: {result} this time")
            return result
        return call_information
    return decorator

# @count_calls(max_calls=1)
# def greet(name):
#     return f"Hello, {name}!"

# @count_calls
# def square(x):
#     return x * x

# greet("Ava")
# square(3)
# square(10)
# greet("Liam")

# Problem 5: Build a Stateful Rate-Limiter using __call__
class RateLimiter:
    def __init__(self, max_calls=3):
        self.max_calls = max_calls
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1  # Explore the difference so when we move to a class we do not need nonlocal
        # I want self.count to be before the limiter function because I need `self` and I do not have this in limiter
        if self.count >= self.max_calls:
            raise RuntimeError(f"Exceeded max number of calls: {self.max_calls}")
        return args

    def reset(self):
        assert self.count != 0
        self.count = 0
        assert self.count == 0
        return

# limiter = RateLimiter(max_calls=4)
# print(limiter("hello"))
# print(limiter("zayn"))
# print(limiter("patel"))
# limiter.reset()
