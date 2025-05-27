import os
import shutil
import xml.etree.ElementTree as ET

# Caminho da pasta com os XMLs
PASTA_XMLS = r"C:\Users\itarg\Downloads\1200 TOME ACU\1200" 

# Namespace dos arquivos
NAMESPACE_EVT = {'evt': 'http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_03_00'}

# Função para extrair o valor do <perApur>
def extrair_perapur(caminho_xml):
    try:
        tree = ET.parse(caminho_xml)
        root = tree.getroot()
        perapur = root.find('.//evt:evtRemun/evt:ideEvento/evt:perApur', NAMESPACE_EVT)
        return perapur.text if perapur is not None else None
    except Exception as e:
        print(f"Erro ao processar {caminho_xml}: {e}")
        return None

# Processar todos os XMLs
for nome_arquivo in os.listdir(PASTA_XMLS):
    if nome_arquivo.endswith(".xml"):
        caminho_arquivo = os.path.join(PASTA_XMLS, nome_arquivo)
        perapur = extrair_perapur(caminho_arquivo)

        if perapur:
            pasta_destino = os.path.join(PASTA_XMLS, perapur)
            os.makedirs(pasta_destino, exist_ok=True)

            novo_caminho = os.path.join(pasta_destino, nome_arquivo)
            shutil.move(caminho_arquivo, novo_caminho)
            print(f"Arquivo '{nome_arquivo}' movido para a pasta '{perapur}'.")
        else:
            print(f"⚠️ Não encontrado <perApur> em '{nome_arquivo}'.")

