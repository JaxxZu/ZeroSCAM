# Bert模型部署教學



1. 下載檔案 xxxx(to be finish)，並解壓縮

```
└── Bert_model
    ├── fine_tuned_bert_model
    │   ├── config.json
    │   ├── model.safetensors
    │   ├── special_tokens_map.json
    │   ├── tokenizer_config.json
    │   └── vocab.txt
    └── server.py
```

2. 安裝必要套件

```
pip install torch transformers flask
```

3. 執行程式Bert\_model\server.py

{% code overflow="wrap" %}
```json
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
 * Running on http://x.x.x.x:5000 (公網ip，如有)
```
{% endcode %}

{% hint style="success" %}
有以下警告是正常的

* WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
{% endhint %}

5.打開ZeroSCAM APP的設定，將詐騙機率檢測模型設定成電腦的ip位址，並使用錄音功能，電腦(server)顯示以下訊息即代表成功運行後端:

<pre><code><strong>[127.0.0.1] - - [15/Feb/2025 11:35:27] "POST /predict HTTP/1.1" 200 -
</strong>[127.0.0.1] - - [15/Feb/2025 11:35:36] "POST /predict HTTP/1.1" 200 -
</code></pre>

