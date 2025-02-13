# ChatbotMarketPlace-ChatBridge

**ChatBridge** is an AI-powered chatbot creation platform that enables users to easily design, deploy, and manage custom chatbots. With advanced retrieval-augmented generation (RAG) capabilities, document embedding, and seamless website integration via an embed script, ChatBridge provides a comprehensive solution for businesses and developers looking to enhance customer engagement.

## Demo Video 🎥

Watch the Demo [here](https://drive.google.com/file/d/1fZN6CdR5oSJ3bji2DC4_3IHk0jXhORID/view?usp=drive_link).

## Features

- **User Authentication:** Secure sign-up and login with email validation.
- **Chatbot Creation:** Build and customize chatbots by configuring company details, domain, industry, and behavior guidelines.
- **Document Upload & Embedding:** Enhance chatbot responses with retrieval-augmented generation by uploading knowledge documents that are processed and embedded.
- **Chat History & Metrics:** View conversation history with metrics such as total conversations, average response time, and total interactions.
- **Embed Script Generator:** Generate an easy-to-integrate embed script for displaying your chatbot as a widget (e.g., in the bottom-right corner) on your website. (Under Develoment)
- **Retrieval-Augmented Generation (RAG):** Leverage LangChain, Chroma, and Redis to retrieve relevant document context and improve chatbot responses.
- **Tracing & Monitoring:** Integrated LangSmith tracing provides detailed monitoring and debugging of AI interactions.
- **Email Integration:** The user will receive the mail regarding the Bot is ready to use.

## Technology Stack

- **Backend:** Python, SQLite, Redis, ChromaDB, LangChain, LangSmith
- **Frontend:** Streamlit
- **AI Models:** ChatGoogleGenerativeAI (Gemini-1.5-flash) and GoogleGenerativeAIEmbeddings
- **Document Processing:** Unstructured, LangChain UnstructuredLoader
- **Deployment:** Local deployment via Streamlit; containerization possible for production environments

## 🏗️ Project Structure

```plaintext
chatbridge/
├── src/
│   ├── app.py                  # Main entry point for the Streamlit app
│   ├── database.py             # SQLite database initialization and file storage setup
│   ├── auth.py                 # User authentication (sign-up, login, account deletion)
│   ├── chatbot.py              # Chatbot creation, retrieval, and deletion functions
│   ├── chat_history.py         # Chat history saving and retrieval functions
│   ├── bot_interaction.py      # Bot interaction logic (LLM chain, RAG integration, LangSmith tracing)
│   ├── document_processor.py   # Document processing and embedding generation (optional)
│   ├── pages.py                # Streamlit pages for login, chatbot creation, dashboard, etc.
│   ├── autogenerated_email.py  # Auto Emal Generation on the creation of the Chatbot
│   ├── metric.py               # Streamlit metrics, Insights of the Chatbot
│   └── logger.py               # Logging configuration
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .env.template               # Environment Variables
```

## 🔧 Installation

### Prerequisites
- **Python 3.8+**

### Setup Instructions

1. **Clone the repository**
    ```sh
   git clone https://github.com/faizrazadec/ChatbotMarketPlace-ChatBridge.git
   cd ChatbotMarketPlace-ChatBridge
   ```

2. **Create a virtual environment**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    ```sh
    cp .env.example .env
    ```

5. **Configure Environment Variables**
    ```env
    GEMINI_API_KEY=''
    REDIS_URL=''
    LANGSMITH_API_KEY=''
    LANGSMITH_PROJECT=''
    LANGSMITH_ENDPOINT=''
    ```

6. **Running the Application**
    ```sh
    streamlit run src/app.py
    ```

## Usage
- **User Authentication:**
    Log in with your username or email. New users can sign up by providing a username, email, and password.

- **Chatbot Creation:**
    After logging in, create a new chatbot by providing the required configuration and optionally uploading knowledge documents. Once created, a confirmation pop-up displays, and you receive an email notification when your chatbot is ready.

- **Chat Dashboard:**
    Select a chatbot from the sidebar to view its conversation history, metrics, and interact with it. ChatBridge supports RAG by retrieving relevant document context to augment chatbot responses.

---

### ⭐ **Support This Project!**  
If you found this useful, **please consider leaving a star ⭐ on GitHub**!  
It motivates me to keep building more **open-source tools** 🚀  

---