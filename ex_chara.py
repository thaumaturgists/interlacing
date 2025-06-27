"""
Character Sorter

This script is licensed under the MIT License. See the https://github.com/thaumaturgists/interlacing/blob/main/LICENSE file for details.

Acknowledgments:
- This project uses data from Wikipedia, licensed under the Creative Commons Attribution-ShareAlike License.
- Unicode data and standards are provided by the Unicode Consortium.
"""

import os
import logging
from collections import defaultdict

# Configure logging
logging.basicConfig(filename='character_sorter.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the input file and output directory
input_file = 'chara_here.txt'
output_dir = 'all_characters'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to determine the script of a character
def get_script(char):
    code_point = ord(char)
    script_ranges = {
        (0x0041, 0x007A): "Latin",  # Latin (A-Z, a-z)
        (0x3040, 0x309F): "Japanese - Hiragana",  # Hiragana (あ-ん)
        (0x30A0, 0x30FF): "Japanese - Katakana",  # Katakana (ア-ン)
        (0x0391, 0x03A9): "Greek",  # Greek (Α-Ω, α-ω)
        (0x0600, 0x06FF): "Arabic",  # Arabic (ا-ي)
        (0x0400, 0x04FF): "Cyrillic",  # Cyrillic (А-Я, а-я)
        (0x0531, 0x058F): "Armenian",  # Armenian (Ա-Ֆ)
        (0x0590, 0x05FF): "Hebrew",  # Hebrew (א-ת)
        (0x0900, 0x097F): "Devanagari",  # Devanagari (अ-ह)
        (0x0980, 0x09FF): "Bengali",  # Bengali (অ-হ)
        (0x0C00, 0x0C7F): "Kannada",  # Kannada (ಅ-ಹ)
        (0x0D00, 0x0D7F): "Malayalam",  # Malayalam (അ-ഹ)
        (0x0E00, 0x0E7F): "Thai",  # Thai (ก-ฮ)
        (0x0F00, 0x0FFF): "Tibetan",  # Tibetan (ཀ-ཾ)
        (0x1E00, 0x1EFF): "Latin Extended",  # Latin Extended Additional
        (0x2C60, 0x2C7F): "Latin Extended-C",  # Latin Extended-C
        (0x2D30, 0x2D7F): "Georgian",  # Georgian (ა-ჰ)
        (0xA840, 0xA87F): "Phonetic Extensions",  # Phonetic Extensions
        (0x1B00, 0x1B7F): "Balinese",  # Balinese (ᬅ-᭿)
        (0x1C00, 0x1C7F): "Glagolitic",  # Glagolitic (Ⰰ-Ɀ)
        (0x1E900, 0x1E9FF): "Ancient Symbols",  # Ancient Symbols
        (0x2D80, 0x2DDF): "Ethiopic",  # Ethiopic (ሀ-ፍ)
        (0xA500, 0xA63F): "Vai",  # Vai (ꔀ-꘿)
        (0x1F600, 0x1F64F): "Emoticons",  # Emoticons
        (0x1F300, 0x1F5FF): "Miscellaneous Symbols and Pictographs",  # Miscellaneous Symbols
        (0x1F680, 0x1F6FF): "Transport and Map Symbols",  # Transport and Map Symbols
        (0x1F700, 0x1F77F): "Alchemical Symbols",  # Alchemical Symbols
        (0x1F780, 0x1F7FF): "Geometric Shapes Extended",  # Geometric Shapes Extended
        (0x1F800, 0x1F8FF): "Supplemental Arrows-C",  # Supplemental Arrows-C
        (0x1F900, 0x1F9FF): "Supplemental Symbols and Pictographs",  # Supplemental Symbols and Pictographs
        (0x1FA00, 0x1FAFF): "Chess Symbols",  # Chess Symbols
        (0x2B50, 0x2BFF): "Miscellaneous Symbols and Arrows",  # Miscellaneous Symbols and Arrows
        (0xA700, 0xA71F): "Modifier Tone Letters",  # Modifier Tone Letters
        (0xA720, 0xA7FF): "Latin Extended-D",  # Latin Extended-D
        (0xA8E0, 0xA8FF): "Saurashtra",  # Saurashtra
        (0xA900, 0xA9FF): "Kayah Li",  # Kayah Li
        (0xAA00, 0xAA5F): "Rejang",  # Rejang
        (0xAA60, 0xAA7F): "Hangul Jamo Extended-B",  # Hangul Jamo Extended-B
        (0xAB30, 0xAB6F): "Cham",  # Cham
        (0xB000, 0xB7FF): "Myanmar",  # Myanmar (Burmese)
        (0xB800, 0xBFFF): "Sinhala",  # Sinhala
        (0xC000, 0xCFFF): "Tagalog",  # Tagalog
        (0xD000, 0xD7FF): "Khmer",  # Khmer
        (0xD800, 0xDFFF): "Surrogate Pair",  # Surrogate Pair
        (0xE000, 0xF8FF): "Private Use",  # Private Use Area
        (0xF900, 0xF9FF): "CJK Compatibility Ideographs",  # CJK Compatibility Ideographs
        (0xFA00, 0xFAFF): "CJK Compatibility Ideographs Supplement",  # CJK Compatibility Ideographs Supplement
        (0xFB00, 0xFB4F): "Alphabetic Presentation Forms",  # Alphabetic Presentation Forms
        (0xFB50, 0xFDFF): "Arabic Presentation Forms",  # Arabic Presentation Forms
        (0xFE00, 0xFE0F): "Variation Selectors",  # Variation Selectors
        (0xFE10, 0xFE1F): "Vertical Forms",  # Vertical Forms
        (0xFE20, 0xFE2F): "Combining Half Marks",  # Combining Half Marks
        (0xFF00, 0xFFEF): "Fullwidth Forms",  # Fullwidth Forms
        (0xFFF0, 0xFFFF): "Specials",  # Specials
        (0x4E00, 0x9FFF): "CJK Unified Ideographs",  # CJK Unified Ideographs
        (0x3400, 0x4DBF): "CJK Unified Ideographs Extension A",  # CJK Unified Ideographs Extension A
        (0x20000, 0x2A6DF): "CJK Unified Ideographs Extension B",  # CJK Unified Ideographs Extension B
        (0x2A700, 0x2B73F): "CJK Unified Ideographs Extension C",  # CJK Unified Ideographs Extension C
        (0x2B740, 0x2B81F): "CJK Unified Ideographs Extension D",  # CJK Unified Ideographs Extension D
        (0x3100, 0x312F): "Bopomofo",  # Bopomofo
        (0x31A0, 0x31BF): "Bopomofo Extended",  # Bopomofo Extended
        (0x0E80, 0x0EFF): "Lao",  # Lao
        (0x2D30, 0x2D7F): "Tifinagh",  # Tifinagh
        (0x1680, 0x169F): "Ogham",  # Ogham
        (0x16A0, 0x16FF): "Runic",  # Runic
        (0x0700, 0x074F): "Syriac",  # Syriac
        (0x13A0, 0x13FF): "Cherokee",  # Cherokee
        (0x1380, 0x139F): "Ethiopic Supplement",  # Ethiopic Supplement
        (0x1C00, 0x1C7F): "Glagolitic",  # Glagolitic
        (0xA840, 0xA87F): "Phonetic Extensions",  # Phonetic Extensions
        (0x1E900, 0x1E9FF): "Ancient Symbols",  # Ancient Symbols
        (0x2D80, 0x2DDF): "Ethiopic",  # Ethiopic
        (0xA700, 0xA71F): "Modifier Tone Letters",  # Modifier Tone Letters
        (0xA720, 0xA7FF): "Latin Extended-D",  # Latin Extended-D
        (0xA8E0, 0xA8FF): "Saurashtra",  # Saurashtra
        (0xA900, 0xA9FF): "Kayah Li",  # Kayah Li
        (0xAA00, 0xAA5F): "Rejang",  # Rejang
        (0xAB30, 0xAB6F): "Cham",  # Cham
        (0xB000, 0xB7FF): "Myanmar",  # Myanmar (Burmese)
        (0xB800, 0xBFFF): "Sinhala",  # Sinhala
        (0xC000, 0xCFFF): "Tagalog",  # Tagalog
        (0xD000, 0xD7FF): "Khmer",  # Khmer
        (0xD800, 0xDFFF): "Surrogate Pair",  # Surrogate Pair
        (0xE000, 0xF8FF): "Private Use",  # Private Use Area
        (0xF900, 0xF9FF): "CJK Compatibility Ideographs",  # CJK Compatibility Ideographs
        (0xFA00, 0xFAFF): "CJK Compatibility Ideographs Supplement",  # CJK Compatibility Ideographs Supplement
        (0xFB00, 0xFB4F): "Alphabetic Presentation Forms",  # Alphabetic Presentation Forms
        (0xFB50, 0xFDFF): "Arabic Presentation Forms",  # Arabic Presentation Forms
        (0xFE00, 0xFE0F): "Variation Selectors",  # Variation Selectors
        (0xFE10, 0xFE1F): "Vertical Forms",  # Vertical Forms
        (0xFE20, 0xFE2F): "Combining Half Marks",  # Combining Half Marks
        (0xFF00, 0xFFEF): "Fullwidth Forms",  # Fullwidth Forms
        (0xFFF0, 0xFFFF): "Specials",  # Specials
        (0x1F600, 0x1F64F): "Emoticons",  # Emoticons
        (0x1F300, 0x1F5FF): "Miscellaneous Symbols and Pictographs",  # Miscellaneous Symbols
        (0x1F680, 0x1F6FF): "Transport and Map Symbols",  # Transport and Map Symbols
        (0x1F700, 0x1F77F): "Alchemical Symbols",  # Alchemical Symbols
        (0x1F780, 0x1F7FF): "Geometric Shapes Extended",  # Geometric Shapes Extended
        (0x1F800, 0x1F8FF): "Supplemental Arrows-C",  # Supplemental Arrows-C
        (0x1FA00, 0x1FAFF): "Chess Symbols",  # Chess Symbols
        (0x2B50, 0x2BFF): "Miscellaneous Symbols and Arrows",  # Miscellaneous Symbols and Arrows
        (0x1F1E6, 0x1F1FF): "Regional Indicator Symbols",  # Regional Indicator Symbols (for flags)
        (0x1F9C0, 0x1F9FF): "Supplemental Symbols and Pictographs",  # Supplemental Symbols and Pictographs
        (0x2D30, 0x2D7F): "Tifinagh",  # Tifinagh
        (0xA720, 0xA7FF): "Latin Extended-D",  # Latin Extended-D
        (0xA800, 0xA82F): "Syllabics",  # Canadian Syllabics
        (0xA840, 0xA87F): "Phonetic Extensions",  # Phonetic Extensions
        (0xA880, 0xA8DF): "Saurashtra",  # Saurashtra
        (0xA900, 0xA9FF): "Kayah Li",  # Kayah Li
        (0xAA00, 0xAA5F): "Rejang",  # Rejang
        (0xAA60, 0xAA7F): "Hangul Jamo Extended-B",  # Hangul Jamo Extended-B
        (0xAB30, 0xAB6F): "Cham",  # Cham
        (0x1D400, 0x1D7FF): "Mathematical Alphanumeric Symbols",  # Mathematical Alphanumeric Symbols
        (0x1D800, 0x1DAAF): "Supplemental Mathematical Operators",  # Supplemental Mathematical Operators
        (0x1DAB0, 0x1DBFF): "Musical Symbols",  # Musical Symbols
        (0x1F000, 0x1F02F): "Mahjong Tiles",  # Mahjong Tiles
        (0x1F030, 0x1F09F): "Domino Tiles",  # Domino Tiles
        (0x1F0A0, 0x1F0FF): "Playing Cards",  # Playing Cards
        (0x1F100, 0x1F1FF): "Enclosed Alphanumeric Supplement",  # Enclosed Alphanumeric Supplement
        (0x1F200, 0x1F251): "Enclosed CJK Letters and Months",  # Enclosed CJK Letters and Months
        (0x1F260, 0x1F27F): "CJK Compatibility",  # CJK Compatibility
        (0x1F780, 0x1F7FF): "Geometric Shapes Extended",  # Geometric Shapes Extended
        (0x1F800, 0x1F8FF): "Supplemental Arrows-C",  # Supplemental Arrows-C
        (0x1F900, 0x1F9FF): "Supplemental Symbols and Pictographs",  # Supplemental Symbols and Pictographs
        (0x2B50, 0x2BFF): "Miscellaneous Symbols and Arrows",  # Miscellaneous Symbols and Arrows
        (0x2B00, 0x2B5F): "Miscellaneous Symbols",  # Miscellaneous Symbols
        (0x1F9C0, 0x1F9FF): "Supplemental Symbols and Pictographs",  # Supplemental Symbols and Pictographs
        (0x1F9D0, 0x1F9FF): "People and Body",  # People and Body
        (0x1F6A0, 0x1F6FF): "Transportation and Map Symbols",  # Transportation and Map Symbols
        (0x1F4A0, 0x1F4FF): "Miscellaneous Symbols",  # Miscellaneous Symbols
        (0x1F300, 0x1F5FF): "Miscellaneous Symbols and Pictographs",  # Miscellaneous Symbols and Pictographs
        (0x1F680, 0x1F6FF): "Transport and Map Symbols",  # Transport and Map Symbols
        (0x1F700, 0x1F77F): "Alchemical Symbols",  # Alchemical Symbols
        (0x1F780, 0x1F7FF): "Geometric Shapes Extended",  # Geometric Shapes Extended
        (0x1F900, 0x1F9FF): "Supplemental Symbols and Pictographs",  # Supplemental Symbols and Pictographs
        (0x1FA00, 0x1FAFF): "Chess Symbols",  # Chess Symbols
        (0x1F1F2, 0x1F1F3): "Flag for Taiwan",  # Flag for Taiwan
        (0x1F1E8, 0x1F1ED): "Flags",  # Regional Indicator Symbols for various flags
        (0x1F1F0, 0x1F1F7): "Regional Indicator Symbols",  # Regional Indicator Symbols for various flags
        (0x1F1F4, 0x1F1F5): "Flag for South Korea",  # Flag for South Korea
        (0x1F1E9, 0x1F1EA): "Flag for Japan",  # Flag for Japan
        (0x1F1E6, 0x1F1E7): "Flag for China",  # Flag for China
        (0x1F1E8, 0x1F1E9): "Flag for France",  # Flag for France
        (0x1F1EB, 0x1F1F7): "Flag for Germany",  # Flag for Germany
        (0x1F1F9, 0x1F1F3): "Flag for United Kingdom",  # Flag for United Kingdom
        (0x1F1FA, 0x1F1F8): "Flag for United States",  # Flag for United States
        (0x1F1F2, 0x1F1E6): "Flag for Canada",  # Flag for Canada
        (0x1F1F5, 0x1F1F1): "Flag for Italy",  # Flag for Italy
        (0x1F1F4, 0x1F1F2): "Flag for Spain",  # Flag for Spain
        (0x1F1F0, 0x1F1F4): "Flag for Brazil",  # Flag for Brazil
        (0x2CEB0, 0x2EBEF): "CJK Unified Ideographs Extension E",  # CJK Unified Ideographs Extension E
        (0x2F800, 0x2FA1F): "CJK Unified Ideographs Extension F",  # CJK Unified Ideographs Extension F
        (0x10300, 0x1032F): "Old Italic",  # Old Italic
        (0x10330, 0x1034F): "Gothic",  # Gothic
        (0x10400, 0x1044F): "Deseret",  # Deseret
        (0x10000, 0x1007F): "Linear B Syllabary",  # Linear B Syllabary
        (0x10080, 0x100FF): "Linear B Ideograms",  # Linear B Ideograms
        (0x10140, 0x1018F): "Ancient Greek Numbers",  # Ancient Greek Numbers
        (0x1950, 0x197F): "Tai Le",  # Tai Le
        (0xA6A0, 0xA6FF): "Bamum",  # Bamum
        (0xB000, 0xB0FF): "Bassa Vah",  # Bassa Vah
        (0x0500, 0x052F): "Cyrillic Supplement",  # Cyrillic Supplement
        (0x1F900, 0x1F9FF): "Supplemental Arrows-D",  # Supplemental Arrows-D
        (0xAC00, 0xD7AF): "Hangul Syllables",  # Korean
        (0x1100, 0x11FF): "Hangul Jamo",  # Korean Jamo
        (0xA960, 0xA97F): "Hangul Jamo Extended-A",  # Hangul Jamo Extended-A
        (0x0041, 0x007A): "Basic Latin",  # English (United States, United Kingdom, Canada, Australia)
        (0x00C0, 0x00FF): "Latin-1 Supplement"  # French, German, Spanish, Italian, Portuguese
    }

    for (start, end), script_name in script_ranges.items():
        if start <= code_point <= end:
            return script_name

    return "Unknown Script"

# Read characters from the input file
try:
    with open(input_file, 'r', encoding='utf-8') as file:
        characters = file.read()
except Exception as e:
    logging.error(f"Error reading input file: {e}")
    raise

# Sort characters into a dictionary by script
sorted_characters = defaultdict(list)

for char in characters:
    script = get_script(char)
    sorted_characters[script].append(char)

# Write characters to files
for script, chars in sorted_characters.items():
    script_dir = os.path.join(output_dir, script)
    
    # Create script directory if it doesn't exist
    os.makedirs(script_dir, exist_ok=True)

    # Split characters into chunks
    for i in range(0, len(chars), 1000):
        chunk = chars[i:i + 1000]
        file_content = ''.join(chunk)
        
        # Check file size
        if len(file_content.encode('utf-8')) > 5000:
            continue  # Skip if the chunk exceeds 5KB

        # Create a file name based on the script and chunk index
        file_name = f"{script}_part_{i // 1000 + 1}.txt"
        file_path = os.path.join(script_dir, file_name)

        # Write to the file with lines of no more than 100 characters
        try:
            with open(file_path, 'w', encoding='utf-8') as output_file:
                for j in range(0, len(file_content), 100):
                    line = file_content[j:j + 100]
                    output_file.write(line + '\n')
        except Exception as e:
            logging.error(f"Error writing to file {file_path}: {e}")

print("Sorting complete!")
