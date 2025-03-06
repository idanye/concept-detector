import re
import requests
from bs4 import BeautifulSoup


class TextExtractor:
    @staticmethod
    def extract_text_from_url(url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = [re.sub(r'\s+', ' ', p.text.strip()) for p in soup.find_all(["p", "div", "span"]) if
                          p.text.strip()]
            extracted_text = "\n".join(paragraphs)

            # Ensure words in mashed-together text are separated
            cleaned_text = re.sub(r'(?<=\w)(?=[A-Z])', ' ',
                                  extracted_text)  # Add space before uppercase words if missing
            # Final cleanup: Remove excessive spaces within lines
            cleaned_text = re.sub(r'[ \t]+', ' ', cleaned_text).strip()

            return cleaned_text if cleaned_text else None

        except Exception as e:
            print(f"Error fetching URL: {e}")
            return None

    @staticmethod
    def extract_text_from_file(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            cleaned_text = re.sub(r'\s+', ' ', text).strip()

            return cleaned_text if cleaned_text else None

        except Exception as e:
            print(f"Error reading file: {e}")
            return None
