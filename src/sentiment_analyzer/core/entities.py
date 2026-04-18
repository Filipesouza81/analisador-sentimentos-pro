from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class SentimentResult:
    text: str
    label: str
    score: float
    timestamp: datetime = datetime.now()