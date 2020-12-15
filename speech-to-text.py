import os
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()
speech_key = os.environ['KEY']
service_location = os.environ['LOCATION']

# Creates an instance of a speech config with specified subscription key and service region.
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_location)
speech_config.speech_recognition_language = "en-GB"

# Creates a speech synthesizer using the default speaker as audio output.
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something!")

# When a sentence is recognized, print it to the screen.
def recognized(args):
    print(args.result.text)

# Wire up the recognized event
speech_recognizer.recognized.connect(recognized)

# Start the recognition. This will trigger the recognized event in the background
speech_recognizer.start_continuous_recognition()

# Loop forever processing speech
while True:
    time.sleep(1)