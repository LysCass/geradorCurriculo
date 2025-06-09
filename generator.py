# generator.py
from fpdf import FPDF
from tkinter import messagebox

class CurriculoGenerator:
    def __init__(self, dados):
        self.dados = dados

    def gerar_curriculo(self, nome_arquivo="curriculo.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Currículo", ln=True, align="C")
        pdf.ln(10)

        # Dados Pessoais
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Dados Pessoais", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Nome: {self.dados.get('nome', '')}", ln=True)
        pdf.cell(0, 10, f"E-mail: {self.dados.get('email', '')}", ln=True)
        pdf.cell(0, 10, f"Telefone: {self.dados.get('telefone', '')}", ln=True)
        pdf.ln(5)

        # Resumo
        if self.dados.get('resumo'):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Resumo Profissional", ln=True)
            pdf.set_font("Arial", '', 12)
            pdf.multi_cell(0, 10, self.dados['resumo'])
            pdf.ln(5)

        # Formação
        if self.dados.get('formacao'):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Formação Acadêmica", ln=True)
            pdf.set_font("Arial", '', 12)
            for item in self.dados['formacao'].splitlines():
                if item.strip():
                    pdf.multi_cell(0, 10, f"- {item.strip()}")
            pdf.ln(5)

        # Experiência
        if self.dados.get('experiencia'):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Experiência Profissional", ln=True)
            pdf.set_font("Arial", '', 12)
            for item in self.dados['experiencia'].splitlines():
                if item.strip():
                    pdf.multi_cell(0, 10, f"- {item.strip()}")
            pdf.ln(5)

        # Habilidades
        if self.dados.get('habilidades'):
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, "Habilidades", ln=True)
            pdf.set_font("Arial", '', 12)
            habilidades = [h.strip() for h in self.dados['habilidades'].split(",")]
            pdf.multi_cell(0, 10, ", ".join(habilidades))
            pdf.ln(5)

        pdf.output(nome_arquivo)
        messagebox.showinfo("Sucesso", f"Currículo salvo como {nome_arquivo}")
