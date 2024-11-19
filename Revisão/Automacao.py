import pyautogui as auto
import time 

#Pausa geral de 0.3 segundos (300 milissegundos)
#auto.PAUSE = 0.3

#espera  um tempo para rodar 
time.sleep(2)

#pegar posição do mouse 
print(auto.position()) 

#ver tamanho da tela
#print(auto.size()) 

#clicar com o mouse
#auto.click(x=207, y=297) 

#clicar com botão direito do mouse 
#auto.click(x=500, y=420, button="right")

#dois clicks no mouse
#auto.click(x=313, y=500, clicks="2")

#mover o mouse
#auto.moveTo(x=651, y=167)

#scroll
#ayto.scroll(-350) para baixo
#ayto.scroll(+350) para cima

#mostrar teclas
#print(auto.KEYBOARD_KEYS)

#escrever
#auto.write("TI")

#duas teclas
#auto.hotkey("ctrl","v")
#para nao perder o controle
#auto.FAILSAFE = TRUE