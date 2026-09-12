# FarmTech Solutions - análise estatística dos dados gerados pelo Python.

options(encoding = "UTF-8")


obter_diretorio_script <- function() {
  argumentos <- commandArgs(trailingOnly = FALSE)
  argumento_arquivo <- grep("^--file=", argumentos, value = TRUE)

  if (length(argumento_arquivo) > 0) {
    caminho <- sub("^--file=", "", argumento_arquivo[1])
    return(dirname(normalizePath(caminho, winslash = "/")))
  }

  getwd()
}


formatar_numero <- function(valor, casas = 2) {
  if (is.na(valor)) {
    return("não aplicável (é necessário ter ao menos 2 registros)")
  }

  format(
    round(valor, casas),
    nsmall = casas,
    decimal.mark = ",",
    big.mark = "."
  )
}


desvio_padrao_seguro <- function(valores) {
  valores_validos <- valores[!is.na(valores)]

  if (length(valores_validos) < 2) {
    return(NA_real_)
  }

  sd(valores_validos)
}


diretorio_script <- obter_diretorio_script()
caminho_csv <- file.path(diretorio_script, "dados_plantios.csv")

if (!file.exists(caminho_csv)) {
  stop(
    paste0(
      "Arquivo dados_plantios.csv não encontrado em: ",
      diretorio_script,
      "\nExecute primeiro o programa farmtech.py."
    ),
    call. = FALSE
  )
}

dados <- tryCatch(
  read.csv(
    caminho_csv,
    header = TRUE,
    sep = ";",
    dec = ".",
    stringsAsFactors = FALSE,
    fileEncoding = "UTF-8",
    check.names = FALSE
  ),
  error = function(erro) {
    stop(
      paste("Não foi possível ler o arquivo CSV:", erro$message),
      call. = FALSE
    )
  }
)

colunas_obrigatorias <- c(
  "cultura",
  "area_hectares",
  "quantidade_insumo",
  "unidade_insumo"
)

colunas_ausentes <- setdiff(colunas_obrigatorias, names(dados))
if (length(colunas_ausentes) > 0) {
  stop(
    paste(
      "O CSV não possui as colunas obrigatórias:",
      paste(colunas_ausentes, collapse = ", ")
    ),
    call. = FALSE
  )
}

if (nrow(dados) == 0) {
  cat("Não existem registros para análise.\n")
  quit(save = "no", status = 0)
}

dados$area_hectares <- as.numeric(dados$area_hectares)
dados$quantidade_insumo <- as.numeric(dados$quantidade_insumo)

cat("\n==================================================\n")
cat(" ANÁLISE ESTATÍSTICA - FARMTECH SOLUTIONS\n")
cat("==================================================\n")
cat("Quantidade total de plantios:", nrow(dados), "\n")

cat("\n--- ESTATÍSTICAS GERAIS DAS ÁREAS ---\n")
cat(
  "Área média:",
  formatar_numero(mean(dados$area_hectares, na.rm = TRUE), 4),
  "ha\n"
)
cat(
  "Desvio-padrão das áreas:",
  formatar_numero(desvio_padrao_seguro(dados$area_hectares), 4),
  "ha\n"
)
cat(
  "Área mínima:",
  formatar_numero(min(dados$area_hectares, na.rm = TRUE), 4),
  "ha\n"
)
cat(
  "Área máxima:",
  formatar_numero(max(dados$area_hectares, na.rm = TRUE), 4),
  "ha\n"
)

cat("\n--- ESTATÍSTICAS POR CULTURA ---\n")

for (nome_cultura in sort(unique(dados$cultura))) {
  grupo <- dados[dados$cultura == nome_cultura, ]
  unidade <- unique(grupo$unidade_insumo)
  unidade_texto <- paste(unidade, collapse = "/")

  cat("\nCultura:", nome_cultura, "\n")
  cat("Quantidade de registros:", nrow(grupo), "\n")
  cat(
    "Área média:",
    formatar_numero(mean(grupo$area_hectares, na.rm = TRUE), 4),
    "ha\n"
  )
  cat(
    "Desvio-padrão da área:",
    formatar_numero(desvio_padrao_seguro(grupo$area_hectares), 4),
    "ha\n"
  )
  cat(
    "Quantidade média de insumo:",
    formatar_numero(mean(grupo$quantidade_insumo, na.rm = TRUE), 2),
    unidade_texto,
    "\n"
  )
  cat(
    "Desvio-padrão do insumo:",
    formatar_numero(desvio_padrao_seguro(grupo$quantidade_insumo), 2),
    unidade_texto,
    "\n"
  )
}

cat("\n--- RESUMO DAS ÁREAS EM HECTARES ---\n")
print(summary(dados$area_hectares))

cat("\nObservação: os insumos são analisados separadamente por cultura,\n")
cat("pois não é correto calcular uma média misturando litros e quilogramas.\n")
