const express = require("express");

const { DiscussServiceClient } = require("@google-ai/generativelanguage");
const { GoogleAuth } = require("google-auth-library");
const dotenv = require("dotenv");

const ejs = require("ejs");

dotenv.config();
const API_KEY = process.env.API_KEY;
const MODEL_NAME = "models/chat-bison-001";

// Replace this with the code to initialize your AI API client
const client = new DiscussServiceClient({
  authClient: new GoogleAuth().fromAPIKey(API_KEY),
});

const app = express();
const PORT = process.env.PORT || 4000;

let conversationHistory = [];

async function medicalChatbot(prompt) {
  const result = await client.generateMessage({
    model: MODEL_NAME,
    temperature: 0.5,
    candidateCount: 1,
    prompt: {
      context: prompt,
      messages: [
        { content: "You are medical bot " },
      ],
    },
  });

  return result[0].candidates[0].content;
}
app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.render("index", { chatMessages: conversationHistory });
});

app.post("/conversation", async (req, res) => {
  const userInput = req.body.user_input;

  if (userInput.toLowerCase() === "exit") {
    conversationHistory.push("You: " + userInput);
    conversationHistory.push("Chatbot: Goodbye! Take care.");
  } else {
    conversationHistory.push("You: " + userInput);
    const prompt = conversationHistory.join("\n");

    const response = await chatbot(prompt);
    conversationHistory.push("Chatbot: " + response);
  }

  res.render("conversation", { conversation: conversationHistory });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
