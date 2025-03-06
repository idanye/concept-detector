import os
from openai import OpenAI
from dotenv import load_dotenv
import speech_recognition as sr

load_dotenv()


class SpeechTranscriber:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.recognizer = sr.Recognizer()

    # Function to use OpenAI Whisper API for speech recognition
    def transcribe_audio(self, audio_data):
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_data,
            language="en",
        )

        return transcription.text

    # Function to listen & transcribe speech while matching keywords
    def listen_and_match_keywords(self, keywords):
        try:
            with sr.Microphone() as source:
                print("\n🎤 Start speaking...")

                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source)

                # Save audio temporarily
                with open("temp_audio.wav", "wb") as f:
                    f.write(audio.get_wav_data())

                # Transcribe using Whisper API
                with open("temp_audio.wav", "rb") as audio_file:
                    transcript = self.transcribe_audio(audio_file)

                highlighted_transcript = self.highlight_matched_words(transcript, keywords)

                return highlighted_transcript

        except KeyboardInterrupt:
            print("\n\n🛑 Stopped by user (Ctrl+C)")
        except Exception as e:
            print(f"❌ Error: {e}")

    @staticmethod
    def highlight_matched_words(transcript, keywords):
        words = transcript.split()
        highlighted_text = " ".join([
            f"\033[1;31m{word}\033[0m" if word.lower() in keywords else word
            for word in words
        ])

        return highlighted_text
