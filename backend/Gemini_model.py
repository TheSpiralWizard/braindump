#installation req. 1: pip3 install -q -U google-generativeai
#installation req. 2: pip3 install ipython

#import textwrap

import google.generativeai as genai
import os

from google.generativeai.types import HarmCategory, HarmBlockThreshold

from google.generativeai.types import HarmCategory, HarmBlockThreshold

"""
#from IPython.display import display
#from IPython.display import Markdown

#def to_markdown(text):
  #text = text.replace('•', '  *')
  #return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyABrxRzsA88dysLAUnpWu03yQahNaF9TBQ")

#check which Gemini models are available
#for m in genai.list_models():
    #if 'generateContent' in m.supported_generation_methods:
        #print(m.name)

model = genai.GenerativeModel('gemini-1.0-pro-001')

chat = model.start_chat(history=[])

#interests = "agriculture"
#interests = ""


global interests
interests = ""

project_names = []
project_descriptions = []
project_stage_names = []
project_stage_descriptions = []
project_resources = []
#num_stages = 0
"""
def process(input):
    interests = input
    project_names = []
    project_descriptions = []
    project_stage_names = []
    project_stage_descriptions = []
    project_resources = []
    genai.configure(api_key="AIzaSyABrxRzsA88dysLAUnpWu03yQahNaF9TBQ")
    model = genai.GenerativeModel('gemini-1.0-pro-001')
    chat = model.start_chat(history=[])

    # Names
    response = chat.send_message("I am a university student who is interested in working on projects about the following: " + interests + ". Think of a small scale personal project I can perform using the information I have provided. Give me ONLY the name of this project (the name of the project must be your only output). The title CANNOT be more than ten words long")
    #text = to_markdown(response.text)
    text = response.text
    text = text.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n"," ")
    project_names.append(text)

    # Description
    response = chat.send_message("Give me a succinct description of what this project would entail (what is the purpose of this project and what does it do?) and what technical skills (softwares, etc.) I need to learn to complete it. It must be MAXIMUM two sentences.")
    #text = to_markdown(response.text)
    text = response.text
    text = text.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n"," ")
    project_descriptions.append(text)

    # Stage Count
    response = chat.send_message("I want a plan for this project that is separated into multiple stages. Analyze the project title and the description to figure out the stages. How many stages will there be? Your only output should be the number, for example, '1', '2', etcetera.")
    text = response.text
    num_stages = text
    num_stages = num_stages.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n"," ")
    #to_markdown(num_stages)
    print(num_stages)
    #print(type(num_stages))
    num_stages = int(num_stages) #fix for type conversion error?

    # Stages
    for i in range (1, num_stages + 1):
        response = chat.send_message("Give me only the name for stage " + str(i) + " of the plan. Make the name a maximum of five words")
        #text = to_markdown(response.text)
        text = response.text
        text = text.replace("*","")
        text = text.replace("#","")
        text = text.replace("\n"," ")
        project_stage_names.append(text)

        response = chat.send_message("For this stage, give me a succinct description of the stage and what it entails. Make the description a maximum of two sentences. DO NOT INCLUDE THE PREVIOUS STAGE TITLE IN YOUR DESCRIPTION.")
        #text = to_markdown(response.text)
        text = response.text
        text = text.replace("*","")
        text = text.replace("#","")
        text = text.replace("\n", " ")
        text = text.replace("Stage " + str(i) + ": " + project_stage_names[i-1], " ")
        project_stage_descriptions.append(text)
        
        # Resources 
        response = chat.send_message("For this stage of the project, locate me one resource to learn the skill required for it. Display only the title of the resource and nothing else.")
        #text = to_markdown(response.text)
        text = response.text
        text = text.replace("*","")
        text = text.replace("#","")
        text = text.replace("\n"," ")

        project_resources.append(text)

    final_list = [project_names, project_descriptions, project_stage_names, project_stage_descriptions, project_resources, num_stages]
    return final_list


"""
chat = model.start_chat(history=[])

def names (): 
    response = chat.send_message("I am a university student who is interested in working on projects about the following: " + interests + ". Think of a personal project I can perform using the information I have provided. Give me ONLY the name of this project (the name of the project must be your only output).", safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    })
    #response = chat.send_message("I am a university student who is interested in working on projects about the following: " + interests + ". Think of a personal project I can perform using the information I have provided. Give me ONLY the name of this project (the name of the project must be your only output). For example, if I am interested in working on stock prediction using machine learning, then you may output 'Sentiment Analysis for Stock Prediction.'")
    #text = to_markdown(response.text)
    text = response.text
    text = text.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n","")
    project_names.append(text)

def description (): 
    response = chat.send_message("Give me a succinct description of what this project would entail (what is the purpose of this project and what does it do?) and what technical skills (softwares, etc.) I need to learn to complete it.", safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    })
    #text = to_markdown(response.text)
    text = response.text
    text = text.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n","")
    project_descriptions.append(text)

def stage_count ():
    response = chat.send_message("I want a plan for this project that is separated into multiple stages. Analyze the project title and the description to figure out the stages. How many stages will there be? Your only output should be the number, for example, '1', '2', etcetera.", safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    })
    text = response.text
    global num_stages
    num_stages = text
    num_stages = num_stages.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n","")
    #to_markdown(num_stages)
    #print(num_stages)
    #print(type(num_stages))
    num_stages = int(num_stages) #fix for type conversion error?

def stages (): 
    for i in range (1, num_stages + 1):
        #response = chat.send_message("Give me only the name for stage " + str(i) + " of the plan. For example, if my project was sentiment analysis for stock behavior prediction, then the output you produce (representing a stage name) could be 'Learning PyTorch'.")
        response = chat.send_message("Give me only the name for stage " + str(i) + " of the plan.", safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
        })
        #text = to_markdown(response.text)
        text = response.text
        text = text.replace("*","")
        text = text.replace("#","")
        text = text.replace("\n","")
        project_stage_names.append(text)

        #response = chat.send_message("For this stage, give me a succinct description of the stage and what it entails. For example, if my project was sentiment analysis for stock behavior prediction and the current stage was 'Learning PyTorch', then your output could be 'PyTorch is a machine learning library for Pyton. By learning PyTorch, you can work with language models to perform sentiment analysis of your data.'")
        response = chat.send_message("For this stage, give me a succinct description of the stage and what it entails.", safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
        })
        #text = to_markdown(response.text)
        text = response.text
        text = text.replace("*","")
        text = text.replace("#","")
        text = text.replace("\n","")
        project_stage_descriptions.append(text)

        resources()

def resources (): 
    #response = chat.send_message("For this stage of the project, locate me the name of one resource to learn the skill required for it. For example, if the personal project is sentiment analysis for stock behavior prediction, and if the stage name is 'Fine Tuning', then you must give me the name of a YouTube tutorial or an article that teaches fine-tuning, that is relevant to my project, to me. Only output the name of the resource (that is, the name of YouTube video or the name of the article). Do not give me the link.")
    response = chat.send_message("For this stage of the project, locate me the name of one resource to learn the skill required for it. Only output the name of the resource (that is, the name of YouTube video or the name of the article). Do not give me the link.", safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
    })
    #text = to_markdown(response.text)
    text = response.text
    text = text.replace("*","")
    text = text.replace("#","")
    text = text.replace("\n","")

    project_resources.append(text)

def run ():
    names()
    description()
    stage_count()
    stages()

#number of projects we want to generate for each idea
iterator = 1

for i in range (iterator):
    run()

def process(input):
    interests = input
    run()
    final_list = [project_names, project_descriptions, project_stage_names, project_stage_descriptions, project_resources, num_stages]
    #final_list = [project_names, project_descriptions, project_stage_names, project_stage_descriptions, num_stages]
    return final_list

if __name__ == "__main__":
    final_list = [project_names, project_descriptions, project_stage_names, project_stage_descriptions, project_resources, num_stages]
    #final_list = [project_names, project_descriptions, project_stage_names, project_stage_descriptions, num_stages]
    print(final_list)
    #return final_list
"""
"""
final_list = process("Farming")
names = final_list[0]
descriptions = final_list[1]
stageNames = final_list[2]
stageDescriptions = final_list[3]
resources = final_list[4]
numStages = final_list[5]
print("Names: " + str(names))
print("\n")

print("Descriptions: " + str(descriptions))
print("\n")

print("Stage Names: " + str(stageNames))
print("\n")

for s in stageDescriptions:
    print("Stage Description: " + s)

print("\n")

print("Resources: " + str(resources))
print("\n")

print("Num Stages: " + str(numStages))
print("\n")
"""