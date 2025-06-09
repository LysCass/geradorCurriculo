import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
from generator import CurriculoGenerator
import os

def criar_interface():
    def gerar_pdf():
        dados = coletar_dados()
        if not dados["nome"]:
            messagebox.showerror("Erro", "O nome é obrigatório!")
            return

        caminho = os.path.join("output", f"curriculo_{dados['nome'].replace(' ', '_')}.pdf")
        gerador = CurriculoGenerator(dados)
        gerador.gerar_curriculo(caminho)

    def visualizar_curriculo():
        dados = coletar_dados()
        if not dados["nome"]:
            messagebox.showerror("Erro", "O nome é obrigatório!")
            return

        visual = Toplevel(root)
        visual.title("Visualização do Currículo")
        visual.geometry("500x600")

        texto = f"""
NOME: {dados['nome']}
EMAIL: {dados['email']}
TELEFONE: {dados['telefone']}

RESUMO:
{dados['resumo']}

FORMAÇÃO:
{dados['formacao']}

EXPERIÊNCIA:
{dados['experiencia']}

HABILIDADES:
{dados['habilidades']}
        """
        tk.Text(visual, wrap="word", height=40, width=60).insert("1.0", texto).pack(padx=10, pady=10)

    def coletar_dados():
        return {
            "nome": nome_var.get(),
            "email": email_var.get(),
            "telefone": telefone_var.get(),
            "resumo": resumo_txt.get("1.0", tk.END).strip(),
            "formacao": formacao_txt.get("1.0", tk.END).strip(),
            "experiencia": experiencia_txt.get("1.0", tk.END).strip(),
            "habilidades": habilidades_txt.get("1.0", tk.END).strip()
        }

    global root
    root = tk.Tk()
    root.title("Gerador de Currículo")
    root.geometry("600x750")

    nome_var = tk.StringVar()
    email_var = tk.StringVar()
    telefone_var = tk.StringVar()

    tk.Label(root, text="Nome:").pack()
    tk.Entry(root, textvariable=nome_var, width=60).pack()

    tk.Label(root, text="E-mail:").pack()
    tk.Entry(root, textvariable=email_var, width=60).pack()

    tk.Label(root, text="Telefone:").pack()
    tk.Entry(root, textvariable=telefone_var, width=60).pack()

    tk.Label(root, text="Resumo Profissional:").pack()
    resumo_txt = tk.Text(root, height=5, width=60)
    resumo_txt.pack()

    tk.Label(root, text="Formação Acadêmica (uma por linha):").pack()
    formacao_txt = tk.Text(root, height=5, width=60)
    formacao_txt.pack()

    tk.Label(root, text="Experiência Profissional (uma por linha):").pack()
    experiencia_txt = tk.Text(root, height=5, width=60)
    experiencia_txt.pack()

    tk.Label(root, text="Habilidades (separadas por vírgula):").pack()
    habilidades_txt = tk.Text(root, height=3, width=60)
    habilidades_txt.pack()

    tk.Button(root, text="Visualizar Currículo", command=visualizar_curriculo, bg="blue", fg="white").pack(pady=5)
    tk.Button(root, text="Gerar Currículo PDF", command=gerar_pdf, bg="green", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    if not os.path.exists("output"):
        os.makedirs("output")
    criar_interface()
