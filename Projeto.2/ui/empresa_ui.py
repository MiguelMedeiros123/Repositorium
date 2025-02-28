import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class ManterEmpresaUI:
    @staticmethod
    def main():
        st.header("Cadastro de empresas")
        listar, inserir, atualizar, excluir, setor = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Mover setor"])

        with listar: ManterEmpresaUI.listar()
        with inserir: ManterEmpresaUI.inserir()
        with atualizar: ManterEmpresaUI.atualizar()
        with excluir: ManterEmpresaUI.excluir()
        with setor: ManterEmpresaUI.mover_setor()
    
    @staticmethod
    def listar():
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
                lcusto.append(e.get_custo_add())

            dic = {"id": lid, "nome" : lnome, "desc": ldesc, "dono": ldono, "fund": lfund, "setores": lsetores, "custo": lcusto}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "desc": "Descição", "dono": "Dono", "fund": "Fundação", "setores": "Nº de setores", "custo": "Custo adicional"}, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informa o nome")
        desc = st.text_input("Informa a descrição")
        dono = st.text_input("Informa o dono")
        fund = st.text_input("Informa a data de fundação (formato dd/mm/aaaa)")
        custo_add = st.text_input("Informa um custo mensal adicional (além dos setores e funcionários)")
        if st.button("Inserir"):
            try:
                view.empresa_inserir(nome, desc, dono, dt.datetime.strptime(fund, "%d/%m/%Y").date(), float(custo_add))
                st.success("Empresa inserida com sucesso.")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        empresas = view.empresa_listar()
        if empresas == []:
            st.write("Não há empresa cadastrada.")
        else:
            e = st.selectbox("Empresa a atualizar", empresas)
            nome = st.text_input("Informa o novo nome", e.get_nome())
            desc = st.text_input("Informa a nova descrição", e.get_desc())
            dono = st.text_input("Informa o novo dono", e.get_dono())
            fund = st.text_input("Informa a nova data de fundação (formato dd/mm/aaaa)", dt.date.strftime(e.get_fund(), "%d/%m/%Y"))
            custo_add = st.text_input("Informa o novo custo mensal adicional (além dos setores e funcionários)", e.get_custo_add())
            if st.button("Atualizar"):
                try:
                    view.empresa_atualizar(e.get_id(), nome, desc, dono, dt.datetime.strptime(fund, "%d/%m/%Y").date(), float(custo_add))
                    st.success("Empresa atualizada com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
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
    def mover_setor():
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