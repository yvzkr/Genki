
from translate import Translator


def translateToTr(sentences="lütfen bir kelime gir."):
    """
    :param sentences:
    :return:
    """
    language="tr"
    translator = Translator(to_lang="tr")
    translation = translator.translate(sentences)
    return translation