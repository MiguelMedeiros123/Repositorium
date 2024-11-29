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
        senha = st.text_input("Informa a tua senha")
        if st.button("Inserir"):
            e = True
            for c in view.cliente_listar():
                if c.email == email: e = False
            if e:
                view.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente inserido.")
                time.sleep(2)
                st.rerun()
            else:
                st.error("Insira um email válido que não está sendo usado.")