## Alguns comandos usado na configuração da base para um projeto python


#### Instalando o pre-commit -> Criar arquivo .pre-commit-config.yaml. Ele irá corrigir conforme hooks antes de commitar
```shell
# pip install pre-commit
# pre-commit install # Gravar as configurações na pasta .git para que de fato funcione os hooks no momento do commit
```


#### Instalando o pylint
```shell
# pip install pylint
# pylint --generate-rcfile  > .pylintrc
```

#### Instalando o black
```shell
# pip install black
```

#### Instalando o flake8
```shell
# pip install flake8
```

#### comandos o fastapi
```shell
pip install fastapi\[all]
uvicorn server:app --reload

```

#### Log de commits
```shell
# git log --oneline
```


