import re
from typing import Any, Dict, List, Text

from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.nlu.training_data import Message

from rasa.nlu.constants import TOKENS_NAMES, MESSAGE_ATTRIBUTES
# import MeCab
import spacy

nlp = spacy.load('ja_ginza')
doc = nlp('あのラーメン屋にはよく行く。美味しいんだ。')

for sent in doc.sents:
    for token in sent:
        info = [
            token.i,         # トークン番号
            token.orth_,     # テキスト
            token._.reading, # 読みカナ
            token.lemma_,    # 基本形
            token.pos_,      # 品詞
            token.tag_,      # 品詞詳細
            token._.inf      # 活用情報
        ]
        print(info)


class JapaneseTokenizer(Tokenizer):

    provides = [TOKENS_NAMES[attribute] for attribute in MESSAGE_ATTRIBUTES]

    def __init__(self, component_config: Dict[Text, Any] = None) -> None:
        super().__init__(component_config)
        # self.mt = MeCab.Tagger()
        nlp = spacy.load('ja_ginza')

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        text = message.get(attribute)
        parsed = self.mt.parse(text)
        x = (parsed.replace('\n', '\t').split('\t'))
        words = []
        for i in range(0, len(x) - 2, 2):
            w = x[i]
            words.append(w)

        running_offset=0
        tokens = []
        for word in words:
            word_offset = text.index(word, running_offset)
            word_len = len(word)
            running_offset = word_offset + word_len
            tokens.append(Token(word, word_offset))
        return tokens