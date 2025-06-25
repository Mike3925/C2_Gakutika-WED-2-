import fugashi
# from B3_output import MeCabParser

# #単に分かち書きする
# wakati = MeCab.Tagger()
# #辞書も表示して分かち書きする
# print(wakati.parse("").split())
# print(tagger.parse("pythonがホームランを売った").split())



def wakatiSentence(sentence):
  tagger = fugashi.Tagger()
  # nouns = [word.feature.lemma for word in tagger(sentence) if (word.feature.pos1 != "助詞" and word.feature.pos1 != "補助記号")]
  nouns = [word.surface for word in tagger(sentence) if (word.feature.pos1 != "助詞" and word.feature.pos1 != "補助記号")]
  # print(tagger(sentence))
  # print("--- 名詞リスト ---")
  # print(nouns)
  out = ""
  for i in range(len(nouns)):
    if nouns[i] != None:
      if (i == len(nouns) - 1):
        out = out + nouns[i]
      else:
        out = out + nouns[i] + " "
  return out

  

print(wakatiSentence("警察官のAとBのような腕による手信号は、矢印の方向からの車に対しては同じ意味を表わしている。"))

