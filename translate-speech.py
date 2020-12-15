import os
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()
speech_key = os.environ['KEY']
service_location = os.environ['LOCATION']

# See https://docs.microsoft.com/azure/cognitive-services/speech-service/language-support?WT.mc_id=academic-11379-jabenn
# for the list of supported languages that can be recognized and translated to
translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=speech_key,
                                                                   region=service_location,
                                                                   speech_recognition_language="en-GB",
                                                                   target_languages=("fr", "en", "zh-Hans"))

# Creates a translation recognizer
speech_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)

print("Say something!")

# When a sentence is recognized, print it to the screen.
def recognized(args):
    if args.result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("English   :", args.result.translations["en"])
        print("French    :", args.result.translations["fr"])
        print("Chinese   :", args.result.translations["zh-Hans"])
        print()

# Wire up the recognized event
speech_recognizer.recognized.connect(recognized)

# Start the recognition. This will trigger the recognized event in the background
speech_recognizer.start_continuous_recognition()

# Loop forever processing speech
while True:
    time.sleep(1)
