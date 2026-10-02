import anthropic

client = anthropic.Anthropic()
reply = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "Explain what O(n log n) means in two sentences."}],
)
print(reply.content[0].text)