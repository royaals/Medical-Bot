const { DiscussServiceClient } = require("@google-ai/generativelanguage");
const { GoogleAuth } = require("google-auth-library");

const MODEL_NAME = "models/chat-bison-001";
const API_KEY = "";

const client = new DiscussServiceClient({
  authClient: new GoogleAuth().fromAPIKey(API_KEY),
});

async function main() {
  const result = await client.generateMessage({
    model: MODEL_NAME,
    temperature: 0.5,
    candidateCount: 1,
    prompt: {
      context: "Respond to all questions with a rhyming poem.",
      examples: [
        {
          input: { content: "What is the capital of California?" },
          output: {
            content: `If the capital of California is what you seek,
Sacramento is where you ought to peek.`,
          },
        },
      ],

      messages: [{ content: "what is signs of Diabetes?" }],
    },
  });

  console.log(result[0].candidates[0].content);
}

main();
