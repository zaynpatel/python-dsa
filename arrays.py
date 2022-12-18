# exercise link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md
monthly_expenses = [2200, 2350, 2600, 2130, 2190]

# in feb, how many dollars were spent in comparison to January?
diff = monthly_expenses[1] - monthly_expenses[0]

# find total expenses for first quarter
multiply = monthly_expenses[0] * monthly_expenses[1] * monthly_expenses[2]

# exactly 2000 in any month
def spend_two():
    for dollars in monthly_expenses:
        if dollars == 2000:
            print('You spent exactly 2000')
        else:
            print('this didn\t' 'happen')
    return dollars

# add june to monthly expenses
add_june = monthly_expenses.append(1980)
#print(monthly_expenses)

# returned an item in April that was bought for $200, update
subtract = monthly_expenses[4] - 200
print(subtract)

# exercise_two
heroes=['spider man','thor','hulk','iron man','captain america']

#length of list
hero_len = len(heroes)

# add black panther
heroes.insert(3, 'black panther')
print(heroes)

r = list(map(lambda x: x.replace('hulk', 'doctor strange'), heroes))
print(r)

# or heros[1:3]=['doctor strange']

r.remove('thor')
print(r)

sorted_heroes = sorted(heroes)
print(sorted_heroes)

# exercise_three
list_of_odd = [1, 3, 5, 9, 21]
def odd_nums(input1, input2):
    if input1 % 2 == 0 or input2 % 2 == 0:
        print('Invalid number. Has to be odd')
    elif input1 < 21 or input2 < 21:
        print('Number has to be higher.')
    else:
        list_of_odd.append(max(input1, input2))

odd_nums(7, 4)
print(list_of_odd)
