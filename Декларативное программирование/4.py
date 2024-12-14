# BEGIN
def number_of_unique_letters(text):
    return len({char.lower() for char in text if char.isalpha()})
# END
