import google.generativeai as palm

palm.configure(api_key="")

models = [
    m for m in palm.list_models() if "generateText" in m.supported_generation_methods
]
model = models[0].name


def generate_response(prompt, model):
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0.8,  # You can adjust the temperature for varied responses
        max_output_tokens=100,  # Control the length of the response
    )
    return completion.result


print("Bot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break

    # Generate a response from the bot
    bot_response = generate_response(user_input, model)
    print("Bot:", bot_response)
