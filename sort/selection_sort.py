def importa_lista(arquivo):
  """
  Lê uma lista de nomes de um arquivo, separando os nomes por vírgulas e removendo aspas.
  """
  lista = []
  with open(arquivo) as tf:
    lines = tf.read().split('","')
  for line in lines:
    lista.append(line)
  return lista


def ordena(lista):
  """
  Ordena a lista de nomes utilizando o algoritmo de ordenação por seleção (Selection Sort).
  """
  tamanho_da_lista = len(lista) - 1

  for posicao_atual in range(0, tamanho_da_lista):
    posicao_menor = posicao_atual
    menor_nome = lista[posicao_menor]

    for posicao_busca in range(posicao_atual, tamanho_da_lista):
      nome_busca = lista[posicao_busca + 1]

      if menor_nome > nome_busca:
        menor_nome = nome_busca
        posicao_menor = posicao_busca + 1

    if posicao_menor != posicao_atual:
      # Troca os nomes de posição
      menor_nome = lista[posicao_menor]
      lista[posicao_menor] = lista[posicao_atual]
      lista[posicao_atual] = menor_nome

  return lista


def main():
  print("=== ORDENADOR DE LISTA DE ALUNOS (SELECTION SORT) ===\n")

  # Caminho do arquivo com lista menor
  caminho_arquivo = 'data/lista_alunos_menor.txt'
  lista_de_alunos = importa_lista(caminho_arquivo)

  # Interação com usuário
  resposta = input("Deseja ordenar a lista de alunos? (s/n): ").strip().lower()

  if resposta == 's':
    ordena(lista_de_alunos)
    print("\nLista ordenada com sucesso!")
  elif resposta == 'n':
    print("A lista será exibida sem ordenação.")
  else:
    print("Resposta inválida. A lista será exibida como está.")

  # Exibe a lista se usuário quiser
  while True:
    exibir = input("\nDeseja ver a lista de alunos? (s/n): ").strip().lower()
    if exibir == 's':
      print("\n--- Lista de Alunos ---")
      for nome in lista_de_alunos:
        print(nome)
      break
    elif exibir == 'n':
      print("Ok, encerrando o programa.")
      break
    else:
      print("Por favor, digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
  main()