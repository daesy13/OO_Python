# Alright, here's a fun task!
# Create a function named combiner that takes a single argument, which will
# be a list made up of strings and numbers.
#
# Return a single string that is a combination of all of the strings in
# the list and then the sum of all of the numbers. For example,
# with the input ["apple", 5.2, "dog", 8], combiner would
# return "appledog13.2". Be sure to use isinstance to
# solve this as I might try to trick you.

def combiner(item):
    # create an empty list to store strings
    string_list = []
    # set up a holder for the sum
    sum = 0
    # iterate on each item on the list
    for n in item:
        # verify if is a string and append into list holder
        if isinstance(n, str) == True:
            string_list.append(n)
        # verify if is a number and added into the sum holder
        elif isinstance(n ,(int, float)) == True:
            sum += n
    # convert sum into str and append into list
    string_list.append(str(sum))
    # return join list
    return "".join(string_list)

print(combiner(["apple", 5.2, "dog", 8]))