# undergraduate-research-2024

Repositório para iniciação cientifica da FIAP (2024).

A ideia principal é construir uma solução baseada em IA que sirva de apoio ao médico dentro do consultório.

À partir disso, todos os recursos que desenvolvermos, funcionará tal como módulos integrativos dentro dessa solução.

Assim, teremos um MVP com um módulo para análise de imagens médicas de diferentes segmentos do corpo, começando pelas mãos, e, posteriormente, adicionaremos outros módulos assistivos para o médico, como um módulo para captação de voz entre a conversa do médico-paciente para elaboração do diagnóstico do paciente, agilizando o processo  de preescrição de receitas e afins.

Por fim, como os dados estão em domínio da nossa solução, o histórico dos pacientes poderá ser compartilhados entre diferentes hospitais à partir da adoção da solução, de tal modo que o histórico do paciente poderia ser facilmente consultado.

## Fluxograma
![Cenário 1](https://github.com/LeandroLuna/undergraduate-research-2024/assets/29809108/34566a78-abe8-45a0-915a-7ad746974c88)

<hr>

![Cenário 2](https://github.com/LeandroLuna/undergraduate-research-2024/assets/29809108/a19f3ef8-0e39-4aed-85df-034e56547535)

## Tecnologias

CNN: YOLO, U-NET e/ou Densenet.

Python.

Class Activation Maps (CAMs).

Tensorflow, Keras, Numpy, Pandas.

FastAPI.

Docker.

## Arquitetura

![Arquitetura](https://github.com/LeandroLuna/undergraduate-research-2024/assets/29809108/f3e35c3c-c7b7-4332-a319-e46421abeb6a)

Explicação:

1. O médico envia a imagem, seja por meio de um microcontrolador ou pela web, para um API Gateway.

2. O API Gateway repassa a requisição, juntamente com os dados da imagem, para uma API construída com FastAPI. A escolha do FastAPI se deu pela capacidade de gerar documentação automaticamente, sem necessidade de muita configuração. Após a correta autorização do usuário, a API realiza uma consulta no banco de dados RDS (Relational Database Service). Nesta etapa, a imagem é processada conforme os requisitos do modelo de deep learning.

5. Se os dados forem encontrados no RDS, ou seja, se a consulta já tiver sido feita anteriormente, a inferência previamente processada é retornada ao médico. Caso contrário, a requisição é encaminhada para um modelo pré-treinado de deep learning, que está armazenado em formato H5 utilizando o Keras e carregado em uma instância EC2. Esta instância EC2 está configurada em um Auto Scaling Group (ASG) e balanceada por um Elastic Load Balancer (ELB). O treinamento com as novas imagens será realizado por meio de uma tarefa agendada no CRON para ocorrer a cada duas semanas ou mensalmente. Essa tarefa pode ser implementada usando uma função serverless, como Lambda.

6. Após a conclusão da inferência, os dados resultantes são salvos no banco de dados, e o resultado é apresentado ao médico. Vale ressaltar que apenas os metadados são armazenados no banco de dados. As imagens são armazenadas em um sistema de hospedagem de BLOB, neste caso, o Amazon S3.

7. Além disso, é possível realizar novas análises dos dados conectando o Amazon Athena ou o Amazon QuickSight aos dados do RDS.

## Dataset

Se vamos apenas classificar (fraturado ou não fraturado), podemos utilizar os dados do dataset MURA. Este dataset é mais simples e ligeiramente mais volumoso:

[Paper](https://arxiv.org/pdf/1712.06957)

[Stanford AIMI Shared Datasets](https://stanfordaimi.azurewebsites.net/datasets/3e00d84b-d86e-4fed-b2a4-bfe3effd661b)

O MURA contém 2.185 imagens, distribuídas da seguinte forma:

- Treinamento:
- - 1497 não fraturadas
- - 521 fraturadas.
- Validação:
- - 101 não fraturadas.
- - 66 fraturadas.
  
<hr>

Se pretendemos segmentar (identificar o tipo/grau de fratura) no nosso projeto, consideramos utilizar os dados abaixo:

[Paper](https://www.nature.com/articles/s41597-023-02432-4)

[figshare - FracAtlas: A Dataset for Fracture Classification, Localization and Segmentation of Musculoskeletal Radiographs](https://figshare.com/articles/dataset/The_dataset/22363012)

Este dataset possui 1.538 imagens de mãos, sendo 437 fraturadas. Inclui imagens nos planos Coronal (frontal), Transversal (superior) e Sagital (lateral).

Observações:

- É possível combinar ambos os datasets para aumentar o volume de dados.
- Em ambos os datasets, é necessário realizar um pré-processamento para manter apenas as imagens de radiografias das mãos.
