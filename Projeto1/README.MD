Se necessário, para evitar conflitos crie um ambiente virtual env para fazer a instalação das dependências com:

Atenção certifique-se de estar na pasta do arquivo

python3 -m venv nome_da_venv

Por exemplo, para criar um ambiente chamado meu_env:

python3 -m venv meu_env

Isso criará uma pasta meu_env contendo os arquivos necessários.

3. Ative o ambiente virtual**
- macOS/Linux:

  source meu_env/bin/activate

- Windows:

  meu_env\Scripts\activate


Após ativado, o terminal mostrará (meu_env), indicando que você está dentro do ambiente virtual.


Para rodar esse código, certifique de ter todas as dependencias instaladas em sua máquina, caso contrário instale-as com o seguinte comando: pip install -r requirements.txt



em seguida rode o código com py main.py  ou python3 main.py
