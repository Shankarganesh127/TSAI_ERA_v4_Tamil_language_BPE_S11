# Tamil BPE Tokenizer - ERA v4 Session 11

## Overview
This project implements a **Byte Pair Encoding (BPE)** tokenizer specifically designed for Tamil text. The implementation demonstrates how BPE compression works on Tamil Unicode characters and achieves significant compression ratios.

## Notebook: `ERA_v4_Tamil_BPE_S11.ipynb`

### Description
The Jupyter notebook contains a complete implementation of a BPE tokenizer trained on Tamil text from Wikipedia. It processes Tamil Unicode text, builds a vocabulary through iterative merging of byte pairs, and provides encoding/decoding functionality.

### Key Features

#### 1. **Data Loading and Preprocessing**
- Loads Tamil text corpus (Wikipedia article on Tiruchirappalli - திருச்சிராப்பள்ளி)
- Cleans text by filtering Tamil Unicode range (`஀-௿`) while preserving basic punctuation
- Converts text to UTF-8 byte representation

#### 2. **BPE Training Algorithm**
The notebook implements the core BPE algorithm with these functions:

- **`get_stats(ids)`**: Counts frequency of adjacent byte pairs
- **`merge(ids, pair, idx)`**: Merges the most frequent byte pair into a new token
- **Iterative Training**: Performs multiple merge operations to build vocabulary

**Training Parameters:**
- Target Vocabulary Size: **6,000 tokens**
- Number of Merges: **5,744** (vocab_size - 256 base bytes)
- Base Vocabulary: 256 (UTF-8 byte values)

#### 3. **Vocabulary Building**
- Starts with 256 base byte tokens (0-255)
- Iteratively merges most frequent byte pairs
- Creates new tokens (256-6000) representing common byte sequences
- Stores merge rules in a dictionary for encoding

#### 4. **Encoding & Decoding Functions**

**`encode(text)`**
- Converts Tamil text string to list of token IDs
- Applies learned merge rules iteratively
- Returns compressed token representation

**Example:**
```python
encode("நான் தமிழ் பேசுகிறேன்")
# Output: [507, 399, 352, 536, 361, 547, 766, 294, 877]
```

**`decode(ids)`**
- Converts token IDs back to original text
- Uses vocabulary to map tokens to byte sequences
- Handles UTF-8 decoding with error replacement

**Example:**
```python
decode([507, 399, 352, 536, 361, 547, 766, 294, 877])
# Output: "நான் தமிழ் பேசுகிறேன்"
```

## BPE Compression Statistics

### Performance Metrics

| Metric | Value |
|--------|-------|
| **Original Token Count** | 131,444 bytes |
| **Compressed Token Count** | 11,116 tokens |
| **Compression Ratio** | **11.82x** |
| **Vocabulary Size** | 6,000 tokens |
| **Space Savings** | 91.5% reduction |

### Compression Analysis

The BPE tokenizer achieves **11.82x compression** on Tamil text, which is exceptionally high. This indicates:

1. **High Redundancy**: Tamil text has many repeated character sequences (especially compound characters with vowel modifiers)
2. **Efficient Encoding**: The learned vocabulary effectively captures common Tamil character combinations
3. **UTF-8 Overhead**: Tamil Unicode characters use 3 bytes per character in UTF-8, so BPE provides significant savings
4. **Optimal Vocabulary**: 6,000 tokens is sufficient to capture most common patterns without over-specialization

### Why Such High Compression?

Tamil script characteristics that enable high compression:
- **Compound Characters**: Base consonants + vowel modifiers (e.g., க + ா = கா)
- **Frequent Patterns**: Common words and suffixes repeat often
- **UTF-8 Encoding**: Each Tamil character = 3 bytes, BPE learns to merge these efficiently
- **Morphological Structure**: Agglutinative language with predictable affixes

## Technical Details

### Algorithm Flow

1. **Initialization**: Convert text to UTF-8 bytes (0-255)
2. **Iteration**: For 5,744 rounds:
   - Count all adjacent byte pairs
   - Find most frequent pair
   - Create new token (ID: 256+i)
   - Replace all occurrences of that pair with new token
3. **Vocabulary**: Build mapping of token IDs to byte sequences
4. **Encoding**: Apply merge rules greedily to new text
5. **Decoding**: Look up tokens in vocabulary and decode UTF-8

### Data Structure

```python
# Merge rules: (byte_pair) -> new_token_id
merges = {(p0, p1): idx, ...}  # 5,744 rules

# Vocabulary: token_id -> byte_sequence
vocab = {idx: bytes([...]), ...}  # 6,000 entries
```

## Use Cases

- **Text Compression**: Reduce storage requirements for Tamil text
- **Language Modeling**: Tokenization for Tamil NLP models
- **Machine Translation**: Subword units for translation systems
- **Text Analysis**: Understanding Tamil text structure and patterns

## Requirements

```python
import re
```

## How to Run

1. Open `ERA_v4_Tamil_BPE_S11.ipynb` in Jupyter
2. Execute cells sequentially
3. The notebook will:
   - Load and preprocess Tamil text
   - Train BPE tokenizer
   - Display compression statistics
   - Demonstrate encoding/decoding

## Example Usage

```python
# Encode Tamil text
text = "நான் தமிழ் பேசுகிறேன்"
tokens = encode(text)
print(tokens)  # [507, 399, 352, 536, 361, 547, 766, 294, 877]

# Decode back to text
decoded = decode(tokens)
print(decoded)  # நான் தமிழ் பேசுகிறேன்
```

## Future Enhancements

- Train on larger Tamil corpus for better coverage
- Implement vocabulary size optimization
- Add support for mixed Tamil-English text
- Create reusable tokenizer class
- Save/load trained model for reuse

## References

- BPE Algorithm: Sennrich et al. (2016) - "Neural Machine Translation of Rare Words with Subword Units"
- Tamil Unicode Range: U+0B80 to U+0BFF
- Training Data: Tamil Wikipedia

---

**Author**: Session 11 Assignment - ERA v4  
**Language**: Tamil (தமிழ்)  
**Encoding**: UTF-8  
**Vocabulary**: 6,000 tokens