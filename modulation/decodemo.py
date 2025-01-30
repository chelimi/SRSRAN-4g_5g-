import numpy as np

def read_from_binfile(filename):
    """Read modulated signal from a binary file."""
    return np.fromfile(filename, dtype=np.float32)

def bpsk_demodulate(signal):
    """Demodulate BPSK signal."""
    return [1 if sample > 0 else 0 for sample in signal]

def symbols_to_binary(symbols):
    """Convert symbols back into binary string."""
    return ''.join(str(symbol) for symbol in symbols)

def binary_to_text(binary_data):
    """Convert binary data back to text."""
    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)
def save_text_to_file(text, filename):
    """Save decoded text to a file."""
    with open(filename, 'w',encoding='ascii') as file:
        file.write(text)

# Read and demodulate
received_signal = read_from_binfile("modulated_signal.bin")
demodulated_symbols = bpsk_demodulate(received_signal)
binary_data_received = symbols_to_binary(demodulated_symbols)
decoded_text = binary_to_text(binary_data_received)
save_text_to_file(decoded_text, "decoded_output.txt")

print("Decoded text has been saved to decoded_output.txt")






'''
import numpy as np
from scipy import signal

def read_from_binfile(filename):
    """Read modulated signal from a binary file."""
    return np.fromfile(filename, dtype=np.float32)

def low_pass_filter(signal_data, cutoff_freq, fs, order=4):
    """Apply a low-pass filter to reduce high-frequency noise."""
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff_freq / nyquist  # Normalized cutoff frequency
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return signal.filtfilt(b, a, signal_data)

def bpsk_demodulate(signal):
    """Demodulate BPSK signal."""
    return [1 if sample > 0 else 0 for sample in signal]

def symbols_to_binary(symbols):
    """Convert symbols back into binary string."""
    return ''.join(str(symbol) for symbol in symbols)

def binary_to_text(binary_data):
    """Convert binary data back to text."""
    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)

def save_text_to_file(text, filename):
    """Save decoded text to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

# Noise cancellation parameters
fs = 1000  # Sampling frequency (Hz)
cutoff_freq = 100  # Cutoff frequency for low-pass filter (Hz)

# Read the received modulated signal
received_signal = read_from_binfile("modulated_signal.bin")

# Apply low-pass filter to reduce noise
filtered_signal = low_pass_filter(received_signal, cutoff_freq, fs)

# Demodulate the BPSK signal
demodulated_symbols = bpsk_demodulate(filtered_signal)

# Convert the demodulated symbols to binary string
binary_data_received = symbols_to_binary(demodulated_symbols)

# Convert the binary data back to text
decoded_text = binary_to_text(binary_data_received)

# Save the decoded text to a file
save_text_to_file(decoded_text, "decoded_output.txt")

print("Decoded text has been saved to decoded_output.txt")
'''
