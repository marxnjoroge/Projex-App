from groq import Groq
import streamlit as st
import streamlit.components.v1 as components

sidebar = st.sidebar
model = ""
sidebar.subheader("Large Language Models")
ident2 = "lmodel"

with sidebar:
  title = st.sidebar.radio("Popular Models:", ("Meta LlaMa3", "Google gemma2-9b-it", "Mistral mixtral-8x7b-32768"), key = ident2)

  if title == 'Meta LlaMa3':
      model = "llama3-8b-8192"

  if title == 'Google gemma2-9b-it':
      model = "gemma2-9b-it"

  if title == 'Mistral mixtral-8x7b-32768':
      model = 'mixtral-8x7b-32768'

# st.title("AI Assistant")
st.markdown(''':gray[Powered by:/~>]''' +title)
st.markdown("This chat is geared toward scientific inquiry.  Enter a query below and learn something new.")
# st.divider()

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
