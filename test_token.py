# import MeCab

# mt = MeCab.Tagger()
# parsed = mt.parse("pythonが大好きです")
# x = (parsed.replace('\n', '\t').split('\t'))

# print(parsed)

import spacy

nlp = spacy.load('ja_ginza')
doc1 = nlp('猫を飼う')
doc2 = nlp('靴を買う')

for sent in doc1.sents:
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