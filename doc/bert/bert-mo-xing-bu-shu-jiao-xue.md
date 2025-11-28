# Bert模型部署教學



1. 下載檔案 ，並解壓縮

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

5.在手機上加入電腦的ip位址，並使用功能，開始錄音詐騙，電腦(server)便會顯示以下訊息:

<pre><code>High risk detected! Asking AI for advice...
External API Error: 400 Client Error: Bad Request for url: https://ai-anti-scam.443.gs/v1/chat/completions?token=7a4c019c-db87-4e21-b90e-9cfc75057f7e
<strong>[網域] - - [28/Nov/2025 14:35:27] "POST /predict?7a4c019c-db87-4e21-b90e-9cfc75057f7e HTTP/1.1" 200 -
</strong>High risk detected! Asking AI for advice...
External API Error: 400 Client Error: Bad Request for url: https://ai-anti-scam.443.gs/v1/chat/completions?token=7a4c019c-db87-4e21-b90e-9cfc75057f7e
[網域] - - [28/Nov/2025 14:35:36] "POST /predict?7a4c019c-db87-4e21-b90e-9cfc75057f7e HTTP/1.1" 200 -
</code></pre>

