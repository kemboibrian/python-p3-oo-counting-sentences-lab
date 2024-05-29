#!/usr/bin/env python3
import re
class MyString:
  
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) != type("asd"):
            print("The value must be a string.")
        self._value = new_value

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        number = []

        if self.value != "":
            number = [count for count in re.split(r"[.!?]+",self.value) if count != ""]
        return len(number)
