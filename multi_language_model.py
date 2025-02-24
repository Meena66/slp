from transformers import MarianMTModel, MarianTokenizer

# Function to load translation model for multi-language support
def load_translation_model():
    # Load MarianMT model for translation (example: English to Spanish)
    model_name = "Helsinki-NLP/opus-mt-en-es"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    return model, tokenizer

# Function to translate text to the target language
def translate_to_target_language(text, model, tokenizer):
    # Translate input text using the model
    translated = model.generate(**tokenizer.prepare_seq2seq_batch([text], return_tensors="pt"))
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Example usage
model, tokenizer = load_translation_model()
text_to_translate = "I have trouble breathing and feel tired during the day."

translated_text = translate_to_target_language(text_to_translate, model, tokenizer)
print(f"Translated text: {translated_text}")
