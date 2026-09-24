import ollama
while True:
    question = input("Ask the question:")
    if question.lower() == "exit":
        break
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content":question
            }
        ]
    )

    print(response["message"]["content"])