import speech_recognition as sr
import time
import os

r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening...")
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                return MyText  # Return the recognized text

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None  # Return None if there's a request error

        except sr.UnknownValueError:
            print("Could not understand audio")  # More specific error message
            continue  # Continue listening for audio

        except OSError as e:
            print("Microphone is not available; {0}".format(e))
            return None  # Return None if there's a microphone error

def output_text(text):
    if text:  # Check if text is not None
        with open("output.txt", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {text}\n")  # Add timestamp
        print("Wrote Text: ", text)  # Print the written text

# Check if microphone is available
try:
    with sr.Microphone() as source:
        print("Microphone is available. Starting the program...")
except OSError as e:
    print("Microphone is not available; {0}".format(e))
    exit(1)  # Exit if microphone is not available

print("Instructions: Speak clearly into the microphone. Say 'stop' to terminate the program.")

try:
    while True:
        text = record_text()
        if text is not None:  # Check if text is not None
            if text.lower() == "stop":  # Check if the recognized text is "stop"
                print("Stopping the program as requested.")
                break  # Exit the loop if "stop" is recognized
            output_text(text)

except KeyboardInterrupt:
    print("\nProgram terminated by user.")