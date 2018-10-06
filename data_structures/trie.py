# https://en.wikipedia.org/wiki/Trie

# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

# https://www.hackerrank.com/contests/hourrank-30/challenges/video-conference/problem

# ***In the trie node, the 'end' is set as initially 0 and
#   incremented as the word repeats.
#
#  1. Search if the input string is already present in the
#     trie structure. If yes, the increment 'end' and
#     print the name along with the 'end' value
#
#  2. ELSE insert it into the trie,
#     2.1 set flag = 1 initially before starting to insert
#     2.3 For every character already present in trie
#         print the character
#     2.3 if the current character is not found and flag
#         is 1, set the flag to 0 and print the character.

class node:
    def __init__(self):
        self.child = [None]*26
        self.count = 0

class Trie:
    def __init__(self):
        self.root = node()

    def insert(self, s):
        temp = self.root
        flag = 1
        for i in range(len(s)):
            index = ord('a') - ord(s[i])
            if not temp.child[index]:
                if flag == 1:
                    flag = 0
                    print(s[i], end='')
                temp.child[index] = node()
            else:
                print(s[i], end='')
            temp = temp.child[index]
        temp.count = 1
        print()

    def search(self, s):
        temp = self.root
        for i in range(len(s)):
            index = ord('a') - ord(s[i])
            if not temp.child[index]:
                return 0
            temp = temp.child[index]
        if temp != None and temp.count != 0:
            temp.count +=1
            return temp.count
        else:
            return 0

if __name__ == '__main__':

    n = int(input().strip())

    t = Trie()

    for _ in range(n):
        name = input()
        temp = t.search(name)
        if temp != 0:
            print(name, temp)
        else:
            t.insert(name)
