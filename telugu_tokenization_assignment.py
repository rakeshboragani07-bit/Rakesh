# Telugu Tokenization Assignment with Comments in English
# Install Indic NLP library before running:
# pip install indic-nlp-library

import re
from indicnlp.tokenize import indic_tokenize  

# Sample Telugu paragraph
text = "రాము బజారుకి వెళ్లాడు. అక్కడ అతను ఆపిల్, మామిడి కొనుగోలు చేశాడు. తర్వాత ఇంటికి వెళ్లిపోయాడు. హైదరాబాద్ సిటీ ప్రసిద్ధి గాంచింది."

# -----------------------------
# 1. Naïve space-based tokenization
# -----------------------------
# Split words using spaces only
naive_tokens = text.split(" ")
print("Naïve Tokenization:\n", naive_tokens)

# -----------------------------
# 2. Rule-based manual correction
# -----------------------------
manual_tokens = []
for token in naive_tokens:
    # Separate punctuation (.,!? etc.)
    token = re.sub(r'([.,!?])', r' \1', token)

    # Split common suffixes (కి, లో, నుండి, తో)
    token = re.sub(r'(కి|లో|నుండి|తో)$', r' \1', token)

    # Split compound verbs (example: వెళ్లిపోయాడు → వెళ్లి + పోయాడు)
    token = token.replace("వెళ్లిపోయాడు", "వెళ్లి పోయాడు")

    manual_tokens.extend(token.split())

print("\nManual Corrected Tokens:\n", manual_tokens)

# -----------------------------
# 3. Using Indic NLP Tool
# -----------------------------
tool_tokens = list(indic_tokenize.trivial_tokenize(text, lang='te'))
print("\nIndic NLP Tool Tokens:\n", tool_tokens)

# -----------------------------
# 4. Multiword Expressions (MWEs)
# -----------------------------
MWEs = [
    "హైదరాబాద్ సిటీ",     # Place name
    "చేతికి పని",        # Idiomatic phrase (employment)
    "వెయ్యి కళ్ళు"        # Fixed phrase (lots of attention)
]

print("\nMultiword Expressions (MWEs):")
for mwe in MWEs:
    print(f"- {mwe} (should be treated as a single token)")

# -----------------------------
# 5. Reflection in English
# -----------------------------
reflection = (
"The hardest part of tokenization is separating root words and suffixes/postpositions. "
"Compared to English, Telugu has a rich morphology (case markers, verb suffixes), so space-based tokenization alone is insufficient. "
"Punctuation can be separated similar to English, but suffixes and compound verbs require special handling. "
"MWEs (e.g., హైదరాబాద్ సిటీ, చేతికి పని) should be treated as single tokens to preserve meaning. "
"Manual correction and Indic NLP tool outputs show differences in tokenization. "
"Accurate tokenization requires Telugu-specific morphological analysis."
)

print("\nReflection in English:\n", reflection)