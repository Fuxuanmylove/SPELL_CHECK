# SPELL_CHECK
a spell checker written by a python green hand

# dictionary.json：
存放了原本的正确词汇

The original correct vocabulary is stored here

# spell_check.zip(spell_check.json):
存放了纠正字典

A correction dictionary is stored here

# spell_check.py:
用户可以通过这个文件进行简单的输入操作，输入正确拼写时会提示输入正确，输入错误拼写时会提供纠正建议。输入的单词无法被检测到或者是原本字典中不存在的单词时，将会告诉用户无法在纠正字典中找到这个单词

Users can use this file to perform simple typing operations, prompt for correct spelling, and suggest correction if they misspell it. If the entered word cannot be detected or the word does not exist in the original dictionary, the user will be told that the word cannot be found in the correction dictionary

# spell_check_generator.py:
包含了三个功能，第一个功能可以让用户更新存放原本单词的字典，第二个功能是删除字典中的词，第三个功能是构建新的纠正字典。请务必在添加或删除单词之后构建新的纠正字典。

Contains two functions, the first of which allows users to update the dictionary where the original word is stored, and the second is to build a new correction dictionary. Be sure to build a new correction dictionary after adding new words.

# 纠正范围：
# Scope of corrections
顺序错误的两个相邻字母 Two adjacent letters in the wrong order

某个被额外连续重复了一遍的字母 Repeat two adjacent letters

某个缺失的字母 A single letter is missing
