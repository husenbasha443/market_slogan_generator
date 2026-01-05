import os
from dotenv import load_dotenv
from groq import Groq

#  Load environment variables from .env
load_dotenv()

# Get API key securely
api_key = os.getenv("GROQ_API_KEY")

#  Create OpenAI client
client = Groq(api_key=api_key)


def build_prompt(product_name, target_audience, tone):
    """
    Builds a reusable prompt for generating marketing slogans.
    """

    prompt = f"""
Role:
You are a professional marketing copywriter.

Task:
Generate a short and catchy marketing slogan for a product.

Context:
Product Name: {product_name}
Target Audience: {target_audience}

Constraints:
- Tone must be {tone}
- Maximum 8 words
- No false or exaggerated claims
"""
    return prompt


def generate_slogan(product_name, target_audience, tone):
    """
    Sends the prompt to OpenAI and returns the slogan.
    """

    prompt = build_prompt(product_name, target_audience, tone)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    product = input("Enter product name: ")
    audience = input("Enter target audience: ")
    tone = input("Enter tone: ")

    slogan = generate_slogan(
        product_name=product,
        target_audience=audience,
        tone=tone
    )

    print("\nGenerated Marketing Slogan:")
    print(slogan)