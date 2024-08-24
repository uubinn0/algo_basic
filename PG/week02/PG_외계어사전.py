'''
https://school.programmers.co.kr/learn/courses/30/lessons/120869

spell이 최대 10이라 걍 itertools 씀
'''

from itertools import permutations

def solution(spell, dic):

    for word_set in permutations(spell,len(spell)):
        word = ''.join(word_set)
        if word in dic:
            return 1

    return 2
