# FarmTech Solutions - consulta meteorológica em R com a API Open-Meteo.

options(encoding = "UTF-8")
options(timeout = 30)


descrever_codigo_meteorologico <- function(codigo) {
  if (codigo == 0) {
    return("Céu limpo")
  } else if (codigo %in% c(1, 2, 3)) {
    return("Parcialmente nublado ou encoberto")
  } else if (codigo %in% c(45, 48)) {
    return("Nevoeiro")
  } else if (codigo %in% c(51, 53, 55)) {
    return("Garoa")
  } else if (codigo %in% c(56, 57)) {
    return("Garoa congelante")
  } else if (codigo %in% c(61, 63, 65)) {
    return("Chuva")
  } else if (codigo %in% c(66, 67)) {
    return("Chuva congelante")
  } else if (codigo %in% c(71, 73, 75, 77)) {
    return("Neve")
  } else if (codigo %in% c(80, 81, 82)) {
    return("Pancadas de chuva")
  } else if (codigo %in% c(85, 86)) {
    return("Pancadas de neve")
  } else if (codigo == 95) {
    return("Trovoada")
  } else if (codigo %in% c(96, 99)) {
    return("Trovoada com granizo")
  }

  "Condição não identificada"
}


consultar_clima <- function(latitude, longitude, local) {
  if (!requireNamespace("jsonlite", quietly = TRUE)) {
    cat("O pacote 'jsonlite' ainda não está instalado.\n")
    cat("Execute no terminal:\n")
    cat(
      "Rscript -e \"install.packages('jsonlite', ",
      "repos='https://cloud.r-project.org')\"\n",
      sep = ""
    )
    return(invisible(NULL))
  }

  variaveis <- paste(
    "temperature_2m",
    "relative_humidity_2m",
    "apparent_temperature",
    "precipitation",
    "wind_speed_10m",
    "weather_code",
    sep = ","
  )

  url <- paste0(
    "https://api.open-meteo.com/v1/forecast",
    "?latitude=", latitude,
    "&longitude=", longitude,
    "&current=", variaveis,
    "&timezone=America%2FSao_Paulo"
  )

  cat("\nConsultando a API meteorológica Open-Meteo...\n")

  resultado <- tryCatch(
    jsonlite::fromJSON(url),
    error = function(erro) {
      cat("Não foi possível consultar a API meteorológica.\n")
      cat("Detalhe:", erro$message, "\n")
      return(NULL)
    }
  )

  if (is.null(resultado)) {
    return(invisible(NULL))
  }

  if (is.null(resultado$current) || is.null(resultado$current_units)) {
    cat("A API respondeu, mas não retornou as condições atuais esperadas.\n")
    return(invisible(NULL))
  }

  clima <- resultado$current
  unidades <- resultado$current_units
  descricao <- descrever_codigo_meteorologico(clima$weather_code)

  cat("\n==================================================\n")
  cat(" INFORMAÇÕES METEOROLÓGICAS\n")
  cat("==================================================\n")
  cat("Local:", local, "\n")
  cat("Data e hora local:", clima$time, "\n")
  cat(
    "Temperatura:", clima$temperature_2m,
    unidades$temperature_2m, "\n"
  )
  cat(
    "Sensação térmica:", clima$apparent_temperature,
    unidades$apparent_temperature, "\n"
  )
  cat(
    "Umidade relativa:", clima$relative_humidity_2m,
    unidades$relative_humidity_2m, "\n"
  )
  cat(
    "Precipitação:", clima$precipitation,
    unidades$precipitation, "\n"
  )
  cat(
    "Velocidade do vento:", clima$wind_speed_10m,
    unidades$wind_speed_10m, "\n"
  )
  cat("Condição meteorológica:", descricao, "\n")
  cat("Código WMO:", clima$weather_code, "\n")
  cat("Fonte dos dados: Open-Meteo (https://open-meteo.com/)\n")

  invisible(resultado)
}


# Coordenadas de Ribeirão Preto, importante região agrícola de São Paulo.
consultar_clima(
  latitude = -21.1775,
  longitude = -47.8103,
  local = "Ribeirão Preto - SP"
)
