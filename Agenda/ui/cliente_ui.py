import streamlit as st
import pandas as pd
import view

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterClienteUI.Listar()
        with inserir: ManterClienteUI.Inserir()
        with atualizar: ManterClienteUI.Atualizar()
        with excluir: ManterClienteUI.Excluir()
    
    @staticmethod
    def Listar():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            lid = []
            lnome = []
            lemail = []
            lfone = []
            for c in clientes:
                lid.append(c.id)
                lnome.append(c.nome)
                lemail.append(c.email)
                lfone.append(c.fone) 
            dic = {"id": lid, "nome" : lnome, "email": lemail, "fone": lfone}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "email": "E-Mail", "fone": "Telefone"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        email = st.text_input("Informa o e-mail")
        fone = st.text_input("Informa o fone")
        senha = st.text_input("Informa a senha")
        if st.button("Inserir"):
            view.cliente_inserir(nome, email, fone, senha)
            st.success("Cliente inserido.")
            st.rerun()

    @staticmethod
    def Atualizar():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Cliente a atualizar", clientes)
            nome = st.text_input("Informa o novo nome", c.nome)
            email = st.text_input("Informa o novo e-mail", c.email)
            fone = st.text_input("Informa o novo fone", c.fone)
            senha = st.text_input("Informa a nova senha")
            if st.button("Atualizar"):
                view.cliente_atualizar(c.id, nome, email, fone, senha)
                st.success("Cliente atualizado.")
                st.rerun()

    @staticmethod
    def Excluir():
        clientes = view.cliente_listar()
        if clientes == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Cliente a excluir", clientes)
            if st.button("Excluir"):
                view.cliente_excluir(c.id)
                st.success("Cliente excluído.")
                st.rerun()