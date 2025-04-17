from groq import Groq

client = Groq(api_key="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") 

def query_groq_llm(prompt: str) -> str:
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return completion.choices[0].message.content.strip()


# prompt = "You need to go through this document and provide a summary documentation in return"
