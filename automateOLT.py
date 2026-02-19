import customtkinter

customtkinter.set_appearance_mode("dark") #general theme
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x750")
janela.title("OLT automate")

# Criando um Label de Título
titulo = customtkinter.CTkLabel(janela, text="OLT Automate", font=("Arial", 28))
titulo.pack(pady=(30, 10))

sub_titulo = customtkinter.CTkLabel(janela, text="ZTE C300/320/350", font=("Arial", 15))
sub_titulo.pack(pady=10)

# Criando um Widget de Texto para Exibir os Comandos
output_text = customtkinter.CTkTextbox(janela, width=480, height=230, state="disabled")# output permite inserir texto
output_text.pack(pady=10)

# As funções que serão exibidas ao clicar nos botões
def verificação_status_command():
    output_text.configure(state="normal") # Habilita edição 
    output_text.delete("1.0", "end") # Limpa o texto anterior dentro do widget
    output_text.insert("end", "STATUS VERIFICATION:\n\nINSERVICE - Operating normally\nCONFIGING - Board is being configured\nCONFIGFAILED - Configuration process failed\nDISABLE - No communication\nHWONLINE - Different software version\nOFFLINE - Board added logically, not physically\nSTANDBY - Standby mode\nTYPE MISMATCH - Board type does not match the physical model\nNO POWER - Powered off\n")
    output_text.configure(state="disabled") #Bloqueia edição novamente

def primeiro_acesso_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "FIRST ACCESS:\n\nThe factory default IP address of the OLT is 136.1.1.100.\nThe default login password is zte.\n\nIf remote access is not possible, connect via the CLI port:\n\nThe connection must be made through the CLI port using 9600 baud rate.\n\nTo enter privileged mode, use the command:\nenable\nThe privileged mode password is zxr10\n")
    output_text.configure(state="disabled")

def alteracao_nome_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "CHANGING THE OLT HOSTNAME:\n\nhostname [NEW NAME]\nexit\n")
    output_text.configure(state="disabled")

def data_hora_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "DATE AND TIME CONFIGURATION:\n\nImportant for correct log and error timestamp identification.\n\nconf t\nclock timezone BRT -3\nexit\n\nclock set 00:00:00 month - day - year\nptp\nexit\n")
    output_text.configure(state="disabled")

def autosave_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "ENABLE AUTO-SAVE AND SAVE CONFIGURATION:\n\nYou can manually save your configuration using the command below:\n\n[CONFIGURATION COMPLETED]\nexit\nwrite\n\nYou can also enable auto-save:\nauto-write\nauto-write 24\n")
    output_text.configure(state="disabled")

def ativacao_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "ENABLING AND DISABLING INTERFACES:\n\nInterface activation and deactivation usually follow this pattern:\n\nenable\nno shutdown\nshutdown\n")
    output_text.configure(state="disabled")

def verificacao_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "VERIFYING APPLIED CONFIGURATIONS:\n\nCommon commands used to verify general configurations:\n\nshow this\nshow running-config\nshow running-config interface mng1\nshow running-config interface gpon-onu\nshow remote-onu wan-ip gpon-onu_1/1/1\n")
    output_text.configure(state="disabled")

def interfaces_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "OLT INTERFACES:\n\nFor better understanding, it is important to know the available interfaces and their purposes:\n\nGPON OLT INTERFACE:\nThis is the OLT port connected to the GPON fiber network. It manages communication between the OLT and client ONUs.\n\nGPON ONU INTERFACE:\nUsed to configure ONUs (Optical Network Units), which are customer-side devices connecting homes to the OLT.\n\nXGEI INTERFACE:\nHigh-speed 10G Ethernet interface, typically used for uplink or backbone communication.\n\nGEI INTERFACE:\n1G Ethernet interface used for lower-speed network connections.\n\nPON INTERFACE:\nPassive Optical Network interface that connects the OLT to the fiber backbone. It is the main distribution port for client internet access.\n")
    output_text.configure(state="disabled")

def pnp_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "ENABLE PLUG-AND-PLAY BOARD AND CHASSIS DETECTION:\n\nconf t\nset-pnp enable\nadd-rack rackno 1 racktype C320Rack\nadd-shelf rackno 1 shelfno 1 shelftype C320_SHELF\n")
    output_text.configure(state="disabled")

def ip_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "CONFIGURE A NEW MANAGEMENT IP:\n\nDefines the IP address for remote OLT access. The subnet mask determines the IP range.\n\ninterface mng1\nip address [IP] [MASK]\nconfig-filename startrun.dat\nnegotiation auto\ntag-mode untag\n")
    output_text.configure(state="disabled")

def gateway_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "ADD DEFAULT GATEWAY:\n\nconf t\nno ip route 0.0.0.0 0.0.0.0\nip route 0.0.0.0 0.0.0.0 [GATEWAY IP]\nexit\nwrite\n")
    output_text.configure(state="disabled")

def vlangerencia_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "MANAGEMENT VLAN:\n\nvlan 100\nname MANAGEMENT\nexit\n\ninterface vlan100\nip address [IP] [MASK]\nexit\n")
    output_text.configure(state="disabled")

def uplink_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "UPLINK GEI INTERFACE:\n\ninterface gei_1/1/1\nno shutdown\nswitchport vlan 100 tag\nlinktrap enable\nport-protect disable\nuplink-isolate disable\n")
    output_text.configure(state="disabled")

def acessoremoto_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "ENABLE SSH:\n\nssh server authentication type chap\nssh server version 2\nusername zte password zte privilege 15\n\nENABLE TELNET:\n\nsecurity-mgmt 999 state enable ingress-type lan protocol telnet\nusername zte password zte privilege 15\nshow security-mgmt\n")
    output_text.configure(state="disabled")

def banda_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "BANDWIDTH CONFIGURATION:\n\nprofile tcont 1G-UP type 5 fixed 64 assured 64 maximum 1048064\nprofile traffic 1G-DOWN sir 1048064 pir 1048064\n\nsir = Guaranteed bandwidth\npir = Maximum bandwidth\n")
    output_text.configure(state="disabled")

def vlanonu_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "ONU VLAN PROFILE:\n\nonu profile vlan [000] tag-mode tag cvlan [000]\n")
    output_text.configure(state="disabled")

def veip_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "REMOTE ACCESS AND ONU VEIP CONFIGURATION:\n\nflow mode 1 tag-filter vlan-filter untag-filter discard\nflow 1 pri 0 vlan 100\ngemport 1 flow 1\nswitchport-bind switch_0/1 iphost 1\nswitchport-bind switch_0/1 veip 1\ndhcp-ip ethuni eth_0/1 from-internet\n\nsecurity-mgmt 998 state enable mode forward ingress-type lan protocol web https\nsecurity-mgmt 999 state enable ingress-type lan protocol ftp telnet ssh snmp tr069\n")
    output_text.configure(state="disabled")

def rede_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "PPPOE, NETWORK AND ONU PASSWORD CONFIGURATION:\n\npon-onu-mng gpon-onu_1/1/1\nmode pppoe username [USERNAME] password [PASSWORD]\npassword [PASSWORD] vlan-profile 100\n\nssid ctrl wifi_0/1 name 2.4G\nssid ctrl wifi_0/5 name 5G\n\nwifi_0/1 encrypt aes key [PASSWORD]\nwifi_0/5 encrypt aes key [PASSWORD]\n\nssid ctrl wifi_0/1 user-isolation disable\n")
    output_text.configure(state="disabled")

def pon_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "PON ACTIVATION:\n\ninterface gpon-olt_1/1/1\nshow this\nshutdown (DISABLED)\nlinktrap disable\n\nno shutdown (ENABLED)\nexit\n")
    output_text.configure(state="disabled")

def autorizar_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "AUTHORIZE ONU:\n\ninterface gpon-olt_1/3/12\nonu [ONU NUMBER] type [MODEL] sn [SERIAL/MAC]\n")
    output_text.configure(state="disabled")

def backup_reset_command():
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    output_text.insert("end", "BACKUP:\n\nUsing MikroTik, locate the backup file before executing the command on the OLT.\n\nMIKROTIK > SYSTEM > USERS\nENABLE FTP PORT\nFILE LIST (OLT BACKUP FILE)\n\nOLT TERMINAL:\nfile upload cfg-startup *.* ftp ipaddress [FTP IP] user [USERNAME] password [PASSWORD]\n\nRESET:\nfile delete cfg-startup *.*\nyes\nreboot\nyes\n")
    output_text.configure(state="disabled")
    
# Criando um Frame para os botões
frame_botoes = customtkinter.CTkFrame(janela)
frame_botoes.pack(pady=10)

# Organizando os botões em três colunas
btn_status = customtkinter.CTkButton(frame_botoes, text="STATUS", command=verificação_status_command)
btn_status.grid(row=0, column=0, padx=10, pady=5)

btn_acesso = customtkinter.CTkButton(frame_botoes, text="FIRST ACCESS", command=primeiro_acesso_command)
btn_acesso.grid(row=0, column=1, padx=10, pady=5)

btn_alterarnome = customtkinter.CTkButton(frame_botoes, text="CHANGE HOSTNAME", command=alteracao_nome_command)
btn_alterarnome.grid(row=0, column=2, padx=10, pady=5)

btn_datahora = customtkinter.CTkButton(frame_botoes, text="DATE & TIME", command=data_hora_command)
btn_datahora.grid(row=1, column=0, padx=10, pady=5)

btn_autosave = customtkinter.CTkButton(frame_botoes, text="AUTO-SAVE", command=autosave_command)
btn_autosave.grid(row=1, column=1, padx=10, pady=5)

btn_ativacao = customtkinter.CTkButton(frame_botoes, text="INTERFACE CONTROL", command=ativacao_command)
btn_ativacao.grid(row=1, column=2, padx=10, pady=5)

btn_verificacao = customtkinter.CTkButton(frame_botoes, text="VERIFY CONFIG", command=verificacao_command)
btn_verificacao.grid(row=2, column=0, padx=10, pady=5)

btn_interfaces = customtkinter.CTkButton(frame_botoes, text="OLT INTERFACES", command=interfaces_command)
btn_interfaces.grid(row=2, column=1, padx=10, pady=5)

btn_pnp = customtkinter.CTkButton(frame_botoes, text="PNP CONFIG", command=pnp_command)
btn_pnp.grid(row=2, column=2, padx=10, pady=5)

btn_ip = customtkinter.CTkButton(frame_botoes, text="SET IP", command=ip_command)
btn_ip.grid(row=3, column=0, padx=10, pady=5)

btn_gateway = customtkinter.CTkButton(frame_botoes, text="SET GATEWAY", command=gateway_command)
btn_gateway.grid(row=3, column=1, padx=10, pady=5)

btn_vlangerencia = customtkinter.CTkButton(frame_botoes, text="MANAGEMENT VLAN", command=vlangerencia_command)
btn_vlangerencia.grid(row=3, column=2, padx=10, pady=5)

btn_uplink = customtkinter.CTkButton(frame_botoes, text="UPLINK CONFIG", command=uplink_command)
btn_uplink.grid(row=4, column=0, padx=10, pady=5)

btn_acessoremoto = customtkinter.CTkButton(frame_botoes, text="TELNET / SSH", command=acessoremoto_command)
btn_acessoremoto.grid(row=4, column=1, padx=10, pady=5)

btn_banda = customtkinter.CTkButton(frame_botoes, text="BANDWIDTH PROFILE", command=banda_command)
btn_banda.grid(row=4, column=2, padx=10, pady=5)

btn_vlanonu = customtkinter.CTkButton(frame_botoes, text="ONU VLAN", command=vlanonu_command)
btn_vlanonu.grid(row=5, column=0, padx=10, pady=5)

btn_veip = customtkinter.CTkButton(frame_botoes, text="ONU VEIP", command=veip_command)
btn_veip.grid(row=5, column=1, padx=10, pady=5)

btn_rede = customtkinter.CTkButton(frame_botoes, text="ONU NETWORK", command=rede_command)
btn_rede.grid(row=5, column=2, padx=10, pady=5)

btn_pon = customtkinter.CTkButton(frame_botoes, text="ACTIVATE PON", command=pon_command)
btn_pon.grid(row=6, column=0, padx=10, pady=5)

btn_autorizar = customtkinter.CTkButton(frame_botoes, text="AUTHORIZE ONU", command=autorizar_command)
btn_autorizar.grid(row=6, column=1, padx=10, pady=5)

btn_backupreset = customtkinter.CTkButton(frame_botoes, text="BACKUP / RESET", command=backup_reset_command)
btn_backupreset.grid(row=6, column=2, padx=10, pady=5)

btn_sair = customtkinter.CTkButton(frame_botoes, text="EXIT", command=janela.quit, fg_color="red", text_color="white")
btn_sair.grid(row=7, column=1, padx=10, pady=5)

janela.mainloop()