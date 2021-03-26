        #CRIAÇÃO DE INTERFACE

import PySimpleGUI as sg

def tela():
    layout = [[sg.Text('tabuada feita \npor bruno dos santos')],
             [sg.Text('digíte um número para ver a sua tabuada ↓↓↓↓')],
             [(sg.Input(key='-pergunta-'))],
             [sg.Text(size=(40, 1), key='chave_a')],
             [sg.Text(size=(40, 1), key='chave_b')],
             [sg.Text(size=(40, 1), key='chave_c')],
             [sg.Text(size=(40, 1), key='chave_d')],
             [sg.Text(size=(40, 1), key='chave_e')],
             [sg.Text(size=(40, 1), key='chave_f')],
             [sg.Text(size=(40, 1), key='chave_g')],
             [sg.Text(size=(40, 1), key='chave_h')],
             [sg.Text(size=(40, 1), key='chave_i')],
             [sg.Text(size=(40, 1), key='chave_j')],
             [sg.Button('enviar'), sg.Button('Quit')]
             ]
    janela = sg.Window('fazedor de tabuada').layout(layout)
    while True:
         evento,valor = janela.read()
         if evento == sg.WINDOW_CLOSED or evento == 'Quit':
             break
         if evento == 'enviar':
             a = int(valor['-pergunta-'])
             janela['chave_a'].update(1 * a)
             janela['chave_b'].update(2 * a)
             janela['chave_c'].update(3 * a)
             janela['chave_d'].update(4 * a)
             janela['chave_e'].update(5 * a)
             janela['chave_f'].update(6 * a)
             janela['chave_g'].update(7 * a)
             janela['chave_h'].update(8 * a)
             janela['chave_i'].update(9 * a)
             janela['chave_j'].update(10 * a)

tela()