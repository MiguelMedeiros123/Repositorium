import streamlit as st
import view

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Informa teu e-mail")
        senha = st.text_input("Informa tua senha", type="password")
        if st.button("Entrar"):
            c = view.autenticar(email, senha)
            if c == None: st.error("E-mail ou senha inválidos.")
            else:
                st.session_state["conta_id"] = c["id"]
                st.session_state["conta_nome"] = c["nome"]
                st.rerun()