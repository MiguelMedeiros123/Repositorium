import streamlit as st
import view
import time
import datetime as dt

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir conta")

        nome = st.text_input("Informa o nome")
        ocup = st.text_input("Informa a ocupação")
        cpf = st.text_input("Informa o cpf")
        email = st.text_input("Informa o e-mail")
        custo = st.text_input("Informa o custo mensal")
        contr = st.text_input("Informa a data de contratação (formato: dd/mm/aaaa)")
        senha = st.text_input("Informa a senha", type="password")
        confirm = st.text_input("Confirmação da senha", type="password")
        if st.button("Abrir conta"):
            try:
                if len(senha) >= 3:
                    if senha == confirm:
                        view.funcionario_inserir(nome, senha, ocup, cpf, email, float(custo), dt.datetime.strptime(contr, "%d/%m/%Y").date())
                        st.success("Conta criada com sucesso.")
                        time.sleep(2)
                        st.rerun()
                    else: st.error("A senha e sua confirmação devem ser iguais.")
                else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
            except Exception as erro:
                st.error(erro)