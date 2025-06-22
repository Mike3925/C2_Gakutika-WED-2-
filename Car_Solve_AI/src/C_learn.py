# データの読み込み

import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv(r'Car_Solve_AI\data\data.csv')

# データの内容を先頭5行表示して確認
# print("--- データの先頭 ---")
# print(df.head())

# データ件数と、ラベルの分布を確認（0と1が何件ずつあるか）
# print("\n--- ラベルの分布 ---")
# print(df['label'].value_counts())

# テキストデータとラベルをそれぞれ変数に格納
X_text = df['text']
y = df['label']

# TF-IDFを利用したベクトル化

from sklearn.feature_extraction.text import TfidfVectorizer

# TfidfVectorizerを初期化
# analyzer='word' は単語単位で処理することを意味します（今回は既に分かち書き済なのでデフォルトでOK）
vectorizer = TfidfVectorizer()

# テキストデータ (X_text) をTF-IDFベクトルに変換
X_vec = vectorizer.fit_transform(X_text)

# 変換後のデータの形状を確認
# (文書数, ユニークな単語数) の形式になっている
# print("\n--- ベクトル化後のデータ形状 ---")
# print(X_vec.shape)

# データの分割

from sklearn.model_selection import train_test_split

# ベクトル化したデータとラベルを、訓練データとテストデータに分割
# test_size=0.2 は、20%をテストデータに使うという意味
# stratify=y は、分割後の訓練/テストデータでラベルの比率が元データと同じになるようにするオプション
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42, stratify=y
)

print("\n--- 分割後のデータサイズ ---")
print(f"訓練データ: {X_train.shape[0]}件")
print(f"テストデータ: {X_test.shape[0]}件")

# モデルの学習

from sklearn.linear_model import LogisticRegression

# ロジスティック回帰モデルを初期化
model = LogisticRegression()

# モデルを訓練データで学習させる
model.fit(X_train, y_train)

print("\n--- モデルの学習が完了しました ---")


#モデルの評価

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# テストデータを使って予測を行う
y_pred = model.predict(X_test)

# 1. 正解率 (Accuracy) の計算
accuracy = accuracy_score(y_test, y_pred)
print(f"\n正解率 (Accuracy): {accuracy:.4f}")

# 2. 適合率、再現率、F1スコアの表示
# これらは、特にラベルの分布に偏りがある場合に重要な指標
print("\n--- 分類レポート (Classification Report) ---")
print(classification_report(y_test, y_pred))

# 3. 混合行列 (Confusion Matrix) の表示
# どのような間違い方をしたかが分かる
print("\n--- 混合行列 (Confusion Matrix) ---")
print(confusion_matrix(y_test, y_pred))