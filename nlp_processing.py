import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

# Function to process user input and extract symptoms
def process_symptoms(user_input):
    # Use spaCy NLP model to parse user input
    doc = nlp(user_input)
    
    # Extract named entities (for symptoms)
    symptoms = []
    for ent in doc.ents:
        if ent.label_ == "SYMPTOM":
            symptoms.append(ent.text)
    
    # Return extracted symptoms
    return symptoms

# Function to compare user input with known symptom list
def compare_with_known_symptoms(user_input, known_symptoms):
    # Vectorize both the input and the known symptoms
    vectorizer = CountVectorizer().fit_transform([user_input] + known_symptoms)
    cosine_sim = cosine_similarity(vectorizer[0:1], vectorizer[1:])
    
    # Return the symptom with the highest similarity score
    most_similar_symptom_idx = cosine_sim.argmax()
    return known_symptoms[most_similar_symptom_idx]

# Example usage
user_input = "I have trouble breathing and feel tired during the day."
known_symptoms = ["snoring", "difficulty breathing", "frequent waking up", "fatigue"]

extracted_symptoms = process_symptoms(user_input)
most_similar_symptom = compare_with_known_symptoms(user_input, known_symptoms)

print(f"Extracted symptoms: {extracted_symptoms}")
print(f"Most similar known symptom: {most_similar_symptom}")
