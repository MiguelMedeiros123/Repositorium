import streamlit as st
import pandas as pd
import view

class indexUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar:
            cid = []
            cnome = []
            cemail = []
            cfone = []
            for c in view.cliente_listar():
                cid.append(c.id)
                cnome.append(c.nome)
                cemail.append(c.email)
                cfone.append(c.fone)
            
            dic = {"id": cid, "nome" : cnome, "email": cemail, "fone": cfone}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "id", "nome": "nome", "email": "e-mail", "fone": "fone"}, hide_index=True)

        with inserir:
            nome = st.text_input("Informe o nome")
            email = st.text_input("Informe o e-mail")
            fone = st.text_input("Informe o fone")
            if st.button("Inserir"):
                view.cliente_inserir(nome, email, fone)