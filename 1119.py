import unittest
from typing import List

def isVowle(s: str) -> bool:
    return s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'

def removeVowels(self, s: str) -> int:
    return ''.join(list(filter(lambda x : not isVowle(x), s)))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('ltcdscmmntyfrcdrs', removeVowels(self, 'leetcodeisacommunityforcoders'))


if __name__ == '__main__':
    unittest.main()
