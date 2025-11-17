# 🚀 Quick Start Guide - Tamil BPE Tokenizer Gradio App

## Prerequisites
- Python 3.7+
- Jupyter Notebook or JupyterLab

## Step-by-Step Setup

### Step 1: Train the Tokenizer
```bash
# Open the notebook
jupyter notebook ERA_v4_Tamil_BPE_S11.ipynb
```

Execute all cells in order. The last cell will save two files:
- `merges.pkl` - Contains the 5,744 merge rules
- `vocab.pkl` - Contains the 6,000-token vocabulary

### Step 2: Install Gradio
```bash
pip install -r requirements.txt
```

This installs:
- `gradio` - Web UI framework
- `pickle5` - For loading saved tokenizer

### Step 3: Launch the App
```bash
python app.py
```

You'll see output like:
```
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://xxxxxxxxxxxx.gradio.live

This share link expires in 72 hours.
```

### Step 4: Use the App

**Local Access:**
- Open http://127.0.0.1:7860 in your browser

**Share with Others:**
- Use the public Gradio URL (valid for 72 hours)
- Anyone can access it without installation

## Using the Interface

1. **Input Text**
   - Type or paste Tamil text in the input box
   - Default example: "நான் தமிழ் பேசுகிறேன்"

2. **Tokenize**
   - Click the "🔍 Tokenize" button
   - Or press Enter in the text box

3. **View Results**
   - **Token IDs**: List of integer tokens
   - **Statistics**: Compression ratio, space savings
   - **Decoded Text**: Verification of reversibility
   - **Token Breakdown**: Detailed ID-to-character mapping

## Example Queries

Try these Tamil phrases:

| Tamil Text | English Meaning |
|------------|-----------------|
| நான் தமிழ் பேசுகிறேன் | I speak Tamil |
| வணக்கம் | Hello |
| நன்றி | Thank you |
| திருச்சிராப்பள்ளி | Tiruchirappalli |
| தமிழ்நாடு | Tamil Nadu |
| மலைக்கோட்டை | Rock Fort |

## Troubleshooting

### Error: "Tokenizer not loaded"
**Solution:** Run the notebook first to create `merges.pkl` and `vocab.pkl`

### Error: "Import gradio could not be resolved"
**Solution:** Install dependencies:
```bash
pip install gradio
```

### Port Already in Use
**Solution:** Specify a different port:
```python
demo.launch(share=True, server_port=7861)
```

### Files Not Found
Ensure these files exist in the same directory:
```bash
ls -la
# Should show:
# merges.pkl
# vocab.pkl
# app.py
```

## Deploying to Hugging Face Spaces

### Option 1: Manual Upload
1. Go to https://huggingface.co/spaces
2. Create a new Space (select Gradio SDK)
3. Upload:
   - `app.py`
   - `merges.pkl`
   - `vocab.pkl`
   - `requirements.txt`

### Option 2: Git Push
```bash
# Clone your HF Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/tamil-bpe-tokenizer

# Copy files
cp app.py merges.pkl vocab.pkl requirements.txt tamil-bpe-tokenizer/

# Push to HF
cd tamil-bpe-tokenizer
git add .
git commit -m "Add Tamil BPE Tokenizer"
git push
```

Your app will be live at:
`https://huggingface.co/spaces/YOUR_USERNAME/tamil-bpe-tokenizer`

## App Features

### 📊 Statistics Display
- Original byte count
- Compressed token count
- Compression ratio (typically 6-12x)
- Space savings percentage

### 🔢 Token Visualization
- Shows the list of token IDs
- Example: `[507, 399, 352, 536, 361, 547, 766, 294, 877]`

### 📋 Detailed Breakdown
For each token:
- Token position number
- Token ID
- Corresponding character(s)

Example:
```
Token 1: ID=507 → 'நா'
Token 2: ID=399 → 'ன்'
Token 3: ID=352 → ' '
...
```

### ✅ Verification
- Decodes tokens back to original text
- Confirms lossless encoding
- Catches any tokenization errors

## Performance Notes

- **Average response time**: < 100ms
- **Concurrent users**: Supports multiple simultaneous users
- **Text length limit**: No hard limit, but optimal for <10KB text
- **Memory usage**: ~50MB (for loaded tokenizer)

## Next Steps

1. **Customize the UI**: Edit `app.py` to change colors, layout, examples
2. **Add more languages**: Train on additional corpora
3. **Export tokens**: Add download button for token sequences
4. **Visualization**: Create graphs showing compression by text length
5. **Batch processing**: Allow file uploads for bulk tokenization

## Support

For issues or questions:
1. Check that notebook completed successfully
2. Verify `merges.pkl` and `vocab.pkl` exist
3. Ensure all dependencies are installed
4. Check console output for error messages

---

**Enjoy your Tamil BPE Tokenizer! 🎉**
