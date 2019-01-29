class Trie:

    def __init__(self):
        self._end = '*'
        self.trie = dict()


    def __repr__(self):
        return repr(self.trie)


    def find_word(self, word):
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False
        else:
            return self._end in sub_trie


    def add_word(self, word):
        if self.find_word(word):
            print('Word already exists.')
            return self.trie

        temp_trie = self.trie
        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                temp_trie = temp_trie.setdefault(letter, {})

        temp_trie[self._end] = self._end

        return temp_trie


    def list_words(self, trie = None):
        result = []
        if trie == None:
            trie = self.trie

        for k, v in trie.items():
            if k != self._end:
                for el in self.list_words(v):
                    result.append(k+el)
            else:
                result.append('')

        return result


t = Trie()
t.add_word('ball')
t.add_word('ballet')
print(t.__repr__())
print(t.find_word('ball'))
print(t.find_word('bat'))

print(t.list_words())
