# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x[1:])

_word_ = 'WWWoooorrrldd'
# print(_word_[1:])


def remove_repetition(word):
    if len(word) == 1:
        return word

    print(f'Word is: {word}')
    print('=' * 20)

    if word[0] == word[1]:  # WWWoooorrrldd
        print(f'Debugging condition {word}\n')
        print('=' * 20)
        return remove_repetition(word[1:])  # slice (1, none, none)

    print(f'Debugging before return {word}')
    print(f'Return value {word[0] + remove_repetition(word[1:])}')
    print('=' * 20)
    return word[0] + remove_repetition(word[1:])
    # Stash [ World ]


print(remove_repetition(_word_))
