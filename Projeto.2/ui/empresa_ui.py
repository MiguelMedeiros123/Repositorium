import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class ManterEmpresaUI:
    @staticmethod
    def main():
        st.header("Cadastro de funcionários")
        listar, inserir, atualizar, excluir, setor = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Mover setor"])

        with listar: ManterEmpresaUI.Listar()
        with inserir: ManterEmpresaUI.Inserir()
        with atualizar: ManterEmpresaUI.Atualizar()
        with excluir: ManterEmpresaUI.Excluir()
        with setor: ManterEmpresaUI.Setor()
    
    @staticmethod
    def Listar():
        empresas = view.empresa_listar()
        if empresas == []:
            st.write("Não há empresa cadastrada.")
        else:
            lid = []
            lnome = []
            ldesc = []
            ldono = []
            lfund = []
            lsetores = []
            lcusto = []

            for e in empresas:
                lid.append(e.get_id())
                lnome.append(e.get_nome())
                ldesc.append(e.get_desc())
                ldono.append(e.get_dono())
                lfund.append(dt.date.strftime(e.get_fund(), "%d/%m/%Y"))
                lsetores.append(e.get_setores())
                lcusto.append("FAZER!!!")

            dic = {"id": lid, "nome" : lnome, "desc": ldesc, "dono": ldono, "fund": lfund, "setores": lsetores, "custo": lcusto}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "desc": "Descição", "dono": "Dono", "fund": "Fundação", "setores": "Nº de setores", "custo": "Custo"}, hide_index=True)

    @staticmethod
    def Inserir():
        nome = st.text_input("Informa o nome")
        desc = st.text_input("Informa a descrição")
        dono = st.text_input("Informa o dono")
        fund = st.text_input("Informa a data de fundação (formato dd/mm/aaaa)")
        if st.button("Inserir"):
            try:
                view.empresa_inserir(nome, desc, dono, dt.datetime.strptime(fund, "%d/%m/%Y").date())
                st.success("Empresa inserida com sucesso.")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def Atualizar():
        empresas = view.empresa_listar()
        if empresas == []:
            st.write("Não há empresa cadastrada.")
        else:
            e = st.selectbox("Empresa a atualizar", empresas)
            nome = st.text_input("Informa o novo nome")
            desc = st.text_input("Informa a nova descrição")
            dono = st.text_input("Informa o novo dono")
            fund = st.text_input("Informa a nova data de fundação (formato dd/mm/aaaa)")
            if st.button("Atualizar"):
                try:
                    view.empresa_atualizar(e.get_id(), nome, desc, dono, dt.datetime.strptime(fund, "%d/%m/%Y").date())
                    st.success("Empresa atualizada com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def Excluir():
        empresas = view.empresa_listar()
        if empresas == []:
            st.write("Não há empresa cadastrado.")
        else:
            e = st.selectbox("Empresa a excluir", empresas)
            if st.button("Excluir"):
                try:
                    view.empresa_excluir(e.get_id())
                    st.success("Empresa excluída.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def Setor():
        empresas = view.empresa_listar()
        setores = view.setor_listar()
        if empresas == []:
            st.write("Não há empresa cadastrada.")
        else:
            if setores == []:
                st.write("Não há setor cadastrado.")
            else:
                s = st.selectbox("Setor a mover", setores)
                e = st.selectbox("Empresa a mover", empresas)
                if st.button("Mover"):
                    try:
                        view.setor_mover_empresa(e.get_id(), s.get_id())
                        st.success("Setor movido à empresa.")
                        time.sleep(2)
                        st.rerun()
                    except Exception as erro:
                        st.error(erro)