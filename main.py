from livro import Livro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    # Criar alguns livros
    livro1 = Livro("Python Básico", "João Silva", 2020, "1111")
    livro2 = Livro("Aprendendo Java", "Maria Souza", 2018, "2222")
    livro3 = Livro("Python Avançado", "Carlos Lima", 2021, "3333")

    # Adicionar livros na biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    print("Livros cadastrados:")
    biblioteca.listar_livros()

    print("\nBuscando livros com 'Python' no título:")
    resultados = biblioteca.buscar_livro("Python")
    for livro in resultados:
        print(livro)

    print("\nRemovendo livro com ISBN '2222':")
    sucesso = biblioteca.remover_livro("2222")
    print("Removido com sucesso." if sucesso else "Livro não encontrado.")

    print("\nLivros após remoção:")
    biblioteca.listar_livros()
    
    from livro import Livro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== Biblioteca ===")
        print("1. Adicionar livro")
        print("2. Mostrar livros")
        print("3. Buscar livro")
        print("4. Remover livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            isbn = input("ISBN: ")
            try:
                ano = int(ano)
            except ValueError:
                print("Ano inválido! Tente novamente.")
                continue
            livro = Livro(titulo, autor, ano, isbn)
            biblioteca.adicionar_livro(livro)
            print(f'Livro "{titulo}" adicionado!')

        elif escolha == "2":
            print("\nLivros cadastrados:")
            biblioteca.listar_livros()

        elif escolha == "3":
            busca = input("Digite parte do título para buscar: ")
            resultados = biblioteca.buscar_livro(busca)
            if resultados:
                print("Livros encontrados:")
                for livro in resultados:
                    print(livro)
            else:
                print("Nenhum livro encontrado com esse título.")

        elif escolha == "4":
            isbn = input("Digite o ISBN do livro para remover: ")
            sucesso = biblioteca.remover_livro(isbn)
            if sucesso:
                print("Livro removido com sucesso.")
            else:
                print("Livro não encontrado.")

        elif escolha == "5":
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
