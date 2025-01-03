import heapq
from collections import Counter

# Class to represent a node in the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Generate Huffman Codes
def generate_codes(node, prefix="", codes={}):
    if node is None:
        return

    if node.char is not None:  # It's a leaf node
        codes[node.char] = prefix

    generate_codes(node.left, prefix + "0", codes)
    generate_codes(node.right, prefix + "1", codes)

    return codes

# Encode the input text
def encode(text, codes):
    return ''.join(codes[char] for char in text)

# Decode the encoded text
def decode(encoded_text, tree):
    decoded_text = []
    node = tree

    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = tree

    return ''.join(decoded_text)

# Main function
def huffman_coding():
    # Take input from the user
    text = input("Enter the text to compress: ")

    # Count character frequencies
    frequency = Counter(text)

    # Build Huffman Tree
    huffman_tree = build_huffman_tree(frequency)

    # Generate Huffman Codes
    codes = generate_codes(huffman_tree)

    # Encode text
    encoded_text = encode(text, codes)

    # Decode text
    decoded_text = decode(encoded_text, huffman_tree)

    print("\nOriginal Text:", text)
    print("Conversion table:", codes)
    print("Encoded Text/Huffman code:", encoded_text)
    print("Decoded Text:", decoded_text)

# Run the program
if __name__ == "__main__":
    huffman_coding()
