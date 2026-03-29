import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator


# Initialize TTS (Mac uses 'nsss')
engine = pyttsx3.init(driverName='nsss')
engine.setProperty('rate', 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Speech-to-Text
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🔎 Recognizing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"✅ You said: {text}")
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")

    return ""


# Translation (stable)
def translate_text(text, target_language="hi"):
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        print(f"🌍 Translated text: {translated}")
        return translated
    except Exception as e:
        print(f"❌ Translation error: {e}")
        return ""


# Language selection
def display_language_options():
    print("\n🌐 Available Languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")

    choice = input("Select language (1-8): ")

    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }

    return language_dict.get(choice, "hi")


# Main
def main():
    target_language = display_language_options()

    original_text = speech_to_text()

    if original_text:
        translated_text = translate_text(original_text, target_language)

        if translated_text:
            speak(translated_text)
            print("✅ Done!")


if __name__ == "__main__":
    main()