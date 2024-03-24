// frontend developer: run npm install @google/generative-ai in your terminal
// frontend developer (for markdown text): run npm install markdown.it --save

const { GoogleGenerativeAI } = require ("@google/generative-ai");

//initialize the model

const genAI = new GoogleGenerativeAI('${import.meta.env.VITE_API_KEY}');

const model = genAI.getGenerativeModel({model: "gemini-1.0-pro-001"});

// INPUT STREAMS

// Input 1: ideas

// assuming that one idea will be inputted at a time
// takes in an idea as an input and 

// Input 2: subjects/topics of interests

// Input 3: preferred timeframe

// const major = ""
// const idea = ""
const interests = ""

let project_names = []
let project_descriptions = []
let project_resources = []

let base_user_prompt = ""  
base_user_prompt = base_user_prompt.concat("I am a university student who is interested in working on projects about the following subjects: ", interests, ". ")
// base_user_prompt = base_user_prompt.concat("I am a university student who is majoring in ", major, ". I am interested in working on projects in the following subjects: ", interests, ". Here is the idea I have for a project: ", idea)
//base_user_prompt = base_user_prompt.concat("I am a university student who is interested in working on projects about the following subjects: ", interests, ". Here is the idea I have for a project: ", idea)

async function names (prompt) {
    prompt = prompt.concat("Think of a personal project I can perform using the information I have provided. Give me only the name of this project. For example, if I am interested in working on stock prediction using machine learning, then you may output 'Sentiment Analysis for Stock Prediction.'")
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    project_names.push(text);
}

async function description (prompt, iterator) {
    prompt = prompt.concat("I want to work on the project ' " + project_names[iterator] + "'. Give me detailed description of what this project would entail (what is the purpose of this project and what does it do?) and what technical skills (softwares, etc.) I need to learn to complete it.")
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    project_descriptions.push(text);
}

async function resources (prompt, iterator) {
    prompt = prompt.concat("Think of a personal project I can perform using the information I have provided (my interests, and my idea). Give me the name of this project and a detailed description of what it entails and what technical skills (softwares, etc.) I need to learn to complete it.")
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    return text;
}

async function run (prompt, iterator) {
    names(base_user_prompt);
    description(base_user_prompt, iterator);
    stages(base_user_prompt, iterator);
    resources(base_user_prompt, iterator);
}

// number of projects we want to generate for each idea
const iterator = 1;

for (let i = 0; i < iterator; i++) {
    run(user_prompt, i);
} 

/*
async function getResponse(prompt) {
    const message = await model.generateContent(prompt);
    const response = await message.response;
    const text = response.text();

    console.log(text);
    return text;
}

//getResponse();

//user chat div
export const userDiv = (data) => {
    return 
    //copy code from frontend
}

//AI chat div
export const aiDiv = (data) => {
    return
    //copy code from frontend
}


async function handleSubmit(envent){
    event.preventDefault();

    let userMessage = document.getElementById("prompt");
    const chatArea = document.getElementById("chat-container");

    var prompt = userMessage.value.trim();
    if (prompt === ""){
        return;
    }

    console.log("user message", prompt);

    chatArea.innerHTML += userDiv(prompt);
    userMessage.value = "";

    const aiResponse = await getResponse(prompt);
    chatArea.innerHTML += aiDiv(aiResponse);

}

const chatForm = document.getElementById("chat-form");
chatForm.addEventListener("submit", handleSubmit);

chatForm.addEventListener("keyup", (event) => {
    if (event.keyCode === 13) handleSubmit(event);
});

*/