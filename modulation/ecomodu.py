import numpy as np
def read_text_file(filename):
    """Read content from a text file."""
    with open(filename, 'r',encoding='utf-8') as file:
        return file.read()

def text_to_binary(text):
    """Convert text to binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)
    

def binary_to_symbols(binary_data, bits_per_symbol=1):
    """Convert binary data into symbols for modulation."""
    return [int(binary_data[i:i+bits_per_symbol], 2) for i in range(0, len(binary_data), bits_per_symbol)]

def bpsk_modulate(symbols):
    """Modulate symbols using BPSK."""
    return np.array([1 if bit == 1 else -1 for bit in symbols], dtype=np.float32)

def save_to_binfile(data, filename):
    """Save modulated signal to a binary file."""
    data.tofile(filename)

# Original text
text = read_text_file("input_text.txt")
binary_data = text_to_binary(text)
print(binary_data)
symbols = binary_to_symbols(binary_data)
modulated_signal = bpsk_modulate(symbols)
save_to_binfile(modulated_signal, "modulated_signal.bin")

print("Encoding and modulation complete. Binary file saved.")

