import openai
from dotenv import load_dotenv
import os

class OpenAIIntegration:
    def __init__(self):
        # Load environment variables from a .env file
        load_dotenv()
        # Retrieve the OpenAI API key from environment variables
        self.api_key = os.getenv("OPENAI_API_KEY")
        # Set the OpenAI API key for the openai library
        openai.api_key = self.api_key

    def call_gpt_4(self, prompt, max_tokens=100):
        """
        Calls the OpenAI GPT-4 model with the provided prompt and returns the generated text.

        Args:
            prompt (str): The input text prompt to generate a response for.
            max_tokens (int, optional): The maximum number of tokens to generate in the response. Defaults to 100.

        Returns:
            str: The generated text response from the GPT-4 model.
        """
        # Call the OpenAI GPT-4 model with the provided prompt and max tokens
        response = openai.Completion.create(
            engine="gpt-4o-mini",
            prompt=prompt,
            max_tokens=max_tokens
        )
        # Return the generated text from the response
        return response.choices[0].text.strip()

    def generate_topic_parser_prompt(self, user_text):
        """
        Generates a prompt for the AI to parse the user's text into primary and secondary topics.

        Args:
            user_text (str): The text input from the user that needs to be parsed.

        Returns:
            str: A formatted prompt string for the AI to identify primary and secondary topics from the user's text.
        """
        # Generate a prompt for the AI to parse the user's text into primary and secondary topics
        prompt = (
            "You are an AI topic parser. Read through the user's text and return a result indicating a primary topic and a secondary topic.\n\n"
            f"User's text: {user_text}\n\n"
            "Result:\n"
            "Primary topic: \n"
            "Secondary topic: "
        )
        return prompt