
import os
import base64
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import PyPDF2
import docx
# from langchain_community.llms import Ollama  #ollama is a lightweight model
from langchain_openai import ChatOpenAI  #openai is a large model
from openai import OpenAI
# enable debug mode
from langchain.globals import set_debug
set_debug(True)
# llm = Ollama(model="llama3.2:1b", temperature=0.3)
# llm = Ollama(model="llam
llm = ChatOpenAI(model="gpt-4o",openai_api_key=openai_api_key)

tittle_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""You are an experienced speech generator.
You need to craft an impactful title for a speech
on the following topic: {topic}
Answer exactly with one title. 
    """
)

speech_prompt = PromptTemplate(
    input_variables=["title"],
    template="""You need to write a powerful speech of 100 words for the following title: {title}
    """
)

tittle_chain = tittle_prompt | llm | StrOutputParser()
speech_chain = speech_prompt | llm | StrOutputParser()

final_chain = tittle_chain | speech_chain

# Create a session state for speech counter if it doesn't exist
if 'speech_counter' not in st.session_state:
    st.session_state.speech_counter = 0
if 'text_response' not in st.session_state:
    st.session_state.text_response = ""

# Create container for text response
text_response_container = st.empty()

# Add this near the top of your script, after other initializations
if 'form_key' not in st.session_state:
    st.session_state.form_key = 0

# Update the title section to replace speech counter with New Speech Text button
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Speech Generator")
with col2:
    if st.button("New Speech Text", key="new_speech"):
        # Clear the text response container
        text_response_container.empty()
        # Clear all session state
        st.session_state.clear()
        # Increment form key to force input refresh
        st.session_state.form_key = st.session_state.get('form_key', 0) + 1
        st.rerun()

# Add input method selection
input_method = st.radio(
    "Choose input method:",
    ["Enter Topic", "Custom Speech Text", "Upload Document"]
)

# Input section based on selected method
if input_method == "Enter Topic":
    # Use the dynamic key for the text input
    topic = st.text_input(
        "Enter a topic for the speech: ",
        value="",
        key=f"topic_input_{st.session_state.form_key}"
    )
    if st.button("Generate Speech Text"):
        if topic:
            # Increment speech counter
            st.session_state.speech_counter += 1
            
            # First generate and display the title
            title = tittle_chain.invoke({"topic": topic})
            st.subheader("Generated Title:")
            st.write(title)
            
            # Then generate and display the full speech
            st.session_state.text_response = speech_chain.invoke({"title": title})
            text_response_container.write(st.session_state.text_response)

elif input_method == "Custom Speech Text":
    custom_text = st.text_area("Enter your speech text:", height=300)
    if st.button("Use Custom Text"):
        if custom_text:
            st.session_state.text_response = custom_text
            text_response_container.write(st.session_state.text_response)

else:  # Upload Document
    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'pdf', 'docx'])
    if uploaded_file is not None:
        try:
            if uploaded_file.type == "text/plain":
                text_response = uploaded_file.read().decode()
            elif uploaded_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                text_response = ""
                for page in pdf_reader.pages:
                    text_response += page.extract_text()
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = docx.Document(uploaded_file)
                text_response = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            
            text_response_container.write(text_response)
            st.success("Document uploaded and processed successfully!")
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")

# Only show voice options if text has been generated
if st.session_state.text_response:
    # Create columns for voice and model selection
    col1, col2 = st.columns(2)
    
    with col1:
        voice_option = st.selectbox(
            "Select a voice:",
            ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
        )
    
    with col2:
        model_option = st.selectbox(
            "Select quality:",
            ["tts-1", "tts-1-hd"]
        )
    
    # Create a container for the audio player and download button
    audio_container = st.empty()
    download_container = st.empty()
    
    # Add a button to generate speech
    if st.button("Generate Speech Audio"):
        try:
            client = OpenAI(api_key=openai_api_key)
            
            with st.spinner('Generating audio...'):
                # Generate speech using OpenAI TTS
                response = client.audio.speech.create(
                    model=model_option,
                    voice=voice_option,
                    input=st.session_state.text_response
                )
                
                # Save to a temporary file
                speech_file = "speech.mp3"
                response.stream_to_file(speech_file)
                
                # Read the audio file and create a player
                with open(speech_file, "rb") as f:
                    audio_bytes = f.read()
                
                # Display audio controls in a container with a title
                st.subheader("🎧 Listen to Speech")
                audio_container.audio(audio_bytes, format="audio/mp3")
                
                # Add a success message
                st.success("Audio generated successfully! You can play it using the audio player above.")
                
                # Add button to generate new speech
                if st.button("Generate New Speech"):
                    # Clear all containers
                    text_response_container.empty()
                    audio_container.empty()
                    download_container.empty()
                    # Reset the page state
                    st.rerun()
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
