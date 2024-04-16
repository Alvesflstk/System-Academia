from importlib.metadata import entry_points
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
from PIL import Image
import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")

# classe main a Home 
class Main:
    def __init__(self,container):
        self.container = container
        self.home()

    def home(self):
        self.banner_image = ctk.CTkImage(dark_image=Image.open('public/images/Main.png'),size=(1106,647))
        self.banner = ctk.CTkLabel(self.container,image=self.banner_image,text="")
        self.banner.place(x=1,y=1)


# classe  de alunos >>>
class crud_membros:
    def __init__(self,container):
        self.container = container
        self.membros_f()
        self.main()

    def membros_f(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def main(self):
        self.button_dados_pessoais = ctk.CTkButton(self.container,text="EDITAR DADOS PESSOAIS",font=('Inria Sans',12,'bold'),fg_color='#ED9F0E',width=150,height=38,corner_radius=10)

        self.button_dados_fisicos = ctk.CTkButton(self.container,text="EDITAR DADOS FÍSICOS",font=('Inria Sans',12,'bold'),fg_color='#ED9F0E',width=150,height=38,corner_radius=10)

        self.button_dados_pessoais.place(x=19,y=127)
        self.button_dados_fisicos.place(x=19,y=193)

        self.frame_membros = ctk.CTkScrollableFrame(self.container,width=880,height=510)
        self.frame_membros.place(x=198,y=96)

# classe para novo registro >>>   
class register:
    def __init__(self,container):
        self.container = container
        self.register_f()
        self.componentes()
        self.imc()
        self.avaliacao_fisica()

    def register_f(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    
    def componentes(self):
        def numero_matricula():
            self.matricula.configure(text='')
            numero = ''.join(str(random.randint(1, 10)) for _ in range(9))
            self.matricula.configure(text=f'{numero}')
        # Frame dados 
        self.container_dados_pessoais = ctk.CTkFrame(self.container,width=329,height=550,border_color="#565252",border_width=4,fg_color='#1a1818')
        self.container_dados_pessoais.place(x=27,y=38)

        self.title_dados = ctk.CTkLabel(self.container_dados_pessoais,text='DADOS PESSOAIS', font=('Inria Sans',24,'bold'))
        self.title_dados.place(x=22,y=22)

        self.entry_name = ctk.CTkEntry(self.container_dados_pessoais,placeholder_text='Nome:',fg_color='#1E1E1E',width=279,height=39,border_color='#2D2A2A',corner_radius=5)
        self.entry_name.place(x=22,y=80)

        self.entry_cpf = ctk.CTkEntry(self.container_dados_pessoais,placeholder_text='CPF:',fg_color='#1E1E1E',width=279,height=39,border_color='#2D2A2A',corner_radius=5)
        self.entry_cpf.place(x=22,y=125)

        self.entry_Endereco = ctk.CTkEntry(self.container_dados_pessoais,placeholder_text='Endereço:',fg_color='#1E1E1E',width=279,height=39,border_color='#2D2A2A',corner_radius=5)

        self.label_matricula_title = ctk.CTkLabel(self.container_dados_pessoais,text='Matrícula:',font=('Inria Sans',16,'bold'))
        self.label_matricula_title.place(x=22,y=220)
        self.entry_Endereco.place(x=22,y=170)

        self.matricula = ctk.CTkLabel(self.container_dados_pessoais,text='',text_color='#ED9F0E',font=('Inria Sans',16,'bold'))
        self.matricula.place(x=128,y=220)

        self.button_gerar = ctk.CTkButton(self.container_dados_pessoais,text='Gerar Matrícula',font=('Inria Sans',16,'bold'),width=152,height=34,fg_color='#000000',hover_color='#ED9F0E',command=numero_matricula)
        self.button_gerar.place(x=22,y=255)

    def imc(self):
        def calcular_imc(event):
            altura =  float(self.entry_altura.get())
            peso = float(self.entry_peso.get())

            altura_metros = altura / 100
            imc = peso / (altura_metros ** 2)
            exat = round(imc,2)
            print(exat)
            self.imc_inicial_calc.configure(text=f'{exat}')

            if exat < 18.5:
                self.status.configure(text="Abaixo do peso")
            elif 18.5 <= exat < 24.9:
                self.status.configure(text="Peso normal")
            elif 25 <= exat < 29.9:
                self.status.configure(text="Sobrepeso")
            elif 30 <= exat < 34.9:
                self.status.configure(text="Obesidade grau 1")
            elif 35 <= exat < 39.9:
                self.status.configure(text="Obesidade grau 2")
            else:
                self.status.configure(text="Obesidade grau 3")


        self.titulo_imc = ctk.CTkLabel(self.container_dados_pessoais,text='IMC',font=('Inria Sans',24,'bold'))
        self.titulo_imc.place(x=22,y=310)

        self.entry_peso = ctk.CTkEntry(self.container_dados_pessoais,placeholder_text='Peso:',fg_color='#1E1E1E',width=279,height=39,border_color='#2D2A2A',corner_radius=5)

        self.entry_altura = ctk.CTkEntry(self.container_dados_pessoais,placeholder_text='Altura (cm):',fg_color='#1E1E1E',width=279,height=39,border_color='#2D2A2A',corner_radius=5)

        self.entry_peso.place(x=22,y=350)
        self.entry_altura.place(x=22,y=396)

        self.imc_inicial = ctk.CTkLabel(self.container_dados_pessoais,text='IMC INICIAL:',font=('Inria Sans',16,'bold'))

        self.imc_inicial.place(x=22,y=440)

        self.imc_inicial_calc = ctk.CTkLabel(self.container_dados_pessoais,text='',text_color='#ED9F0E',font=('Inria Sans',16,'bold'))
        self.imc_inicial_calc.place(x=130,y=440)

        self.status = ctk.CTkLabel(self.container_dados_pessoais,text='',font=('Inria Sans',16,'italic','bold'))
        self.status.place(x=22,y=468)

        self.entry_altura.bind('<KeyRelease>',calcular_imc)

    def avaliacao_fisica(self):
        self.title_av = ctk.CTkLabel(self.container,text='AVALIAÇÃO FÍSICA',font=('Inria Sans',24,'bold'),text_color='#ED9F0E')
        self.title_av.place(x=620,y=23)
        self.img_banner_representacao = ctk.CTkImage(dark_image=Image.open('public/images/path/representacao_humana.png'),size=(332,492))

        self.rp_human = ctk.CTkLabel(self.container,text='',image=self.img_banner_representacao)
        self.rp_human.place(x=550,y=126)

        self.entry_peitoral_medida = ctk.CTkEntry(self.container,placeholder_text='Peitoral',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.entry_ombroD_medida = ctk.CTkEntry(self.container,placeholder_text='Ombro D',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.entry_ombroE_medida = ctk.CTkEntry(self.container,placeholder_text='Ombro E',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.entry_BicepsRelaxado_medida = ctk.CTkEntry(self.container,placeholder_text='Bíceps Relaxado',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.entry_BicepsContraido_medida = ctk.CTkEntry(self.container,placeholder_text='Bíceps Contraido',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')

        self.entry_BicepsRelaxadoE_medida = ctk.CTkEntry(self.container,placeholder_text='Bíceps Relaxado',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.entry_BicepsContraidoE_medida = ctk.CTkEntry(self.container,placeholder_text='Bíceps Contraido',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')

        self.entry_ombroE_medida.place(x=895,y=105)
        self.entry_ombroD_medida.place(x=375,y=105)
        self.entry_peitoral_medida.place(x=600,y=92)
        self.entry_BicepsRelaxado_medida.place(x=370,y=228)
        self.entry_BicepsContraido_medida.place(x=370,y=269)
        self.entry_BicepsContraidoE_medida.place(x=895,y=235)
        self.entry_BicepsRelaxadoE_medida.place(x=895,y=278)


        self.tricepsRelaxadoE_medida = ctk.CTkEntry(self.container,placeholder_text='Tríceps Relaxado',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.tricepsContraidoE_medida = ctk.CTkEntry(self.container,placeholder_text='Tríceps Contraído',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')

        self.tricepsRelaxado_medida = ctk.CTkEntry(self.container,placeholder_text='Tríceps Relaxado',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')
        self.tricepsContraido_medida = ctk.CTkEntry(self.container,placeholder_text='Tríceps Contraído',width=174,height=28,fg_color='#1E1E1E',border_color='#2D2A2A')

        self.tricepsRelaxadoE_medida.place(x=895,y=330)
        self.tricepsContraidoE_medida.place(x=895,y=371)
        self.tricepsRelaxado_medida.place(x=370,y=330)
        self.tricepsContraido_medida.place(x=370,y=369)

        self.coxaD = ctk.CTkEntry(self.container,width=174,height=28,placeholder_text='Coxa D',fg_color='#1E1E1E',border_color='#2D2A2A')
        self.coxaE = ctk.CTkEntry(self.container,width=174,height=28,placeholder_text='Coxa E',fg_color='#1E1E1E',border_color='#2D2A2A')

        self.coxaD.place(x=370,y=435)
        self.coxaE.place(x=895,y=435)

        self.panturrilhaD = ctk.CTkEntry(self.container,width=174,height=28,placeholder_text='Panturrilha D',fg_color='#1E1E1E',border_color='#2D2A2A')
        self.panturrilhaE = ctk.CTkEntry(self.container,width=174,height=28,placeholder_text='Panturrilha E',fg_color='#1E1E1E',border_color='#2D2A2A')

        self.panturrilhaD.place(x=370,y=516)
        self.panturrilhaE.place(x=895,y=516)

        self.finish = ctk.CTkButton(self.container,text='Finalizar', fg_color='#ED9F0E',text_color='#FFFFFF',width=148,height=34,font=('Verdana',14,'bold'))

        self.finish.place(x=940,y=588)

# fichas de treino 
class treino:
    def __init__(self,container):
        self.container = container
        self.treino_f()
        self.window_train()

    def treino_f(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def window_train(self):
        self.title = ctk.CTkLabel(self.container,text='PLANILHA DE TREINOS',font=('Inria Sans',48))
        self.title.place(x=22,y=30)
        self.img_trein = ctk.CTkImage(dark_image=Image.open('public/images/IMG-TREINO.png'),size=(492,482))
        self.banner_focus = ctk.CTkLabel(self.container,image=self.img_trein,text='')
        self.banner_focus.place(x=0,y=136)

        self.button_HM = ctk.CTkButton(self.container,text='HIPERTROFIA MASCULINO',font=('Inria Sans',32),width=457,height=123,fg_color='#000000',corner_radius=10,hover_color='#ED9F0E',command=self.downloadHM)
        self.button_HM.place(x=518,y=153)

        self.button_CS = ctk.CTkButton(self.container,text='CROSFIT',font=('Inria Sans',32),width=265,height=135,fg_color='#000000',corner_radius=10,hover_color='#ED9F0E',command=self.downloadCS)
        self.button_TR = ctk.CTkButton(self.container,text='TERAPÊUTICO',font=('Inria Sans',32),width=265,height=135,fg_color='#000000',corner_radius=10,hover_color='#ED9F0E',command=self.downloadTR)
        self.button_CS.place(x=518,y=289)
        self.button_TR.place(x=518,y=434)

        self.button_HF = ctk.CTkButton(self.container,text='HIPERTROFIA\nFEMININO',font=('Inria Sans',24),width=172,height=280,fg_color='#000000',corner_radius=10,hover_color='#ED9F0E',command=self.downloadHF)
        self.button_HF.place(x=797,y=289)

    def downloadHM(self):
        self.archives('public/archive/Hipertrofia_H.pdf')
    
    def downloadHF(self):
        self.archives('public/archive/Hipertrofia_F.pdf')

    def downloadCS(self):
        self.archives('public/archive/Crosfit.pdf')

    def downloadTR(self):
        self.archives('public/archive/Terapeutico.pdf')

    def archives(self,url):
        self.caminho_do_arquivo = url
        self.local_de_destino = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivos PDF", "*.pdf")])
        if self.local_de_destino:
            shutil.copy(self.caminho_do_arquivo, self.local_de_destino)

# janela vazia sem componetização
class container:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("ACADEMY")
        self.centralizar_janela(self.window)      
        self.container_after()
        self.nav_bar()
        Main(self.container_before)
        self.window.mainloop()

    def centralizar_janela(self,janela):
        self.largura_janela = 1200
        self.altura_janela = 650

        self.largura_tela = janela.winfo_screenwidth()
        self.altura_tela = janela.winfo_screenheight()

        self.x_pos = (self.largura_tela - self.largura_janela) // 2
        self.y_pos = (self.altura_tela - self.altura_janela) // 2

        self.posicao_geometrica = f"{self.largura_janela}x{self.altura_janela}+{self.x_pos}+{self.y_pos}"
        janela.geometry(self.posicao_geometrica)

    def register(self):
        register(self.container_before)

    def treino(self):
        treino(self.container_before)

    def membros(self):
        crud_membros(self.container_before)
    def container_after(self):
        self.container_before = ctk.CTkFrame(self.window,width=1106,height=647,fg_color='#1a1818')
        self.container_before.place(x=92,y=2)

    def nav_bar(self):
        self.frame_nav = ctk.CTkFrame(self.window,width=92,height=648,fg_color='#1A1818')
        self.frame_nav.place(x=0,y=1)

        self.icon_new_photo = ctk.CTkImage(dark_image=Image.open('public/images/path/new.png'),size=(32,32))
        self.icon_list_photo = ctk.CTkImage(dark_image=Image.open('public/images/path/list.png'),size=(32,32))
        self.icon_money_photo = ctk.CTkImage(dark_image=Image.open('public/images/path/money.png'),size=(32,32))
        self.icon_pag_photo = ctk.CTkImage(dark_image=Image.open('public/images/path/wallet.png'),size=(32,32))
        self.icon_config_photo = ctk.CTkImage(dark_image=Image.open('public/images/path/config.png'),size=(32,32))
        self.icon_case_photo = ctk.CTkImage(dark_image=Image.open('public/images/path/case.png'),size=(32,32))

        self.button_case = ctk.CTkButton(self.frame_nav,image=self.icon_case_photo,text='', width=32,height=32,fg_color='#1a1818',hover_color='#ED9F0E',command=self.treino)
        self.button_new = ctk.CTkButton(self.frame_nav,image=self.icon_new_photo,text='', width=32,height=32,fg_color='#1a1818',hover_color='#ED9F0E',command=self.register)
        self.button_list = ctk.CTkButton(self.frame_nav,image=self.icon_list_photo,text='', width=32,height=32,fg_color='#1a1818',hover_color='#ED9F0E',command=self.membros)
        self.button_money = ctk.CTkButton(self.frame_nav,image=self.icon_money_photo,text='', width=32,height=32,fg_color='#1a1818',hover_color='#ED9F0E')
        self.button_pag = ctk.CTkButton(self.frame_nav,image=self.icon_pag_photo,text='', width=32,height=32,fg_color='#1a1818',hover_color='#ED9F0E')
        self.button_config = ctk.CTkButton(self.frame_nav,image=self.icon_config_photo,text='', width=32,height=32,fg_color='#1a1818',hover_color='#ED9F0E')


        self.button_case.place(x=23,y=97)
        self.button_new.place(x=23,y=176)
        self.button_list.place(x=23,y=248)
        self.button_money.place(x=23,y=329)
        self.button_pag.place(x=23,y=401)
        self.button_config.place(x=23,y=473)

if __name__ == '__main__':
    container() 