import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import matplotlib.pyplot as plt
import os


def main():
    load_dotenv()

    st.set_page_config(page_title="🤖 Agente de Análise de Dados CSV")
    st.title("🤖 Agente de Análise de Dados CSV")
    st.markdown(
        """
    <style>
        .response-container {
            overflow-x: auto;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    st.write("Faça perguntas em linguagem natural sobre o seu arquivo CSV.")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("Amostra dos dados carregados:")
            st.dataframe(df.head())

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    if message["role"] == "assistant":
                        st.markdown(
                            f'<div class="response-container">{message["content"]}</div>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(message["content"])
                    if "image" in message:
                        st.image(message["image"])

            prompt = st.chat_input("Qual a sua pergunta?")

            if prompt:
                agent_prefix = """
                Você é um assistente especialista em Análise Exploratória de Dados (E.D.A.) e relatórios em geral.
                Sua função é analisar um arquivo de dados em formato de tabela (CSV) fornecido por um usuário.
                Você deve responder perguntas sobre os dados, identificar padrões [cite: 29], detectar anomalias [cite: 33] e gerar gráficos conforme solicitado[cite: 20].
                Seja preciso, objetivo e claro em suas respostas.
                """
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                llm = ChatGoogleGenerativeAI(
                    model="gemini-2.5-flash",
                    temperature=0,
                    convert_system_message_to_human=True,
                )

                agent = create_pandas_dataframe_agent(
                    llm,
                    df,
                    prefix=agent_prefix,
                    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                    verbose=True,
                    allow_dangerous_code=True,
                )

                instrucao_grafico = (
                    "IMPORTANTE: Se a pergunta exigir a criação de um gráfico, "
                    "gere o código para criar o gráfico com matplotlib ou seaborn e OBRIGATORIAMENTE "
                    "salve o gráfico em um arquivo chamado 'temp_plot.png'. "
                    "Não use plt.show(). Responda com o texto 'Gráfico gerado.' e nada mais."
                )

                with st.spinner("Analisando e gerando resposta..."):
                    response = None
                    try:
                        prompt_final_para_agente = f"""
                            Pense passo a passo. Primeiro, entenda a pergunta do usuário. Em seguida, escreva e execute o código python para respondê-la.
                            Sempre termine sua resposta final com o prefixo 'Final Answer:'.

                            Pergunta do usuário: {prompt}

                            {instrucao_grafico}
                        """
                        input_data = {"input": prompt_final_para_agente}
                        result = agent.invoke(input_data)
                        response = result["output"]

                    except Exception as e:
                        if "Could not parse LLM output:" in str(e):
                            response = (
                                str(e).split("Could not parse LLM output: `")[1].strip()
                            )
                            if response.endswith("`"):
                                response = response[:-1]
                        else:
                            st.error(f"Ocorreu um erro inesperado: {e}")

                    if response:
                        message_data = {"role": "assistant", "content": response}
                        image_path = "temp_plot.png"
                        if "gráfico gerado" in response.lower() and os.path.exists(
                            image_path
                        ):
                            message_data["image"] = image_path

                        st.session_state.messages.append(message_data)

                        st.rerun()

        except Exception as e:
            st.error(f"Erro ao carregar o arquivo: {e}")


if __name__ == "__main__":
    main()
