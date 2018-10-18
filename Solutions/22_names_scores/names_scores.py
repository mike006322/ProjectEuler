#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler022

class Names():

    def __init__(self):
        self.names = []
        self.namesDict = dict()

    def insert(self, name):
        self.names.append(name.lower())

    def sort(self):
        self.names.sort()

    def score(self):
        for i, name in enumerate(self.names):
            self.namesDict[name] = (i+1)*sum([ord(i) - 96 for i in name])

    def get_score(self, name):
        return self.namesDict[name.lower()]

if __name__ == '__main__':
    n = Names()
    N = int(input())
    for _ in range(N):
        name = input()
        n.insert(name)
    n.sort()
    n.score()
    q = int(input())
    for _ in range(q):
        name = input()
        print(n.get_score(name))
