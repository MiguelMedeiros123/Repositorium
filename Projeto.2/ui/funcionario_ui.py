import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class ManterFuncionarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de funcionários")
        listar, inserir, atualizar, excluir = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with listar: ManterFuncionarioUI.listar()
        with inserir: ManterFuncionarioUI.inserir()
        with atualizar: ManterFuncionarioUI.atualizar()
        with excluir: ManterFuncionarioUI.excluir()
    
    @staticmethod
    def listar():
        funcionarios = view.funcionario_listar()
        if funcionarios == []:
            st.write("Não há funcionário cadastrado.")
        else:
            lid = []
            lnome = []
            locup = []
            lcpf = []
            lemail = []
            lcusto = []
            lcontr = []
            lsetor = []
            for f in funcionarios:
                lid.append(f.get_id())
                lnome.append(f.get_nome())
                locup.append(f.get_ocup())
                lcpf.append(f.get_cpf())
                lemail.append(f.get_email()) 
                lcusto.append(f.get_custo())
                lcontr.append(dt.date.strftime(f.get_contr(), "%d/%m/%Y"))

                bs = False
                for s in view.setor_listar():
                    if s.get_id() == f.get_id_setor():
                        lsetor.append(s.get_nome())
                        bs = True
                        break
                if bs == False: lsetor.append("Nenhum")

            dic = {"id": lid, "nome" : lnome, "ocup": locup, "cpf": lcpf, "email": lemail, "custo": lcusto, "contr": lcontr, "setor": lsetor}
            graph = pd.DataFrame(dic)
            st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "ocup": "Ocupação", "cpf": "CPF", "email": "E-Mail", "custo": "Custo", "contr": "Contratação", "setor": "Setor"}, hide_index=True)

    @staticmethod
    def inserir():
        nome = st.text_input("Informa o nome")
        ocup = st.text_input("Informa a ocupação")
        cpf = st.text_input("Informa o CPF")
        custo = st.text_input("Informa o custo mensal")
        contr = st.text_input("Informa a data de contratação (formato dd/mm/aaaa)")
        email = st.text_input("Informa o e-mail")
        senha = st.text_input("Informa a senha", type="password")
        confirm = st.text_input("Confirmação da senha", type="password")
        if st.button("Inserir"):
            try:
                if len(senha) >= 3:
                    if senha == confirm:
                        view.funcionario_inserir(nome, senha, ocup, cpf, email, float(custo), dt.datetime.strptime(contr, "%d/%m/%Y").date())
                        st.success("Funcionário inserido com sucesso.")
                        time.sleep(2)
                        st.rerun()
                    else: st.error("A senha e sua confirmação devem ser iguais.")
                else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        funcionarios = view.funcionario_listar()
        if funcionarios == []:
            st.write("Não há funcionário cadastrado.")
        else:
            f = st.selectbox("Funcionário a atualizar", funcionarios)
            nome = st.text_input("Informa o novo nome", f.get_nome())
            ocup = st.text_input("Informa a nova ocupação", f.get_ocup())
            cpf = st.text_input("Informa o novo CPF", f.get_cpf())
            custo = st.text_input("Informa o novo custo mensal", f.get_custo())
            contr = st.text_input("Informa a nova data de contratação (formato dd/mm/aaaa)", dt.date.strftime(f.get_contr(), "%d/%m/%Y"))
            email = st.text_input("Informa o novo e-mail", f.get_email())
            senha = st.text_input("Informa a nova senha", f.get_senha(), type="password")
            confirm = st.text_input("Confirmação da nova senha", type="password")
            if st.button("Atualizar"):
                try:
                    if len(senha) >= 3:
                        if senha == confirm:
                            view.funcionario_atualizar(f.get_id(), nome, senha, ocup, cpf, email, float(custo), dt.datetime.strptime(contr, "%d/%m/%Y"))
                            st.success("Funcionário atualizado com sucesso.")
                            time.sleep(2)
                            st.rerun()
                        else: st.error("A senha e sua confirmação devem ser iguais.")
                    else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                except Exception as erro:
                    st.error(erro)

    @staticmethod
    def excluir():
        funcionarios = view.funcionario_listar()
        if funcionarios == []:
            st.write("Não há funcionário cadastrado.")
        else:
            f = st.selectbox("Funcionário a excluir", funcionarios)
            if st.button("Excluir"):
                try:
                    view.funcionario_excluir(f.get_id())
                    st.success("Funcionário excluído.")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)