from groq import Groq
import streamlit as st
import streamlit.components.v1 as components

sidebar = st.sidebar
model = ""
sidebar.subheader("Large Language Models")
ident2 = "langmodel"

with sidebar:
  title = st.sidebar.radio("Popular Models:", ("Google gemma2-9b-it", "Meta LlaMa3", "Mistral mixtral-8x7b-32768", "Deepseek-R1-Distill-70b"), key = ident2)

  if title == 'Google gemma2-9b-it':
      model = "gemma2-9b-it"

  if title == 'Meta LlaMa3':
      model = "llama3-8b-8192"

  if title == 'Mistral mixtral-8x7b-32768':
      model = 'mixtral-8x7b-32768'

  if title == 'Deepseek-R1-Distill-70b':
      model = 'deepseek-r1-distill-llama-70b'  

# st.title("AI Assistant")
st.markdown(''':gray[Powered by:/~>]''' +title)
st.markdown("This chat is geared toward scientific inquiry.  Enter a query below and learn something new.")
st.write("---")

client = Groq(api_key=st.secrets.get("GROQ_API_KEY"))

if "default_model" not in st.session_state:
    st.session_state["default_model"] = "llama3-8b-8192"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# print(st.session_state)

# Show Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input prompt for user queries.
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_text = st.empty()

        completion = client.chat.completions.create(
            temperature = 0.5,
            n = 1,
            model = model,
            max_tokens = 1024,
            messages = [
            {"role": m["role"], "content": m["content"]} 
            for m in st.session_state.messages
            ],
            stream = True,
        )

        response = ""

        for chunk in completion:
            response += chunk.choices[0].delta.content or ""
            response_text.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
