def load_names_from_file(filepath):
  """
  Lê os nomes de um arquivo onde os nomes estão separados por vírgulas e aspas,
  e retorna uma lista ordenada e padronizada em letras minúsculas.
  """
  with open(filepath, encoding='utf-8') as f:
    texto = f.read().strip()
    # Remove aspas externas se houver
    if texto.startswith('"') and texto.endswith('"'):
      texto = texto[1:-1]
    # Divide os nomes pelo separador "," com aspas
    nomes = texto.split('","')
    # Normaliza e ordena os nomes
    return sorted([nome.lower() for nome in nomes if nome.strip()])


def binary_search(lista, nome_pesquisado):
  """
  Realiza busca binária em uma lista ordenada.
  Retorna o índice do nome se encontrado, senão retorna -1.
  """
  inicio, fim = 0, len(lista) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2

    if lista[meio] == nome_pesquisado:
      return meio
    elif lista[meio] < nome_pesquisado:
      inicio = meio + 1
    else:
      fim = meio - 1

  return -1


def main():
  # Caminho do arquivo com os nomes
  caminho_arquivo = 'data/lista_alunos.txt'

  # Carrega e ordena os nomes do arquivo
  lista_de_alunos = load_names_from_file(caminho_arquivo)

  # Loop de interação com o usuário
  while True:
    nome = input("Digite o nome do aluno que deseja buscar (ou 'sair' para encerrar): ").strip().lower()

    if nome == 'sair':
      print("Encerrando o programa.")
      break

    # Realiza a busca binária pelo nome informado
    posicao = binary_search(lista_de_alunos, nome)

    if posicao != -1:
      print(f"Aluno(a) {nome} está na posição {posicao}.")
    else:
      print(f"Aluno(a) {nome} não foi encontrado(a).")


# Executa o programa principal
if __name__ == "__main__":
  main()
