from pythainlp.tokenize import word_tokenize


class TokenizeService:
    def tokenize(self, text: str) -> str:
        """
        Tokenize Thai text (and mixed Thai-English) using PyThaiNLP.
        Returns tokens joined by space.
        Engine 'newmm' handles mixed Thai-English well.
        """
        tokens = word_tokenize(text, engine="newmm", keep_whitespace=False)
        return " ".join(tokens)