import google.generativeai as genai
import os

genai.configure(api_key="")

#check which Gemini models are available
#for m in genai.list_models():
    #if 'generateContent' in m.supported_generation_methods:
        #print(m.name)

model = genai.GenerativeModel('gemini-1.0-pro-001')

chat = model.start_chat(history=[])
response = chat.send_message("")
print(response.text)

#response = chat.send_message("")
