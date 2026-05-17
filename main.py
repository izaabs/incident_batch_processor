# Esse arquivo funciona como pipeline:
# entrada → processamento → classificação → saída estruturada
# -------------------------------------------------------------

import os
import json
from parser import extrair_dados

resultados = [] # Lista que armazenará todos os resultados processados
pasta_incidentes = "incidentes" # Pasta onde os arquivos de incidentes estão

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta_incidentes):
    # Cria caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_incidentes, arquivo)

    try:
        # Abre arquivo para leitura
        with open(caminho_arquivo, "r", encoding="utf-8") as f:

            # Percorre linha por linha
            for linha in f:
                
                linha = linha.strip() # Remove espaços e quebras de linha
                incidente = extrair_dados(linha) # Envia linha para o parser

                # Se encontrou um incidente válido
                if incidente:

                    incidente["arquivo"] = arquivo   # Adiciona nome do arquivo ao resultado
                    codigo = int(incidente["codigo"]) # Converte código para inteiro

                    # Classifica severidade do incidente
                    if codigo >= 500:
                        incidente["severidade"] = "Alta"
                    
                    elif codigo >= 400:
                        incidente["severidade"] = "Média"

                    else:
                        incidente["severidade"] = "Baixa"

                    resultados.append(incidente) # Adiciona resultado à lista

    except Exception as e:
        # Caso aconteça algum erro durante leitura/processamento
        print(f"Erro ao processar arquivo {arquivo}: {e}")

# Salva saída final em JSON
with open("output.json", "w", encoding="utf-8") as saida:

    json.dump(
        resultados,
        saida,
        indent=4,
        ensure_ascii=False
    )

# Exibe resultado final
print("Processamento concluído. Resultados salvos em output.json")

# Mostra incidentes processados
for resultado in resultados:
    print(f"Arquivo: {resultado['arquivo']} | Código: {resultado['codigo']} | Sistema: {resultado['sistema']} | Padrão: {resultado['padrao_incidente']} | Severidade: {resultado['severidade']}")