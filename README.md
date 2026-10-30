# Programming Logic Algorithms

Este repositório reúne minhas resoluções para uma lista de exercícios de lógica de programação proposta na faculdade. Os exercícios são desenvolvidos em Python e praticam conceitos fundamentais da linguagem.

## Exercício: condicionais

O script `conditionals.py` solicita o valor unitário e a quantidade de um produto e calcula o valor total. A partir desse total, aplica um desconto progressivo: quanto maior o valor da compra, maior o desconto; compras abaixo do valor mínimo definido no exercício não recebem desconto.

O exercício demonstra o uso de estruturas condicionais em Python. O `if` verifica a primeira condição, os `elif` permitem testar outras faixas quando as anteriores não são atendidas, e o `else` cobre o caso restante. Assim, o programa escolhe uma única regra de desconto para cada compra.

O programa exibe os valores total e com desconto. Se a entrada não for numérica ou inteira conforme solicitado, ele pede os dados novamente.

## Como executar

É necessário ter o Python 3 instalado. No terminal, na pasta do repositório, execute:

```bash
python conditionals.py
```

Em alguns sistemas, o comando pode ser `python3 conditionals.py`.
