# 📚 Estudo OOP - Biblioteca de Livros

Este projeto é uma aplicação simples para gerenciar uma biblioteca, utilizando conceitos de **Programação Orientada a Objetos (OOP)** em Python.

---

## 🚀 O que foi feito?

- Criamos uma classe `Livro` que representa um livro com atributos como título, autor, ano e ISBN.
- Implementamos o método especial `__str__` para mostrar as informações do livro de forma amigável.
- Criamos uma classe `Biblioteca` que armazena uma lista de objetos `Livro` e possui métodos para:
  - Adicionar livros
  - Remover livros pelo ISBN
  - Listar todos os livros cadastrados
  - Buscar livros pelo título (busca parcial)
- Organizei o código em arquivos separados para manter o projeto limpo e modular:
  - `livro.py` — contém a classe `Livro`
  - `biblioteca.py` — contém a classe `Biblioteca`
  - `main.py` — script principal com menu interativo para o usuário interagir com a biblioteca
- Implementamos um menu no terminal para adicionar, listar, buscar e remover livros de forma interativa.

---

## 🛠 Tecnologias utilizadas

- Python 3.x
- Programação Orientada a Objetos (classes, métodos especiais)
- Manipulação básica de listas
- Modularização com múltiplos arquivos Python

---

## 🎯 Como usar

1. Clone este repositório:

```bash
git clone https://github.com/teteuzinho-o-proprio/Biblioteca-de-Livros-com-Classes-e-Arquivos-Separados.git
cd estudo_OOP_biblioteca
