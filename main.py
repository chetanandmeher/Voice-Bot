from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# speech Engine initialisation
engine = pyttsx3.init()
# get the voice property
voice = engine.getProperty("voice")
# set the voice property
engine.setProperty("voice", voice[1])  # 0 for male  1 for female
# an wakeuo word
activationWord = "bingo"

# selecting the browser
# set the path for the browser
chromePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
edgePath = r''
# register the browser to the webbrowser so that you can choose later
webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chromePath))


# function for speaking
def speakUp(text, rate=120):  # rate at which the AI will say
    engine.setProperty("rate", rate)
    # make the AI speak
    engine.say(text)
    # make it waits
    engine.runAndWait()


# create a function for getting the command
def takeCommand():
    # activate the speech recogniser
    listener = sr.Recognizer()
    print("What's NOW???????")

    # setup the system microphone
    with sr.Microphone() as source:
        # time before it stop listesing after i speakuo
        listener.pause_threshold = 2
        # get the info from the microphone
        inputSpeech = listener.listen(source)

    # recognizing the user
    try:
        print("Hoping i know you :<)")
        query = listener.recognize_google(inputSpeech, language="en_gb")
        print(f'So this is what you said-- {query}')
        speakUp("I Know you.")

    # if the speaker is not recognized
    except Exception as exception:
        print("Wait a minute.............")
        print("WHO ARE YOU??????????")
        speakUp("Wait a minute.............")
        speakUp("WHO ARE YOU??????????")

        print(exception)
        return "None"
    print("query-->> ",query)
    return query


if __name__ == "__main__":
    speakUp("Hello there... What can i do for you??")
    # turning on the system
    while True:
        # make a list of what i said
        query = takeCommand().lower().split()

        # Checking for the Wakeup word first
        if query[0] == activationWord:
            query.pop(0)

            # listing Commands
            if query[0] == "say":
                if "hello" in query:
                    speakUp("hye")
                else:
                    query.pop(0)    # removing the "say"
                    speech = " ".join(query)
                    speakUp((speech))

            # navigating to websites
            if query[0]== "go" and query[1] == "to":
                speakUp("opening...")
                query = " ".join(query[2:])
                webbrowser.get("chrome").open_new(query)