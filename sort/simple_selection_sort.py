def ordena(lista):
  """
  Ordena a lista utilizando o algoritmo de ordenação por seleção (Selection Sort).
  """
  tamanho_da_lista = len(lista) - 1

  for posicao_atual in range(0, tamanho_da_lista):
    posicao_menor = posicao_atual
    menor_nome = lista[posicao_menor]

    # Busca o menor nome no restante da lista
    for posicao_busca in range(posicao_atual, tamanho_da_lista):
      nome_busca = lista[posicao_busca + 1]
      if menor_nome > nome_busca:
        menor_nome = nome_busca
        posicao_menor = posicao_busca + 1

    # Troca as posições, se necessário
    if posicao_menor != posicao_atual:
      menor_nome = lista[posicao_menor]
      lista[posicao_menor] = lista[posicao_atual]
      lista[posicao_atual] = menor_nome

  return lista


def main():
  print("=== LISTA FIXA DE ALUNOS ===\n")

  lista_de_alunos = ["Brendo", "Erica", "Monica", "Nico", "Paulo", "Rodrigo", "Wanessa"]

  # Interação com o usuário
  resposta = input("Deseja ordenar a lista de alunos? (s/n): ").strip().lower()

  if resposta == 's':
    ordena(lista_de_alunos)
    print("\nLista ordenada com sucesso!\n")
  elif resposta == 'n':
    print("\nA lista será exibida na ordem original.\n")
  else:
    print("\nResposta inválida. A lista será exibida como está.\n")

  # Exibe a lista
  print("--- Lista de Alunos ---")
  for nome in lista_de_alunos:
    print(nome)


if __name__ == "__main__":
  main()