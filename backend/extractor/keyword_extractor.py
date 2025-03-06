from sklearn.feature_extraction.text import TfidfVectorizer


class KeywordExtractor:
    @staticmethod
    def extract_keywords_tfidf(text, min_score=0.09):
        print(text)

        if not text or text.strip() == "":
            print("Error: No valid text found for keyword extraction.")
            return []

        try:
            vectorizer = TfidfVectorizer(stop_words="english")
            tfidf_matrix = vectorizer.fit_transform([text])
            feature_names = vectorizer.get_feature_names_out()

            # Get the TF-IDF scores for each word
            tfidf_scores = tfidf_matrix.toarray()[0]

            # Create a dictionary of word -> score
            word_tfidf = {word.lower(): score for word, score in zip(feature_names, tfidf_scores)}

            # Filter words with a score above `min_score`
            filtered_keywords = [word for word, score in word_tfidf.items() if score > min_score]

            # Sort the filtered words by their TF-IDF score in descending order
            filtered_keywords.sort(key=lambda w: word_tfidf[w], reverse=True)

            # for word in sorted_keywords:
            #     print(f"{word}: {word_tfidf[word]}")

            # print(f"Sorted keywords before return: {sorted_keywords}")
            return filtered_keywords

        except ValueError:
            print("Error: No significant text found for TF-IDF extraction.")
            return []
