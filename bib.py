from tkinter import*

def FORMULARIO_ATIVAR_LEITURA():

	def FUNCAO_ATIVAR_LEITURA():
		total_versiculo_biblico = 31102
		try:
			total_dias_leitura  = 0
			total_dias_leitura = int (text_button_1.get())
			total_1 = ( total_versiculo_biblico ) // total_dias_leitura
		except ZeroDivisionError:
			borda_mostrar_1["text"] = "NÚMERO ZERO NÃO É PERMITIDO. \nESCOLHA DE 1 DIA ATÉ 3285 DIAS. "
		except ValueError:
			borda_mostrar_1["text"] = "CARACTERE NÃO PERMITIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "	
		except KeyboardInterrupt:
			borda_mostrar_1["text"] = "NÃO INFORMOU OS DADOS. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "
		except TypeError:
			borda_mostrar_1["text"] = "DADO É INVÁLIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		else:	
			total_dias_leitura
			if total_dias_leitura > 3285:
					borda_mostrar_1["text"] = "   ACIMA DE 3285 NÃO É VALIDO,\nDIGITE UM NÚMERO VALIDO."

			elif total_dias_leitura < 3285 or total_dias_leitura > 0:
				
					borda_mostrar_1["text"] = "TOTAL AO DIA: %d" %total_1
	top_ativar_leitura = Toplevel()                           ### ATIVADO ATRAVEZ DO BOTAO JANELA PRINCIPAL
	top_ativar_leitura.title("ATIVAR LEITURA")
	top_ativar_leitura.geometry("400x400")
	top_ativar_leitura.configure(background = "#DEB887")      ## cor madeira robusta
	top_ativar_leitura.resizable(False,False)

	label_at_lei_1 = Label(top_ativar_leitura,
					text =  "CALCULO DE VERSICULO POR DIA",
					background = "#00BFFF",                   ## cor deep skyblue
					font = 'Arial 15 bold',                    
					width = 400)                   
	label_at_lei_1.pack(pady = 5)#nenhum command
	
				##################################
	label_button_1= Label(top_ativar_leitura,                                       
				text =       "QUANTIDADE  DE DIAS: ",
				background = "#F0F8FF",                         ## cor ALICE BLUE
				font =       'Arial 10 bold',
				width =       25)
				
	label_button_1.place(y = 50)

	text_button_1 = Entry(top_ativar_leitura)                                             ####entry$$
	text_button_1.place(x = 185,y = 48, width = 40)
	bt_entrada_calculo_1 = Button(top_ativar_leitura,         ####botao
							text = "CALCULAR",
							font = 'Arial 10 bold',            ##cor frente verde limão
							foreground = "#32CD32",
							command = FUNCAO_ATIVAR_LEITURA)
	bt_entrada_calculo_1.place(x = 230, y = 48, width = 90 )
							####################################
	borda_mostrar_1 = Label(top_ativar_leitura,
						text = "ESCOLHA DE 1 DIA ATÉ 3285 DIAS.",
						font = "Arial 10 bold",
						background = "#DEB887")                ## cor madeira robusta
	borda_mostrar_1.place(y = 90)
	

	butoes_para_leitura = Label(top_ativar_leitura,
					text =  "ESCOLHA QUAL É PARA ATIVAR",
					background = "#00BFFF",                   ## cor deep skyblue
					font = 'Arial 15 bold',                    
					width = 400)                   
	butoes_para_leitura.pack(pady = 100)#nenhum command

	top_ativar_leitura.mainloop()


app = Tk()                                                     #janela principal

app.title("LEITURA BIBLICA")
app.geometry("400x500")      #lar x alt
app.configure(background = "#836FFF")                          ##cor slatebue1
app.resizable(False,False)

						###############################################################
label_aap_1 = Label(app,                                        #nome da janela
				text =       "CONFIGURAÇÕES",
				background = "#8A2BE2",                         ## cor blue violet
				font =       'Arial 20 bold',
				width = 400)
label_aap_1.pack()
						###############################################################

btn_app_1 = Button(app, 
				text =       "ATIVAR LEITURA",
				background = "#FAEBD7", foreground = "#32CD32",  ## cor fundo branco antigo |||cor frente verde limão
				font =       'Arial 15 bold',
				width = 20,
				command =     FORMULARIO_ATIVAR_LEITURA)
btn_app_1.pack(pady = 40)


app. mainloop()