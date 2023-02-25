import pyttsx3

# Create a new instance of the pyttsx3 engine
engine = pyttsx3.init()

# Set the speed of the speech (optional)
engine.setProperty('rate', 150)

# Set the voice of the speech (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a voice by its index

# Get the text to be converted to speech
text = input("Enter the text to be converted to speech: ")

# Convert the text to speech and play it
engine.say(text)
engine.runAndWait()
