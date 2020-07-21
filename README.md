# Script em Python para acessar o twitter, fazer login e rolar a home page automaticamente

# Requisitos
- Python 3.x
- Geckodriver -> instruções de instalação no site oficial (https://github.com/mozilla/geckodriver/releases)
- Firefox ou outro browser

# Instalando os requisitos listados no requirements.txt
- pip install -r requirements.txt

# Instruções
- dentro de main.py, temos algumas variáveis que você deverá preencher para que o login no Twitter funcione:
    ```
    TWITTER_USERNAME_OR_EMAIL = ""
    TWITTER_PASSWORD = ""
    ```
- temos a variável SLEEP_TIME_BEFORE_NEW_SCROLL para definir o tempo entre um scrool e outro, caso queira aumentar ou diminuir, apenas troque o valor 5 por outro 
- temos a variável LIMIT_LOOP_COUNTER para definir o máximo de scrools que usaremos para testes, caso queira aumentar ou diminuir, apenas troque o valor 10 por outro.

# Rodando o script
```
python webscraping.py
```

