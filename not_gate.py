from nand import NAND_gate

def NOT_gate(input):
  if NAND_gate(input, input):
    return 1
  else:
    return 0
  
# TEST CASE
print("A: 0 | Output: {0}".format(NOT_gate(0)))
print("A: 1 | Output: {0}".format(NOT_gate(1)))
