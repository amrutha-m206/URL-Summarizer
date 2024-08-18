import nltk
import os

# Set NLTK data directory (modify this path if necessary)
nltk_data_dir = "/app/nltk_data"
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download the 'wordnet' resource
try:
    nltk.download("wordnet", download_dir=nltk_data_dir)
    print("wordnet downloaded successfully")
except Exception as e:
    print(f"Failed to download wordnet: {e}")
