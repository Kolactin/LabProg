def notifications():
    total_not = 0
    gastos_diarios = []
    totD = int(input("Nº de dias totais:"))
    d = int(input("Nº de dias para análise:"))
    if totD < 4:
        print("impossível realizar o programa. Encerrando sessão!")
        raise SystemExit
    
    for c in range(1, totD + 1):
        gastos = int(input(f"Informe o valor gasto no {c}º dia :"))
        gastos_diarios.append(gastos)
        if c > d:
            anteriores = gastos_diarios[c - 4 : c - 1]
            mediana = sorted(anteriores)[1]

            if gastos>= 2 * mediana:
                total_not += 1
            
    return total_not

if __name__ == "__main__":
    total_not = notifications()
    print(f"O cliente recebeu {total_not} notificações")