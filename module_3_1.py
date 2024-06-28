calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    list_ = []
    a = len(string)
    b = string.upper()
    c = string.lower()
    list_.append(a)
    list_.append(b)
    list_.append(c)
    tuple_ = tuple(list_)
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    list_ = []
    for i in list_to_search:
        i = i.upper()
        list_.append(i)
    string = string.upper()
    if string in list_:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


