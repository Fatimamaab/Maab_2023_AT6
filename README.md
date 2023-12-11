Designing a method in a class that performs data validation on a list of user inputs.
The data_validation class contains the following methods:
import re

class data_validation:
    def __init__(self):
        self.valid_integers = []
    def is_valid(self, input_data):
        if re.match(r'^[1-9]\d*$', input_data):
            return True
        else: 
            retun False
            
   def input_validation(self, input_list):
      for input_data in input_list:
          if self.is_valid(input_data):
              self.valid_integers.append(int(input_data))
   def get_val_int(self):
      return self.valid_integers
