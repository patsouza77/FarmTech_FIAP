# Roteiro de demonstração - duração máxima de 5 minutos

Antes de gravar, aumente a fonte do terminal, desative notificações e feche
janelas que possam revelar dados pessoais. O arquivo `dados_plantios.csv` já
possui quatro registros para que os cálculos estatísticos tenham uma amostra
adequada.

## 0:00 a 0:25 - Apresentação

> Olá. Este é o projeto FarmTech Solutions. Desenvolvemos uma aplicação em
> Python para cadastrar plantios de soja e milho, calcular áreas e manejo de
> insumos, além de uma análise estatística e uma consulta meteorológica em R.

## 0:25 a 2:45 - Aplicação Python

Execute:

```bash
python farmtech.py
```

### Cadastro de soja - opção 1

Use estes valores para facilitar a explicação:

```text
Talhão: S-VIDEO
Comprimento: 100
Largura: 50
Quantidade de ruas: 20
Comprimento de cada rua: 100
Dosagem: 2
```

Explique brevemente:

> A área retangular é de 5.000 metros quadrados, ou meio hectare. Para 20 ruas
> de 100 metros e dosagem de 2 mililitros por metro, são necessários 4 litros
> de herbicida.

### Cadastro de milho - opção 2

```text
Talhão: M-VIDEO
Base maior: 120
Base menor: 80
Altura: 100
Dosagem: 250
```

Explique que a área trapezoidal é de 10.000 m², equivalente a 1 hectare, e que
a quantidade calculada é de 250 kg de fertilizante.

Em seguida:

1. Use a opção **3** para mostrar a saída e as posições do vetor.
2. Use a opção **4**, selecione a posição do `S-VIDEO`, pressione Enter nos
   dados que serão mantidos e altere a dosagem para `3`. Mostre o recálculo.
3. Use a opção **5** e exclua o registro `M-VIDEO`, digitando `S` para confirmar.
4. Use a opção **6** para salvar e sair.

> Confira na listagem qual posição foi atribuída aos novos registros; com o CSV
> original, normalmente serão as posições 4 e 5.

## 2:45 a 3:35 - Estatística em R

Execute:

```bash
Rscript analise_estatistica.R
```

> O R lê o mesmo CSV produzido pelo Python e calcula quantidade de registros,
> média, desvio-padrão, mínimo e máximo das áreas. Os insumos são separados por
> cultura porque a soja usa litros e o milho usa quilogramas.

## 3:35 a 4:25 - API meteorológica em R

Execute:

```bash
Rscript clima_api.R
```

> Esta é a parte Ir além. O código R envia uma requisição à API pública
> Open-Meteo, recebe JSON, processa o código da condição meteorológica e exibe
> as informações atuais de Ribeirão Preto em texto no terminal.

Mostre temperatura, umidade, precipitação e vento.

## 4:25 a 4:50 - Encerramento

> Assim, o projeto atende às duas culturas, cálculos geométricos e de insumos,
> vetor, entrada, saída, atualização, deleção, loops, decisões, estatística em R,
> API meteorológica e versionamento colaborativo no GitHub. Obrigado.

Pare a gravação antes de cinco minutos. Assista ao arquivo uma vez antes de
publicá-lo como **Não listado** no YouTube.
