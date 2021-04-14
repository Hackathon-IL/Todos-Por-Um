# Todos-Por-Um

## Guia de Uso do Docker

### Instalação
Primeiramente é necessário ter o docker instalado, caso não tenha acesse o [Instalação docker](https://docs.docker.com/engine/installation/linux/docker-ce/). Após feito isso, instale o [Docker-compose](https://docs.docker.com/compose/install/).

### Utilizando o ambiente

&emsp;&emsp; Para a utilização do ambiente, basta dar o comando abaixo e ele irá ligar o container:
 
 ```terminal
  docker-compose up -d
 ```

 &emsp;&emsp; Após isso, é necessário acessar o container usando o comando abaixo:
 ```terminal
  docker-compose exec web bash
 ```

  &emsp;&emsp; Em seguida, ao entrar no bash do container, utilize o seguinte comando para subir as migrations:
 ```terminal
  ./manage.py migrate
 ```

&emsp;&emsp; em caso dos arquivos criados ficarem sem permissão use:

```
sudo chown -R $USER:$USER .
```
 &emsp;&emsp; Para a visualização dos logs use o comando abaixo:
 ```terminal
  docker-compose logs -f
 ```

 &emsp;&emsp; Para parar o container use o comando abaixo:
 
  ```terminal
  docker-compose stop
 ```
 &emsp;&emsp; E para religar um container parado use o comando: 
 
 ```terminal
  docker-compose start
 ```

 &emsp;&emsp; Caso deseje remover um container:
 ```terminal
  docker-compose down
 ```

[tutorial](https://docs.docker.com/compose/django/)