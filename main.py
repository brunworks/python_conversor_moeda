def converter_moeda(taxa, valor):
    return valor * taxa

valor = float(input('Digite o valor deseja converter:'))
taxa = float(input('Digite a taxa de câmbio:'))

resultado = converter_moeda(taxa, valor)
print(f'O valor convertido com a taxa de câmbio em {taxa} é {resultado}')