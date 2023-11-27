# TP1 - Grupo 6

**Integrantes do Grupo**:

- Gabriel Roger Amorim da Cruz: 200018248
- Iago de Paula Cabral: 190088745
- Joao Pedro de Camargo Vaz: 200020650
- Matheus Soares Arruda: 190093480
- Pedro Henrique Nogueira Gonçalves: 190094486
- Victor Hugo Oliveira Leão: 200028367
- Vinicius Assumpcao de Araujo: 200028472

## Entendimento do problema

### Diagrama

![Blank diagram](https://github.com/victorleaoo/tp1-g6-tppe/assets/33530818/c74d4cdd-e86f-48d6-9aa4-4e7cd04ab279)

### Funções a serem desenvolvidas

O trabalho deverá apresentar o emprego das três técnicas de TDD (falsificação, duplicação e triangulação) na implementação das seguintes funcionalidades:

* Cadastro de Produtos: 
  - Garantir que o produto está cadastrado no sistema informando
    obrigatoriamente o nome do produto, seu código de barras, preço de compra, 
    preço de venda e quantidade inicial em estoque. 
  - Se algum desses itens acima não for informando, garantir que o produto não
    seja cadastrado através do lançamento da exceção `DescricaoEmBrancoException`.
  - Se os valores de compra e venda e a quantidade de itens inicial em estoque
    for menor ou igual a zero, garantir que o item não seja cadastrado através
    do lançamento da exceção `ValorInvalidoException`.  
  
* Consulta de Estoque: 
  -  Garantir que o produto seja recuperado toda vez que ele for recuperado em
     buscas pelo seu nome ou pelo seu código de barras.

* Gestão de Transações:
  - Garantir que os seguintes tipos de transações sejam realizadas e os estoques dos produtos sejam atualizados: recebimento de mercadoria, vendas, transferências entre filiais, devoluções, ajustes de estoque. 
  - Garantir que não serão informadas quantidades negativas para as transações,
    exceto para ajustes de estoque. Nos outros casos, lançar exceções do tipo
`ValorInvalidoException`. 

* Alertas de Estoque Baixo:
  - Configuração de alertas automáticos que notificam os usuários quando os níveis de estoque de um produto atingem um limite mínimo predefinido, indicando a necessidade de reabastecimento.

* Rastreamento de Lotes e Validade:
  - Permite o rastreamento detalhado de lotes de produtos, especialmente útil para itens com data de validade. O sistema pode alertar sobre produtos próximos ao vencimento.

#### 

## Padrão de Commit

Para cada funcionalidade desenvolvida por meio do **TDD**, os *commits* devem ocorrer na seguinte ordem e seguindo o seguinte padrão:

- **falsificação**: git commit -m "falsificacao: <funcionalidade_desenvolvida>;
- **duplicação**: git commit -m "duplicação: <funcionalidade_desenvolvida>;
- **triangulação**: git commit -m "triangulação: <funcionalidade_desenvolvida>;

Todas as funcionalidades também devem conter **testes parametrizados**.
