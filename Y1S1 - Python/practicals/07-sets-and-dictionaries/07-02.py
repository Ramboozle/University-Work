# Write and test three functions that each take two words (strings) as parameters and
#  return sorted lists (as defined above) representing respectively:
#  Letters that appear in at least one of the two words.
#  Letters that appear in both words.
#  Letters that appear in either word, but not in both.
#  Hint: These could all be done programmatically, but consider carefully what topic we
#  have been discussing this week! Each function can be exactly one line

def letters_in_either(word1, word2):
    return sorted(set(word1 + word2))

def letters_in_both(word1, word2):
    return sorted(set(word1).intersection(set(word2)))

def letters_in_either_not_both(word1, word2):
    return sorted(set(word1).symmetric_difference(set(word2)))

print(letters_in_either('cheese', 'cake'))
print(letters_in_both('cheese', 'cake'))
print(letters_in_either_not_both('cheese', 'cake'))