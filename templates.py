from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def define_prompt_template(model, language):
    system_prompt = "Você é um assistente prestativo e está respondendo perguntas gerais. Responda única e exclusivamente na linguagem {language}."
    if 'huggingface' in str(model.__class__).lower():
        user_prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n{input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    else:
        user_prompt = "{input}"
    
    prompt_template = ChatPromptTemplate.from_messages([("system", system_prompt),
                                                        MessagesPlaceholder(variable_name='chat_history'),
                                                        ("user", user_prompt)])
    return prompt_template