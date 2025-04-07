import streamlit as st
import openai

# 🛠️ Page setup
st.set_page_config(page_title="EchoCast - AI Podcast", layout="centered")

# 🔑 API Key setup (replace with your own key)
openai.api_key = "Enter Your Key"

# 🎙️ Title and Introduction
st.title("🎧 EchoCast: AI-Powered Podcast")
st.markdown("Talk with historical legends or hear immersive stories from history.")

# 🕰️ Select a character or event
topic = st.selectbox(
    "Choose a Historical Figure or Event:",
    ["Mahatma Gandhi", "World War II", "Albert Einstein", "Rani Lakshmi Bai", "The French Revolution"]
)

# 💬 Prompt for the AI
prompt = st.text_area(
    "What would you like to ask or hear about?",
    placeholder="Tell me your role in the freedom struggle..."
)

# ▶️ Start Podcast Button
if st.button("🎤 Start Podcast"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt to start the conversation.")
    else:
        with st.spinner("Generating your podcast... 🎧"):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": f"You are {topic}, narrating in first person like a podcast. Be detailed, immersive, and emotional."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=700,
                    temperature=0.8
                )

                # 📢 Display Response
                reply = response.choices[0].message.content
                st.markdown("### 🎙️ Podcast Segment")
                st.success(reply)

                st.markdown("---")
                st.info("📤 Publishing and audio features coming soon...")

            except Exception as e:
                st.error(f"Oops! Something went wrong: {e}")