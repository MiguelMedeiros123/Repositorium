import streamlit as st
import pandas as pd
import view

class IndexUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar:
            ManterClienteUI.main(1)

        with inserir:
            ManterClienteUI.main(2)

        with atualizar:
            ManterClienteUI.main(3)

        with excluir:
            ManterClienteUI.main(4)


class ManterClienteUI:
    @staticmethod
    def main(op):
        if op == 1: ManterClienteUI.Listar()
        if op == 2: ManterClienteUI.Inserir()
        if op == 3: ManterClienteUI.Atualizar()
        if op == 4: ManterClienteUI.Excluir()
    
    @staticmethod
    def Listar():
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

    @staticmethod
    def Inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            view.cliente_inserir(nome, email, fone)

    @staticmethod
    def Atualizar():
        c = st.selectbox("Cliente a atualizar", view.cliente_listar())
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        if st.button("Atualizar"):
            view.cliente_atualizar(c.id, nome, email, fone)

    @staticmethod
    def Excluir():
        c = st.selectbox("Cliente a excluir", view.cliente_listar())
        if st.button("Excluir"):
            view.cliente_excluir(c.id)