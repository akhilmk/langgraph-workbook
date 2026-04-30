import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    print("Hello from lang-graph!")
    
    # Your LangGraph logic goes here
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in environment or .env file")
    else:
        print("Environment loaded successfully.")

if __name__ == "__main__":
    main()
