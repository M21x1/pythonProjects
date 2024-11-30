class UltraSuperCalculator:
    def __init__(self, name):
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''

        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)
    
    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1

        self.number_registers[self.numbers_index] = int(value_to_store, 2)

        print(f"Value: {int(value_to_store, 2)} stored in register: {self.numbers_index}.")
        self.numbers_index += 1
    
    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value
    
    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0

        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index
        
    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value
    
    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value
    
    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value
    
    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0

        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print(f"Division by 0 error: {num1}/{num2}.")
        
        return calculated_value
    
    def get_last_calculation(self):
        if self.temp_history_index > 0:
            self.temp_history_index -= 1
        else:
            self.temp_history_index = len(self.history_registers) - 1

        last_value = f"The last calculated value was: {int(self.history_registers[self.temp_history_index], 2)}"
        self.update_display(last_value)
    
    def binary_reader(self, instruction):
        if len(instruction) != 32:
            self.update_display("Invalid Instruction Length")
            return

        opcode = instruction[0:6]
        source_one = instruction[6:11]
        source_two = instruction[11:16]
        store = instruction[16:26]
        function_code = instruction[26:]

        if opcode == '000001':
            self.store_value_to_register(store)
            return
        elif opcode == '100001':
            self.get_last_calculation()
            return
        elif opcode != '000000':
            self.update_display("Invalid OPCODE")
            return
        
        result = 0

        if function_code == '100000':
            result = self.add(source_one, source_two)
        elif function_code == '100010':
            result = self.subtract(source_one, source_two)
        elif function_code == '011000':
            result = self.multiply(source_one, source_two)
        elif function_code == '011010':
            result = self.divide(source_one, source_two)
        else:
            self.update_display("Invalid Function")
            return
        
        self.store_to_history_register(result)
        self.update_display(f"The result is: {result}")

# Example usage:
your_calc_name = UltraSuperCalculator("Maxxi")

# Adds 5 and 10 to number registers
your_calc_name.binary_reader("00000100000000000000000101000000")  # Store 5 in register 1
your_calc_name.binary_reader("00000100000000000000001010000000")  # Store 10 in register 2

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
your_calc_name.binary_reader("00000000001000010000000000100000")  # Add registers 1 and 2
your_calc_name.binary_reader("00000000001000010000000000100010")  # Subtract registers 1 and 2
your_calc_name.binary_reader("00000000001000010000000000011000")  # Multiply registers 1 and 2
your_calc_name.binary_reader("00000000001000010000000000011010")  # Divide registers 1 and 2

# Gets the last three calculations
your_calc_name.binary_reader("10000100000000000000000000000000")
your_calc_name.binary_reader("10000100000000000000000000000000")
your_calc_name.binary_reader("10000100000000000000000000000000")