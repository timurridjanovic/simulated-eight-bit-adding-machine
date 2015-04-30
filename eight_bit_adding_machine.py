import re


#Logic gates
def and_gate(in_1, in_2):
    validate_inputs(in_1, in_2)
    if in_1 == '1' and in_2 == '1':
        return '1'
    else:
        return '0'

def or_gate(in_1, in_2):
    validate_inputs(in_1, in_2)
    if in_1 == '1' and in_2 == '0':
        return '1'
    if in_1 == '0' and in_2 == '1':
        return '1'
    if in_1 == '1' and in_2 == '1':
        return '1'
    else:
        return '0'

def xor_gate(in_1, in_2):
    validate_inputs(in_1, in_2)
    if in_1 == '1' and in_2 == '0':
        return '1'
    if in_1 == '0' and in_2 == '1':
        return '1'
    else:
        return '0'

def nor_gate(in_1, in_2):
    validate_inputs(in_1, in_2)
    out = or_gate(in_1, in_2)
    return inverter(out)

def nand_gate(in_1, in_2):
    validate_inputs(in_1, in_2)
    out = and_gate(in_1, in_2)
    return inverter(out)

#half adder and full-adder
def half_adder(in_1, in_2):
    validate_inputs(in_1, in_2)
    sum_out = xor_gate(in_1, in_2)
    carry_out = and_gate(in_1, in_2)
    return sum_out, carry_out

def full_adder(carry_in, in_1, in_2):
    validate_inputs(carry_in, in_1, in_2)
    sum_out_1, carry_out_1 = half_adder(in_1, in_2)
    final_sum_out, carry_out_2 = half_adder(carry_in, sum_out_1)
    final_carry_out = or_gate(carry_out_1, carry_out_2)
    return final_sum_out, final_carry_out

#eight bit adding machine
def eight_bit_adding_machine(eight_bit_str_1, eight_bit_str_2):
    validate_eight_bit_strings(eight_bit_str_1, eight_bit_str_2)

    in_1_a = eight_bit_str_1[-1]
    in_1_b = eight_bit_str_2[-1]
    in_2_a = eight_bit_str_1[-2]
    in_2_b = eight_bit_str_2[-2]
    in_3_a = eight_bit_str_1[-3]
    in_3_b = eight_bit_str_2[-3]
    in_4_a = eight_bit_str_1[-4]
    in_4_b = eight_bit_str_2[-4]
    in_5_a = eight_bit_str_1[-5]
    in_5_b = eight_bit_str_2[-5]
    in_6_a = eight_bit_str_1[-6]
    in_6_b = eight_bit_str_2[-6]
    in_7_a = eight_bit_str_1[-7]
    in_7_b = eight_bit_str_2[-7]
    in_8_a = eight_bit_str_1[-8]
    in_8_b = eight_bit_str_2[-8]

    sum_out_1, carry_out_1 = full_adder('0', in_1_a, in_1_b)
    sum_out_2, carry_out_2 = full_adder(carry_out_1, in_2_a, in_2_b)
    sum_out_3, carry_out_3 = full_adder(carry_out_2, in_3_a, in_3_b)
    sum_out_4, carry_out_4 = full_adder(carry_out_3, in_4_a, in_4_b)
    sum_out_5, carry_out_5 = full_adder(carry_out_4, in_5_a, in_5_b)
    sum_out_6, carry_out_6 = full_adder(carry_out_5, in_6_a, in_6_b)
    sum_out_7, carry_out_7 = full_adder(carry_out_6, in_7_a, in_7_b)
    sum_out_8, carry_out_8 = full_adder(carry_out_7, in_8_a, in_8_b)

    return carry_out_8 + sum_out_8 + sum_out_7 + sum_out_6 + sum_out_5 + sum_out_4 + sum_out_3 + sum_out_2 + sum_out_1

    

#Utility functions
def inverter(in_1):
    """
    turns 0 to a 1 and 1 to a 0
    """
    validate_inputs(in_1)
    if in_1 == '0':
        return '1'
    else:
        return '0'

def validate_inputs(*args):
    """
    validate inputs to logic gates
    """
    for e in args:
        if type(e) != str:
            raise TypeError("you must provide a 0 or 1 string as parameters to this function") 
        if e != '1' and e != '0':
            raise ValueError("you must provide a 1 or a 0 string as inputs to this function")

def validate_eight_bit_strings(*args):
    """
    valiate inputs to eight bit adding machine
    """
    for e in args:
        if type(e) != str:
            raise TypeError("you must provide 8 bit strings as parameters to this function")
        if re.match(r'^[01]{8}$', e) == None:
            raise ValueError("you must provide 8 bit strings composed of only 0s and 1s as parameters to this function")
        

class Tester(object):
    """
    very simple tests... Kept it very simple...
    """
    def __init__(self):
        self.counter = 1
    
    def test(self, assertion):
        try:
            assert assertion
            print 'Test number %s has passed' % self.counter
        except AssertionError:
            raise AssertionError("test number %s failed" % self.counter)
        self.counter += 1
        

def main():
    t = Tester()
    t.test(eight_bit_adding_machine('11011101', '11101001') == '111000110')
    t.test(eight_bit_adding_machine('00000001', '00000001') == '000000010')
    t.test(eight_bit_adding_machine('11111111', '11111111') == '111111110')
    t.test(eight_bit_adding_machine('00001001', '10000001') == '010001010')
    t.test(eight_bit_adding_machine('10000000', '00000001') == '010000001')
    t.test(eight_bit_adding_machine('10101010', '01010101') == '011111111')

    print 'all tests passed successfully'

if __name__ == '__main__':
    main()
