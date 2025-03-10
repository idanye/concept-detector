import os
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


# Function to use OpenAI GPT4
def get_definition(word):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write me the definition of this word: " + word
            }
        ]
    )

    return completion.choices[0].message.content


def show_popup(word):
    definition = get_definition(word=word)

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(word.capitalize(), definition)


class GUIApp:
    def __init__(self, root, speech_transcriber, keywords):
        self.root = root
        self.root.title("Keyword Highlighter")
        self.speech_transcriber = speech_transcriber
        self.keywords = keywords

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Arial", 12))
        self.text_area.pack(padx=10, pady=10)

        self.listening = True
        self.listen_thread = threading.Thread(target=self.update_transcription)
        self.listen_thread.daemon = True
        self.listen_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_transcription(self):
        while self.listening:
            highlighted_text = self.speech_transcriber.listen_and_match_keywords(self.keywords)
            self.root.after(0, self.append_transcription, highlighted_text)

    def append_transcription(self, text):
        self.text_area.tag_configure("highlight", foreground="blue", underline=True)

        if text:
            words = text.split()

            for word in words:
                if "\033[1;31m" in word:  # Detect ANSI color encoding for highlighted words
                    clean_word = word.replace("\033[1;31m", "").replace("\033[0m", "")
                    self.text_area.insert(tk.END, clean_word + " ", ("highlight",))
                    self.text_area.tag_add("highlight", "end-2c", "end-1c")
                    self.text_area.tag_bind("highlight", "<Button-1>", self.on_word_click)
                else:
                    self.text_area.insert(tk.END, word + " ")

            self.text_area.insert(tk.END, "\n")

    def on_word_click(self, event):
        index = self.text_area.index(tk.CURRENT)

        word_start = self.text_area.search(r"\s", index, backwards=True, regexp=True)
        if not word_start:
            word_start = "1.0"  # If no whitespace is found, assume start of text
        else:
            word_start = self.text_area.index(f"{word_start} +1c")  # Move forward one char

        word_end = self.text_area.search(r"\s", index, forwards=True, regexp=True)
        if not word_end:
            word_end = tk.END  # If no whitespace is found, assume end of text

        word = self.text_area.get(word_start, word_end).strip()

        # Remove previous hyperlinks to avoid duplicates
        self.text_area.tag_remove("highlight", "1.0", tk.END)

        # Apply hyperlink style to the selected word
        self.text_area.tag_add("highlight", word_start, word_end)

        if word:
            show_popup(word)

    def on_close(self):
        self.listening = False
        self.root.destroy()
