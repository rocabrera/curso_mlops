# Container

Normalmente não basta desenvolver o software, precisamos colocar ele para funcionar para os clientes, processo chamado de **deploy** em produção. Logo é interessante desenvolver da mais reprodutivel possível, porque voce vai precisar reproduzir a execução da sua aplicação em algum servidor. 

A utilização de ambientes virtuais é o começo, o ambiente virtual permite a gente fixar os pacotes utilizados, mas as vezes a aplicação **depende** de alguma peculiaridade que não está relacionada a linguagem de programação que estamos utilizando, por exemplo uma variável de ambiente. Nesta aula vamos aprender sobre containers, tecnologia qual vai permitir tornar nosso desenvolvimento ainda mais reprodutivel, escalavel e maleavel para mudanças de hardware (como exemplo, trocar uma aplicação da cloud X para Y).

Atualmente, precisamos realizar o deploy de diferentes tipos de software, como bancos de dados relacionais, serviços de fila, endpoints, entre outros. No entanto, há diversas opções de hardware disponíveis, desde laptops até servidores robustos. Os containers oferecem uma padronização que permite a execução desses serviços de maneira intercambiável em diferentes hardwares. De forma análoga, existe a padronização de transporte de produtos via containers, conforme mostra a Figura 1. 

<center><img src="figures/containers.png" width=350></center>

Esses produtos (softwares) são colocados em containers (padronização) que são transportados por navios de diferentes marcas e modelos (diferentes hardwares), portanto qualquer meio capaz de transportar containers é capaz de movimentar esses produtos (realizar o deploy).

Basicamente, se voce construir um container que funciona na sua máquina local seu código vai funcionar em qualquer lugar. A ferramenta mais famosa para construir esses containers é o Docker.

Quando utilizamos Docker existem três principais conceitos para aprendermos:

- Imagens: Conceitualmente similares a Classes.
- Layers: Conceitualmente similares a Herança.
- Containers: Conceitualmente similares a objetos instanciados por uma classe.

Assim como os pacotes python ficam em um indice, as imagens docker ficam salvas em um *container registry*, o mais conhecido chama[docker hub](https://hub.docker.com), mas existem *container registry* proprietários, por exemplo a AWS (do inglês, Amazon Web Service) tem um serviço chamado ECR (do inglês, Elastic Container Registry).

Primeiro instale o docker no seu sistema operacional (Se voce estiver utilizando o CodeSpace não precisa, ele ja vem instalado). Quando voce digitar no terminal o comando ```docker verison``` deve aparecer algo semelhante a seguinte mensagem: ```Docker version 24.0.2, build cb74dfc```.

A maioria dos comandos do docker vão seguir o seguinte padrão:
- ```docker <command> <sub-command> [options]```
Porém alguns comandos podem seguir o padrão antigo:
- ```docker <sub-command> [options]```
De qualquer forma a maioria dos comandos são retrocompativeis com versões anteriores, logo voce pode encontrar na internet alguns comandos diferentes do apresentado nessa aula que fazem a mesma coisa.

As principais categorias de comando são:
- image
- container
- volume
- network

Nesta aula não vamos explorar os comandos relacionados a network pois eles são mais avançados. Para cada categoria existe um conjunto de subcomandos, como exemplo:

- docker image ls
- docker images ls
- docker container ls
- docker network ls
- docker volume ls

Vamos agora construir nossa primeira imagem. Elas funcionam como uma receita, isto é uma sequência de comandos em uma ordem especifica. Ela normalmente começa com o comando ```FROM```, como exemplo:

> FROM python:3.9

Coloque esse conteudo em um arquivo chamado **MyFirstDockerfile** e execute o seguinte comando (Estamos falando, vamos buildar a imagem que está no diretório local, com nome de arquivo igual a MyFirstDockerfile):

- docker image build -f MyFirstDockerfile .

Caso a sua imagem (arquivo com o comando FROM) esteja em outro diretório execute este comando (Estamos falando, vamos buildar a imagem que está no diretório dockerfolder, com nome de arquivo igual a MyFirstDockerfile):

- docker image build -f ./dockerfolder/MyFirstDockerfile dockerfolder

Vai aparecer algo no seu terminal semelhante a Figura 2. 
<center><img src="figures/build_image.png" width=450></center>

Agora vamos ver essa imagem com o comando:

- docker image ls

Vai aparecer algo no seu terminal semelhante a Figura 3.
<center><img src="figures/image_ls_command.png" width=450></center>

Perceba que ela tem uma propriedade chamada **IMAGE ID** e toda vez que precisarmos nos referencias a essa imagem precisamos saber o ID. Entretanto, voce pode dar um apelido para essa imagem usando o parametro -t, como mostra o seguinte comando:

- docker image build -f MyFirstDockerfile -t my_image .

Vai aparecer algo no seu terminal semelhante a Figura 4.

<center><img src="figures/image_tag_param.png" width=450></center>

Usualmente utilizamos o nome de arquivo default Dockerfile e executamos o comando no mesmo diretório do arquivo. Assim sendo, o comando fica:

- docker image build .

Com a imagem criada podemos criar containers com base nela (a analogia é que o container é uma instancia e a imagem é uma classe).

- docker container run my_image

Perceba que aparentemente nada aconteceu, mas se voce digitar o comando:

- docker container ps -a 

Vai aparecer no terminal algo semelhante a  Figura 5. Assista a aula para entender todos os campos.
<center><img src="figures/docker_container_run.png" width=450></center>

Agora vamos criar outro container, mas dessa vez adicionando o parametro ```--rm```:

- docker container run --rm my_image

Essa flag indica que o container deve ser deletado após terminar sua execução (normalmente falado, após sair do container). As vezes pode ser interessante utilizar essa flag para não poluir o ambiente com um monte de container, mas depende de caso a caso. Assista a aula para saber mais sobre.