# import pyttsx3
# # Initialize the converter
# converter = pyttsx3.init()
# voices = converter.getProperty('voices')
# for voice in voices:
# # to get the info. about various voices in our PC
# print("Voice:")
# print("ID: %s" %voice.id)
# print("Name: %s" %voice.name)
# # print("Age: %s" %voice.age)
# # print("Gender: %s" %voice.gender)
# # print("Languages Known: %s" %voice.languages)
# # Sets speed percent, can be more than 100
# converter.setProperty('rate', 100)
# # Set volume 0-1
# converter.setProperty('volume', 0.7)
# # English
# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# converter.setProperty('voice', voice_id)
# converter.say("Hello GeeksforGeeks")
# converter.say("I'm also a geek")
# converter.runAndWait()
# # dostosuj, jeśli na komputerze są dostępne inne głosy
# # Polski
# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0"
# converter.setProperty('voice', voice_id)
# converter.say("Cześć jak się masz?")
# converter.runAndWait()