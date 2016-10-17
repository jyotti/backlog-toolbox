# coding:utf-8
import re

__author__ = 'Atsushi Nakajyo'


# `*** heading`
RE_HEADING = re.compile(r"(^\*+)(\s*)(.*)")

# `- unordered list`
RE_UNORDERED_LIST = re.compile(r"(^-+)(\s*)(.*)")
# `+ ordered list`
RE_ORDERED_LIST = re.compile(r"(^\++)(\s*)(.*)")


def markdown(text):
    print("------------ markdown ------------")
    for line in text.splitlines(keepends=False):

        match = RE_HEADING.match(line)
        if match:
            print(line)
            print("heading :" + match.group(1))
            # print(match.group(2))
            print("content :" + match.group(3))

        match = RE_UNORDERED_LIST.match(line)
        if match:
            print(line)
            print("list :" + match.group(1))
            # print(match.group(2))
            print("content :" + match.group(3))

        match = RE_ORDERED_LIST.match(line)
        if match:
            print(line)
            print("list :" + match.group(1))
            # print(match.group(2))
            print("content :" + match.group(3))


test_text = """
* 見出し1
ああああああああああああ
いいいいいいいいいいいい
ううううううううう

- 箇条書き1
- 箇条書き2
-- 箇条書き2-1
--- 箇条書き2-1-1

** 見出し2
+ 箇条書き1
+ 箇条書き2
++ 箇条書き3

*** 見出し3

***
"""

if __name__ == '__main__':
    markdown(test_text)
