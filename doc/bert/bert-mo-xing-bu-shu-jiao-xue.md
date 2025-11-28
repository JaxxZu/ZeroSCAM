# bert模型部署教學



1. 下載檔案:fine\_tuned\_bert\_model\_drive\_1，model，並解壓縮
2.  將fine\_tuned\_bert\_model\_drive\_1 裡面的五個檔案覆蓋掉model\model\fine\_tuned\_bert\_model裡的五個檔案<br>

    ```
    └── model
        ├── api.py
        ├── data.csv
        ├── fine_tuned_bert_model <-覆蓋此資料夾(名稱記得不變)
        │   ├── config.json
        │   ├── model.safetensors
        │   ├── special_tokens_map.json
        │   ├── tokenizer_config.json
        │   └── vocab.txt
        └── server.py
    ```
3.  開啟model\model\server.py，下載必要檔案(requirements)\
    在終端輸入:

    ```
    pip install torch transformers flask
    ```
4.  執行程式\
    用cd.. 進入儲存./fine\_tuned\_bert\_model的路徑

    應會跑出類似下方輸出結果:

{% code overflow="wrap" %}
```json
 * Running on all addresses (0.0.0.0)
 * Running on http://[電腦ip位址]
 * Running on http://[網域]
 * Running on http://[網域]
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

