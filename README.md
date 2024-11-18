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

## 🛠️ **Setup Instructions**  

Follow these steps to set up and run the project:  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/your-username/google-sheets-dashboard.git (https://github.com/Programmer-govind/Breakout-AI-Agent-Project.git)   
   ```  

2. **Create a Virtual Environment**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Up Environment Variables**  
   Create a `.env` file in the project directory (details below).  

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

## ✨ **Optional Features**  

### **1. Enhanced Search with AI**  
- Incorporates Groq API for intelligent data parsing and query optimization.  

### **2. Result Visualization**  
- Integrated charts and graphs for better understanding of data trends.  

### **3. Night Mode**  
- Switch between light and dark themes for a comfortable viewing experience.  

---

## ❤️ **Contributing**  
Your feedback and contributions are welcome! Feel free to submit feature suggestions or report bugs to make this project even better.  

---

## 🚀 **Conclusion**  
The Google Sheets Search Dashboard highlights my skills in Python, API integration, and user-centric design. I’m excited about the opportunity to bring such expertise to your team and contribute to meaningful projects! 
