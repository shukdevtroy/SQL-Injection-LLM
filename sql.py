import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def check_sql_injection(code):
    prompt = (
        "Analyze the following Python code for SQL injection vulnerabilities. "
        "Provide feedback on any potential issues:\n\n"
        f"{code}\n\n"
        "Please highlight any specific lines that are vulnerable and suggest "
        "how to fix them."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )

    return response.choices[0].message['content']

def scan_file(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()
    return check_sql_injection(source_code)

def main():
    # Change this to the directory you want to scan
    directory = 'py/'  # Change this to your directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                print(f"Scanning {file}...")
                feedback = scan_file(os.path.join(root, file))
                print(f"Feedback for {file}:\n{feedback}\n")

if __name__ == "__main__":
    main()
