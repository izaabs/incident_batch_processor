# O objetivo desse arquivo é:
# transformar texto bagunçado em dados organizados
# Isso é parsing
# --------------------------------------------------

import re

# Função responsável por processar uma linha de incidente
def extrair_dados(linha):
    # Regex para capturar:
    # código do erro + descrição
    #
    # Exemplo:
    # ERROR 500 - timeout API_A
    #
    # (\d+) → captura números
    # (.+) → captura o restante da mensagem
    padrao = r"ERROR (\d+) - (.+)"
    resultado = re.search(padrao, linha)  # Procura o padrão dentro da linha

    if resultado:
        codigo = resultado.group(1)  # Grupo 1 → código do erro
        descricao = resultado.group(2)  # Grupo 2 → descrição do erro
        descricao_normalizada = descricao.lower()  # Normaliza texto para facilitar busca

        # Identifica sistema relacionado
        if "api_a" in descricao_normalizada:
            sistema = "API_A"

        elif "api_b" in descricao_normalizada:
            sistema = "API_B"

        else:
            sistema = "Desconhecido"

        # Identifica padrão do incidente
        if "timeout" in descricao_normalizada:
            padrao_incidente = "timeout"

        elif "token" in descricao_normalizada:
            padrao_incidente = "autenticação"
        
        elif "pagamento" in descricao_normalizada:
            padrao_incidente = "pagamento"

        else:
            padrao_incidente = "outros"

        # Retorna tudo estruturado em formato de dicionário
        return {
            "codigo": codigo,
            "descricao": descricao,
            "sistema": sistema,
            "padrao_incidente": padrao_incidente
        }

    # Caso não encontre padrão
    return None  