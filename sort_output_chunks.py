import os

# Define the paths
output_folder = 'output_chunks/'
all_words_folder = 'all_words/'

# Ensure the all_words folder exists
os.makedirs(all_words_folder, exist_ok=True)

# Function to read all words from the all_words folder into a set
def load_existing_words(all_words_folder):
    existing_words = set()
    for filename in os.listdir(all_words_folder):
        file_path = os.path.join(all_words_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    existing_words.add(line.strip())
    return existing_words

# Function to add new words to the all_words folder
def add_new_words(output_folder, all_words_folder):
    existing_words = load_existing_words(all_words_folder)
    new_words = []
    current_file_index = 1
    current_file_path = os.path.join(all_words_folder, f'words_{current_file_index}.txt')
    
    # Ensure the first file is created
    if not os.path.exists(current_file_path):
        with open(current_file_path, 'w', encoding='utf-8') as f:
            pass  # Create an empty file

    # Iterate through each chunk file in the output folder
    for filename in sorted(os.listdir(output_folder)):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip()
                    if word and word not in existing_words:
                        new_words.append(word)
                        existing_words.add(word)  # Add to existing words to avoid duplicates
                        
                        # Check if we need to write to a new file
                        if len(new_words) >= 150000:
                            with open(current_file_path, 'a', encoding='utf-8') as out_file:
                                out_file.write('\n'.join(new_words) + '\n')
                            new_words = []  # Reset the list for the next batch
                            current_file_index += 1
                            current_file_path = os.path.join(all_words_folder, f'words_{current_file_index}.txt')

    # Write any remaining new words to the last file
    if new_words:
        with open(current_file_path, 'a', encoding='utf-8') as out_file:
            out_file.write('\n'.join(new_words) + '\n')

# Run the function to add new words
add_new_words(output_folder, all_words_folder)

print("New words processing complete.")
