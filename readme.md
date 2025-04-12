# Banco Python

Este é um simples sistema de banco em Python que permite realizar três operações principais: depósito, saque e extrato. O sistema armazena transações e fornece um extrato detalhado das operações realizadas, com controle de limites de saque e saques diários.

## Funcionalidades

- **Depositar**: Permite adicionar dinheiro à conta.
- **Sacar**: Permite retirar dinheiro da conta, com restrições de limite diário e limite máximo de saque.
- **Extrato**: Exibe um histórico das transações realizadas, incluindo depósitos e saques, além do saldo atual.

## Como usar

1. Clone este repositório em sua máquina:

    ```bash
    git clone https://github.com/seuusuario/banco-python.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd banco-python
    ```

3. Execute o script Python:

    ```bash
    python banco.py
    ```

4. O menu será exibido, permitindo que você escolha entre as opções:

    - **1** para depositar
    - **2** para sacar
    - **3** para visualizar o extrato
    - **4** para sair

## Como funciona

Ao iniciar o programa, o menu principal será exibido com as opções disponíveis. O usuário pode selecionar uma das opções para realizar as operações desejadas:

- **1 para depositar**: Permite adicionar dinheiro à conta.
- **2 para sacar**: Permite retirar dinheiro da conta, respeitando os limites estabelecidos.
- **3 para visualizar o extrato**: Exibe o histórico de transações e o saldo atual.
- **4 para sair**: Encerra o programa.

### Detalhes das Operações

#### Depósito

Ao escolher a opção de depósito, o usuário poderá informar o valor, que será adicionado ao saldo da conta. O depósito será registrado no extrato com o valor correspondente.

#### Saque

O usuário pode realizar saques, mas com as seguintes limitações:

- **Saldo insuficiente**: O valor solicitado não pode ser superior ao saldo disponível.
- **Limite de saque excedido**: O valor solicitado não pode ultrapassar o limite de R$500,00 por saque.
- **Limite de saques diários excedido**: O usuário pode realizar no máximo 3 saques por dia.

#### Extrato

O extrato lista todas as transações realizadas (depósitos e saques) e o saldo atual da conta. O número de saques e depósitos é exibido, juntamente com o saldo atualizado.

## Estrutura do Código

- **`menu()`**: Exibe o menu principal e retorna a opção escolhida pelo usuário.
- **`depositar()`**: Realiza o depósito e registra a transação, verificando se o valor é positivo.
- **`saque()`**: Realiza o saque e verifica as condições de saldo, limite e saques diários.
- **`extrato()`**: Exibe o extrato com o histórico das transações e o saldo atual.

## Exemplo de Execução

### Menu Principal

--------------------------------------------
                     Banco Python
--------------------------------------------

--------------------------------------------
                     [1] Depositar
                     [2] Sacar
                     [3] Extrato
                     [4] Sair
--------------------------------------------

--------------------------------------------
                     Digite uma opção:
--------------------------------------------


### Exemplo de Depósito


--------------------------------------------
                                Depósito:
--------------------------------------------

Digite o valor do depósito: 100.00

-------------------------------------------------------
Depósito de 100.00 realizado com sucesso!

Saldo atual: R$ 100.00
-------------------------------------------------------


### Exemplo de Saque


--------------------------------------------
                                Saque:
--------------------------------------------

Saldo atual: R$ 100.00

Digite o valor do saque: 50.00

----------------------------------------------------
Saque de 50.00 realizado com sucesso!
-----------------------------------------------------


### Exemplo de Extrato


--------------------------------------------
                                Extrato:
--------------------------------------------

Depósito: R$ 100.00
Saque: R$ 50.00

-----------------------------------------------
                Extrato do dia:

          => Total de depósitos: 1
          => Total de saques: 1
          => Saldo atual: R$ 50.00
------------------------------------------------


## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no projeto.
