import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()
speech_key = os.environ['KEY']
service_location = os.environ['LOCATION']

# Creates an instance of a speech config with specified subscription key and service region.
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_location)
speech_config.speech_synthesis_language = "en-GB"
speech_config.speech_synthesis_voice_name = "en-GB-MiaNeural"

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

print("Hello, I'm Mia. What do you want me to say?")

# Loop forever
while True:
    # Get what the user wants to say
    speech_input = input()

    # Say the text
    speech_synthesizer.speak_text(speech_input)