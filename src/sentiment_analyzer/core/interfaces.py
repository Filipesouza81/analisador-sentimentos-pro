from typing import Protocol
from .entities import SentimentResult

class SentimentAnalyzerProvider(Protocol):
    """
    Define o contrato para qualquer motor de análise de sentimento.
    """
    def analyze(self, text: str) -> SentimentResult:
        ...