#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Введите предложение: ")

    first_comma_index = sentence.find(',')

    second_comma_index = sentence.find(',', first_comma_index + 1)

    if second_comma_index == -1:
        print("Символы после первой запятой:", sentence[first_comma_index + 1:])
    else:
        print("Символы между первой и второй запятой:", sentence[first_comma_index + 1:second_comma_index])
