import pyttsx3  # Library for text-to-speech conversion
import speech_recognition as sr  # Library for speech recognition
import datetime  # Library to handle date and time
import wikipedia  # Library to fetch data from Wikipedia
import webbrowser  # Library to open web browsers
import os  # Library to interact with the operating system
import smtplib  # Library to send emails

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # Get available voices
engine.setProperty('voice', voices[0].id)  # Set the voice to the first available voice

def speak(audio):
    """
    Function to convert text to speech.
    :param audio: Text to be spoken
    """
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """
    Function to greet the user based on the current time.
    """
    hour = int(datetime.datetime.now().hour)  # Get the current hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    """
    Function to take microphone input from the user and return it as a string.
    :return: Recognized speech as text
    """
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("Listening...")
        r.pause_threshold = 1  # Pause threshold for the recognizer
        audio = r.listen(source)  # Listen for the user's input

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize the speech using Google's speech recognition
        print(f"User said: {query}\n")
    except Exception as e:
        speak("say that again please....")
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    """
    Function to send an email.
    :param to: Recipient email address
    :param content: Email content
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Set up the SMTP server
    server.ehlo()  # Identify to the SMTP server
    server.starttls()  # Secure the connection
    server.login('youremail@gmail.com', 'your-password')  # Log in to your email account
    server.sendmail('youremail@gmail.com', to, content)  # Send the email
    server.close()  # Close the connection

if __name__ == "__main__":
    wishMe()  # Call the wishMe function to greet the user
    while True:
        query = takeCommand().lower()  # Take the user's command and convert it to lowercase

        # Logic for executing tasks based on the query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")  # Remove the word 'wikipedia' from the query
            results = wikipedia.summary(query, sentences=2)  # Fetch the summary from Wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  # Open YouTube

        elif 'open google' in query:
            webbrowser.open("google.com")  # Open Google
            speak("open google sir....")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  # Open Stack Overflow

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'  # Specify the directory containing music
            songs = os.listdir(music_dir)  # List all files in the music directory
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song in the directory

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current time
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Path to VS Code
            os.startfile(codePath)  # Open VS Code

        elif 'email to gajendra' in query:
            try:
                speak("What should I say?")
                content = takeCommand()  # Get the content of the email
                to = "gajendrastembotix@gmail.com"  # Recipient email address
                sendEmail(to, content)  # Send the email
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Gajendra bhai. I am not able to send this email")
