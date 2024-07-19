import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def chat(question, aaple):
    genai.configure(api_key=os.getenv("gemini_api"))

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    model = genai.GenerativeModel(
        model_name="gemini-pro", generation_config=generation_config)

    prompt_parts = [
        f"""Answer following question: {question} in 20-30 words. 
    Based on below data {aaple}
    """,
    ]
    response = model.generate_content(prompt_parts)
    output = response.text
    print(response.text)
    return output

def motivation(stock, aaple):
    genai.configure(api_key=os.getenv("gemini_api"))

    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config)

    prompt_parts = [
        f"""Create a notification for user which can motivate them in Sustainable stocks to invest in this sustainable stock {stock} in 10-20 words.
        Based on below data {aaple}
        Keep it cool, engaging and short. Keep it trendy and genZ way.""",
    ]
    response = model.generate_content(prompt_parts)
    output = response.text
    print(response.text)
    return output
