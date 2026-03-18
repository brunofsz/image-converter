import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image
import os

janela = tk.Tk()
janela.title("Conversor de Imagens")
janela.geometry("700x560")
janela.configure(bg="#f4f6f8")
janela.resizable(False, False)

arquivos_selecionados = []


def selecionar_imagens():
    caminhos = filedialog.askopenfilenames(
        title="Selecione as imagens",
        filetypes=[
            ("Arquivos de imagem", "*.png *.jpg *.jpeg *.webp *.bmp"),
            ("Todos os arquivos", "*.*")
        ]
    )

    if caminhos:
        arquivos_selecionados.clear()
        arquivos_selecionados.extend(caminhos)

        lista_arquivos.delete(0, tk.END)

        for caminho in arquivos_selecionados:
            nome_arquivo = os.path.basename(caminho)
            lista_arquivos.insert(tk.END, nome_arquivo)

        status_label.config(
            text=f"{len(arquivos_selecionados)} imagem(ns) selecionada(s)"
        )


def converter_imagens():
    if not arquivos_selecionados:
        status_label.config(text="Nenhuma imagem selecionada")
        messagebox.showwarning("Aviso", "Selecione pelo menos uma imagem.")
        return

    pasta_saida = "output"

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    total = len(arquivos_selecionados)
    convertidas = 0

    barra_progresso["value"] = 0
    barra_progresso["maximum"] = total

    status_label.config(text="Iniciando conversão...")
    janela.update_idletasks()

    for i, caminho in enumerate(arquivos_selecionados, start=1):
        try:
            status_label.config(
                text=f"Convertendo {i}/{total}: {os.path.basename(caminho)}"
            )
            janela.update_idletasks()

            with Image.open(caminho) as imagem:
                if imagem.mode in ("RGBA", "P", "LA"):
                    imagem = imagem.convert("RGB")
                elif imagem.mode != "RGB":
                    imagem = imagem.convert("RGB")

                nome_arquivo = os.path.basename(caminho)
                nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
                novo_caminho = os.path.join(pasta_saida, nome_sem_extensao + ".jpg")

                imagem.save(novo_caminho, "JPEG", quality=95)
                convertidas += 1

        except Exception as erro:
            print(f"Erro em {caminho}: {erro}")

        barra_progresso["value"] = i
        janela.update_idletasks()

    status_label.config(
        text=f"Conversão finalizada! {convertidas} imagem(ns) convertida(s)"
    )

    if convertidas > 0:
        messagebox.showinfo(
            "Sucesso",
            f"Conversão finalizada!\n{convertidas} imagem(ns) convertida(s)."
        )
    else:
        messagebox.showerror("Erro", "Nenhuma imagem foi convertida.")


def abrir_pasta_saida():
    pasta_saida = "output"

    if os.path.exists(pasta_saida):
        os.startfile(pasta_saida)
    else:
        status_label.config(text="A pasta output ainda não foi criada")
        messagebox.showwarning("Aviso", "A pasta output ainda não foi criada.")


titulo = tk.Label(
    janela,
    text="Conversor de Imagens",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8",
    fg="#1f2937"
)
titulo.pack(pady=(20, 10))

subtitulo = tk.Label(
    janela,
    text="Selecione imagens e converta para JPG",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#6b7280"
)
subtitulo.pack(pady=(0, 20))

frame_principal = tk.Frame(janela, bg="#ffffff", bd=1, relief="solid")
frame_principal.pack(padx=30, pady=10, fill="both", expand=True)

frame_botoes = tk.Frame(frame_principal, bg="#ffffff")
frame_botoes.pack(pady=20)

botao_selecionar = tk.Button(
    frame_botoes,
    text="Selecionar Imagens",
    command=selecionar_imagens,
    bg="#2563eb",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2"
)
botao_selecionar.grid(row=0, column=0, padx=10)

botao_converter = tk.Button(
    frame_botoes,
    text="Converter para JPG",
    command=converter_imagens,
    bg="#16a34a",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2"
)
botao_converter.grid(row=0, column=1, padx=10)

botao_abrir_pasta = tk.Button(
    frame_botoes,
    text="Abrir Pasta",
    command=abrir_pasta_saida,
    bg="#374151",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=8,
    relief="flat",
    cursor="hand2"
)
botao_abrir_pasta.grid(row=0, column=2, padx=10)

frame_lista = tk.Frame(frame_principal, bg="#ffffff")
frame_lista.pack(padx=20, pady=10, fill="both", expand=True)

lista_arquivos = tk.Listbox(
    frame_lista,
    width=80,
    height=15,
    font=("Arial", 10),
    bd=0,
    highlightthickness=1,
    highlightbackground="#d1d5db",
    selectbackground="#dbeafe",
    selectforeground="#111827"
)
lista_arquivos.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(
    frame_lista,
    orient="vertical",
    command=lista_arquivos.yview
)
scrollbar.pack(side="right", fill="y")

lista_arquivos.config(yscrollcommand=scrollbar.set)

barra_progresso = ttk.Progressbar(
    frame_principal,
    orient="horizontal",
    length=500,
    mode="determinate"
)
barra_progresso.pack(pady=(10, 5))

status_label = tk.Label(
    frame_principal,
    text="Nenhuma imagem selecionada",
    font=("Arial", 10),
    bg="#ffffff",
    fg="#374151"
)
status_label.pack(pady=(0, 15))

janela.mainloop()