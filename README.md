# undergraduate-research-2024

Repositório para iniciação cientifica da FIAP (2024).

Detecção de fraturas nas mãos em imagens X-RAY. 

## Fluxograma
![Cenário 1](https://github.com/LeandroLuna/undergraduate-research-2024/assets/29809108/34566a78-abe8-45a0-915a-7ad746974c88)

<hr>

![Cenário 2](https://github.com/LeandroLuna/undergraduate-research-2024/assets/29809108/a19f3ef8-0e39-4aed-85df-034e56547535)

## Tecnologias

CNN, YOLO e U-NET.

Python.

Class Activation Maps (CAMs).

Densenet.

Tensorflow, Keras, Numpy, Pandas.

FastAPI.

## Arquitetura

![Arquitetura](https://github.com/LeandroLuna/undergraduate-research-2024/assets/29809108/f3e35c3c-c7b7-4332-a319-e46421abeb6a)

Explicação:

1. O médico envia a imagem, seja por meio de um microcontrolador ou pela web, para um API Gateway.

2. O API Gateway repassa a requisição, juntamente com os dados da imagem, para uma API construída com FastAPI. A escolha do FastAPI se deu pela capacidade de gerar documentação automaticamente, sem necessidade de muita configuração. Após a correta autorização do usuário, a API realiza uma consulta no banco de dados RDS (Relational Database Service). Nesta etapa, a imagem é processada conforme os requisitos do modelo de deep learning.

5. Se os dados forem encontrados no RDS, ou seja, se a consulta já tiver sido feita anteriormente, a inferência previamente processada é retornada ao médico. Caso contrário, a requisição é encaminhada para um modelo pré-treinado de deep learning, que está armazenado em formato H5 utilizando o Keras e carregado em uma instância EC2. Esta instância EC2 está configurada em um Auto Scaling Group (ASG) e balanceada por um Elastic Load Balancer (ELB). 

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
