#gemini model functions 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")

def generate_story(prompt, genre, length):
    story_prompt = f"Write a creative, imaginative {genre} story based on: {prompt}. Limit it to {length} words."
    response = model.generate_content(story_prompt)
    return response.text.strip()

def generate_title(prompt, genre):
    title_prompt = f"Give a short and catchy title for a {genre} story about: {prompt}"
    response = model.generate_content(title_prompt)
    return response.text.strip()

def continue_story(existing_story, genre, word_limit):
    continuation_prompt = f"Continue this {genre} story:\n\n{existing_story}\n\nAdd another {word_limit} words."
    response = model.generate_content(continuation_prompt)
    return response.text.strip()
