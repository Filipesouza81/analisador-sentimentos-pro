import sys
from pathlib import Path

# Garante que o Python encontre o código na pasta src
sys.path.append(str(Path(__file__).parent / "src"))

from sentiment_analyzer.models.huggingface_provider import HuggingFaceAnalyzer
from sentiment_analyzer.core.services import SentimentBatchService

def main():
    # 1. Inicializa os componentes (Injeção de Dependência)
    model = HuggingFaceAnalyzer()
    service = SentimentBatchService(model)
    
    print("\n--- Analisador de Sentimentos Profissional ---")
    print("1. Analisar frase única")
    print("2. Analisar ficheiro CSV (Lote)")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        texto = input("Digite a frase para análise: ")
        res = model.analyze(texto)
        print(f"\nResultado: {res.label} (Confiança: {res.score:.2%})")
        print(f"Data da análise: {res.timestamp}")
    
    elif opcao == "2":
        path = input("Caminho do ficheiro CSV: ")
        coluna = input("Nome da coluna que contém os textos: ")
        
        try:
            df_resultado = service.process_csv(path, coluna)
            output_path = "resultado_analise.csv"
            df_resultado.to_csv(output_path, index=False)
            print(f"\n✅ Sucesso! O resultado foi guardado em: {output_path}")
        except Exception as e:
            print(f"\n❌ Erro ao processar o ficheiro: {e}")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()