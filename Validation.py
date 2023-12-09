import re

class data_validation:
    def __init__(self):
        self.valid_integers = []


    def is_valid(self, input_data):
        
        if re.match(r'^[1-9]\d*$', input_data):
            return True
        else: 
            retun False
