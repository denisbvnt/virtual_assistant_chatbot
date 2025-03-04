from langchain_core.output_parsers import StrOutputParser
from templates import define_prompt_template
from models import load_model


def model_response(model_name, chat_history, user_query, language):
    llm = load_model(model_name)
    prompt_template = define_prompt_template(llm, language)
    chain = prompt_template | llm | StrOutputParser()
    return chain.stream({
        'chat_history': chat_history,
        'input': user_query,
        'language': language
    })