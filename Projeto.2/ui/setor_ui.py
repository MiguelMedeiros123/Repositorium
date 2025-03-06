import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class ManterSetorUI:
    @staticmethod
    def main():
        st.header("Cadastro de setores")
        listar, inserir, atualizar, excluir, func = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Mover funcionário"])

        with listar: ManterSetorUI.listar()
        with inserir: ManterSetorUI.inserir()
        with atualizar: ManterSetorUI.atualizar()
        with excluir: ManterSetorUI.excluir()
        with func: ManterSetorUI.mover_func()
    
    @staticmethod
    def listar():
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
                lcusto.append(s.get_custo_add())

                be = False
                for e in view.empresa_listar():
                    if e.get_id() == s.get_id_empresa():
                        lempresa.append(e.get_nome())
                        be = True
                        break
                if be == False: lempresa.append("Nenhuma")

            dic = {"id": lid, "nome" : lnome, "desc": ldesc, "data": ldata, "funcionarios": lfuncionarios, "custo": lcusto, "empresa": lempresa}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "desc": "Descrição", "data": "Fundação", "funcionarios": "Nº de funcionários", "custo" : "Custo adicional", "empresa": "Empresa"}, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informa o nome")
        desc = st.text_input("Informa a descrição")
        data = st.text_input("Informa a data de fundação (formato dd/mm/aaaa)")
        custo_add = st.text_input("Informa um custo mensal adicional (além dos funcionários)")
        if st.button("Inserir"):
            try:
                view.setor_inserir(nome, desc, dt.datetime.strptime(data, "%d/%m/%Y").date(), float(custo_add))
                st.success("Setor inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        setores = view.setor_listar()
        if setores == []:
            st.write("Não há setor cadastrado.")
        else:
            s = st.selectbox("Setor a atualizar", setores)
            nome = st.text_input("Informa o novo nome", s.get_nome())
            desc = st.text_input("Informa a nova descrição", s.get_desc())
            data = st.text_input("Informa a nova data de fundação (formato dd/mm/aaaa)", dt.date.strftime(s.get_data(), "%d/%m/%Y"))
            custo_add = st.text_input("Informa o novo custo mensal adicional (além dos funcionários)", s.get_custo_add())
            if st.button("Atualizar"):
                try:
                    view.setor_atualizar(s.get_id(), nome, desc, dt.datetime.strptime(data, "%d/%m/%Y").date(), float(custo_add))
                    st.success("Setor atualizado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
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

    @staticmethod
    def mover_func():
        setores = ["Nenhum"]
        for se in view.setor_listar(): setores.append(se)
        funcionarios = view.funcionario_listar()
        if setores == ["Nenhum"]:
            st.write("Não há setor cadastrado.")
        else:
            if funcionarios == []:
                st.write("Não há funcionários cadastrados.")
            else:
                f = st.selectbox("Funcionário a mover", funcionarios)
                s = st.selectbox("Setor a mover", setores)
                if st.button("Mover"):
                    try:
                        if s != "Nenhum":
                            view.funcionario_mover_setor(s.get_id(), f.get_id())
                            st.success("Funcionário movido ao setor.")
                        else:
                            view.funcionario_mover_setor(0, f.get_id())
                            st.success("Funcionário removido de setores.")
                        time.sleep(2)
                        st.rerun()
                    except Exception as erro:
                        st.error(erro)