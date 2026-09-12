# Configuração do notebook - Windows 10 ou 11

Este guia parte de um computador sem ferramentas de desenvolvimento. Instale
os programas usando somente as páginas oficiais.

## 1. Visual Studio Code

1. Acesse <https://code.visualstudio.com/Download>.
2. Baixe a versão **User Installer** para Windows.
3. Durante a instalação, marque as opções para adicionar ao PATH e para abrir
   pastas com o Visual Studio Code.

No VS Code, instale as extensões:

- **Python**, publicada pela Microsoft.
- **R**, publicada por REditorSupport (opcional, mas conveniente).

## 2. Python

1. Acesse <https://www.python.org/downloads/windows/>.
2. Baixe o instalador atual do Python 3.
3. Na primeira tela, marque **Add python.exe to PATH**.
4. Escolha **Install Now**.

Feche e abra novamente o VS Code. No terminal, confirme:

```powershell
python --version
```

Se `python` abrir a Microsoft Store, use o iniciador do Windows:

```powershell
py --version
```

## 3. R

1. Acesse <https://cran.r-project.org/bin/windows/base/>.
2. Baixe e instale a versão atual do R com as opções padrão.
3. Feche e abra novamente o VS Code.
4. Confirme no terminal:

```powershell
Rscript --version
```

Se o comando não for encontrado, localize a pasta semelhante a:

```text
C:\Program Files\R\R-4.x.x\bin
```

Pesquise no menu Iniciar por **Editar as variáveis de ambiente do sistema**,
abra **Variáveis de Ambiente**, selecione `Path`, clique em **Novo** e adicione
a pasta `bin` encontrada. Depois, reinicie o VS Code.

Instale o pacote usado pela API:

```powershell
Rscript -e "install.packages('jsonlite', repos='https://cloud.r-project.org')"
```

## 4. Git

1. Acesse <https://git-scm.com/download/win>.
2. Execute o instalador e mantenha as opções padrão.
3. Confirme:

```powershell
git --version
```

Configure seu nome e o mesmo e-mail usado no GitHub:

```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

## 5. Abrir e testar o projeto

1. Extraia o ZIP.
2. No VS Code, escolha **Arquivo > Abrir Pasta** e selecione
   `FarmTechSolutions`.
3. Abra **Terminal > Novo Terminal**.
4. Execute, nesta ordem:

```powershell
python -m unittest discover -s tests -v
python farmtech.py
Rscript analise_estatistica.R
Rscript clima_api.R
```

Se os seis testes mostrarem `OK`, o menu abrir normalmente, as estatísticas
forem impressas e o clima for exibido, o ambiente está pronto.

## Erros comuns

- **Comando não reconhecido:** reinicie o VS Code depois de instalar ou ajustar
  o PATH.
- **Pacote jsonlite ausente:** repita o comando de instalação do pacote.
- **CSV não encontrado:** mantenha `farmtech.py`, os dois scripts R e o CSV na
  mesma pasta.
- **API não responde:** confirme a conexão com a internet e tente novamente.
- **Acentos estranhos:** use o terminal integrado do VS Code ou o Windows
  Terminal e mantenha os arquivos em UTF-8.
