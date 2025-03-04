import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from tasks import model_response


load_dotenv()

# Streamlit config
st.set_page_config(page_title='Seu assistente virtual 🤖', page_icon='🤖')
st.markdown(
    """
    <style>
    label {
        color: white !important;
        font-weight: bold;
    }
    .stApp {
        background-color: #f2f2f2;
    }
    .stSidebar {
        background-color: #1877F2;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title('Seu assistente virtual 🤖')
st.divider()

model_options = ['OLlama'] # 'HuggingFace', 'OpenAI'
language_options = ['Português', 'Inglês', 'Espanhol']

if "model_name" not in st.session_state:
    st.session_state.model_name = model_options[0]
if "language" not in st.session_state:
    st.session_state.language = language_options[0]

model_name = st.sidebar.selectbox('Modelo', model_options, index=model_options.index(st.session_state.model_name))
language = st.sidebar.selectbox('Idioma', language_options, index=language_options.index(st.session_state.language))

if model_name != st.session_state.model_name or language != st.session_state.language:
    st.session_state.model_name = model_name
    st.session_state.language = language
    st.rerun()


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [AIMessage(content='Olá, sou o seu assistente virtual! Como posso ajudá-lo?')]

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message('AI'):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message('Human'):
            st.write(message.content)

user_query = st.chat_input('Digite sua mensagem aqui...')
if '' != user_query is not None:
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message('Human'):
        st.markdown(user_query)
    with st.chat_message('AI'):
        resp = st.write_stream(model_response(model_name=st.session_state.model_name,
                                              user_query=user_query,
                                              chat_history=st.session_state.chat_history,
                                              language=st.session_state.language))
    st.session_state.chat_history.append(AIMessage(content=resp))