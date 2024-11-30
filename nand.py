def NAND_gate(a, b):
  if a:
    if b:
      return 0
  return 1

# TEST CASES

print("A: 0, B: 0 | Output: {0}".format(NAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(NAND_gate(1, 1)))
