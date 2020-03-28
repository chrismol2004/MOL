"""
16.	A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
17.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
18.	Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
19.	Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
20.	Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
21.	Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
22.	Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
23.	Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
24.	Faça um programa que calcule o mostre a média aritmética de N notas.
25.	Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
26.	Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
27.	Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
28.	Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
29.	O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
o	Lojas Quase Dois - Tabela de preços
o	1 - R$ 1.99
o	2 - R$ 3.98
o	...
o	50 - R$ 99.50
30.	O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
o	Preço do pão: R$ 0.18
o	Panificadora Pão de Ontem - Tabela de preços
o	1 - R$ 0.18
o	2 - R$ 0.36
o	...
o	50 - R$ 9.00
31.	O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
o	Lojas Tabajara
o	Produto 1: R$ 2.20
o	Produto 2: R$ 5.80
o	Produto 3: R$ 0
o	Total: R$ 9.00
o	Dinheiro: R$ 20.00
o	Troco: R$ 11.00
o	...
32.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
o	Fatorial de: 5
o	5! =  5 . 4 . 3 . 2 . 1 = 120
33.	O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
34.	Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
35.	Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
36.	Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
o	Montar a tabuada de: 5
o	Começar por: 4
o	Terminar em: 7

o	Vou montar a tabuada de 5 começando em 4 e terminando em 7:
o	5 X 4 = 20
o	5 X 5 = 25
o	5 X 6 = 30
o	5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
37.	Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
38.	Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
a.	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
b.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
c.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
39.	Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
40.	Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a.	Código da cidade;
b.	Número de veículos de passeio (em 1999);
c.	Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d.	Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e.	Qual a média de veículos nas cinco cidades juntas;
f.	Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
41.	Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
o	Os juros e a quantidade de parcelas seguem a tabela abaixo:
o	Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
o	1       0
o	3       10
o	6       15
o	9       20
o	   12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
42.	Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
43.	O cardápio de uma lanchonete é o seguinte:
o	Especificação   Código  Preço
o	Cachorro Quente 100     R$ 1,20
o	Bauru Simples   101     R$ 1,30
o	Bauru com ovo   102     R$ 1,50
o	Hambúrguer      103     R$ 1,20
o	Cheeseburguer   104     R$ 1,30
o	Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
44.	Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
o	1 , 2, 3, 4  - Votos para os respectivos candidatos
o	(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
o	5 - Voto Nulo
o	6 - Voto em Branco
Faça um programa que calcule e mostre:
o	O total de votos para cada candidato;
o	O total de votos nulos;
o	O total de votos em branco;
o	A percentagem de votos nulos sobre o total de votos;
o	A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
45.	Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
a.	Maior e Menor Acerto;
b.	Total de Alunos que utilizaram o sistema;
c.	A Média das Notas da Turma.
d.	Gabarito da Prova:
o	01 - A
o	02 - B
o	03 - C
o	04 - D
o	05 - E
o	06 - E
o	07 - D
o	08 - C
o	09 - B
o	10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
"""