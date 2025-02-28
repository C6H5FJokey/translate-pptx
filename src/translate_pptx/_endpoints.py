def prompt_openai(message: str, model="deepseek-chat"):
    """A prompt helper function that sends a message to openAI
    and returns only the text response.
    """
    import openai

    message = [{"role": "user", "content": message}]

    client = openai.OpenAI(base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    return response.choices[0].message.content

def prompt_nop(message:str):
    """A prompt helper function that does nothing but returns the contained json. This function is useful for testing."""
    return "```json" + message.split("```json")[1]
