# Pancakes START
# by stefan@mycourseresource.com
# https://eu.pythonanywhere.com/
answer = input('Do we have all the ingredients? [YES/NO]')
answer_uppercase = answer.upper()
answer_uppercase_stripped_spaces = answer_uppercase.strip()
if answer_uppercase_stripped_spaces == 'YES':
    print('Happy days, we can make pancakes :-)')
else:
    print('Sad .... we need to go shopping :-(')

