import streamlit as st
import pandas as pd
import view
import time

class ManterPerfilUI:
    def main():
        st.header("Cadastro de perfis")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterPerfilUI.Listar()
        with inserir: ManterPerfilUI.Inserir()
        with atualizar: ManterPerfilUI.Atualizar()
        with excluir: ManterPerfilUI.Excluir()
    
    @staticmethod
    def Listar():
        perfis = view.perfil_listar()
        if perfis == []:
            st.write("Não há serviço cadastrado.")
        else:
            lid = []
            lnome = []
            ldescricao = []
            lbeneficios = []
            for p in perfis:
                lid.append(p.get_id())
                lnome.append(p.get_nome())
                ldescricao.append(p.get_descricao())
                lbeneficios.append(p.get_beneficios())
            dic = {"id": lid, "nome" : lnome, "descricao": ldescricao, "beneficios": lbeneficios}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "descricao": "Descrição", "beneficios": "Benefícios"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        descricao = st.text_input("Informa a descrição")
        beneficios = st.text_input("Informa os benefícios")
        if st.button("Inserir"):
            try:
                view.perfil_inserir(nome, descricao, beneficios)
                st.success("Serviço inserido.")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def Atualizar():
        perfis = view.perfil_listar()
        if perfis == []:
            st.write("Não há perfil cadastrado.")
        else:
            p = st.selectbox("Perfil a atualizar", perfis)
            nome = st.text_input("Informa o nome", p.get_nome())
            descricao = st.text_input("Informa a descrição", p.get_descricao())
            beneficios = st.text_input("Informa os benefícios", p.get_beneficios())
            if st.button("Atualizar"):
                try:
                    view.perfil_atualizar(p.get_id(), nome, descricao, beneficios)
                    st.success("Perfil atualizado.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def Excluir():
        perfis = view.perfil_listar()
        if perfis == []:
            st.write("Não há perfil cadastrado.")
        else:
            p = st.selectbox("Perfil a excluir", perfis)
            if st.button("Excluir"):
                try: 
                    view.perfil_excluir(p.get_id())
                    st.success("Perfil excluído.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)