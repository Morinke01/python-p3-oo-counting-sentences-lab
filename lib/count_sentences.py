#!/usr/bin/env python3

class MyString:
    def __init__(self, initial_value ='') -> None:
        self._value=initial_value
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        self._value = new_value

    def is_sentence(self) -> bool:
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self) -> int:
        # Replace various sentence-ending punctuations with a period
        replaced_value = self._value.replace('!', '.').replace('?', '.')

        # Split the modified string into a list of sentences
        sentences = replaced_value.split('.')

        # Filter out empty strings
        non_empty_sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

        # Return the count of sentences
        return len(non_empty_sentences)
  
