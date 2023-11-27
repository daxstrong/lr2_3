#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1 = "прроцесор"
    word1_corrected = word1.replace('рр', 'р').replace('с', 'сс')
    print("Исправленное слово:", word1_corrected)

    phrase1 = "теекстовыйфайл"
    phrase1_corrected = phrase1.replace('ее', 'е').replace('овый', 'овый ')
    print("Исправленная фраза:", phrase1_corrected)

    phrase2 = "програма и аллгоритм"
    phrase2_corrected = phrase2.replace('програма', 'программа').replace('аа', 'а').replace('лл', 'л')
    print("Исправленная фраза:", phrase2_corrected)

    phrase3 = "процесор и паммять"
    phrase3_corrected = phrase3.replace('с', 'сс').replace('мм', 'м')
    print("Исправленная фраза:", phrase3_corrected)
