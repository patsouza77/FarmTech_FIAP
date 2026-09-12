"""FarmTech Solutions - cadastro e manejo de plantios.

Projeto acadêmico desenvolvido apenas para demonstrar conceitos de Python.
As dosagens informadas não constituem recomendação agronômica.
"""

import csv
from pathlib import Path


# O enunciado solicita dados organizados em vetores. Em Python, a estrutura
# equivalente usada neste projeto é uma lista; cada posição contém um dicionário.
plantios = []

ARQUIVO_CSV = Path(__file__).resolve().parent / "dados_plantios.csv"

COLUNAS_CSV = [
    "id",
    "talhao",
    "cultura",
    "figura",
    "comprimento_m",
    "largura_m",
    "base_maior_m",
    "base_menor_m",
    "altura_m",
    "area_m2",
    "area_hectares",
    "insumo",
    "dosagem",
    "unidade_dosagem",
    "numero_ruas",
    "comprimento_rua_m",
    "quantidade_insumo",
    "unidade_insumo",
]

CAMPOS_INTEIROS = {"id", "numero_ruas"}
CAMPOS_DECIMAIS = {
    "comprimento_m",
    "largura_m",
    "base_maior_m",
    "base_menor_m",
    "altura_m",
    "area_m2",
    "area_hectares",
    "dosagem",
    "comprimento_rua_m",
    "quantidade_insumo",
}


def ler_texto_obrigatorio(mensagem):
    """Lê um texto e não aceita conteúdo vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("O texto não pode ficar vazio.")


def ler_float(mensagem):
    """Lê e valida um número decimal maior que zero."""
    while True:
        try:
            valor = float(input(mensagem).strip().replace(",", "."))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número maior que zero.")


def ler_inteiro(mensagem):
    """Lê e valida um número inteiro maior que zero."""
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro maior que zero.")


def ler_texto_opcional(mensagem, valor_atual):
    """Mantém o texto atual quando o usuário pressiona Enter."""
    texto = input(f"{mensagem} [{valor_atual}]: ").strip()
    return texto if texto else valor_atual


def ler_float_opcional(mensagem, valor_atual):
    """Lê um decimal opcional, mantendo o valor atual com Enter."""
    while True:
        entrada = input(f"{mensagem} [{valor_atual:g}]: ").strip()
        if not entrada:
            return valor_atual
        try:
            valor = float(entrada.replace(",", "."))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número ou pressione Enter.")


def ler_inteiro_opcional(mensagem, valor_atual):
    """Lê um inteiro opcional, mantendo o valor atual com Enter."""
    while True:
        entrada = input(f"{mensagem} [{valor_atual}]: ").strip()
        if not entrada:
            return valor_atual
        try:
            valor = int(entrada)
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um inteiro ou pressione Enter.")


def calcular_area_retangulo(comprimento, largura):
    """Retorna a área do retângulo em metros quadrados e hectares."""
    area_m2 = comprimento * largura
    return area_m2, area_m2 / 10_000


def calcular_area_trapezio(base_maior, base_menor, altura):
    """Retorna a área do trapézio em metros quadrados e hectares."""
    area_m2 = ((base_maior + base_menor) * altura) / 2
    return area_m2, area_m2 / 10_000


def calcular_herbicida_litros(numero_ruas, comprimento_rua, dosagem_ml_metro):
    """Calcula o herbicida em litros a partir da dosagem linear."""
    quantidade_ml = numero_ruas * comprimento_rua * dosagem_ml_metro
    return quantidade_ml / 1_000


def calcular_fertilizante_kg(area_hectares, dosagem_kg_hectare):
    """Calcula o fertilizante em kg a partir da dosagem por hectare."""
    return area_hectares * dosagem_kg_hectare


def criar_registro_soja(
    identificador,
    talhao,
    comprimento,
    largura,
    numero_ruas,
    comprimento_rua,
    dosagem_ml_metro,
):
    """Monta e retorna um registro completo de plantio de soja."""
    area_m2, area_hectares = calcular_area_retangulo(comprimento, largura)
    quantidade_litros = calcular_herbicida_litros(
        numero_ruas, comprimento_rua, dosagem_ml_metro
    )

    return {
        "id": identificador,
        "talhao": talhao,
        "cultura": "Soja",
        "figura": "Retângulo",
        "comprimento_m": comprimento,
        "largura_m": largura,
        "base_maior_m": 0.0,
        "base_menor_m": 0.0,
        "altura_m": 0.0,
        "area_m2": area_m2,
        "area_hectares": area_hectares,
        "insumo": "Herbicida líquido",
        "dosagem": dosagem_ml_metro,
        "unidade_dosagem": "mL/metro linear",
        "numero_ruas": numero_ruas,
        "comprimento_rua_m": comprimento_rua,
        "quantidade_insumo": quantidade_litros,
        "unidade_insumo": "litros",
    }


def criar_registro_milho(
    identificador,
    talhao,
    base_maior,
    base_menor,
    altura,
    dosagem_kg_hectare,
):
    """Monta e retorna um registro completo de plantio de milho."""
    area_m2, area_hectares = calcular_area_trapezio(
        base_maior, base_menor, altura
    )
    quantidade_kg = calcular_fertilizante_kg(
        area_hectares, dosagem_kg_hectare
    )

    return {
        "id": identificador,
        "talhao": talhao,
        "cultura": "Milho",
        "figura": "Trapézio",
        "comprimento_m": 0.0,
        "largura_m": 0.0,
        "base_maior_m": base_maior,
        "base_menor_m": base_menor,
        "altura_m": altura,
        "area_m2": area_m2,
        "area_hectares": area_hectares,
        "insumo": "Fertilizante granulado",
        "dosagem": dosagem_kg_hectare,
        "unidade_dosagem": "kg/hectare",
        "numero_ruas": 0,
        "comprimento_rua_m": 0.0,
        "quantidade_insumo": quantidade_kg,
        "unidade_insumo": "kg",
    }


def proximo_id():
    """Retorna o próximo identificador disponível."""
    return 1 if not plantios else max(item["id"] for item in plantios) + 1


def ler_bases_trapezio():
    """Lê bases válidas e garante que a base maior não seja a menor."""
    while True:
        base_maior = ler_float("Base maior do trapézio, em metros: ")
        base_menor = ler_float("Base menor do trapézio, em metros: ")
        if base_maior >= base_menor:
            return base_maior, base_menor
        print("A base maior deve ser maior ou igual à base menor. Tente novamente.")


def cadastrar_soja():
    """Solicita os dados e cadastra um plantio de soja."""
    print("\n=== CADASTRO DE SOJA ===")
    talhao = ler_texto_obrigatorio("Identificação do talhão: ")

    print("\n--- Área retangular ---")
    comprimento = ler_float("Comprimento da área, em metros: ")
    largura = ler_float("Largura da área, em metros: ")

    print("\n--- Manejo do herbicida ---")
    numero_ruas = ler_inteiro("Quantidade de ruas da lavoura: ")
    comprimento_rua = ler_float("Comprimento de cada rua, em metros: ")
    dosagem = ler_float("Dosagem do herbicida, em mL por metro linear: ")

    registro = criar_registro_soja(
        proximo_id(),
        talhao,
        comprimento,
        largura,
        numero_ruas,
        comprimento_rua,
        dosagem,
    )
    plantios.append(registro)
    salvar_csv()

    print("\nPlantio de soja cadastrado com sucesso.")
    exibir_resumo_registro(registro)


def cadastrar_milho():
    """Solicita os dados e cadastra um plantio de milho."""
    print("\n=== CADASTRO DE MILHO ===")
    talhao = ler_texto_obrigatorio("Identificação do talhão: ")

    print("\n--- Área trapezoidal ---")
    base_maior, base_menor = ler_bases_trapezio()
    altura = ler_float("Altura do trapézio, em metros: ")

    print("\n--- Manejo do fertilizante ---")
    dosagem = ler_float("Dosagem do fertilizante, em kg por hectare: ")

    registro = criar_registro_milho(
        proximo_id(), talhao, base_maior, base_menor, altura, dosagem
    )
    plantios.append(registro)
    salvar_csv()

    print("\nPlantio de milho cadastrado com sucesso.")
    exibir_resumo_registro(registro)


def exibir_resumo_registro(plantio):
    """Exibe os dados principais de um registro."""
    print(f"Área: {plantio['area_m2']:.2f} m²")
    print(f"Área: {plantio['area_hectares']:.4f} ha")
    print(
        "Insumo necessário: "
        f"{plantio['quantidade_insumo']:.2f} "
        f"{plantio['unidade_insumo']}"
    )


def listar_plantios():
    """Exibe todos os registros e suas posições no vetor."""
    print("\n=== PLANTIOS CADASTRADOS ===")
    if not plantios:
        print("Nenhum plantio foi cadastrado.")
        return

    for posicao, plantio in enumerate(plantios):
        print("-" * 64)
        print(f"Posição no vetor: {posicao}")
        print(f"ID: {plantio['id']}")
        print(f"Talhão: {plantio['talhao']}")
        print(f"Cultura: {plantio['cultura']}")
        print(f"Figura geométrica: {plantio['figura']}")

        if plantio["cultura"] == "Soja":
            print(
                "Dimensões: "
                f"{plantio['comprimento_m']:.2f} m × "
                f"{plantio['largura_m']:.2f} m"
            )
            print(
                f"Ruas: {plantio['numero_ruas']} × "
                f"{plantio['comprimento_rua_m']:.2f} m"
            )
        else:
            print(
                "Dimensões: bases de "
                f"{plantio['base_maior_m']:.2f} m e "
                f"{plantio['base_menor_m']:.2f} m; "
                f"altura de {plantio['altura_m']:.2f} m"
            )

        print(f"Área: {plantio['area_m2']:.2f} m²")
        print(f"Área: {plantio['area_hectares']:.4f} ha")
        print(f"Insumo: {plantio['insumo']}")
        print(
            f"Dosagem: {plantio['dosagem']:.2f} "
            f"{plantio['unidade_dosagem']}"
        )
        print(
            f"Quantidade necessária: {plantio['quantidade_insumo']:.2f} "
            f"{plantio['unidade_insumo']}"
        )
    print("-" * 64)


def selecionar_posicao(acao):
    """Solicita uma posição existente do vetor ou retorna None."""
    listar_plantios()
    if not plantios:
        return None

    try:
        posicao = int(input(f"\nDigite a posição que deseja {acao}: ").strip())
    except ValueError:
        print("Posição inválida. Digite um número inteiro.")
        return None

    if posicao < 0 or posicao >= len(plantios):
        print("Posição inexistente.")
        return None
    return posicao


def atualizar_plantio():
    """Atualiza qualquer registro escolhido pela posição no vetor."""
    posicao = selecionar_posicao("atualizar")
    if posicao is None:
        return

    atual = plantios[posicao]
    print("\nPressione Enter para manter o valor exibido entre colchetes.")
    talhao = ler_texto_opcional("Identificação do talhão", atual["talhao"])

    if atual["cultura"] == "Soja":
        comprimento = ler_float_opcional(
            "Comprimento da área em metros", atual["comprimento_m"]
        )
        largura = ler_float_opcional(
            "Largura da área em metros", atual["largura_m"]
        )
        numero_ruas = ler_inteiro_opcional(
            "Quantidade de ruas", atual["numero_ruas"]
        )
        comprimento_rua = ler_float_opcional(
            "Comprimento de cada rua em metros", atual["comprimento_rua_m"]
        )
        dosagem = ler_float_opcional(
            "Dosagem do herbicida em mL por metro", atual["dosagem"]
        )
        atualizado = criar_registro_soja(
            atual["id"],
            talhao,
            comprimento,
            largura,
            numero_ruas,
            comprimento_rua,
            dosagem,
        )
    else:
        while True:
            base_maior = ler_float_opcional(
                "Base maior em metros", atual["base_maior_m"]
            )
            base_menor = ler_float_opcional(
                "Base menor em metros", atual["base_menor_m"]
            )
            if base_maior >= base_menor:
                break
            print("A base maior deve ser maior ou igual à base menor.")

        altura = ler_float_opcional("Altura em metros", atual["altura_m"])
        dosagem = ler_float_opcional(
            "Dosagem do fertilizante em kg por hectare", atual["dosagem"]
        )
        atualizado = criar_registro_milho(
            atual["id"], talhao, base_maior, base_menor, altura, dosagem
        )

    plantios[posicao] = atualizado
    salvar_csv()
    print("\nPlantio atualizado com sucesso.")
    exibir_resumo_registro(atualizado)


def excluir_plantio():
    """Exclui um registro escolhido pela posição no vetor."""
    posicao = selecionar_posicao("excluir")
    if posicao is None:
        return

    selecionado = plantios[posicao]
    confirmacao = input(
        f"Excluir o talhão '{selecionado['talhao']}'? Digite S para confirmar: "
    ).strip().lower()

    if confirmacao != "s":
        print("Exclusão cancelada.")
        return

    removido = plantios.pop(posicao)
    salvar_csv()
    print(f"O plantio do talhão '{removido['talhao']}' foi excluído.")


def salvar_csv():
    """Persiste o vetor em CSV, inclusive quando estiver vazio."""
    try:
        with ARQUIVO_CSV.open("w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(
                arquivo, fieldnames=COLUNAS_CSV, delimiter=";"
            )
            escritor.writeheader()
            escritor.writerows(plantios)
    except OSError as erro:
        print(f"Não foi possível salvar o arquivo CSV: {erro}")


def converter_linha_csv(linha):
    """Converte os textos lidos do CSV para os tipos numéricos esperados."""
    convertida = dict(linha)
    for campo in CAMPOS_INTEIROS:
        convertida[campo] = int(convertida[campo])
    for campo in CAMPOS_DECIMAIS:
        convertida[campo] = float(convertida[campo])
    return convertida


def carregar_csv():
    """Carrega o CSV existente para o vetor no início do programa."""
    plantios.clear()
    if not ARQUIVO_CSV.exists():
        salvar_csv()
        return

    try:
        with ARQUIVO_CSV.open("r", newline="", encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo, delimiter=";")
            if leitor.fieldnames != COLUNAS_CSV:
                raise ValueError("o cabeçalho do CSV não corresponde ao esperado")
            for linha in leitor:
                plantios.append(converter_linha_csv(linha))
    except (OSError, ValueError, KeyError) as erro:
        plantios.clear()
        print(f"Aviso: não foi possível carregar o CSV ({erro}).")
        print("O programa continuará com o vetor vazio.")


def exibir_menu():
    """Exibe o menu principal."""
    print("\n" + "=" * 48)
    print(" FARMTECH SOLUTIONS - AGRICULTURA DIGITAL")
    print("=" * 48)
    print("1 - Cadastrar plantio de soja")
    print("2 - Cadastrar plantio de milho")
    print("3 - Listar plantios (saída de dados)")
    print("4 - Atualizar um plantio")
    print("5 - Excluir um plantio")
    print("6 - Sair do programa")
    print("=" * 48)


def executar_programa():
    """Controla o programa usando repetição e estruturas de decisão."""
    carregar_csv()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_soja()
        elif opcao == "2":
            cadastrar_milho()
        elif opcao == "3":
            listar_plantios()
        elif opcao == "4":
            atualizar_plantio()
        elif opcao == "5":
            excluir_plantio()
        elif opcao == "6":
            salvar_csv()
            print("\nDados salvos. Programa encerrado.")
            break
        else:
            print("\nOpção inválida. Escolha uma opção de 1 a 6.")


if __name__ == "__main__":
    try:
        executar_programa()
    except (KeyboardInterrupt, EOFError):
        salvar_csv()
        print("\nExecução interrompida. Os dados foram salvos.")
