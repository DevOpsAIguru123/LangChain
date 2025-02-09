# LangChain

# Speech Generator

A powerful web application that generates and converts text to speech using LangChain and OpenAI's APIs. This application allows users to generate speeches from topics, input custom text, or upload documents, and then convert them to natural-sounding audio.

## Features

- **Multiple Input Methods:**
  - Generate speeches from topics using AI
  - Input custom speech text
  - Upload and process documents (supports TXT, PDF, and DOCX formats)

- **AI-Powered Speech Generation:**
  - Generates engaging titles for topics
  - Creates 100-word speeches based on titles
  - Uses GPT-4 for high-quality content generation

- **Text-to-Speech Capabilities:**
  - Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)
  - Two quality levels (tts-1, tts-1-hd)
  - Real-time audio generation and playback

## Technologies Used

- **Frontend:** Streamlit
- **AI/ML:**
  - LangChain for orchestrating AI operations
  - OpenAI's GPT-4 for text generation
  - OpenAI's Text-to-Speech API
- **Document Processing:**
  - PyPDF2 for PDF files
  - python-docx for DOCX files

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install required packages:
```bash
pip install streamlit langchain openai pypdf2 python-docx
```

3. Set up your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run speech-agent.py
```

2. Choose your input method:
   - Enter a topic for AI-generated speech
   - Input custom speech text
   - Upload a document

3. If using the AI generation feature:
   - Enter your topic
   - Click "Generate Speech Text"
   - Review the generated title and speech

4. For text-to-speech conversion:
   - Select your preferred voice
   - Choose the quality level
   - Click "Generate Speech Audio"
   - Use the audio player to listen to the generated speech

## License
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Authors
- Vinod Vulavakayala - Initial work, core development

