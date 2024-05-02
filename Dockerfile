# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .
# Install Python dependencies
RUN pip install --no-cache-dir streamlit audio_recorder_streamlit streamlit_float openai langchain langchain-pinecone langchain-openai

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip install python-dotenv

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Expose the port on which Streamlit will run (default: 8501)
EXPOSE 8501
