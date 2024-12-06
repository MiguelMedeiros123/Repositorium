import streamlit as st
import view
import time

class AtualizarContaUI:
    @staticmethod
    def main():
        st.header("Atualizar dados da conta")
        
        if st.session_state["conta_tipo"] == "cliente":
            cli = view.cliente_listar_id(st.session_state["conta_id"])
            if st.session_state["conta_nome"] == "admin":
                senhanova = st.text_input("Informa a nova senha", cli.get_senha(), type="password")
                confirmacao = st.text_input("confirmação da nova senha", type="password") 
                if st.button("Atualizar conta"):
                    try:
                        if len(senhanova) >= 3:
                            if senhanova == confirmacao:
                                view.cliente_atualizar(cli.get_id(), cli.get_nome(), cli.get_email(), cli.get_fone(), senhanova, cli.get_idPerfil())
                                st.success("Conta atualizada com sucesso.")
                                time.sleep(2)
                                st.rerun()
                            else: st.error("A senha e sua confirmação devem ser iguais.")
                        else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                    except Exception as erro:
                        st.error(erro)
            else:
                nome = st.text_input("Informa o novo nome", cli.get_nome())
                email = st.text_input("Informa o novo e-mail", cli.get_email())
                fone = st.text_input("Informa o novo fone", cli.get_fone())
                senhanova = st.text_input("Informa a nova senha", cli.get_senha(), type="password")
                confirmacao = st.text_input("confirmação da nova senha", type="password")            
                if st.button("Atualizar conta"):
                    try:
                        if len(senhanova) >= 3:
                            if senhanova == confirmacao:
                                view.cliente_atualizar(cli.get_id(), nome, email, fone, senhanova, cli.get_idPerfil())
                                st.success("Conta atualizada com sucesso.")
                                time.sleep(2)
                                st.rerun()
                            else: st.error("A senha e sua confirmação devem ser iguais.")
                        else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                    except Exception as erro:
                        st.error(erro)
        
        elif st.session_state["conta_tipo"] == "profissional":
            pro = view.profissional_listar_id(st.session_state["conta_id"])
            nome = st.text_input("Informa o novo nome", pro.get_nome())
            especialidade = st.text_input("Informa a nova especialidade", pro.get_especialidade())
            conselho = st.text_input("Informa o novo conselho", pro.get_conselho())
            email = st.text_input("Informa o novo e-mail", pro.get_email())
            senhanova = st.text_input("Informa a nova senha", pro.get_senha(), type="password")
            confirmacao = st.text_input("confirmação da nova senha", type="password")            
            if st.button("Atualizar conta"):
                try:
                    if len(senhanova) >= 3:
                        if senhanova == confirmacao:
                            view.profissional_atualizar(pro.get_id(), nome, especialidade, conselho, email, senhanova)
                            st.success("Conta atualizada com sucesso.")
                            time.sleep(2)
                            st.rerun()
                        else: st.error("A senha e sua confirmação devem ser iguais.")
                    else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                except Exception as erro:
                    st.error(erro)