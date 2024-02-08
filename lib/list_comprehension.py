#!/usr/bin/env python3

def return_evens(num_list):
    even_elements= [num for num in num_list if num %2 ==0]
    return even_elements

def make_exclamation(sentence_list):
    sentences_with_exclamation = [sentence + '!' for sentence in sentence_list]
    return sentences_with_exclamation