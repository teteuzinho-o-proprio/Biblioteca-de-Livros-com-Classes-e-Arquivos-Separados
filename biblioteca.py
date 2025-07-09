from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def remover_livro(self, isbn: str):
        for i, livro in enumerate(self.livros):
            if livro.isbn == isbn:
                del self.livros[i]
                return True
        return False

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)

    def buscar_livro(self, titulo: str):
        encontrados = []
        for livro in self.livros:
            if titulo.lower() in livro.titulo.lower():
                encontrados.append(livro)
        return encontrados
