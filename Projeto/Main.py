class Main: # Declara uma classe.
    pass # Utiliza-se quando nenhuma estrutura será definida no corpo dessa classe.

from Cliente import Cliente # Importa a classe Cliente do código Cliente.
from Conta import Conta

# c1 = Cliente("João", "9299956-4513") # Após criarmos a referência da classe, adicionamos, na linha seguinte, o novo objeto, passando por parâmetro os valores para inicialização dos atributos.
                                     # c1: A declaração de um novo objeto funciona como declarar uma nova variável.
                                     # Cliente: Passamos o nome da classe que será instanciada.
                                     # Passamos todos os atributos criados no Método Construtor da classe Cliente. (Parâmetros)

# print(c1) # Imprime a referência do objeto (id). Será apresentado o ID do objeto.
# print(c1.nome, "e", c1.telefone) # Imprime o conteúdo adicionado. Será exibido o conteúdo do objeto.

# conta = Conta(c1._nome, 6565, 0)

# print(conta.titular, "Numero:", conta.numero, "Seu saldo:", conta.saldo)

c1 = Cliente("Yan", "9298456-1734")
conta = Conta(c1.get_nome(), 1222, 0)

conta.depositar(100)
conta.saque(50)
conta.extrato()
