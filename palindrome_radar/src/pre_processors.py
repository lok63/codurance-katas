from abc import abstractmethod, ABC
import spacy


class AbstractPreprocessor(ABC):

    @abstractmethod
    def lower_case(self, text: str) -> str:
        """Convert text to lowercase"""
        pass

    @abstractmethod
    def remove_punctuation(self, text: str) -> str:
        """
        Any character other than alphanumeric characters are classed as punctuation
        """
        pass

    def pre_process(self, word: str) -> str:
        """Apply all preprocessing steps to the input text"""
        text = self.lower_case(word)
        text = self.remove_punctuation(text)
        return text


class BasicPreprocessor(AbstractPreprocessor):

    def lower_case(self, word: str) -> str:
        """Lower-case all letters"""
        return word.lower()

    def remove_punctuation(self, word: str) -> str:
        """ """
        return "".join([c for c in word if c.isalnum()])


class SpacyPreprocessor(AbstractPreprocessor):

    def __init__(self, model_name: str = "es_core_news_md"):
        """Initialize with a spaCy model"""
        try:
            self.nlp = spacy.load(model_name)
        except OSError:
            raise ValueError(
                f"SpaCy model '{model_name}' not found. Install with: python -m spacy download {model_name}"
            )

    def lower_case(self, text: str) -> str:
        """Convert text to lowercase using spaCy token normalization"""
        doc = self.nlp(text)
        return "".join([token.lower_ for token in doc])

    def remove_punctuation(self, text: str) -> str:
        """Remove punctuation using spaCy's linguistic analysis"""
        doc = self.nlp(text)
        result = ""
        for token in doc:
            for char in token.text:
                if char.isalnum():
                    result += char
        return result
