import requests
import csv

url = "http://localhost:11434/v1/chat/completions"
model_name = "microsoft/phi-4-reasoning-plus"


with open("phi-4-reasoning-plus.txt", "a", encoding="utf-8") as fs:


    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = row["text"]

            resp = requests.post(
                url,
                json={
                    "stream": False,

                    "model": model_name,
                    "messages": [

                        {
                            "role": "system",
                            "content": "判斷以下內容是否為詐騙，是的話輸出1，不是的話輸出0。",
                        }, {
                            "role": "user",
                            "content": text,
                        },
                    ],
                    "max_tokens": 200,

                },
            )

            resp.raise_for_status()

            data = resp.json()

            fs.write(f"{text},{data['choices'][0]['message']['content'].replace('\n', '')}\n")

            print(text,",",data["choices"][0]["message"]["content"] + "\n")
