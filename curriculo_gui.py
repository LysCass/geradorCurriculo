import tkinter as tk
from tkinter import filedialog, messagebox
from generator import CurriculoGenerator
import json

# Função para coletar dados da interface
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

# Função para gerar o PDF
def gerar_pdf():
    dados = coletar_dados()
    gerador = CurriculoGenerator(dados)
    gerador.gerar_curriculo()

# Função para visualizar o conteúdo antes de gerar
def visualizar_curriculo():
    dados = coletar_dados()

    visual = tk.Toplevel()
    visual.title("Visualização do Currículo")

    texto = f"""Nome: {dados['nome']}
E-mail: {dados['email']}
Telefone: {dados['telefone']}

Resumo Profissional:
{dados['resumo']}

Formação Acadêmica:
{dados['formacao']}

Experiência Profissional:
{dados['experiencia']}

Habilidades:
{dados['habilidades']}"""

    # CORRIGIDO: separar criação do Text, inserção e pack
    text_box = tk.Text(visual, wrap="word", height=40, width=60)
    text_box.insert("1.0", texto)
    text_box.pack(padx=10, pady=10)

# Função para carregar modelo JSON
def carregar_template():
    caminho = filedialog.askopenfilename(title="Selecione um modelo", filetypes=[("JSON files", "*.json")])
    if not caminho:
        return

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    nome_var.set(dados.get("nome", ""))
    email_var.set(dados.get("email", ""))
    telefone_var.set(dados.get("telefone", ""))
    resumo_txt.delete("1.0", tk.END)
    resumo_txt.insert(tk.END, dados.get("resumo", ""))
    formacao_txt.delete("1.0", tk.END)
    formacao_txt.insert(tk.END, dados.get("formacao", ""))
    experiencia_txt.delete("1.0", tk.END)
    experiencia_txt.insert(tk.END, dados.get("experiencia", ""))
    habilidades_txt.delete("1.0", tk.END)
    habilidades_txt.insert(tk.END, dados.get("habilidades", ""))

# Interface Gráfica
root = tk.Tk()
root.title("Gerador de Currículo")

# Variáveis
nome_var = tk.StringVar()
email_var = tk.StringVar()
telefone_var = tk.StringVar()

# Layout
tk.Label(root, text="Nome:").pack()
tk.Entry(root, textvariable=nome_var).pack(fill="x", padx=10)

tk.Label(root, text="E-mail:").pack()
tk.Entry(root, textvariable=email_var).pack(fill="x", padx=10)

tk.Label(root, text="Telefone:").pack()
tk.Entry(root, textvariable=telefone_var).pack(fill="x", padx=10)

tk.Label(root, text="Resumo Profissional:").pack()
resumo_txt = tk.Text(root, height=3)
resumo_txt.pack(fill="both", padx=10)

tk.Label(root, text="Formação Acadêmica (uma por linha):").pack()
formacao_txt = tk.Text(root, height=3)
formacao_txt.pack(fill="both", padx=10)

tk.Label(root, text="Experiência Profissional (uma por linha):").pack()
experiencia_txt = tk.Text(root, height=3)
experiencia_txt.pack(fill="both", padx=10)

tk.Label(root, text="Habilidades (separadas por vírgula):").pack()
habilidades_txt = tk.Text(root, height=2)
habilidades_txt.pack(fill="both", padx=10)

# Botões
tk.Button(root, text="Carregar Modelo JSON", command=carregar_template, bg="gray", fg="white").pack(pady=5)
tk.Button(root, text="Visualizar Currículo", command=visualizar_curriculo, bg="blue", fg="white").pack(pady=5)
tk.Button(root, text="Gerar Currículo PDF", command=gerar_pdf, bg="green", fg="white").pack(pady=5)

# Iniciar aplicação
root.mainloop()
