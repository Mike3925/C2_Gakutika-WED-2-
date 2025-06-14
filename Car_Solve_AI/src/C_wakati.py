import MeCab
#単に分かち書きする
wakati = MeCab.Tagger("-Owakati")
#辞書も表示して分かち書きする
tagger = MeCab.Tagger()

# print(wakati.parse("pythonが大好きです").split())
# print(tagger.parse("pythonが大好きです"))

def wakatiSentense(sentense):
  return wakati.parse(sentense).split()