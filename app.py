from google.oauth2.service_account import Credentials
import streamlit as st
import pandas as pd
import requests
import time
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# App Title
st.title("AI Agent Dashboard")

# Define Google Sheets Scope
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# API Keys (replace with your keys)
SERP_API_KEY = "your_serp_api_key"
GROQ_API_KEY = "your_groq_api_key"

# Initialize session state variables
if "data" not in st.session_state:
    st.session_state["data"] = None
if "query_template" not in st.session_state:
    st.session_state["query_template"] = ""
if "results" not in st.session_state:
    st.session_state["results"] = []
if "selected_column" not in st.session_state:
    st.session_state["selected_column"] = None
if "selected_values" not in st.session_state:
    st.session_state["selected_values"] = []


# Function to Fetch Google Sheets Data
def fetch_google_sheets_data(sheet_id, sheet_range):
    try:
        # Replace With path to Credentials.json
        creds = Credentials.from_service_account_file(
            r"path/to/Credentials.json"  
        )
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
        values = result.get("values", [])
        if values:
            return pd.DataFrame(values[1:], columns=values[0])
        else:
            st.warning("No data found in the specified range.")
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()


# Function to Upload and Read CSV
def upload_csv():
    st.subheader("Upload a CSV File")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        try:
            return pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")
            return pd.DataFrame()
    return pd.DataFrame()


# Groq API Integration
def groq_request(query, model="llama-3.1-8b-instant"):
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ],
            "stop": ["\n"],
            "max_tokens": 500,
            "temperature": 0.7,
        }
        response = requests.post(
            url="https://api.groq.com/openai/v1/chat/completions",
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        raise Exception(f"Groq API error: {e}")


# Serp API for Context
def serp_api_request(query):
    try:
        url = f"https://serpapi.com/search.json?q={query}&api_key={SERP_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        results = response.json()
        return results.get("organic_results", [])
    except Exception as e:
        st.error(f"Error fetching context from Serp API: {e}")
        return []


# Data Processing Function
def data_processing():
    st.subheader("Data Processing")
    data = st.session_state["data"]

    if data is None or data.empty:
        st.warning("No data to process.")
        return

    # Display data
    st.write("Preview of Data:")
    st.dataframe(data)

    # Select column for processing
    st.session_state["selected_column"] = st.selectbox(
        "Select the column to process", data.columns
    )

    # Multiselect for specific rows
    st.session_state["selected_values"] = st.multiselect(
        "Select specific data from the column (leave blank to process all)",
        data[st.session_state["selected_column"]].unique(),
    )

    # Input query template
    st.session_state["query_template"] = st.text_input(
        "Enter your query template (e.g., 'Find details about {column_value}')",
        value=st.session_state["query_template"],
    )

    # Process Queries
    if st.button("Process Query"):
        query_template = st.session_state["query_template"]
        selected_column = st.session_state["selected_column"]
        selected_values = st.session_state["selected_values"]

        if not query_template or "{column_value}" not in query_template:
            st.error("Query template must include '{column_value}'.")
            return

        results = []
        data_to_process = selected_values if selected_values else data[selected_column]
        for entity in data_to_process:
            # Refine query dynamically
            context = serp_api_request(entity)
            refined_query = (
                f"{query_template.format(column_value=entity)}\nContext: {context}"
            )

            try:
                response_text = groq_request(refined_query)
                results.append({"Entity": entity, "Extracted Info": response_text})
                st.write(f"Extracted Info for {entity}: {response_text}")
            except Exception as e:
                st.error(f"Error processing query for {entity}: {e}")
            time.sleep(1)

        # Save results in session
        st.session_state["results"] = results
        result_df = pd.DataFrame(results)
        st.write("Processed Results:")
        st.dataframe(result_df)

        # Download results as CSV
        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Results as CSV", csv, "results.csv")


# Main App Function
def main():
    st.sidebar.title("Choose Input Method")
    options = st.sidebar.radio(
        "Select Input Type:", ["Upload CSV", "Connect Google Sheets"]
    )

    if options == "Upload CSV":
        st.session_state["data"] = upload_csv()
    else:
        sheet_id = st.text_input("Enter Google Spreadsheet ID:")
        sheet_range = st.text_input("Enter Sheet Range (e.g., Sheet1!A1:D10):")
        if st.button("Fetch Google Sheets Data"):
            st.session_state["data"] = fetch_google_sheets_data(sheet_id, sheet_range)

    if st.session_state["data"] is not None:
        data_processing()


if __name__ == "__main__":
    main()
