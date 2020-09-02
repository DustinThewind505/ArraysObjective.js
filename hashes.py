### ========== FUNCTION ==========
def my_hash(str, limit):
    encoded_string = str.encode()
    
    total = 0
    for character in encoded_string:
       total += character

    return total % limit

# ===== Creates an array with 8 empty slot =====
hash_table = [None] * 8
print(hash_table)


index = my_hash('Ello', len(hash_table))  # Creates a slot for the word "Poppet"
hash_table[index] = 'Value for "Ello"'    # Insert the word "Poppet" in an empty slot
print(index)

index = my_hash('Poppet', len(hash_table))  # Creates a slot for the word "Poppet"
hash_table[index] = 'Value for "Poppet"'    # Insert the word "Poppet" in an empty slot
print(index)
print(hash_table)

hash_table[index] = 'Value for "Hello World"'   # Overwrites(Puts) the VALUE at given index
print(hash_table)