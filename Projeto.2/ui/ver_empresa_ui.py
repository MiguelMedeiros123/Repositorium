import streamlit as st
import pandas as pd
import view
import datetime as dt
import time

class VerEmpresaUI:
    def main():
        st.header("Empresa")
        empresa, listar_setor, listar_func, custos, reajustes, realocamentos = st.tabs(["Empresa", "Setores", "Funcionários", "Custos", "Reajustes", "Realocamentos"])

        with empresa: VerEmpresaUI.empresa()
        with listar_setor: VerEmpresaUI.listar_setor()
        with listar_func: VerEmpresaUI.listar_func()
        with custos: VerEmpresaUI.custos()
        with reajustes: VerEmpresaUI.reajustes()
        with realocamentos: VerEmpresaUI.realocamentos()

    def empresa():
        if st.session_state["conta_nome"] == "admin":
            em = st.selectbox("Escolhe a empresa", view.empresa_listar())
            if st.button("Escolher"):
                st.session_state["empresa_id"] = em.get_id()
                st.rerun()

        if "empresa_id" not in st.session_state: pass
        else:
            e = view.empresa_listar_id(st.session_state["empresa_id"])
            if e == None:
                st.subheader("Indisponível")
                st.write("O administrador deve inserir-te no sistema da empresa.")
            else:
                st.subheader(e.get_nome())
                st.write(f"Dono(a): {e.get_dono()}")
                st.write(e.get_desc())
                st.write(f"Fundada a {dt.date.strftime(e.get_fund(), "%d/%m/%Y")}")
                st.write(f"Custo mensal: {view.empresa_custo(e.get_id())}")

    def listar_setor():
        if "empresa_id" not in st.session_state: st.write("Escolhe a empresa.")
        else:
            e = view.empresa_listar_id(st.session_state["empresa_id"])
            if e == None:
                st.subheader("Indisponível")
                st.write("O administrador deve inserir-te no sistema da empresa.")
            else:
                st.subheader("Setores da empresa")
                setores = view.empresa_setores(e.get_id())
                if setores == []: st.write("Não há setor cadastrado na empresa.")
                else:
                    st.write(f"N.º total: {e.get_setores()} setor(es).")

                    lid = []
                    lnome = []
                    ldesc = []
                    ldata = []
                    lfuncionarios = []
                    lcusto = []
                    for s in setores:
                        lid.append(s.get_id())
                        lnome.append(s.get_nome())
                        ldesc.append(s.get_desc())
                        ldata.append(dt.date.strftime(s.get_data(), "%d/%m/%Y"))
                        lfuncionarios.append(s.get_funcionarios())
                        lcusto.append(view.setor_custo(s.get_id()))

                    dic = {"id": lid, "nome" : lnome, "desc": ldesc, "data": ldata, "funcionarios": lfuncionarios, "custo": lcusto}
                    graph = pd.DataFrame(dic)
                    st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "desc": "Descrição", "data": "Fundação", "funcionarios": "N.º de funcionários", "custo" : "Custo mensal"}, hide_index=True)

    def listar_func():
        if "empresa_id" not in st.session_state: st.write("Escolhe a empresa.")
        else:
            e = view.empresa_listar_id(st.session_state["empresa_id"])
            if e == None:
                st.subheader("Indisponível")
                st.write("O administrador deve inserir-te no sistema da empresa.")
            else:
                st.subheader("Funcionários da empresa")
                setores = view.empresa_setores(e.get_id())
                funcionarios = []
                for s in setores:
                    for f in view.setor_funcionarios(s.get_id()):
                        funcionarios.append(f)
                if funcionarios == []: st.write("Não há funcionários cadastrados na empresa")
                else:
                    st.write(f"N.º total: {len(funcionarios)} funcionário(s).")

                    lid = []
                    lnome = []
                    locup = []
                    lcpf = []
                    lemail = []
                    lcusto = []
                    lcontr = []
                    lsetor = []
                    if st.session_state["conta_nome"] == "admin":
                        for f in funcionarios:
                            lid.append(f.get_id())
                            lnome.append(f.get_nome())
                            locup.append(f.get_ocup())
                            lcpf.append(f.get_cpf())
                            lemail.append(f.get_email()) 
                            lcusto.append(f.get_custo())
                            lcontr.append(dt.date.strftime(f.get_contr(), "%d/%m/%Y"))
                            lsetor.append(s.get_nome())

                        dic = {"id": lid, "nome" : lnome, "ocup": locup, "cpf": lcpf, "email": lemail, "custo": lcusto, "contr": lcontr, "setor": lsetor}
                        graph = pd.DataFrame(dic)
                        st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "ocup": "Ocupação", "cpf": "CPF", "email": "E-Mail", "custo": "Custo", "contr": "Contratação", "setor": "Setor"}, hide_index=True)
                    else:
                        for f in funcionarios:
                            lid.append(f.get_id())
                            lnome.append(f.get_nome())
                            locup.append(f.get_ocup())
                            lemail.append(f.get_email()) 
                            lcontr.append(dt.date.strftime(f.get_contr(), "%d/%m/%Y"))
                            lsetor.append(s.get_nome())

                        dic = {"id": lid, "nome" : lnome, "ocup": locup, "email": lemail, "contr": lcontr, "setor": lsetor}
                        graph = pd.DataFrame(dic)
                        st.dataframe(graph, column_config = {"id": "ID", "nome": "Nome", "ocup": "Ocupação", "email": "E-Mail", "contr": "Contratação", "setor": "Setor"}, hide_index=True)

    def custos():
        pass
    
    def reajustes():
        pass

    def realocamentos():
        pass