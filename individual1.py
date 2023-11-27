#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Введите предложение:")

    result = []

    for i in range(len(sentence) - 1):
        if sentence[i:i + 2] == "нн":
            result.append(sentence[i:i + 2])

    print(result)
