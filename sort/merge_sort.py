# search/merge_sort_interativo.py

from array import array

def importa_lista(arquivo):
  """
  Lê os dados de um arquivo de texto onde os nomes estão entre aspas e separados por vírgulas.
  Retorna uma lista com os nomes.
  """
  lista = []
  with open(arquivo) as tf:
    lines = tf.read().split('","')
  for line in lines:
    lista.append(line)
  return lista


def ordena(lista):
  """
  Função que inicializa o processo de ordenação utilizando o algoritmo Merge Sort.
  """
  tamanho_da_lista = len(lista)
  lista_temporaria = [0] * tamanho_da_lista
  merge_sort(lista, lista_temporaria, 0, tamanho_da_lista - 1)


def merge_sort(lista, lista_temporaria, inicio, fim):
  """
  Implementa a recursão do Merge Sort para dividir a lista em sublistas.
  """
  if inicio < fim:
    meio = (inicio + fim) // 2
    merge_sort(lista, lista_temporaria, inicio, meio)
    merge_sort(lista, lista_temporaria, meio + 1, fim)
    merge(lista, lista_temporaria, inicio, meio + 1, fim)


def merge(lista, lista_temporaria, inicio, meio, fim):
  """
  Realiza a mesclagem (merge) de duas sublistas ordenadas.
  """
  fim_primeira_parte = meio - 1
  indice_temporario = inicio
  tamanho_da_lista = fim - inicio + 1

  while inicio <= fim_primeira_parte and meio <= fim:
    if lista[inicio] <= lista[meio]:
      lista_temporaria[indice_temporario] = lista[inicio]
      inicio += 1
    else:
      lista_temporaria[indice_temporario] = lista[meio]
      meio += 1
    indice_temporario += 1

  while inicio <= fim_primeira_parte:
    lista_temporaria[indice_temporario] = lista[inicio]
    indice_temporario += 1
    inicio += 1

  while meio <= fim:
    lista_temporaria[indice_temporario] = lista[meio]
    indice_temporario += 1
    meio += 1

  for i in range(0, tamanho_da_lista):
    lista[fim] = lista_temporaria[fim]
    fim -= 1


def main():
  # Título de boas-vindas
  print("=== ORDENADOR DE LISTA DE ALUNOS ===")

  # Importa a lista de alunos do arquivo
  lista_de_alunos = importa_lista('data/lista_alunos_menor.txt')

  # Pergunta ao usuário se deseja ordenar a lista
  resposta_ordenar = input("Deseja ordenar a lista de alunos? (s/n): ").strip().lower()

  if resposta_ordenar == 's':
    ordena(lista_de_alunos)
    print("\nLista ordenada com sucesso!")
  elif resposta_ordenar == 'n':
    print("A lista será exibida sem ordenação.")
  else:
    print("Entrada inválida. A lista será exibida sem ordenação.")

  # Pergunta se o usuário quer ver a lista
  while True:
    resposta_mostrar = input("\nDeseja ver a lista ordenada de alunos? (s/n): ").strip().lower()

    if resposta_mostrar == 's':
      print("\n--- Lista de Alunos ---")
      for nome in lista_de_alunos:
        print(nome)
      break
    elif resposta_mostrar == 'n':
      print("Ok, encerrando o programa...")
      break
    else:
      print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
  print("Encerrando o programa...")


if __name__ == "__main__":
  main()
