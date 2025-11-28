from operator import attrgetter, itemgetter, add, sub, mul
# Conceptual question: Define a first-class object in Python (Hint: There are four things to satisfy)
# 1. Can be passed as an argument to a function
# 2. Can be assigned to (assigned to variable or element)
# 3. Created at runtime (*)
# 4. Returned as the result of a function (*)
# Conceptual question 2: Give an example of first class objects that are not functions
# ints, strings, dicts

# Question on using `itemgetter`
students = [
    ("Alex", 14, 88),
    ("Sana", 8, 94),
    ("Derek", 21, 72),
    ("Maya", 18, 88),
    ("Zayn", 18, 94)
]

# Sort the list by exam score. If tie then sort alphabetically by the student name
# We cannot use `reverse=True` anywhere because that applies to the entire tuple. 
# Adding "Zayn" with the same score as "Sana" means that we needed a small fcn for sorting
students_exam_scores = itemgetter(2, 0)
def key_function(row):
    score, name = students_exam_scores(row)  # We see that itemgetter is its own function *but only does extraction not transformation* which returns a tuple and we can unpack this and apply to each row
    return (-score, name)
# print(sorted(students, key=key_function))

# Question on `attrgetter` (Reminder: attrgetter extracts *object attributes* by name)
class File:
    def __init__(self, name, size_kb, extension):
        self.name = name
        self.size_kb = size_kb
        self.extension = extension

files = [
    File("data", 220, "csv"),
    File("report", 180, "pdf"),
    File("analysis", 220, "txt"),
    File("summary", 120, "pdf"),
]

# This creates a function and when this fcn is called it returns these three attributes from an object
file_sort = attrgetter("size_kb", "extension", "name")
def sort_fcn(obj):
    """Sorts the attributes"""
    size_kb, extension, name = file_sort(obj)
    return (-size_kb, extension, name)  # This is the sorting key

# for f in sorted(files, key=sort_fcn):
#     print(f.name, f.size_kb, f.extension)

# Function registry
def mod(a, b):
    return a % b

# We can store functions as values in a dictionary because just like int, float, str functions are objects
calc_dict = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "mod": mod
}

def conduct_op(op_name: str, a: float, b: float):
    if op_name not in calc_dict:  # Python treats membership on keys by default
        raise KeyError(f"Unknown operation: {op_name}. Valid operations include: {[key for key in calc_dict.keys()]}")
    return calc_dict[op_name](a, b)
