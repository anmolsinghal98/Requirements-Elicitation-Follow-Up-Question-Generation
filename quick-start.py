import pandas as pd
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# loads environment variables
load_dotenv()

# Initialize OpenAI client
# Make sure to set your OpenAI API key in the environment variable OPENAI_API_KEY
# Alternatively, you can pass the key directly to the OpenAI constructor with `api_key='your_api_key'`
client = OpenAI()

def query_gpt(prompt):
    """
    Queries the GPT model with a given prompt and returns the completion.
    
    Args:
        prompt (str): The input prompt to send to the GPT model
        
    Returns:
        str: The model's response/completion text
    """
    # Call the OpenAI API to get a completion
    # Ensure you have the correct model and parameters set
    chat_completion = client.chat.completions.create(
        messages = [
            {
                'role': 'system',
                'content': '',
            },
            {
                'role': 'user',
                'content': prompt,
            }

        ],
        model='gpt-4o',
        max_tokens=1000
    )
    completion = chat_completion.choices[0].message.content
    return completion

def context_prompt(interview_domain, interview_turns):
    """
    Generates a prompt for generating follow-up questions based on interview context.
    
    Args:
        interview_domain (str): The domain/topic of the interview
        interview_turns (str): The conversation history between interviewer and interviewee
        
    Returns:
        str: A formatted prompt for generating follow-up questions
    """
    prompt = f"You are an AI agent capable of generating context summaries.\
      During a requirements elicitation interview with an interviewee about how the interviewee conducts {interview_domain}, \
      the INTERVIEWEE and INTERVIEWER have had the following conversation: {interview_turns}. \
      Generate a follow-up question that the Interviewer should ask next based on the conversation. \
      Restrict your response to only show the follow-up question without explanation."
    return prompt

# Study 1

print("Sample Output for Study 1...")

# Specify the path to your CSV file containing the interview data
# The default path to reproduce the results in the paper is '~/datasets/study1.csv'
notebook_dir = os.getcwd()
df = pd.read_csv(notebook_dir+ '/datasets/study1.csv')

print("Examining the first row of the dataset...")
interview_domain = df.iloc[0]['Interview Domain']
print(f"Interview Domain: {interview_domain}")
interview_turns = df.iloc[0]['Interview Turns']
print(f"Interview Turns: {interview_turns}")

# Generate the context prompt for the current interview turn
prompt = context_prompt(interview_domain, interview_turns)
# Query the GPT model with the generated prompt
response = query_gpt(prompt)

print(f"LLM-generated question for interview turn: {response}")