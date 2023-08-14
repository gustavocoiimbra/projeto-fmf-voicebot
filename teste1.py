'''
Instalar:
pip install openai
pip install gtts
pip install SpeechRecognition
sudo apt-get install portaudio19-dev
pip install pyaudio
pip install playsound
'''


import openai
from gtts import gTTS
import speech_recognition as sr
import os

openai.api_key = "chave da api"

def conversa_com_gpt(mensagem):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um bot de voz que traduz texto para fala."},
            {"role": "user", "content": mensagem}
        ]
    )

    return resposta.choices[0].message["content"]

reconhecer = sr.Recognizer()
with sr.Microphone() as fonte:
    print("Fale algo:")
    audio = reconhecer.listen(fonte)

try:
    entrada_usuario = reconhecer.recognize_google(audio)
    print("Entrada de fala:", entrada_usuario)
except sr.UnknownValueError:
    print("Não foi possível reconhecer a fala.")
    entrada_usuario = input("Digite sua mensagem: ")

resposta_bot = conversa_com_gpt(entrada_usuario)

print("Resposta do bot:", resposta_bot)

tts = gTTS(text=resposta_bot, lang='en')
tts.save("resposta_bot.mp3")

os.system("xdg-open resposta_bot.mp3")
