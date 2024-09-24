from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Model and Get Responses
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")  # Load the Gemini Pro model
    try:
        response = model.generate_content(question)  # Correct method for generating content
        return response.text  # Accessing the text content properly
    except AttributeError as e:
        return f"Error: {e}. Please check the API documentation for the correct method."
    except TypeError as e:
        return f"Error: {e}. Please check the response format."

# Initialize the Streamlit App
st.set_page_config(page_title="Q&A Demo", page_icon="smiley")

st.header("Gemini LLM Application")

user_input = st.text_input("Input:", key="input")  # Changed input to user_input to avoid name conflict
submit = st.button("Ask Your Question!")

# When Submit is clicked
if submit:
    if user_input:  # Check if there is an input
        response = get_gemini_response(user_input)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please enter a question.")
