import streamlit as st
import view
import time

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir conta")

        nome = st.text_input("Informa o teu nome")
        email = st.text_input("Informa o teu e-mail")
        fone = st.text_input("Informa o teu fone")
        senha = st.text_input("Informa a tua senha", type="password")
        confirm = st.text_input("Confirmação da senha", type="password")
        if st.button("Abrir conta"):
            try:
                if len(senha) >= 3:
                    if senha == confirm:
                        view.cliente_inserir(nome, email, fone, senha)
                        st.success("Conta criada com sucesso.")
                        time.sleep(2)
                        st.rerun()
                    else: st.error("A senha e sua confirmação devem ser iguais.")
                else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
            except Exception as erro:
                st.error(erro)