from tkinter import*
import sqlite3
from sqlite3 import Error

##python3.9 tes.py
##############################################VARIAVEIS GLOBAIS##################

bib             = 31102                      #QUANTIDADE DE VERSICULO BIBLICO
qt_dias_ativar  = 0                          # iniciar variavel
qt_dias_max     = 3285                       # ativar maximo de dias de leitura
qt_dias_min     = 0                          # dias minimo para ser ativado

###############################################cores
madeira_robusta = "#DEB887"
verde_limao     = "#32CD32"
alice_blue      = "#F0F8FF"
deep_skyblue    = "#00BFFF"
branco_antigo   = "#FAEBD7"
blue_violet     = "#8A2BE2"
slate_bue_1     = "#836FFF"

###############################################BOTOES ATIVAÇÃO

BT_desabilitado = "disabled"
BT_ativo        = "normal"

############################################### CARACTERISTICA ESCRITA

esc_BT_vGB_15 = "Arial 15 bold"
esc_BT_vGB_10 = "Arial 10 bold"

esc_LBL_vGB_20 = "Arial 20 bold"
esc_LBL_vGB_15 = "Arial 15 bold"
esc_LBL_vGB_10 = "Arial 10 bold"

######################################################################################################################
				#######################janela ativar leitura 1 - pai- janela ativar leitura##############
######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def FUNCAO_TERCIARIA_CHAMADABTEXT_vv_ATIVARLEITURA_PT_1():
######################################################funcoes ternarias LH1############################################

	def BASIC_TERC_CHAMADABTINT_cc_CALCULO_SALVAR_dbTB_ATIVARLEITURA_LINHA1():                                                           # adicona no banco
		
		total_vers_bib_BB_LH1 = bib
		
		try:
			total_dias_lei_BB_LH1 = qt_dias_ativar 
			total_dias_lei_BB_LH1 = int(ENTRY_TEXT_plano4_WIND_TERC_zz_entryinterno_t1.get())

			CALCULO_INTEIRO_LH1	  = (total_vers_bib_BB_LH1) // total_dias_lei_BB_LH1
			CALCULO_PARCIAL_LH1   = total_vers_bib_BB_LH1   %  total_dias_lei_BB_LH1
		except ZeroDivisionError:
			LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "NÚMERO ZERO NÃO É PERMITIDO. \nESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except ValueError:
			LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "CARACTERE NÃO PERMITIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "       								#$ERRO AO CLICAR EM VALOR NOME CARACTERE

		except KeyboardInterrupt:
			LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "NÃO INFORMOU OS DADOS. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except TypeError:
			LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "DADO É INVÁLIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		else:	
			total_dias_lei_BB_LH1

			if   total_dias_lei_BB_LH1 > qt_dias_max:
					LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "   ACIMA DE 3285 NÃO É VALIDO,\nDIGITE UM NÚMERO VALIDO."

			elif total_dias_lei_BB_LH1 < qt_dias_max or total_dias_lei_BB_LH1 > qt_dias_min:

					BD_SIST_TERC_nn_SALdata_imp = sqlite3.connect('app_banco.db')                                                       #conectar ao banco de dados
					CURSOR_DB_EXE_lh1 = BD_SIST_TERC_nn_SALdata_imp.cursor()                                                            # processo de banco

					inserir_valordb_calc_LH1     = "INSERT INTO  ativar_leitura ( leitura_dia, leitura_final, qt_dias) VALUES (?,?,?)"  # campos da tabela, valores a ser inserido
					variav_valor_calc_SQLDATA_LH1 = (CALCULO_INTEIRO_LH1, CALCULO_PARCIAL_LH1, total_dias_lei_BB_LH1)                   # variaveis das funções de calculo

					CURSOR_DB_EXE_lh1.execute(inserir_valordb_calc_LH1, variav_valor_calc_SQLDATA_LH1)                                  # execução da chamada das funções
					
					BD_SIST_TERC_nn_SALdata_imp.commit()                                                                                #SALVAR

					
					def FuncaoBase_TERC_AUTOEXE_ee_IMPRIMIR_DADOSDB_TBLH1():
						sql_visual_lh1 = 'SELECT *FROM ativar_leitura where id_ativar_leitura = "1" '
						CURSOR_DB_EXE_lh1.execute(sql_visual_lh1)
						cf         =  CURSOR_DB_EXE_lh1.fetchone()
						
						LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "  QUANTIDADE DIA:         {}\nQUANTIDADE FINAL:     {}\nQUANTIDADE DE DIAS: {}".format(cf[1],cf[2],cf[3])

					FuncaoBase_TERC_AUTOEXE_ee_IMPRIMIR_DADOSDB_TBLH1()  
					                                                                         
					BD_SIST_TERC_nn_SALdata_imp.close()  #sair do banco

					LBL_vrd_WIND_TERC_zz_lblimp_fcbd_lh_1["text"] = "DADOS SALVO COM SUCESSO"

					TOP_TERC_SWITH_STATE_PT2()###FUNÇÃO DO TK interno

					FUNCAO_TOP_AUTOEXE_WIND_SEGUNDO_zz_BT2_ATIV_LEI_LH1_2()

	def BASIC_TERC_CHAMADABTINT_cc_btapagar_bdlh_1():                                                                                  # apagar do banco
		BD_ap_1 = sqlite3.connect('app_banco.db')
		CURSOR_ap_lh1 = BD_ap_1.cursor()
		sql_rein = 'DELETE FROM ativar_leitura WHERE id_ativar_leitura = 1'
		CURSOR_ap_lh1.execute(sql_rein)

		BD_ap_1.commit()
		BD_ap_1.close()
		
		LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "ESCOLHA DE 1 DIA ATÉ 3285 DIAS."
		LBL_vrd_WIND_TERC_zz_lblimp_fcbd_lh_1["text"] = "LEITURA APAGADO\n COM SUCESSO"

		TOP_TERC_SWITH_STATE_PT1()

########################################################################################################################
########################################janela inserir dados- pai janela secundaria######
#########################################################################################################################

	top_ativar_leitura_BD_1 = Toplevel()                                     ####top level
	top_ativar_leitura_BD_1.title        ("ATIVAR LEITURA 1")
	top_ativar_leitura_BD_1.geometry     ("400x200")                         #lar x alt
	top_ativar_leitura_BD_1.configure    (background = madeira_robusta)       
	top_ativar_leitura_BD_1.resizable    (False,False)

############################################FUNCOES DE HABILITACAO
	def TOP_TERC_SWITH_STATE_PT1():
		BTN_vrv_WIND_TERC_zz_btvrv_ENTRY_linha1["state"] = BT_ativo
		BT_vrd_WIND_TERC_zz_btvrd_t1["state"] = BT_desabilitado

	def TOP_TERC_SWITH_STATE_PT2():
		BTN_vrv_WIND_TERC_zz_btvrv_ENTRY_linha1["state"] = BT_desabilitado
		BT_vrd_WIND_TERC_zz_btvrd_t1["state"] = BT_ativo

#####################################################FUNCOES DO SISTEMA DO TOP
	def FUNCAO_top_AUTOEXE_WIND_TERC_zz_fcTOP1():
		
		try:
			banco_rei    = sqlite3.connect('app_banco.db')
			cur_rei      = banco_rei.cursor()

			sql_rei_data_lh1 = 'SELECT *FROM ativar_leitura where id_ativar_leitura = "1" '
			cur_rei.execute(sql_rei_data_lh1)
			cfc          = cur_rei.fetchone()

			if cfc[0] == 1:
				TOP_TERC_SWITH_STATE_PT2()
				
			banco_rei.close()

		except TypeError:
			
			TOP_TERC_SWITH_STATE_PT1()
					
			

	def FUNCAO_TOP_AUTOEXE_WIND_TERC_zz_fcBD_IMPRIMIR_LH1():

		try:
			BD_imp_lh1     = sqlite3.connect('app_banco.db')
			CUR_exe_bd_lh1 = BD_imp_lh1.cursor()

			sql_vis_lh_1   = 'SELECT *FROM ativar_leitura where id_ativar_leitura = "1" '
			CUR_exe_bd_lh1.execute(sql_vis_lh_1)
			csf_lh1 = CUR_exe_bd_lh1.fetchone()

			LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1["text"] = "  QUANTIDADE DIA:         {}\nQUANTIDADE FINAL:     {}\nQUANTIDADE DE DIAS: {}".format(csf_lh1[1],csf_lh1[2],csf_lh1[3])

			BD_imp_lh1.close()

		except AttributeError:

			LBL_vrd_WIND_TERC_zz_lblimp_fcbd_lh_1["text"] = "DADOS INEXISTENTE"

		except TypeError:

			LBL_vrd_WIND_TERC_zz_lblimp_fcbd_lh_1["text"] = "DADOS INEXISTENTE"
			
################################################SISTEMA DO TK
	LBL_fxbasic_WIND_TERC_zz_lblfx_t1    = Label(top_ativar_leitura_BD_1,                                     ###label - fixa
							text         =  "QUANTIDADE  DE DIAS: ",
							background   =  alice_blue,                        
							font         =  esc_LBL_vGB_10,
							width        =  25)
	LBL_fxbasic_WIND_TERC_zz_lblfx_t1.place(y = 20)

	ENTRY_TEXT_plano4_WIND_TERC_zz_entryinterno_t1 = Entry(top_ativar_leitura_BD_1)                                   ###entry++
	ENTRY_TEXT_plano4_WIND_TERC_zz_entryinterno_t1.place(x = 185, y = 18, width = 40)
	
	BTN_vrv_WIND_TERC_zz_btvrv_ENTRY_linha1 = Button(top_ativar_leitura_BD_1,                            ###botao - função(função_criação de dados)
								text        =  "SALVAR",
								font        =  esc_BT_vGB_15,           
								foreground  =  verde_limao,
								command     =  BASIC_TERC_CHAMADABTINT_cc_CALCULO_SALVAR_dbTB_ATIVARLEITURA_LINHA1)
	BTN_vrv_WIND_TERC_zz_btvrv_ENTRY_linha1.place(x = 230, y = 18, width = 90 )


	LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1    = Label(top_ativar_leitura_BD_1,                                 ###labe1 -- de funçao
									text        =  "ESCOLHA DE 1 DIA ATÉ 3285 DIAS.",
									font        =  esc_LBL_vGB_10,
									background  =  madeira_robusta)                
	LBL_vrd_WIND_TERC_zz_lblimp_funcaolh1_t1.place(y = 65)

	LBL_vrd_WIND_TERC_zz_lblimp_fcbd_lh_1   = Label(top_ativar_leitura_BD_1,
								font        = esc_LBL_vGB_10,
								background  = madeira_robusta)
	LBL_vrd_WIND_TERC_zz_lblimp_fcbd_lh_1.place(y = 130)

	BT_vrd_WIND_TERC_zz_btvrd_t1 = Button(top_ativar_leitura_BD_1,                           ###botao - função()
							text        = 	"APAGAR LEITURA",
							font        =   esc_BT_vGB_10,            
							foreground  =   verde_limao,
							command     =   BASIC_TERC_CHAMADABTINT_cc_btapagar_bdlh_1 )
	BT_vrd_WIND_TERC_zz_btvrd_t1.place(x = 230, y = 120, width = 150 )

	FUNCAO_top_AUTOEXE_WIND_TERC_zz_fcTOP1()

	FUNCAO_TOP_AUTOEXE_WIND_TERC_zz_fcBD_IMPRIMIR_LH1()

#############################################
	top_ativar_leitura_BD_1.mainloop()                           #*************************FIM****************************


###############################################################################################################################
									##################### janela ativar leitura 2 - pai- janela ativar leitura##################
################################################################################################################################
################################################################################################################################
################################################################################################################################

def FUNCAO_TERCIARIA_CHAMADABTEXT_vv_ATIVARLEITURA_PT_2():

########################################################################################################################
########################################janela inserir dados- pai janela secundaria######
#########################################################################################################################

	top_ativar_leitura_BD_2 = Toplevel()   
	top_ativar_leitura_BD_2.title      ("ATIVAR LEITURA 2")
	top_ativar_leitura_BD_2.geometry   ("400x200")
	top_ativar_leitura_BD_2.configure  (background = madeira_robusta)
	top_ativar_leitura_BD_2.resizable  (False,False)
	###########################################
	top_ativar_leitura_BD_2.mainloop()

################################################################################################################################2
									######################janela ativar leitura - pai- janela principal##################
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################

def FUNCAO_SECUNDARIA_CHAMADABTEXT_vv_WINDOW_ATIVAR_LEITURA():
#######################################################################funcoes secundaria########################

	def BASIC_SEC_AUTOEXE_cc_CRIAR_BANCO():                                                                ###cria banco

		BD_SIST_SEC_nn_APPBANCO = sqlite3.connect('app_banco.db')                                           
		CURSOR_APPBANCO         = BD_SIST_SEC_nn_APPBANCO.cursor()

		def FuncaoBase_SEC_AUTOEXE_ee_CRIAR_TABELA():

			BD_SIST_SEC_nn_APPBANCO.execute('CREATE TABLE IF NOT EXISTS ativar_leitura (id_ativar_leitura integer NOT NULL PRIMARY KEY , \
											leitura_dia   integer  NULL, \
											leitura_final integer  NULL, \
											qt_dias       integer  NULL )')#existe tabela, se nao tiver cria

		FuncaoBase_SEC_AUTOEXE_ee_CRIAR_TABELA()

		BD_SIST_SEC_nn_APPBANCO.commit()
		BD_SIST_SEC_nn_APPBANCO.close()

	BASIC_SEC_AUTOEXE_cc_CRIAR_BANCO()                                                                     # chamar tabela   

	def BASIC_SEC_CHAMADABTINT_cc_CALCULO_sSALVAR():                                                
		total_versiculo_biblico_sSALVAR = bib

		try:
			total_dias_leitura_sSALVAR  = qt_dias_ativar
			total_dias_leitura_sSALVAR  = int (ENTRY_TEXT_plano4_WIND_SECUNDARIO_zz_entry4interno_A_1.get())

			TOTAL_CALCULO_sSALVAR       = ( total_versiculo_biblico_sSALVAR ) // total_dias_leitura_sSALVAR

		except ZeroDivisionError:
			LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1["text"]     = "NÚMERO ZERO NÃO É PERMITIDO. \nESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except ValueError:
			LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1["text"]     = "CARACTERE NÃO PERMITIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except KeyboardInterrupt:
			LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1["text"]     = "NÃO INFORMOU OS DADOS. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		except TypeError:
			LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1["text"]     = "DADO É INVÁLIDO. \n       ESCOLHA DE 1 DIA ATÉ 3285 DIAS. "

		else:	
			total_dias_leitura_sSALVAR

			if   total_dias_leitura_sSALVAR > qt_dias_max:    

					LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1["text"] = "   ACIMA DE 3285 NÃO É VALIDO,\nDIGITE UM NÚMERO VALIDO."            

			elif total_dias_leitura_sSALVAR < qt_dias_max or total_dias_leitura_sSALVAR > qt_dias_min:

					LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1["text"] = "TOTAL AO DIA: %d" %TOTAL_CALCULO_sSALVAR

	
	##################################################################################################################################
	############################## ATIVADO ATRAVEZ DO BOTAO JANELA PRINCIPAL###
	##################################################################################################################################

	top_ativar_leitura = Toplevel()
	top_ativar_leitura.title       ("ATIVAR LEITURA")
	top_ativar_leitura.geometry    ("400x400")                   #lar x alt
	top_ativar_leitura.configure   (background = madeira_robusta)      
	top_ativar_leitura.resizable   (False,False)

####################################################FUNÇÃO ORGANIZACAO DE SISTEMA

	def FUNCAO_TOP_AUTOEXE_WIND_SEGUNDO_zz_BT2_ATIV_LEI_LH1_2():

		try:
			BD_TOP_LH1    = sqlite3.connect('app_banco.db')
			cur_bd_lh1      = BD_TOP_LH1.cursor()

			sql_rei_data_lh1 = 'SELECT *FROM ativar_leitura where id_ativar_leitura = "1" '
			cur_bd_lh1.execute(sql_rei_data_lh1)
			cfc          = cur_bd_lh1.fetchone()

			if cfc[0] == 1:
				BTN_fx_WIND_SECUDARIO_zz_btnext_a_2["state"] = BT_ativo
				
			BD_TOP_LH1.close()

		except TypeError:

			BTN_fx_WIND_SECUDARIO_zz_btnext_a_2["state"] = BT_desabilitado
			
		except NameError:
			BTN_fx_WIND_SECUDARIO_zz_btnext_a_2["state"] = BT_desabilitado
		
			
	LBL_fxexp_WIND_SECUNDARIO_zz_lblexp_A_1     = Label(top_ativar_leitura,                             		 ###label-expandida
								text        	=  "CALCULO DE VERSICULO POR DIA",
								background  	=  deep_skyblue,                   
								font       		=  esc_LBL_vGB_15,                    
								width       	=   400)                   
	LBL_fxexp_WIND_SECUNDARIO_zz_lblexp_A_1.pack(pady = 5)
	
				
	LBL_FXBASIC_WIND_SECUNDARIO_zz_lblbasic_A_1   = Label(top_ativar_leitura,                                ###label - fixa                                  
									  text        =  "QUANTIDADE  DE DIAS: ",
									  background  =  alice_blue,                         
									  font        =  esc_LBL_vGB_10,
									  width       =  25)
				
	LBL_FXBASIC_WIND_SECUNDARIO_zz_lblbasic_A_1.place(y = 50)

	ENTRY_TEXT_plano4_WIND_SECUNDARIO_zz_entry4interno_A_1 = Entry(top_ativar_leitura)                       ###entry++
	ENTRY_TEXT_plano4_WIND_SECUNDARIO_zz_entry4interno_A_1.place(x = 185, y = 48, width = 40)

	BTN_fx_WIND_SECUNDARIO_zz_btninterno_A_1  = Button(top_ativar_leitura,                     				 ###botao - função( função ativar leitura)
								  text        = 	"CALCULAR",
								  font        =  esc_BT_vGB_10,            
								  foreground  =   verde_limao,
								  command     =   BASIC_SEC_CHAMADABTINT_cc_CALCULO_sSALVAR)
	BTN_fx_WIND_SECUNDARIO_zz_btninterno_A_1.place(x = 230, y = 48, width = 90 )
							
	LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1 = Label(top_ativar_leitura,                            			###label-movel--
							  text        =  "ESCOLHA DE 1 DIA ATÉ 3285 DIAS.",
							  font        =  esc_LBL_vGB_10,
							  background  =  madeira_robusta)               
	LBL_vrv_WIND_SECUNDARIO_zz_lblvrv_A_1.place(y = 90)
	
	LBL_fxesp_WIND_SECUNDARIO_zz_lblesp_a_1  = Label(top_ativar_leitura,                        			###label-expandida
								 text        =  "ATIVAR LEITURA",		
								 background  =  deep_skyblue,                   
								 font        =  esc_LBL_vGB_15,                    
								 width       =  400)                   
	LBL_fxesp_WIND_SECUNDARIO_zz_lblesp_a_1.pack(pady = 100)

	BTN_fx_WIND_SECUDARIO_zz_btnext_a_1 = Button(top_ativar_leitura,                       					 ###botao - função(ativar leitura 1 db)
					text        =  "ATIVAR LEITURA 1",
					background  =  branco_antigo, foreground = verde_limao,  
					font        =  esc_BT_vGB_15,
					width       = 	20,
					command     =   FUNCAO_TERCIARIA_CHAMADABTEXT_vv_ATIVARLEITURA_PT_1)
	BTN_fx_WIND_SECUDARIO_zz_btnext_a_1.place(x= 70, y = 180)

	BTN_fx_WIND_SECUDARIO_zz_btnext_a_2 = Button(top_ativar_leitura,                       					 ###botao - função(ativar leitura 2 db)
					text        =  "ATIVAR LEITURA 2",
					background  =  branco_antigo, foreground = verde_limao,  
					font        =  esc_BT_vGB_15,
					width       = 	20,
					command     =   FUNCAO_TERCIARIA_CHAMADABTEXT_vv_ATIVARLEITURA_PT_2)
	BTN_fx_WIND_SECUDARIO_zz_btnext_a_2.place(x= 70, y = 230)

	FUNCAO_TOP_AUTOEXE_WIND_SEGUNDO_zz_BT2_ATIV_LEI_LH1_2()
	
#####################################
	top_ativar_leitura.mainloop()#########################********************FIM************************#

##################################################################################################################1
											#####################janela principal####################
###################################################################################################################
###################################################################################################################
###################################################################################################################

app = Tk()                                                
app.title      ("LEITURA BIBLICA")                                                         ####tela principal-menus
app.geometry   ("400x500")               #lar x alt                                                  
app.configure  (background = slate_bue_1)                          
app.resizable  (False,False)

LBL_fxexp_WIND_PRINC_zz_lblexp_1 	= Label(app,                                           ###label - expandida
					 text       =  "CONFIGURAÇÕES",
				   	 background =  blue_violet,                         
					 font       =  esc_LBL_vGB_20,
					 width      =  400)
LBL_fxexp_WIND_PRINC_zz_lblexp_1.pack()

BTN_fx_WIND_PRINC_func_TKEXT_zz_bt_1  = Button(app,                                       ###botao - funçao (formulario ativar leitura)
						   text       =  "ATIVAR LEITURA",
						   background =  branco_antigo, foreground = verde_limao,   
						   font       =  esc_BT_vGB_15,
						   width      =  20,
						   command    =  FUNCAO_SECUNDARIA_CHAMADABTEXT_vv_WINDOW_ATIVAR_LEITURA)
BTN_fx_WIND_PRINC_func_TKEXT_zz_bt_1.pack(pady = 40)
						
########################
app. mainloop()################################**********FIM***********************#
