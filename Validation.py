import re

class data_validation:
    def __init__(self):
        self.valid_integers = []


    def is_valid(self, input_data):
        
        if re.match(r'^[1-9]\d*$', input_data):
            return True
        else: 
            return False    
            
    def input_validation(self, input_list):
        for input_data in input_list:
            if self.is_valid(input_data):
               self.valid_integers.append(int(input_data))
     

    def get_val_int(self):
        return self.valid_integers



if __name__ == "__main__":
    validator = data_validation()
    user_inputs = ["10", "ahrt", "42", "-15", "0", "199"]

    validator.input_validation(user_inputs)
    valid_integers = validator.get_val_int()

    print("Valid integers: ", valid_integers)
