import ollama
question=input("Ask the question:")
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"Give the answer in 2-3 line only"
        },
        {
            "role":"user",
            "content":question
        }
    ],
    options={
        "temperature": 0.7,
    }

)
print(response["message"]["content"])    