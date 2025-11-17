import gradio as gr
import pickle
import os

# Helper functions
def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids, pair, idx):
    newids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

# Load pre-trained merges and vocab (you'll need to save these first)
def load_tokenizer():
    if os.path.exists('merges.pkl') and os.path.exists('vocab.pkl'):
        with open('merges.pkl', 'rb') as f:
            merges = pickle.load(f)
        with open('vocab.pkl', 'rb') as f:
            vocab = pickle.load(f)
        return merges, vocab
    else:
        return None, None

merges, vocab = load_tokenizer()

def encode(text, merges):
    """Encode text to token IDs"""
    tokens = list(text.encode("utf-8"))
    while len(tokens) >= 2:
        stats = get_stats(tokens)
        pair = min(stats, key=lambda p: merges.get(p, float("inf")))
        if pair not in merges:
            break
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens

def decode(ids, vocab):
    """Decode token IDs back to text"""
    tokens = b"".join(vocab[idx] for idx in ids)
    text = tokens.decode("utf-8", errors="replace")
    return text

def tokenize_text(input_text):
    """Main function to tokenize input and return statistics"""
    if not merges or not vocab:
        return "❌ Error: Tokenizer not loaded. Please run the notebook first to train the model.", "", "", "", ""
    
    if not input_text.strip():
        return "⚠️ Please enter some text to tokenize.", "", "", "", ""
    
    # Encode the text
    token_ids = encode(input_text, merges)
    
    # Calculate statistics
    original_bytes = len(input_text.encode("utf-8"))
    compressed_tokens = len(token_ids)
    compression_ratio = original_bytes / compressed_tokens if compressed_tokens > 0 else 0
    
    # Decode back to verify
    decoded_text = decode(token_ids, vocab)
    
    # Format token IDs for display
    token_ids_str = str(token_ids)
    
    # Create detailed statistics
    stats_text = f"""
📊 **Tokenization Statistics**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Original Bytes: {original_bytes}
• Token Count: {compressed_tokens}
• Compression Ratio: {compression_ratio:.2f}x
• Space Savings: {(1 - compressed_tokens/original_bytes)*100:.1f}%
• Vocabulary Size: {len(vocab)} tokens
"""
    
    # Token breakdown with emojis
    token_breakdown = "🔢 **Token ID Breakdown:**\n"
    for i, tid in enumerate(token_ids):
        try:
            byte_seq = vocab[tid]
            char_repr = byte_seq.decode('utf-8', errors='replace')
            token_breakdown += f"Token {i+1}: ID={tid} → '{char_repr}'\n"
        except:
            token_breakdown += f"Token {i+1}: ID={tid} → [byte sequence]\n"
    
    return stats_text, token_ids_str, decoded_text, token_breakdown, "✅ Tokenization successful!"

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="Tamil BPE Tokenizer") as demo:
    gr.Markdown("""
    # 🇮🇳 Tamil BPE Tokenizer
    ### Byte Pair Encoding for Tamil Text
    
    Enter Tamil text below to see how the BPE tokenizer encodes it. The tokenizer was trained on Tamil Wikipedia text 
    and achieves **11.82x compression** with a vocabulary of 6,000 tokens.
    """)
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="📝 Input Tamil Text",
                placeholder="நான் தமிழ் பேசுகிறேன்",
                lines=5,
                value="நான் தமிழ் பேசுகிறேன்"
            )
            
            with gr.Row():
                tokenize_btn = gr.Button("🔍 Tokenize", variant="primary", size="lg")
                clear_btn = gr.ClearButton([input_text], value="🗑️ Clear")
        
        with gr.Column():
            status_output = gr.Textbox(label="Status", lines=1, interactive=False)
            stats_output = gr.Markdown(label="Statistics")
    
    with gr.Row():
        with gr.Column():
            token_ids_output = gr.Textbox(
                label="🎯 Token IDs",
                lines=3,
                interactive=False
            )
        
        with gr.Column():
            decoded_output = gr.Textbox(
                label="✅ Decoded Text (Verification)",
                lines=3,
                interactive=False
            )
    
    token_breakdown_output = gr.Textbox(
        label="📋 Detailed Token Breakdown",
        lines=10,
        interactive=False
    )
    
    gr.Markdown("""
    ---
    ### 📚 Examples
    Try these Tamil phrases:
    - நான் தமிழ் பேசுகிறேன் (I speak Tamil)
    - வணக்கம் (Hello)
    - திருச்சிராப்பள்ளி (Tiruchirappalli)
    - தமிழ்நாடு (Tamil Nadu)
    
    ### ℹ️ About
    This tokenizer uses **Byte Pair Encoding (BPE)** algorithm trained on Tamil text. 
    It learns common character combinations and merges them into single tokens, achieving efficient text compression.
    
    **Training Stats:**
    - Vocabulary Size: 6,000 tokens
    - Number of Merges: 5,744
    - Average Compression: 11.82x on Tamil Wikipedia text
    """)
    
    # Set up the tokenize button click event
    tokenize_btn.click(
        fn=tokenize_text,
        inputs=[input_text],
        outputs=[stats_output, token_ids_output, decoded_output, token_breakdown_output, status_output]
    )
    
    # Also trigger on Enter key in text box
    input_text.submit(
        fn=tokenize_text,
        inputs=[input_text],
        outputs=[stats_output, token_ids_output, decoded_output, token_breakdown_output, status_output]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True)
