from sklearn.feature_extraction.text import TfidfVectorizer


class KeywordExtractor:
    @staticmethod
    def extract_keywords_tfidf(text, num_keywords=10):
        if not text or text.strip() == "":
            print("Error: No valid text found for keyword extraction.")
            return []

        try:
            vectorizer = TfidfVectorizer(stop_words="english", max_features=num_keywords)
            tfidf_matrix = vectorizer.fit_transform([text])
            feature_names = vectorizer.get_feature_names_out()
            return [word.lower() for word in feature_names]

        except ValueError:
            print("Error: No significant text found for TF-IDF extraction.")
            return []
