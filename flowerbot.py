import streamlit as st
import openai
from PIL import Image
from io import BytesIO
import base64
from openai import OpenAI
import os
import requests

client = OpenAI(
api_key = os.getenv('OPENAI_API_KEY')
)

# Title
st.markdown(
    f"""
    <h1 style="color: white; text-align: center; 
        font-size: 48px; 
        text-shadow: 2px 2px 2px LightBlue;">FloraBot</h1> 
    <hr/>
    """,
    unsafe_allow_html=True,
)

# Function to convert image to base64 (for embedding within prompts)
def img_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/jpeg;base64,{img_str}"

# Sidebar for image upload
with st.sidebar:
    uploaded_file = st.file_uploader("Upload a Flower Image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        img_base64 = img_to_base64(image)

    submit_button = st.button('Search')
        # Prepare the prompt
if submit_button:
    prompt = f"Identify the flower in this image and provide information about its name, species, and other relevant details. {img_base64}"
    response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
        {	
      "role": "user",
      "content": [
      {"type": "text", "text": "Identify the flower in this image and provide information about its name, species, and other relevant details."},
      {	
          "type": "image_url",
          "image_url": {
            "url": f"{img_base64}",
          },
        },
      ],
      }
    ],
      temperature=0.7,
      max_tokens=400,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
  )

    # Display the response
    st.header("About this flower!")
    st.write(response.choices[0].message.content)




