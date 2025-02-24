from backend.extractor.keyword_extractor import KeywordExtractor
from backend.extractor.text_extractor import TextExtractor
from backend.speech_transcriber import SpeechTranscriber
from frontend.gui_app import GUIApp
import tkinter as tk


def run_application():
    try:
        print("\n🔹 Speech Transcription with Context Highlighting 🔹")
        print("1️⃣ Extract from URL\n2️⃣ Extract from file")
        choice = input("Enter choice: ").strip()
        context_text = ""

        text = TextExtractor()

        if choice == "1":
            context_text = text.extract_text_from_url(input("Enter URL: ").strip())
        elif choice == "2":
            context_text = text.extract_text_from_file(input("Enter file path: ").strip())
        else:
            print("Invalid choice. Exiting.")
            return

        if not context_text:
            print("No valid text extracted. Exiting.")
            return

        key = KeywordExtractor()
        speech_transcriber = SpeechTranscriber()

        keywords = key.extract_keywords_tfidf(context_text)

        if not keywords:
            print("\nNo significant keywords found. Exiting.")
            return
        else:
            print(f"Extracted Keywords: {', '.join(list(keywords)[:10])}...")

        root = tk.Tk()
        app = GUIApp(root, speech_transcriber, keywords)
        root.mainloop()

    except KeyboardInterrupt:
        print("\n\n🛑 Stopped by user (Ctrl+C)")

    #     key = KeywordExtractor
    #     text = TextExtractor
    #     speech = SpeechTranscriber
    #
    #     context_text = ""
    #     if choice == "1":
    #         url = input("\nEnter the URL: ").strip()
    #         context_text = text.extract_text_from_url(url)
    #     elif choice == "2":
    #         file_path = input("\nEnter the file path: ").strip()
    #         context_text = text.extract_text_from_file(file_path)
    #     else:
    #         print("Invalid choice. Exiting.")
    #         return
    #
    #     if not context_text:
    #         return
    #
    #     keywords = key.extract_keywords_tfidf(context_text)
    #     keywords = {word.lower() for word in keywords}
    #
    #     if not keywords:
    #         print("\nNo significant keywords found. Exiting.")
    #         return
    #
    #     print(f"\nExtracted Keywords: {', '.join(list(keywords)[:10])}... (showing top 10)")
    #
    #     speech.listen_and_match_keywords(keywords)


if __name__ == "__main__":
    run_application()
