
# baixar bibliotecas :pip install pyautogui e configurações
import pyautogui
pyautogui.PAUSE = 1 #TROCAR A CONF ORIGINAL DO PYAUTOGUI
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
import time


# Passo 1: Entrar no sistema da empresa
print("Inicio ✅")

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer logim
pyautogui.click(x=719, y=404)
pyautogui.write("alomabarros@hotmail.com")
pyautogui.click(x=717, y=507)
pyautogui.write("estouautomatizandoumprojeto")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Abrir a base de dados

import pandas
import openpyxl
tabeladeprodutos = pandas.read_csv(r"C:\Users\Aloma Barros\Documents\AulaPython\Meus estudos\#hastag\Aula01\meus_codigos\produtos.csv")

# Passo 4: Cadastrar o produto

for linha in tabeladeprodutos.index:
    pyautogui.click(x=684, y=291)

    #produto
    produto = str(tabeladeprodutos.loc[linha, "codigo"])
    pyautogui.write(produto)
    pyautogui.press("tab")
    #marca
    marca = str(tabeladeprodutos.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabeladeprodutos.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabeladeprodutos.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco
    preco = str(tabeladeprodutos.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(tabeladeprodutos.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabeladeprodutos.loc[linha, "obs"])
    if obs != "nam":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

pyautogui.hotkey("alt","f4")
print("Finalizado📍")

