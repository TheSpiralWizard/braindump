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
const interests = "";

let project_names = [];
let project_descriptions = [];
let project_stage_names = [];
let project_stage_descriptions = [];
let project_resources = [];
let num_stages = 0;

chat = model.start_chat(history=[])

async function names () {
    response = chat.send_message("I am a university student who is interested in working on projects about the following subjects: " + interests + ". Think of a personal project I can perform using the information I have provided. Give me ONLY the name of this project (the name of the project must be your only output). For example, if I am interested in working on stock prediction using machine learning, then you may output 'Sentiment Analysis for Stock Prediction.'");
    const text = response.text();
    console.log(text);
    project_names.push(text);
}

async function description () {
    response = chat.send_message("Give me a detailed description of what this project would entail (what is the purpose of this project and what does it do?) and what technical skills (softwares, etc.) I need to learn to complete it.");
    const text = response.text();
    console.log(text);
    project_descriptions.push(text);
}

async function stage_count() {
    response = chat.send_message("I want a plan for this project that is separated into multiple stages. Analyze the project title and the description to figure out the stages. How many stages will there be? Your only output should be the number, for example, '1', '2', etcetera.");
    const text = response.text();
    num_stages = text;
}

async function stages () {
    for (let i = 1; i <= num_stages; i++) {
        response = chat.send_message("Give me only the name for stage " + i + " of the plan. For example, if my project was sentiment analysis for stock behavior prediction, then the output you produce (representing a stage name) could be 'Learning PyTorch'.");
        const text = response.text();
        console.log(text);
        project_stage_names.push(text);

        response = chat.send_message("For this stage, give me a detailed description of the stage and what it entails. For example, if my project was sentiment analysis for stock behavior prediction and the current stage was 'Learning PyTorch', then your output could be 'PyTorch is a machine learning library for Pyton. By learning PyTorch, you can work with language models to perform sentiment analysis of your data.'");
        text = response.text();
        console.log(text);
        project_stage_descriptions.push(text);

        resources();
    }
}

async function resources () {
    response = chat.send_message("For this stage of the project, locate me one resource to learn the skill required for it. For example, if the personal project is sentiment analysis for stock behavior prediction, and if the stage name is 'Fine Tuning', then you must give me a YouTube tutorial or an article that teaches fine-tuning, that is relevant to my project, to me. Only output the name of the resource (that is, the name of YouTube video or the name of the article). For example, your output may be 'Fine-Tuning for Beginners'");
    const text = response.text();

    console.log(text);
    project_resources.push(text);
}

async function run () {
    names();
    description();
    stage_count();
    stages();
}

// number of projects we want to generate for each idea
const iterator = 1;

for (let i = 0; i < iterator; i++) {
    run();
}

const final_list = [project_names, project_descriptions, project_stage_names, project_stage_descriptions, project_resources, num_stages];
return final_list;

/*
let base_user_prompt = "";
base_user_prompt = base_user_prompt.concat("I am a university student who is interested in working on projects about the following subjects: ", interests, ". ");
// base_user_prompt = base_user_prompt.concat("I am a university student who is majoring in ", major, ". I am interested in working on projects in the following subjects: ", interests, ". Here is the idea I have for a project: ", idea)
//base_user_prompt = base_user_prompt.concat("I am a university student who is interested in working on projects about the following subjects: ", interests, ". Here is the idea I have for a project: ", idea)

async function names () {
    base_user_prompt = base_user_prompt.concat("Think of a personal project I can perform using the information I have provided. Give me only the name of this project. For example, if I am interested in working on stock prediction using machine learning, then you may output 'Sentiment Analysis for Stock Prediction.'");
    const result = await model.generateContent(base_user_prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    project_names.push(text);
}

async function description (iterator) {
    base_user_prompt = base_user_prompt.concat("I want to work on the project ' " + project_names[iterator] + "'. Give me detailed description of what this project would entail (what is the purpose of this project and what does it do?) and what technical skills (softwares, etc.) I need to learn to complete it.");
    const result = await model.generateContent(base_user_prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    project_descriptions.push(text);
}

async function stages (iterator) {
    base_user_prompt = base_user_prompt.concat("Think of a personal project I can perform using the information I have provided (my interests, and my idea). Give me the name of this project and a detailed description of what it entails and what technical skills (softwares, etc.) I need to learn to complete it.");
    const result = await model.generateContent(base_user_prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    project_stages.push(text);
    resources(base_user_prompt);
}

async function resources (iterator) {
    base_user_prompt = base_user_prompt.concat("Think of a personal project I can perform using the information I have provided (my interests, and my idea). Give me the name of this project and a detailed description of what it entails and what technical skills (softwares, etc.) I need to learn to complete it.");
    const result = await model.generateContent(base_user_prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    project_resources.push(text);
}
*/

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