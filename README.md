# Translation from Python using the API at DeepL

We will use the API to operate DeepL, the world's best machine translation using cutting-edge AI technology. deepl's library allows us to write less than the usual POST code written in Python, so this time we will add practical code to read the API key from .env.

最先端のAI技術を使った世界最高レベルの機械翻訳のDeepLをAPIで操作します。deeplのライブラリを使うとPythonで書く通常のPOSTのコードよりも記述量を少なくできるので、今回は.envからAPIキーを読み込ませる実践的なコードを追加します。

- Python 3.9.1

## Usage / 使い方

### Install Library form requirements.txt.

requirements.txtからライブラリをインストール


	pip install -r requirements.txt

### Specify API key in .env

.envにAPIキーを指定

    touch .env
	DEEPL_API_KEY=YOURAPIKEY
	
## Sample usage / 実行方法

	python translate_deepl.py

## Result / 結果
"DeepLの翻訳技術を使って日本語を英語に翻訳します。"

↓ 

"Translate Japanese into English using the translation technology at DeepL."


## Author / 作成者

- [Fantom, Inc. (JP)](https://twitter.com/Fantomcojp)