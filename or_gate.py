from nand import NAND_gate

def OR_gate(a,b):
  return NAND_gate(NAND_gate(a,a), NAND_gate(b,b))

# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(OR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(OR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(OR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(OR_gate(1, 1)))
