
import re

def extrair_dados_fatura(texto):
    try:
        nome_unidade = re.search(r"Unidade Consumidora: (.+)", texto).group(1).strip()
        numero_instalacao = re.search(r"Nº da Instalação: (\d+)", texto).group(1).strip()
        vencimento = re.search(r"Vencimento: (\d{2}/\d{2}/\d{4})", texto).group(1).strip()
        valor_total = float(re.search(r"Total a Pagar.*?R\$\s*([\d,.]+)", texto).group(1).replace('.', '').replace(',', '.'))
        iof = float(re.search(r"IOF.*?R\$\s*([\d,.]+)", texto).group(1).replace('.', '').replace(',', '.'))
        competencia = re.search(r"Referente a:\s*(\w+\/\d{4})", texto).group(1).strip()
        numero_conta = re.search(r"Nº da Conta:\s*(\d+)", texto).group(1).strip()

        return {
            "nome_unidade": nome_unidade,
            "numero_instalacao": numero_instalacao,
            "vencimento": vencimento,
            "valor_total": valor_total,
            "iof": iof,
            "competencia": competencia,
            "numero_conta": numero_conta
        }
    except Exception:
        return None
