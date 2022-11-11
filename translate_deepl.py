import os
from dotenv import load_dotenv
import deepl

load_dotenv()
DEEPL_API_KEY = os.environ["DEEPL_API_KEY"]

text = "DeepLの翻訳技術を使って日本語を英語に翻訳します。"

traslator = deepl.Translator(DEEPL_API_KEY)

result = traslator.translate_text(text, target_lang="EN-US")
print(result.text)
