from tkinter import*
import sqlite3
from sqlite3 import Error


##############################################VARIAVEIS GLOBAIS##################

bib             = 31102                      #QUANTIDADE DE VERSICULO BIBLICO
qt_dias_ativar  = 0                          # iniciar variavel
qt_dias_max     = 3285                       # ativar maximo de dias de leitura
qt_dias_min     = 0                          # dias minimo para ser ativado
############################cores
madeira_robusta = "#DEB887"
verde_limao     = "#32CD32"
alice_blue      = "#F0F8FF"
deep_skyblue    = "#00BFFF"
branco_antigo   = "#FAEBD7"
blue_violet     = "#8A2BE2"
slate_bue_1     = "#836FFF"
									#################janela ativar leitura 1 - pai- janela ativar leitura#######
def ATIVAR_LEITURA_1_db():

	def FUNCAO_CRIACAO_DE_DADOS():

		
		total_vers_bib = bib
		
		try:
			total_dias_lei = qt_dias_ativar 
			total_dias_lei = int(text_1.get())

			ttl_1          = (total_vers_bib) // total_dias_lei
			ttl_x          = total_vers_bib   %  total_dias_lei

		except ZeroDivisionError:
			borda_1["text"] = "NÚMERO ZERO NÃO É PERMITIDO. \nESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except ValueError:
			borda_1["text"] = "CARACTERE NÃO PERMITIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except KeyboardInterrupt:
			borda_1["text"] = "NÃO INFORMOU OS DADOS. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except TypeError:
			borda_1["text"] = "DADO É INVÁLIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		else:	
			total_dias_lei

			if   total_dias_lei > qt_dias_max:
					borda_1["text"] = "   ACIMA DE 3285 NÃO É VALIDO,\nDIGITE UM NÚMERO VALIDO."

			elif total_dias_lei < qt_dias_max or total_dias_lei > qt_dias_min:
					#borda_1["text"] = "QUANTIDADE POR DIA: {}\nRESTANTE DA LEITURA: {}". format(ttl_1,ttl_x)
					
					banco = sqlite3.connect('app_banco.db')                                                       #conectar ao banco de dados
					curso = banco.cursor()                                                                        # processo de banco

					                                                                             
					
					inserir = "INSERT INTO  ativar_leitura ( leitura_dia, leitura_final, qt_dias) VALUES (?,?,?)"  # campos da tabela, valores a ser inserido
					sql_data = (ttl_1, ttl_x, total_dias_lei)                                                      # variaveis das funções de calculo

					curso.execute(inserir, sql_data)                                                               # execução da chamada das funções
					
					banco.commit()  

					
					def MOSTRAR_DATA():
						sql_visual = 'SELECT *FROM ativar_leitura where id_ativar_leitura = "1" '
						curso.execute(sql_visual)
						cf         =  curso.fetchone()
						
						borda_1["text"] = "  QUANTIDADE DIA:         {}\nQUANTIDADE FINAL:     {}\nQUANTIDADE DE DIAS: {}".format(cf[1],cf[2],cf[3])

					MOSTRAR_DATA()  
					                                                                         #salvar  no  banco
					banco.close()                                                            #sair do banco
	def REINICIAR():
		banco_reiniciar = sqlite3.connect('app_banco.db')
		cs_db = banco_reiniciar.cursor()
		sql_rein = 'UPDATE ativar_leitura SET leitura_dia = NULL WHERE id_ativar_leitura = "1"'
		cs_db.execute(sql_rein)
		cs_db.commit()
		cs_db.close()


	top_ativar_leitura_BD_1 = Toplevel()                                     ####top level
	top_ativar_leitura_BD_1.title        ("ATIVAR LEITURA 1")
	top_ativar_leitura_BD_1.geometry     ("400x200")                         #lar x alt
	top_ativar_leitura_BD_1.configure    (background = madeira_robusta)       
	top_ativar_leitura_BD_1.resizable    (False,False)

	lab_1= Label(top_ativar_leitura_BD_1,                                     ###label - fixa
				text         =  "QUANTIDADE  DE DIAS: ",
				background   =  alice_blue,                        
				font         =  'Arial 10 bold',
				width        =  25)
				
	lab_1.place(y = 20)

	text_1 = Entry(top_ativar_leitura_BD_1)                                   ###entry++
	text_1.place(x = 185,
		y = 18, 
		width = 40)
	
	bt_entrada_1 = Button(top_ativar_leitura_BD_1,                            ###botao - função(função_criação de dados)
							text        =  "SALVAR",
							font        =  'Arial 10 bold',           
							foreground  =  verde_limao,
							command     =  FUNCAO_CRIACAO_DE_DADOS)
							
	bt_entrada_1.place(x = 230, y = 18, width = 90 )


	borda_1 = Label(top_ativar_leitura_BD_1,                                 ###labe1 --
						text        =  "ESCOLHA DE 1 DIA ATÉ 3285 DIAS.",
						font        =  "Arial 10 bold",
						background  =  madeira_robusta)                
	borda_1.place(y = 65)

	"""borda_1_a = Label(top_ativar_leitura_BD_1,
				text        = "ESTADO DO BANCO",
				font        = "Arial 10 bold",
				background  = madeira_robusta)
	borda_1_a.place(y = 130)"""


	def ESTADO_REINICIAR():
		"""def deslogar bt_reiniciar"""

		est_rein     = "disabled"
		
		try:
			banco_rei    = sqlite3. connect('app_banco.db')
			cur_rei      = banco_rei.cursor()

		#def INS_DATA():
			#cur_rei.execute("INSERT INTO ativar_leitura( leitura_dia, leitura_final, qt_dias) VALUES (1, 1, 1)")


			sql_rei_data = 'SELECT *FROM ativar_leitura where id_ativar_leitura = "1" '
			cur_rei.execute(sql_rei_data)
			cfc          = cur_rei.fetchone()

			if cfc[0] == 1:
				est_rein = "normal"
		
		
			banco_rei.close()

		except TypeError:
			

		else:
			BT_reiniciar = Button(top_ativar_leitura_BD_1,                           ###botao - função()
							text        = 	"REINICIAR LEITURA",
							font        =   'Arial 10 bold',            
							foreground  =  verde_limao,
							state       = est_rein,
							command     = REINICIAR )
			BT_reiniciar.place(x = 230, y = 120, width = 150 )
	ESTADO_REINICIAR()


	"""BT_apagar = Button(top_ativar_leitura_BD_1,                              ###botao - função()
							text        = 	"APAGAR LEITURA",
							font        =  'Arial 10 bold',            
							foreground  =  verde_limao,
							state       = DISABLED)
	BT_apagar.place(x = 10, y = 120, width = 150 )"""

############################
	top_ativar_leitura_BD_1.mainloop()                           #*************************FIM****************************

	                                     #######################janela ativar leitura - pai- janela principal##################

def FORMULARIO_ATIVAR_LEITURA():

	def CRIAR_TABELA():
		banco_1_1_TOP = sqlite3.connect('app_banco.db')                       #conectar ao banco de dados
		curso = banco_1_1_TOP.cursor()
		def EXECUTAR_CRIAR_TABELA():
			banco_1_1_TOP.execute('CREATE TABLE IF NOT EXISTS ativar_leitura (id_ativar_leitura integer NOT NULL PRIMARY KEY , \
											leitura_dia   integer  NULL, \
											leitura_final integer  NULL, \
											qt_dias       integer  NULL )')     #existe tabela, se nao tiver cria
		EXECUTAR_CRIAR_TABELA()
		banco_1_1_TOP.commit()
		banco_1_1_TOP.close()
	CRIAR_TABELA()                                                              # chamar tabela                             
	def FUNCAO_ATIVAR_LEITURA():                                                ####funçao
		total_versiculo_biblico = bib

		try:
			total_dias_leitura  = qt_dias_ativar
			total_dias_leitura  = int (text_button_1.get())

			total_1             = ( total_versiculo_biblico ) // total_dias_leitura

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

			if   total_dias_leitura > qt_dias_max:                                   
					borda_mostrar_1["text"] = "   ACIMA DE 3285 NÃO É VALIDO,\nDIGITE UM NÚMERO VALIDO."            

			elif total_dias_leitura < qt_dias_max or total_dias_leitura > qt_dias_min:
					borda_mostrar_1["text"] = "TOTAL AO DIA: %d" %total_1    ###printar

	top_ativar_leitura = Toplevel()                                        #### ATIVADO ATRAVEZ DO BOTAO JANELA PRINCIPAL
	top_ativar_leitura.title       ("ATIVAR LEITURA")
	top_ativar_leitura.geometry    ("400x400")                             #lar x alt
	top_ativar_leitura.configure   (background = madeira_robusta)      
	top_ativar_leitura.resizable   (False,False)

	label_at_lei_1 = Label(top_ativar_leitura,                              ###label-expandida
					text        =  "CALCULO DE VERSICULO POR DIA",
					background  =  deep_skyblue,                   
					font        =  'Arial 15 bold',                    
					width       =   400)                   
	label_at_lei_1.pack(pady = 5)
	
				
	label_button_1= Label(top_ativar_leitura,                                ###label - fixa                                  
				text        =  "QUANTIDADE  DE DIAS: ",
				background  =  alice_blue,                         
				font        =  'Arial 10 bold',
				width       =  25)
				
	label_button_1.place(y = 50)

	text_button_1 = Entry(top_ativar_leitura)                              ###entry++
	text_button_1.place(x = 185,
				y = 48, 
				width = 40)

	bt_entrada_calculo_1 = Button(top_ativar_leitura,                      ###botao - função( função ativar leitura)
							text        = 	"CALCULAR",
							font        =  'Arial 10 bold',            
							foreground  =   verde_limao,
							command     =   FUNCAO_ATIVAR_LEITURA)
	bt_entrada_calculo_1.place(x = 230, y = 48, width = 90 )
							
	borda_mostrar_1 = Label(top_ativar_leitura,                            ###label-movel--
						text        =  "ESCOLHA DE 1 DIA ATÉ 3285 DIAS.",
						font        =  "Arial 10 bold",
						background  =  madeira_robusta)               
	borda_mostrar_1.place(y = 90)
	
	butoes_para_leitura = Label(top_ativar_leitura,                        ###label-expandida
					text        =  "ESCOLHA QUAL É PARA ATIVAR",
					background  =  deep_skyblue,                   
					font        =  'Arial 15 bold',                    
					width       =  400)                   
	butoes_para_leitura.pack(pady = 100)

	
	
	botao_leitura_1_db  = Button(top_ativar_leitura,                        ###botao - função(ativar leitura 1 db)
					text        =  "ATIVAR LEITURA 1",
					background  =  branco_antigo, foreground = verde_limao,  
					font        =  'Arial 15 bold',
					width       = 	20,
					command     =   ATIVAR_LEITURA_1_db)
	botao_leitura_1_db.place(x= 70, y = 180)
	
#######################
	top_ativar_leitura.mainloop()                           #********************FIM************************


app = Tk()                                                      #########janela principal####################                        
app.title      ("LEITURA BIBLICA")                              ####tela principal-menus
app.geometry   ("400x500")                                      #lar x alt
app.configure  (background = slate_bue_1)                          
app.resizable  (False,False)

						
label_aap_1 = Label(app,                                        ###label - expandida
				text       =  "CONFIGURAÇÕES",
				background =  blue_violet,                         
				font       =  'Arial 20 bold',
				width      =  400)
label_aap_1.pack()
						

btn_app_1   = Button(app,                                       ###botao - funçao (formulario ativar leitura)
				text       =  "ATIVAR LEITURA",
				background =  branco_antigo, foreground = verde_limao,   
				font       =  'Arial 15 bold',
				width      =  20,
				command    =  FORMULARIO_ATIVAR_LEITURA)
btn_app_1.pack(pady = 40)

####
app. mainloop()                                                  ###**********FIM***********************
