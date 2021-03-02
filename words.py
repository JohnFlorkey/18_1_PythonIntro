def print_upper_words(words, must_start_with):
    """For a list of words, print out each word on a separate line, but in all uppercase, 
        and only if it begins with one of the specified letters regardless of case."""

    lower_string = ''

    for char in must_start_with:
        lower_string = lower_string + char.lower()
        
    lower_must_start_with = tuple((lower_string))

    for word in words:
        if word.lower().startswith(lower_must_start_with):
            print(word.upper())

print_upper_words(['hello','hey','goodbye','yo','yes','Ebola','eduardo'], must_start_with=('g','E'))