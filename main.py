# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="")

st.write("## Capitani'sGPT")

# session_state = memoria do streamlit
if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []

for mensagem in st.session_state["lista_mensagem"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)
     

mensagem_usuariro = st.chat_input("Pergunte alguma coisa")

if mensagem_usuariro:
    #print(mensagem_usuariro) #Para aparecer a mensagem enviada no terminal
    # Mensagem do usuario
    st.chat_message("user").write(mensagem_usuariro)
    mensagem = {"role": "user", "content": mensagem_usuariro}
    st.session_state["lista_mensagem"].append(mensagem)

    resposta_modelo = modelo.chat.completions.create(
        messages = st.session_state["lista_mensagem"],
        model="gpt-4o"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content
   
    # resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)

    





