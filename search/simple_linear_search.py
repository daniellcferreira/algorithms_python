def busca(lista, nome_pesquisado):
  """
  Realiza uma busca linear na lista de nomes.
  Retorna a posição do nome se encontrado, ou -1 se não estiver presente
  """
  for i in range(len(lista)):
    if lista[i].lower() == nome_pesquisado:
      return i
  return -1

def main():
  # lista fixa de nomes
  lista_de_alunos = ["Brendo", "Erica", "Monica", "Nico", "Paulo", "Rodrigo", "Wanessa"]

  # Converte todos os nomes para minúsculas para facilitar a busca
  lista_normalizada = [nome.lower() for nome in lista_de_alunos]

  # Loop de interação com o usuário
  while True:
    nome = input("Digite o nome do aluno que deseja buscar (ou 'sair' para encerrar): ").strip().lower()

    if nome == 'sair':
      print("Encerrando o programa...")
      break

    # Busca o nome informado
    posicao = busca(lista_normalizada, nome)
    if posicao != -1:
      print(f"Aluno(a) {lista_de_alunos[posicao]} está na posição {posicao}.")
    else:
      print(f"Aluno(a) {nome} não encontrado(a).")

if __name__ == "__main__":
  main()