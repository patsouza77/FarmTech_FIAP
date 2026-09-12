# FarmTech Solutions

Projeto acadêmico para apoiar a migração de uma fazenda para a Agricultura
Digital. A solução reúne uma aplicação de terminal em Python, análise
estatística em R e consulta a uma API meteorológica pública.

## Integrantes

> Antes da entrega, substitua esta observação pelos nomes e RM de todos os
> integrantes do grupo.

- Nome completo - RM
- Nome completo - RM
- Nome completo - RM
- Nome completo - RM

## Funcionalidades

- Cadastro de plantios de soja e milho.
- Cálculo da área retangular da soja em m² e hectares.
- Cálculo da área trapezoidal do milho em m² e hectares.
- Cálculo do herbicida líquido da soja em litros.
- Cálculo do fertilizante granulado do milho em quilogramas.
- Dados organizados no vetor `plantios`, uma lista de dicionários.
- Listagem, atualização por posição e exclusão de registros.
- Persistência e integração entre Python e R pelo arquivo CSV.
- Estatísticas gerais e por cultura em R.
- Consulta meteorológica à API Open-Meteo usando R.

As dosagens são informadas pelo usuário apenas para fins acadêmicos. Uma
aplicação real exigiria recomendação de profissional habilitado, considerando
cultura, produto, solo e demais condições da propriedade.

## Fórmulas utilizadas

### Soja - retângulo e herbicida

```text
área em m² = comprimento × largura
área em hectares = área em m² ÷ 10.000
herbicida em litros = ruas × comprimento da rua × dosagem em mL/m ÷ 1.000
```

### Milho - trapézio e fertilizante

```text
área em m² = (base maior + base menor) × altura ÷ 2
área em hectares = área em m² ÷ 10.000
fertilizante em kg = área em hectares × dosagem em kg/ha
```

## Estrutura

```text
FarmTechSolutions/
├── farmtech.py
├── analise_estatistica.R
├── clima_api.R
├── dados_plantios.csv
├── resumo_artigo.pdf
├── resumo_artigo_fonte.txt
├── video_youtube.txt
├── ROTEIRO_VIDEO.md
├── GUIA_CONFIGURACAO_WINDOWS.md
├── CHECKLIST_ENTREGA.md
├── README.md
├── .gitignore
└── tests/
    └── test_farmtech.py
```

## Pré-requisitos

- Python 3.11 ou superior.
- R 4.3 ou superior.
- Pacote `jsonlite` do R, usado somente na consulta meteorológica.
- Git para o versionamento colaborativo.

O Visual Studio Code é recomendado como editor, mas não é obrigatório. Não é
necessário instalar nenhuma ferramenta de IA para executar o projeto.

Consulte `GUIA_CONFIGURACAO_WINDOWS.md` para preparar um computador novo.

## Como executar

Abra o terminal dentro da pasta `FarmTechSolutions`.

### 1. Aplicação Python

```bash
python farmtech.py
```

Se o Windows não reconhecer `python`, tente:

```bash
py farmtech.py
```

O programa lê e atualiza automaticamente o arquivo `dados_plantios.csv`.

### 2. Testes automatizados do Python

```bash
python -m unittest discover -s tests -v
```

### 3. Instalação do pacote necessário no R

Execute uma única vez:

```bash
Rscript -e "install.packages('jsonlite', repos='https://cloud.r-project.org')"
```

### 4. Análise estatística

```bash
Rscript analise_estatistica.R
```

O script apresenta quantidade de registros, média, desvio-padrão, mínimo e
máximo das áreas. As quantidades de insumo são analisadas separadamente por
cultura para não misturar litros com quilogramas.

### 5. Consulta meteorológica

```bash
Rscript clima_api.R
```

O script consulta condições atuais de Ribeirão Preto - SP na Open-Meteo,
processa o código meteorológico e exibe temperatura, sensação térmica, umidade,
precipitação e velocidade do vento. As coordenadas podem ser alteradas no final
do arquivo `clima_api.R`.

Documentação da API: <https://open-meteo.com/en/docs>

## Trabalho colaborativo no GitHub

O histórico do repositório precisa mostrar colaboração real. Uma divisão
possível é:

1. Um integrante cria o repositório com `README.md` e `.gitignore`.
2. Um integrante adiciona `farmtech.py` e os testes em uma branch própria.
3. Outro adiciona `analise_estatistica.R` em outra branch.
4. Outro adiciona `clima_api.R` em outra branch.
5. Outro adiciona o resumo e a documentação em outra branch.
6. Cada branch gera um Pull Request, revisado por outro integrante antes do
   merge na `main`.

Exemplo de fluxo:

```bash
git checkout -b feature/estatistica-r
git add analise_estatistica.R
git commit -m "Implementa análise estatística dos plantios em R"
git push -u origin feature/estatistica-r
```

Depois do `push`, o integrante abre um Pull Request no GitHub. Cada pessoa deve
usar sua própria conta e efetivamente trabalhar na parte que assinar.

## Referências principais

- JORGE, Lúcio André de Castro; INAMASU, Ricardo Y. *Uso de veículos aéreos
  não tripulados (VANT) em Agricultura de Precisão*. Embrapa, 2014.
  <https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1003485/1/CAP8.pdf>
- Open-Meteo. *Weather Forecast API*. <https://open-meteo.com/en/docs>.
