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

## Dataset

Se fomos ter somente classificação (fraturado ou não fraturado), podemos utilizar os dados do dataset Mura. Ele é mais simples e ligeiramente mais volumoso:

[Paper](https://arxiv.org/pdf/1712.06957)

[Stanford AIMI Shared Datasets](https://stanfordaimi.azurewebsites.net/datasets/3e00d84b-d86e-4fed-b2a4-bfe3effd661b)

Possui 2185 imagens, onde:
- Treino:
- - 1497 não fraturadas
- - 521 fraturadas.
- Validação:
- - 101 não fraturadas.
- - 66 fraturadas.
  
<hr>

Se fomos ter segmentação (qual tipo da fratura) no nosso projeto, pensar na utilização dos dados abaixo:

[Paper](https://www.nature.com/articles/s41597-023-02432-4)

[figshare - FracAtlas: A Dataset for Fracture Classification, Localization and Segmentation of Musculoskeletal Radiographs](https://figshare.com/articles/dataset/The_dataset/22363012)

Esse dataset possui 1.538 imagens de mãos, onde 437 são fraturadas. Nesse segundo dataset, temos imagens do tipo Coronal (de frente), Transversal (de cima) e Sagital (de lado).

OBS.: É possível unir ambos os datasets para ter um maior volume de dados. 
OBS. 2: Em ambos os datasets, precisa fazer um pré-processamento dos dados para deixar somente as imagens de X-RAY das mãos. 
