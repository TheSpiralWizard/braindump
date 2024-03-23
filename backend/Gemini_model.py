pip install -q -U google-generativeai

import google.generativeai as genai

genai.configure(api_key=os.environ["AIzaSyABrxRzsA88dysLAUnpWu03yQahNaF9TBQ"])

model = genai.GenerativeModel('gemini-1.0-pro-001')

chat = model.start_chat()
response = chat.send_message("")
print(response.text)
response = chat.send_message("")
