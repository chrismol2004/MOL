"""18.	Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
mes_dia = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11:30, 12: 31 }
mes_n = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6:"Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
print("Ente com uma data!!!!")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

if 0 < mes < 13:
    if (dia <= mes_dia[mes]):
        if mes != 2:
            print("Data é: dia ", dia, "de ", mes_n[mes], " de ", ano)
        else:
            if ano % 4 != 0 and dia == 29:
                print("ERROR: Data inexistente!!!")
            else:
                print("ANO BISSEXTO!!! Data é: dia ", dia, "de ", mes_n[mes], " de ", ano)
    else:
        print("ERROR: Data inexistente!!!")
else:
    print("ERROR: Data inexistente!!!")