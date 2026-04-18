import re

class TextCleaner:
    """
    Classe responsável por normalizar o texto antes da IA processar.
    Remove ruídos comuns que podem confundir o modelo.
    """
    
    @staticmethod
    def clean(text: str) -> str:
        if not isinstance(text, str):
            return ""

        # 1. Converte para minúsculas
        text = text.lower()
        
        # 2. Remove links (http, https, www)
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # 3. Remove menções (@usuario) e hashtags (#)
        text = re.sub(r'\@\w+|\#','', text)
        
        # 4. Remove múltiplos espaços em branco
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text