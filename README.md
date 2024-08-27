Este programa é um sistema de pedidos para uma copiadora, onde o cliente pode escolher um serviço, o número de páginas e, opcionalmente, serviços extras. Aqui está uma descrição passo a passo do que o programa faz.

Funções do Programa.

escolha_servico():

Esta função exibe um menu para o usuário escolher o tipo de serviço que deseja.

DIG: Digitalização, que custa R$ 1,10 por página.

ICO: Impressão colorida, que custa R$ 1,00 por página.

IPB: Impressão preto e branco, que custa R$ 0,40 por página.

FOT: Fotocópia, que custa R$ 0,20 por página.

O usuário é solicitado a escolher um serviço digitando o código correspondente. A função retorna o custo por página para o serviço escolhido. A função inclui um loop while para continuar pedindo uma entrada válida caso o usuário insira uma opção inválida.

num_paginas():

Esta função calcula o custo total com base no número de páginas, aplicando descontos conforme a quantidade.

Sem desconto para 1 a 19 páginas.

15% de desconto para 20 a 199 páginas.

20% de desconto para 200 a 1.999 páginas.

Fixo a R$ 75 para 2.000 a 19.999 páginas.

A função verifica a quantidade de páginas inserida pelo usuário e retorna o custo total após aplicar o desconto apropriado. Se o número de páginas for fora do intervalo aceito, o usuário é solicitado a inserir um número válido.

servico_extra():

Esta função permite ao usuário escolher um serviço adicional.

Encadernação Simples: R$ 15,00.

Encadernação Capa Dura: R$ 40,00.

Ou nenhum serviço extra.

A função retorna o custo do serviço extra escolhido ou 0 se o usuário não desejar nenhum serviço adicional. Inclui tratamento de erros para garantir que o usuário insira uma opção válida.
Funcionamento Geral do Programa.

Escolha do Serviço.

O programa chama escolha_servico() para obter o custo por página do serviço escolhido pelo usuário.

Entrada do Número de Páginas.

O usuário é solicitado a inserir o número de páginas que deseja processar. Este valor é usado pela função num_paginas() para calcular o custo total das páginas após os descontos.

Escolha de Serviços Extras.

O programa chama servico_extra() para permitir que o usuário adicione serviços extras, se desejado.

Cálculo do Total.

O custo total é calculado multiplicando o custo por página pelo número de páginas, após aplicar o desconto, e adicionando o custo do serviço extra.
Finalmente, o programa exibe o total detalhado, incluindo o custo do serviço, o número de páginas, e quaisquer extras.
