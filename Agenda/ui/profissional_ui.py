import streamlit as st
import pandas as pd
import view
import time

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de profissionais")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterProfissionalUI.Listar()
        with inserir: ManterProfissionalUI.Inserir()
        with atualizar: ManterProfissionalUI.Atualizar()
        with excluir: ManterProfissionalUI.Excluir()
    
    @staticmethod
    def Listar():
        profissionais = view.profissional_listar()
        if profissionais == []:
            st.write("Não há profissional cadastrado.")
        else:
            lid = []
            lnome = []
            lespecialidade = []
            lconselho = []
            lemail = []
            for p in profissionais:
                lid.append(p.get_id())
                lnome.append(p.get_nome())
                lespecialidade.append(p.get_especialidade())
                lconselho.append(p.get_conselho())
                lemail.append(p.get_email()) 
            dic = {"id": lid, "nome" : lnome, "especialidade": lespecialidade, "conselho": lconselho, "email": lemail}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "especialidade": "Especialidade", "conselho": "Conselho", "email": "E-Mail"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        especialidade = st.text_input("Informa a especialidade")
        conselho = st.text_input("Informa o conselho")
        email = st.text_input("Informa o e-mail")
        senha = st.text_input("Informa a senha", type="password")
        confirm = st.text_input("Confirmação da senha", type="password")
        if st.button("Inserir"):
            try:
                if len(senha) >= 3:
                    if senha == confirm:
                        view.profissional_inserir(nome, especialidade, conselho, email, senha)
                        st.success("Profissional inserido com sucesso.")
                        time.sleep(2)
                        st.rerun()
                    else: st.error("A senha e sua confirmação devem ser iguais.")
                else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def Atualizar():
        profissionais = view.profissional_listar()
        if profissionais == []:
            st.write("Não há cliente cadastrado.")
        else:
            p = st.selectbox("Cliente a atualizar", profissionais)
            nome = st.text_input("Informa o novo nome", p.get_nome())
            especialidade = st.text_input("Informa a nova especialidade", p.get_especialidade())
            conselho = st.text_input("Informa o novo conselho", p.get_conselho())
            email = st.text_input("Informa o novo e-mail", p.get_email())
            senha = st.text_input("Informa a nova senha", p.get_senha(), type="password")
            confirm = st.text_input("Confirmação da nova senha", type="password")
            if st.button("Atualizar"):
                try:
                    if len(senha) >= 3:
                        if senha == confirm:
                            view.profissional_atualizar(p.get_id(), nome, especialidade, conselho, email, senha)
                            st.success("Profissional atualizado com sucesso.")
                            time.sleep(2)
                            st.rerun()
                        else: st.error("A senha e sua confirmação devem ser iguais.")
                    else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def Excluir():
        profissionais = view.profissional_listar()
        if profissionais == []:
            st.write("Não há cliente cadastrado.")
        else:
            c = st.selectbox("Profissional a excluir", profissionais)
            if st.button("Excluir"):
                try:
                    view.profissional_excluir(c.get_id())
                    st.success("Profissional excluído.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)