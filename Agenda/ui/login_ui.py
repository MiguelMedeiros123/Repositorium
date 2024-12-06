import streamlit as st
import view

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Informa teu e-mail")
        senha = st.text_input("Informa tua senha", type="password")
        if st.button("Entrar"):
            a = view.autenticar(email, senha)
            if a == None: st.error("E-mail ou senha inválidos.")
            else:
                st.session_state["conta_id"] = a["id"]
                st.session_state["conta_nome"] = a["nome"]
                st.session_state["conta_tipo"] = a["tipo"]
                st.rerun()