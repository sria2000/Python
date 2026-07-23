///
Problem: Suffix-Stripping Stemmer

Scenario
Stemming is the process of extracting the base word from a word. For instance, the base for "worked" is "work".

Algorithm to stem a word:

If the word ends in 'ed', 'ly', or 'ing', remove the suffix.
If the resulting word is longer than 8 letters, keep only the first 8 letters.

Task
Implement a function that takes a string of space-separated words and returns its stemmed counterpart (each word replaced by its stem).

Constraints

Every character in text is either an English lowercase letter or a space.
text starts and ends with a letter. No two consecutive characters are spaces.
text contains at most 100 words.
No word is longer than 18 letters.

Example 1

Input:  'an extremely dangerous dog is barking'
Output: 'an extreme dangerou dog is bark'
'an' — no suffix match, under 8 letters → unchanged
'extremely' → ends in 'ly' → 'extreme' (7 letters, kept)
'dangerous' — no suffix match, but 9 letters → truncate to 8 → 'dangerou'
'dog', 'is' — unchanged
'barking' → ends in 'ing' → 'bark' (4 letters, kept)

Example 2

Input:  'a boy is jumping quickly'
Output: 'a boy is jump quick'

Example 3

Input:  'the results cannot be extrapolated to other patient group'
Output: 'the results cannot be extrapol to other patient group'

///
#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'stemmer' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING text as parameter.
#

def stemmer(text):
    words = text.split(' ')
    result = []
    for word in words:
        if word.endswith('ing'):
            word = word[:-3]
        elif word.endswith('ed'):
            word = word[:-2]
        elif word.endswith('ly'):
            word = word[:-2]
        if len(word) > 8:
            word = word[:8]
        result.append(word)
    return ' '.join(result)

if __name__ == '__main__':
    text = input()
    result = stemmer(text)
    print(result)


  /// when runing the script - type - a boy is jumping quickly  ///
