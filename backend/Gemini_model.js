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

idea = ""
major = ""
interests = ""

base_user_prompt = "I am a university student who is majoring in " + major + ". I am interested in working on projects in the following subjects: " + interests + ". Here is the idea I have for a project: " + idea 

async function projects (prompt) {
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    return text;
}

async function projects (prompt) {
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    return text;
}

projects(user_prompt);

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