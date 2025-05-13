import requests
import customtkinter as ctk
from tkinter import messagebox
from dotenv import load_dotenv
import os

# Carregar variável de ambiente
load_dotenv()
chave_api = os.getenv('API_KEY')  # Seu .env deve conter: API_KEY=655152422da656a68cbd7eaf5374f0bf

# Tema
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

# Janela de login
app = ctk.CTk()
app.title('Login')

largura = 400
altura = 300
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()

pos_x = (largura_tela - largura) //2 # canto direito)
pos_y = (altura_tela - altura) //2
app.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')
app.resizable(False, False)


# Widgets de login
ctk.CTkLabel(app, text='Usuário', font=ctk.CTkFont(size=18, weight='bold')).pack(pady=10)

entrada_nome = ctk.CTkEntry(app, placeholder_text='Digite seu nome')
entrada_nome.pack(pady=10)

entrada_nome.bind('<Return>', lambda event: entrada_idade.focus()) # foca na proxima entrada


entrada_idade = ctk.CTkEntry(app, placeholder_text='Digite sua idade')
entrada_idade.pack(pady=10)

entrada_idade.bind('<Return>', lambda event: verificar_login())


def setar_foco():
    app.focus_force()
    entrada_nome.focus()

app.after(200, setar_foco)

# Função para abrir o sistema de temperatura
def abrir_sistema(nome):
    app.destroy()

    sistema = ctk.CTk()
    sistema.title('Temperatura')
    largura = 400
    altura = 150
    largura_tela = sistema.winfo_screenwidth()
    altura_tela = sistema.winfo_screenheight()

    pos_x = (largura_tela - largura) //2 # canto direito
    pos_y = (altura_tela - altura) //2
    sistema.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')
    sistema.resizable(False, False)

    ctk.CTkLabel(sistema, text=f'Olá {nome}! Diga sua cidade.', font=ctk.CTkFont(size=18, weight='bold')).pack(pady=10)
    
    entrada_cidade = ctk.CTkEntry(sistema, placeholder_text='Digite o nome da cidade')
    entrada_cidade.pack(pady=10)

    entrada_cidade.bind('<Return>', lambda event: obter_temperatura())

    def setar_foco():
        sistema.focus_force()
        entrada_cidade.focus()

    sistema.after(200, setar_foco)

    

    def obter_temperatura():
        cidade = entrada_cidade.get()

        if not cidade:
            messagebox.showerror("Erro", "Por favor, digite uma cidade!")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code == 200:
            temperatura = dados['main']['temp']
            descricao = dados['weather'][0]['description']
            messagebox.showinfo("Clima", f"Temperatura em {cidade}: {temperatura}°C, {descricao}\nTenha um ótimo dia {nome}!")
        else:
            messagebox.showerror("Erro", "Cidade não encontrada ou erro na API.")

    ctk.CTkButton(sistema, text='Verificar Temperatura', command=obter_temperatura).pack(pady=20)

    sistema.mainloop()

# Função de login
def verificar_login():
    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if not idade.isdigit():
        messagebox.showerror('Erro', 'Idade precisa ser um número!')
        return

    idade = int(idade)
    if idade < 18:
        messagebox.showwarning('Acesso Negado', f'{nome}, você é menor de idade!')
    else:
        messagebox.showinfo('Bem-vindo', f'Bem-vindo ao sistema, {nome}!')
        abrir_sistema(nome)

# Botão de login
ctk.CTkButton(app, text='Entrar', command=verificar_login).pack(pady=20)

# Iniciar app
app.mainloop()
