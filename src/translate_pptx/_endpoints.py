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

class Prompt:
    """A class that produces prompt functions."""
    
    def __init__(self, model=None, pptx=None):
        """Initialize the Prompt with a model name."""
        self.model = model
        self.pptx = pptx
    
    def __call__(self, message: str) -> str:
        """Makes the Prompt instance callable like a function.
        
        Args:
            message: The message to send to the model.
        
        Returns:
            The response from the model.
        """
        if self.model and self.model.startswith("deepseek"):
            return prompt_openai(message, model=self.model)
        elif self.model is None:
            return prompt_nop(message)
        else:
            raise ValueError(f"Unknown model: {self.model}")
    
    def __str__(self):
        return f"Prompt using model: {self.model or 'none'}"