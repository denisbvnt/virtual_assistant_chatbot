# 🤖 Virtual Assistant Chatbot

This is a virtual assistant built with **Python**, featuring an interactive interface using **Streamlit** and support for **Large Language Models (LLMs)**. It performs automated tasks based on dynamically generated prompts from user input.

## 📷 Screenshot
![image](https://github.com/user-attachments/assets/fa7abbcf-2e5e-491b-a6d4-1e5cbe99ff68)

## 📁 Project Structure

- `main.py`: Launches the Streamlit app.
- `models.py`: Loads the LLMs used to generate responses.
- `templates.py`: Contains prompt templates and transforms user input into model-friendly formats.
- `tasks.py`: Implements automated tasks the assistant can perform.
- `requirements.txt`: Lists all project dependencies.

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/denisbvnt/virtual_assistant_chatbot.git
   cd virtual_assistant_chatbot
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run main.py
   ```

4. The app will automatically open in your default browser (usually at `http://localhost:8501`).

## 🧠 Features

- Clean and simple interface with Streamlit
- Language generation powered by LLMs
- Dynamic prompt formatting based on user input
- Execution of custom tasks through natural language commands

## 🛠️ Technologies Used

- **Python** – Core programming language used throughout the project
- **Streamlit** – Lightweight framework for building the interactive web interface
- **LangChain** – Framework for chaining together components to build LLM-powered applications
- **Hugging Face Transformers** – Access to pre-trained LLMs for text generation and understanding
- **LLMs** – Used for natural language understanding and response generation
- Additional libraries and tools are listed in `requirements.txt`
  
## 📄 License

This project is licensed under the [MIT License](LICENSE).
