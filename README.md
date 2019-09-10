# django_crypto_chat

## Proposta
O objetivo do aplicativo "Crypto Chat", é fazer com que as pessoas se comuniquem de forma ampla e segura, logo o mesmo criptografaria todas as mensagens enviadas e recebidas, de forma que a mensagem
só apareceria para quem a mesma foi direcionada. O projeto também busca possibilitar o envio de imagens, vídeos e documentos em diversos formatos, todos de forma criptografada.


### Pré-requesitos
É necessario que você possua em seu computador uma pasta com um `virtualenv` ativo em algum diretório do seu computador, caso não tenha, siga os passos a seguir:

```sh
$ python3.7 -m venv env
$ source env/bin/activate
```

### Instalação

Primeiramente, tenha certeza de estar ultilizando a versão mais recento do **Python** será preciso ter todos os arquivos necessários em seu computador, para isso copie o link do projeto e depois execute o comando "git clone" no terminal, assim o programa será instalado em sua máquina.

```
$ git clone https://github.com/AdrielHigor/django_crypto_chat.git
```

Depois de terminar esta etapa, é preciso que o executar a instalação das bibliotecas necessárias para rodar o projeto `requirements.txt` .Execute o seguinte comando:

```sh
(venv)$$ pip install -r requirements.txt
```

Or

```sh
(venv)$ python -m pip install -r requirements.txt
```

### DataBase

Com tudo isso instalado, é hora de configurar a conexão com o banco de dados.Na pasta `/crypto_chat/settings` estão as configurações do banco de dados que podem ser alteradas ou ultilizadas para a criação de um banco de dados com o postgresql. 

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crypto_chat',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

### Migrations

Com todos os passos anteriores feitos com sucesso, agora será preciso aplicar o comando `makemigrations` e `migrate`.

```sh
(venv)$ cd 'path_to_project'/django_crypto_chat
(venv)$ python manage.py makemigrations core
(venv)$ python manage.py makemigrations chat
(venv)$ python manage.py migrate
```

### Criando um administrador

Para ter acesso às ferramentas de administrador do sistema, é preciso criar uma conta como `superuser`, assim como mostra o exemplo:

```sh
(venv)$ python manage.py createsuperuser
```


### Iniciando o servidor

Por fim, o que será acertado a se fazer é iniciar o funcionamento do servidor com o comando `runserver`.

```sh
(venv)$ cd django_crypto_chat
(venv)$ python manage.py runserver
```

## Desenvolvido com

*[Python](https://www.python.org) - Linguagem de programação
*[Django](https://www.djangoproject.com) - O web framework ultilizado

## Autores

* **Adriel Higor Rodrigues Lins da Silva**
* **Davi Meireles de Brito**
* **Daniel Artur Jacobino**
* **Guiherme Moreira Lira**
* **Isaque Gomes Dantas**



