import os

# Define the paths
input_folder = 'chunky/'
output_folder = 'output_chunks/'
dictionary_file = 'chara_here.txt'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Part 1: Check characters against the dictionary and update it
def update_dictionary(input_folder, dictionary_file):
    # Read existing characters from the dictionary
    with open(dictionary_file, 'r', encoding='utf-8') as f:
        existing_chars = set(f.read().strip())

    # Iterate through each chunk folder
    for chunk_folder in os.listdir(input_folder):
        chunk_path = os.path.join(input_folder, chunk_folder)
        if os.path.isdir(chunk_path):
            for filename in os.listdir(chunk_path):
                file_path = os.path.join(chunk_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            for char in line.strip():
                                existing_chars.add(char)  # Add new characters
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write updated characters back to the dictionary
    with open(dictionary_file, 'w', encoding='utf-8') as f:
        f.write(''.join(sorted(existing_chars)))

# Part 2: Extract words and save them in chunks
def extract_words_and_chunk(input_folder, output_folder):
    word_count = 0
    chunk_index = 1
    chunk_file_path = os.path.join(output_folder, f'chunk_{chunk_index}.txt')
    
    # Open the first chunk file for writing
    chunk_file = open(chunk_file_path, 'w', encoding='utf-8')

    # Iterate through each chunk folder
    for chunk_folder in os.listdir(input_folder):
        chunk_path = os.path.join(input_folder, chunk_folder)
        if os.path.isdir(chunk_path):
            for filename in os.listdir(chunk_path):
                file_path = os.path.join(chunk_path, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            # Replace underscores with spaces and split into words
                            words = line.strip().replace('_', ' ').split()
                            for word in words:
                                chunk_file.write(word + '\n')
                                word_count += 1
                                # Check if we need to create a new chunk file
                                if word_count >= 100000:
                                    chunk_file.close()
                                    chunk_index += 1
                                    chunk_file_path = os.path.join(output_folder, f'chunk_{chunk_index}.txt')
                                    chunk_file = open(chunk_file_path, 'w', encoding='utf-8')
                                    word_count = 0
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Close the last chunk file
    chunk_file.close()

# Run the functions
update_dictionary(input_folder, dictionary_file)
extract_words_and_chunk(input_folder, output_folder)

print("Processing complete.")
