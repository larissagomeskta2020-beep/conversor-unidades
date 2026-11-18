def celsius_para_fahrenheit(celsius):
    """Converte a tempreratura de Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def km_para_milhas(km):
        """Converte a distancia de quilômetros para milhas."""
        milhas = km * 0.621371
        return milhas

def kg_para_libras(kg):
    """Converte a massa de quilogramas para libras."""
    libras = kg * 2.20462
    return libras 

def main():
    print("Escolha a conversão que deseja realizar:")
    print("1. Celsius para Fahrenheit")
    print("2. Quilômtros para Milhas")
    print("3. Quilogramas para Libras")
    print("4. Sair")

    opcao = input("Digite o número sa opção desejada:")
    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit}°F")
    elif opcao == "2":
        km = float(input("Digite a distância em quilômetros: "))
        milhas = km_para_milhas(km)
        print(f"{km} km é igual a {milhas} milhas")
    elif opcao == "3":
        kg = float(input("Digite a massa em quilogramas: "))
        libras = kg_para_libras(kg)
        print(f"{kg} kg é igual a {libras} libras")
    elif opcao == "4":
        print("Saindo do programa...")
        return
    else:
        print("'Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()



        