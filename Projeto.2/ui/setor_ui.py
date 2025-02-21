import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class ManterSetorUI:
    @staticmethod
    def main():
        st.header("Cadastro de setores")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterSetorUI.Listar()
        with inserir: ManterSetorUI.Inserir()
        with atualizar: ManterSetorUI.Atualizar()
        with excluir: ManterSetorUI.Excluir()
    
    @staticmethod
    def Listar():
        setores = view.setor_listar()
        if setores == []:
            st.write("Não há setor cadastrado.")
        else:
            lid = []
            lnome = []
            ldesc = []
            ldata = []
            lfuncionarios = []
            lcusto = []
            lempresa = []
            for s in setores:
                lid.append(s.get_id())
                lnome.append(s.get_nome())
                ldesc.append(s.get_desc())
                ldata.append(dt.date.strftime(s.get_data(), "%d/%m/%Y"))
                lfuncionarios.append(s.get_funcionarios())
                lcusto.append("FAZER!!!")

                be = False
                for e in view.empresa_listar():
                    if e.get_id() == s.get_id_empresa():
                        lempresa.append(e.get_nome())
                        be = True
                        break
                if be == False: lempresa.append("Nenhuma")

            dic = {"id": lid, "nome" : lnome, "desc": ldesc, "data": ldata, "funcionarios": lfuncionarios, "custo": lcusto, "empresa": lempresa}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "desc": "Descrição", "data": "Fundação", "funcionarios": "Nº de funcionários", "custo" : "Custo", "empresa": "Empresa"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        desc = st.text_input("Informa a descrição")
        data = st.text_input("Informa a data de fundação (formato dd/mm/aaaa)")
        if st.button("Inserir"):
            try:
                view.setor_inserir(nome, desc, dt.datetime.strptime(data, "%d/%m/%Y").date())
                st.success("Setor inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def Atualizar():
        setores = view.setor_listar()
        if setores == []:
            st.write("Não há setor cadastrado.")
        else:
            s = st.selectbox("Setor a atualizar", setores)
            nome = st.text_input("Informa o novo nome")
            desc = st.text_input("Informa a nova descrição")
            data = st.text_input("Informa a nova data de fundação (formato dd/mm/aaaa)")
            if st.button("Atualizar"):
                try:
                    view.setor_atualizar(s.get_id(), nome, desc, dt.datetime.strptime(data, "%d/%m/%Y").date())
                    st.success("Setor atualizado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def Excluir():
        setores = view.setor_listar()
        if setores == []:
            st.write("Não há setor cadastrado.")
        else:
            s = st.selectbox("Setor a excluir", setores)
            if st.button("Excluir"):
                try:
                    view.setor_excluir(s.get_id())
                    st.success("Setor excluído.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)