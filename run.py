from textExtraction import extract_text_from_pdf
from openAiConnection import OpenAIIntegration
import sys

def main(file_path):
    # Extract text from the PDF file
    text = extract_text_from_pdf(file_path)
    
    # Initialize the OpenAI integration
    openai_integration = OpenAIIntegration()
    
    # Generate a prompt for the topic parser using the extracted text
    prompt = openai_integration.generate_topic_parser_prompt(text)
    
    # Call GPT-4 with the generated prompt and get the response
    response = openai_integration.call_gpt_4(prompt)
    
    # Print the response from GPT-4
    print(f"Response: {response}\n")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python run.py <path_to_pdf_file>")
    else:
        # Call the main function with the provided file path
        main(sys.argv[1])