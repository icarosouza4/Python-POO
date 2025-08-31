# Projeto inicial.

class Cliente: # Declara uma classe.
    def __init__(self, n, fone): # O termo def é utilizada para a declaração de método.
                                 # O termo __init__ é um método especial que será chamado sempre que criarmos um objeto de classe.
                                 # O termo self é um parâmetro que exporta as características do objeto.
        self._nome = n # Com o parâmetro self são passados os parâmetros que serão utilizados para inicialização dos atributos.
        self._telefone = fone # Inicializamos os atributos com os valores passados por parâmetro.

    # Método get - Sempre retornam valores.
    def get_nome(self):
        return self._nome

    # Método set - Recebem valores por parâmetros.
    def set_nome(self, nome):
        self._nome = nome

