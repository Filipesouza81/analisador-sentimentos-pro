from transformers import pipeline
from ..core.entities import SentimentResult
from ..core.interfaces import SentimentAnalyzerProvider

class HuggingFaceAnalyzer(SentimentAnalyzerProvider):
    def __init__(self, model_name: str = "finiteautomata/bertweet-base-sentiment-analysis"):
        # O pipeline baixa o modelo na primeira vez (~500MB)
        self._classifier = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, text: str) -> SentimentResult:
        raw_result = self._classifier(text)[0]
        return SentimentResult(
            text=text,
            label=raw_result['label'],
            score=raw_result['score']
        )