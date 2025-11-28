---
description: 本網站協助您在本機端部署ZeroSCAM後端，一步步帶你在自己的電腦部署我們的APP
---

# 首頁

模型部署一共分兩部分: Bert模型和LLM

\
Bert模型
------

Bert模型功能：根據對話文本識別詐騙機率

client請求：   &#x20;

```json
{
    "message": string
}
```



server回應：

```json
{
    "text_received": text,
    "scam_probability": float
}
```

## LLM

LLM功能 : 根據對話文本產生防騙建議

Client請求：

```json
{
        "model": model_name,
        "messages": [
            {"role": "system", "content": "用繁體中文回答。"},
            {"role": "system", "content": "考慮使用者是臺灣人。"},
            {"role": "system",
             "content": "根據電話內容，你只需要輸出一兩句話告訴使用者怎麼做。比如收到“您兒子涉及事故，需先支付醫療預繳金5000元”就輸出：“請先聯絡兒子確認是否真的發生事故，並聯絡165 反詐騙專線或醫院方官方電話確認。”"},
            {"role": "user",
             "content": "針對以下詐騙來電的來電內容產生建議：“這裡是蝦皮，您的賣場未簽署金流，24小時內未完成簽署將凍結所有款項，現在為您轉接真人客服請稍等”。"}
        ],
        "max_tokens": 200
    }
```

Server回應：

```json
{
  "id": "chatcmpl-763ns4nmob4aeomlgu9qj6",
  "object": "chat.completion",
  "created": 1763915455,
  "model": "qwen/qwen3-30b-a3b-2507",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "請勿輕信，請立即掛斷並前往蝦皮官方網站或APP確認帳戶狀態，或直接聯繫蝦皮官方客服確認，勿透過來電轉接的電話進行任何操作。",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 152,
    "completion_tokens": 45,
    "total_tokens": 197
  },
  "stats": {},
  "system_fingerprint": "qwen/qwen3-30b-a3b-2507"
}
```
