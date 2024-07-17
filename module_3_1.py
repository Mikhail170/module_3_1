calls = 0


def count_calls():
    global calls
    result = calls + 1
    return result


def string_info(string):
    global calls
    calls = count_calls()
    lenth_of_string = len(string)
    upper = string.upper()
    lower = string.lower()
    tuple = (lenth_of_string, upper, lower)
    return tuple


def is_contains(string, list_to_search):
    global calls
    calls = count_calls()
    list_to_search = [s.lower() for s in list_to_search]
    return string.lower() in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)