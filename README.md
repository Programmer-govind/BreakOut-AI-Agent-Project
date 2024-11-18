# AI Agent Project

📊 **Google Sheets Search Dashboard**  

Welcome to the Google Sheets Search Dashboard! This project harnesses the power of Python, Streamlit, Groq API, and Serp API to provide an intuitive and efficient way to search and analyze data from Google Sheets.

---

## 🌟 **Project Description**  

The **Google Sheets Search Dashboard** simplifies the process of working with large datasets in Google Sheets by providing:  
- **Dynamic Search**: Perform fast, intelligent searches across Google Sheets.  
- **Smart Queries**: Use custom search filters for targeted results.  
- **Interactive Dashboard**: Access and analyze data with a visually appealing interface built using Streamlit.  
- **API Integration**: Seamlessly fetch and display search results using Groq API and Serp API.  

---

### **Project Structure**
![image](https://github.com/user-attachments/assets/9b53604a-74d1-46e6-b017-3a05b2b3e312)



## 🛠️ **Setup Instructions**  

Follow these steps to set up and run the project:  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/Programmer-govind/Breakout-AI-Agent-Project.git
   cd Breakout-AI-Agent-Project
   ```  

2. **Create a Virtual Environment**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: cd venv\Scripts\
   activate 
   ```  

3. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. ### **Setup Environment Variables**

   Follow these steps to securely manage API keys and other sensitive information using a `.env` file:

   #### 1. **Install Required Library**
   Use `python-dotenv` to load environment variables from a `.env` file into your Python application:
   ```bash
   pip install python-dotenv
   ```

   #### 2. **Create a `.env` File**
   In the root directory of the project, create a file named `.env`. Add your API keys and other sensitive configurations inside    the file:
   ```
   SERP_API_KEY=your_serp_api_key
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_SERVICE_ACCOUNT_FILE=credentials.json
   ```

   #### 3. **Use Environment Variables in Your Code**
   In your `app.py` file, load the `.env` file and access the variables using the `os` module:
   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from the .env file
   load_dotenv()

   # Access the variables
   SERP_API_KEY = os.getenv("SERP_API_KEY")
   GROQ_API_KEY = os.getenv("GROQ_API_KEY")
   GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
   ```

---  

5. **Run the Application**  
   ```bash  
   streamlit run app.py  
   ```  

6. **Access the Dashboard**  
   Open your browser and navigate to:  
   ```  
   http://localhost:8501  
   ```  

---

## **Screenshots**
![Dashboard1](https://github.com/user-attachments/assets/150bf236-5647-4945-aa4b-e5ae03ed6e41)
![Sheet-DashBoard](https://github.com/user-attachments/assets/2c80ff7e-b6d1-4c71-9919-37b387d3d534)
![Dashboard2-Function](https://github.com/user-attachments/assets/ee86c1ff-6783-47f5-8f49-3b010c09fc20)
![Sheet-Function2](https://github.com/user-attachments/assets/2b3ee7f6-07c3-48a3-8013-ac12a7b130ea)
![download_results](https://github.com/user-attachments/assets/066372a8-4021-40e6-b582-266834165a10)



## 📖 **Usage Guide**  

### **Connecting Google Sheets**  
1. Authenticate with your Google account if prompted.  
2. Enter the Google Sheet URL or ID in the provided input field.  
3. The dashboard will fetch and display the data in an interactive table.  

### **Setting Up Search Queries**  
- Use the search box to input keywords or structured queries.  
- Apply advanced filters to narrow down the results further.  

### **Features of the Dashboard**  
- **Search History**: Review your previous search queries.  
- **Result Export**: Download filtered data as a CSV file.  
- **Visualization**: Generate quick charts for better insights.  

---

## 🔑 **API Keys and Environment Variables**  

To ensure smooth operation, the following are required:  

1. **Groq API Key**  
   - Sign up and generate your API key from the [Groq website](https://groq.com/).  

2. **Serp API Key**  
   - Obtain your key by creating an account at [Serp API](https://serpapi.com/).  

3. **Environment Variables**  
   Create a `.env` file in the root directory and include the following:  
   ```env  
   GROQ_API_KEY=your-groq-api-key  
   SERP_API_KEY=your-serp-api-key  
   GOOGLE_SHEET_ID=your-google-sheet-id  
   ```  

---
### **Video Walkthrough**

**Category**: Demonstration of AI Agent Functionality  
**Description**: This video provides a quick walkthrough of the **Breakout AI Agent Project**, showcasing the following:
- Uploading CSV files and connecting Google Sheets
- Performing web searches using SERP API
- Query processing via Groq API
- Viewing and downloading structured results in a tabular format

**Video Link**: [Watch the 2-Minute Demo](https://drive.google.com/file/d/12_S-pj2Ss9vYi8DFzA7UsV60cdloxs2O/view?usp=drive_link)

---

## ✨ **Optional Features**  

### **1. Enhanced Search with AI**  
- Incorporates Groq API for intelligent data parsing and query optimization.
### **2. Download Locally**
- Download results in csv format for further processing.
### **3. Night Mode**  
- Switch between light and dark themes for a comfortable viewing experience.
- Dark Mode:
  ![Dark_Theme](https://github.com/user-attachments/assets/2c80df31-ad06-4e61-8607-f3cdeeff5c95)
- Light Mode
  ![Light_Theme](https://github.com/user-attachments/assets/ade386d0-b651-46a7-b62a-549c6ad78a42)

 

---

## ❤️ **Contributing**  
Your feedback and contributions are welcome! Feel free to submit feature suggestions or report bugs to make this project even better.  

---

## 🚀 **Conclusion**  
The Google Sheets Search Dashboard highlights my skills in Python, API integration, and user-centric design. I’m excited about the opportunity to bring such expertise to your team and contribute to meaningful projects! 
