import pandas as pd
from .interfaces import SentimentAnalyzerProvider
from .entities import SentimentResult
from .text_processor import TextCleaner  # <-- Importamos a nova classe

class SentimentBatchService:
    def __init__(self, analyzer: SentimentAnalyzerProvider):
        self._analyzer = analyzer

    def process_csv(self, input_path: str, text_column: str) -> pd.DataFrame:
        df = pd.read_csv(input_path)
        
        if text_column not in df.columns:
            raise ValueError(f"A coluna '{text_column}' não foi encontrada.")

        print(f"Limpando e processando {len(df)} linhas...")
        
        # A Mágica acontece aqui: limpamos o texto ANTES de analisar
        df['text_cleaned'] = df[text_column].apply(TextCleaner.clean)
        
        # Analisamos o texto já limpo
        results = df['text_cleaned'].apply(self._analyzer.analyze)
        
        df['sentiment_label'] = [r.label for r in results]
        df['sentiment_score'] = [r.score for r in results]
        df['analysis_at'] = [r.timestamp for r in results]
        
        return df