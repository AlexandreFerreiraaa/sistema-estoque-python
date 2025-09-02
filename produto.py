class Produto:
    def __init__(self, codigo, nome, categoria, quantidade, preco, descricao, fornecedor):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor

    def __str__(self):
        return f"{self.codigo} - {self.nome} | Estoque: {self.quantidade} | Preço: R${self.preco:.2f}"
