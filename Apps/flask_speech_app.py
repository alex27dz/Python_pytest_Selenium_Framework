from flask import Flask, render_template, request
import speech_recognition as sr
import pyaudio

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_speech.html')

@app.route('/convert', methods=['POST'])
def convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)

    except sr.UnknownValueError:
        text = "Could not understand audio"
    except sr.RequestError as e:
        text = "Could not request results; {0}".format(e)

    print(type(text))
    print(text)
    new_content = text
    file = open('../hello.txt', 'w')
    file.write(new_content)
    file.close()
    return render_template('index_speech.html', text=text)

if __name__ == '__main__':
    app.run()
