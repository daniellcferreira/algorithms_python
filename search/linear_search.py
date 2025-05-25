def importa_lista(arquivo):
  """
  Lê os nomes de um arquivo onde os nomes estão em uma única linha,
  separados por vírgula, e retorna uma lista com os nomes.
  """
  lista = []
  with open(arquivo, encoding='utf-8') as f:
    linhas = f.read().strip().split('","')

  for nome in linhas:
    lista.append(nome.strip('"').lower()) # Remove aspas e normaliza para minúsculas

  return lista

def busca(lista, nome_pesquisado):
  """
  Realiza uma busca linear na lista de nomes.
  Retorna a posição do nome se encontrado, ou -1 se não estiver presente
  """
  for i in range(len(lista)):
    if lista[i] == nome_pesquisado:
      return i
  return -1

def main():
  # Caminho para o arquivo com a lista de nomes dos alunos
  caminho_arquivo = "data/lista_alunos.txt"

  # Carrega a normaliza a lista de nomes
  lista_de_alunos = importa_lista(caminho_arquivo)

  # Loop de interação com o usuário
  while True:
    nome = input("Digite o nome do aluno que deseja buscar (ou 'sair' para encerrar): ").strip().lower()

    if nome == 'sair':
      print("Encerrando o programa...")
      break

    # Busca o nome informado
    posicao = busca(lista_de_alunos, nome)
    if posicao != -1:
      print(f"Aluno(a) {nome} está na posição {posicao}.")
    else:
      print(f"Aluno(a) {nome} não encontrado(a).")

if __name__ == "__main__":
  main()