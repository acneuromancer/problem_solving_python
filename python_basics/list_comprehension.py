def practice_1():
    sq_list = [x * x for x in range(1, 11)]
    print(sq_list)

    sq_list = [x * x for x in range(1, 11) if x % 2 != 0]
    print(sq_list)

    ch_list = [ch.upper() for ch in "Hello World!" if ch not in 'aeiou']
    print(ch_list)


def method_1():
    word_list = ['cat', 'dog', 'rabbit']
    letter_list = []

    for word in word_list:
        for ch in word:
            letter_list.append(ch)

    print(letter_list)


def method_2():
    word_list = ['cat', 'dog', 'rabbit']
    ch_list = []
    [ch_list.append(ch) for word in word_list for ch in word if ch not in ch_list]
    print(ch_list)
