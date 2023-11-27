#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")
    word3 = input("Введите третье слово: ")

    unique_letters = []

    for letter in word1:
        if letter not in unique_letters and letter not in word2 and letter not in word3:
            unique_letters.append(letter)

    for letter in word2:
        if letter not in unique_letters and letter not in word1 and letter not in word3:
            unique_letters.append(letter)

    for letter in word3:
        if letter not in unique_letters and letter not in word1 and letter not in word2:
            unique_letters.append(letter)

    print("Неповторяющиеся буквы:", ''.join(unique_letters))
