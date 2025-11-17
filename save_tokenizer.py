"""
Save the trained BPE tokenizer (merges and vocab) to pickle files
Run this script after training the tokenizer in the notebook
"""
import pickle

# Instructions:
# 1. Run the ERA_v4_Tamil_BPE_S11.ipynb notebook completely
# 2. After training, add this cell to save the tokenizer:

save_code = """
import pickle

# Save merges dictionary
with open('merges.pkl', 'wb') as f:
    pickle.dump(merges, f)

# Save vocabulary dictionary
with open('vocab.pkl', 'wb') as f:
    pickle.dump(vocab, f)

print("✅ Tokenizer saved successfully!")
print(f"  - merges.pkl: {len(merges)} merge rules")
print(f"  - vocab.pkl: {len(vocab)} vocabulary entries")
"""

print("=" * 60)
print("INSTRUCTIONS TO SAVE YOUR TRAINED TOKENIZER")
print("=" * 60)
print("\n1. Open ERA_v4_Tamil_BPE_S11.ipynb")
print("\n2. After the training cell (where merges and vocab are created),")
print("   add a new cell with this code:\n")
print(save_code)
print("\n3. Run that cell to save merges.pkl and vocab.pkl")
print("\n4. Then you can run: python app.py")
print("\n" + "=" * 60)
