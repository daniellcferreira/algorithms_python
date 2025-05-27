# search/quick_sort_interativo.py

from array import array

def importa_lista(arquivo):
  """
  Lê uma lista de nomes de um arquivo de texto com nomes entre aspas e separados por vírgulas.
  """
  lista = []
  with open(arquivo) as tf:
    lines = tf.read().split('","')
  for line in lines:
    lista.append(line)
  return lista


def ordena(lista):
  """
  Inicia o algoritmo Quick Sort se a lista não estiver vazia.
  """
  tamanho_da_lista = len(lista)
  if tamanho_da_lista > 0:
    quick_sort(lista, 0, tamanho_da_lista - 1)


def quick_sort(lista, inicio, fim):
  """
  Implementação do algoritmo de ordenação Quick Sort.
  """
  if inicio > fim:
    return

  anterior = inicio
  posterior = fim
  pivo = lista[inicio]

  while anterior < posterior:
    # Move o ponteiro da direita até encontrar um valor menor que o pivô
    while anterior < posterior and lista[posterior] > pivo:
      posterior -= 1

    if anterior < posterior:
      lista[anterior] = lista[posterior]
      anterior += 1

    # Move o ponteiro da esquerda até encontrar um valor maior que o pivô
    while anterior < posterior and lista[anterior] <= pivo:
      anterior += 1

    if anterior < posterior:
      lista[posterior] = lista[anterior]
      posterior -= 1

  lista[anterior] = pivo

  # Ordena as sublistas
  quick_sort(lista, inicio, anterior - 1)
  quick_sort(lista, anterior + 1, fim)


def main():
  # Título
  print("=== ORDENADOR DE LISTA DE ALUNOS (QUICK SORT) ===")

  # Carrega a lista do arquivo
  lista_de_alunos = importa_lista('data/lista_alunos_menor.txt')

  # Pergunta ao usuário se deseja ordenar
  resposta = input("Deseja ordenar a lista de alunos? (s/n): ").strip().lower()

  if resposta == 's':
    ordena(lista_de_alunos)
    print("\nLista ordenada com sucesso!")
  elif resposta == 'n':
    print("Lista não será ordenada.")
  else:
    print("Resposta inválida. A lista será exibida sem ordenação.")

  # Pergunta se deseja exibir a lista
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
      print("Resposta inválida. Digite 's' ou 'n'.")


if __name__ == "__main__":
  main()
