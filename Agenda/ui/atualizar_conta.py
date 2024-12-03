import streamlit as st
import view
import time

class AtualizarContaUI:
    @staticmethod
    def main():
        st.header("Atualizar dados da conta")
        senha = st.text_input("Insere sua senha", type="password")
        if st.button("Confirmar senha"):
            cli = view.cliente_listar_id(st.session_state["conta_id"])
            a = view.cliente_autenticar(cli.email, senha)
            if a == None: st.error("Senha incorreta")
            else:
                nome = st.text_input("Informa o novo nome", cli.nome)
                email = st.text_input("Informa o teu e-mail", cli.email)
                fone = st.text_input("Informa o teu fone", cli.fone)
                senha = st.text_input("Informa a tua senha", cli.senha, type="password")
                confirm = st.text_input("Confirmação da senha", type="password")
                if st.button("Atualizar conta"):
                    if email != "": e = True
                    else: e = False
                    for c in view.cliente_listar():
                        if c.email == email: 
                            if c.id != cli.id: e = False
                    if e:
                        if len(senha) >= 3:
                            if senha == confirm:
                                view.cliente_atualizar(cli.id, nome, email, fone, senha)
                                st.success("Conta atualizada com sucesso.")
                                time.sleep(2)
                                st.rerun()
                            else: st.error("A senha e sua confirmação devem ser iguais.")
                        else: st.error("Insere uma senha de, no mínimo, 3 caracteres.")
                    else: st.error("Insere um email válido que não esteja em uso.")