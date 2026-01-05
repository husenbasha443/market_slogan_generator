import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from prompts.prompts_library import GENERAL_SLOGAN_PROMPT


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Marketing Slogan Generator", layout="centered")

st.title(" Marketing Slogan Generator")
st.write("Generate short marketing slogans using prompt engineering and Groq LLMs.")

product_name = st.text_input("Product Name", "Fitness Tracker")
target_audience = st.text_input("Target Audience", "Young Professionals")
tone = st.selectbox(
    "Tone",
    ["motivational", "friendly", "professional", "bold"]
)


if st.button("Generate Slogan"):
    filled_prompt = GENERAL_SLOGAN_PROMPT.format(
        product_name=product_name,
        target_audience=target_audience,
        tone=tone
    )

    with st.spinner("Generating slogan..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": filled_prompt}
            ]
        )

    st.success("Slogan Generated!")
    st.markdown("### 🏷️ Marketing Slogan")
    st.write(response.choices[0].message.content)
