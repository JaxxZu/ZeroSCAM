# ZeroSCAM
基於Bert與LLM的實時通話詐騙檢測與防騙建議產生APP
    
## 系統架構
<img width="1754" height="1030" alt="firefox_tulggly7yj" src="https://github.com/user-attachments/assets/8c3affa4-1f3a-459f-84d7-0b625a2dad15" />

  
## 使用教學
### 獲取雅婷即時STT api 密鑰
1. 進入https://developer.yating.tw/dashboard ，註冊並完成簡訊驗證，可獲取1000新臺幣圓試用金   
![](https://github.com/user-attachments/assets/75fbcb33-a5dc-4b02-9d72-354b3a0f008a)
2. 複製api key，填寫進app中  
![-2147483648_-216901](https://github.com/user-attachments/assets/793f1686-43bf-4443-a53f-34207992fa39)

##  前端
  使用Android Studio，下載APK，將程式部署到手機上，手機透過選取server，連接cloudflare和後端進行練線
##  後端部署
  查看[後端部署文檔](https://zeroscam-team.gitbook.io/zeroscam-docs/backend/bert-mo-xing-bu-shu-jiao-xue)
##  實驗
  ### 實驗一
  對比 Bert 與 LLM 識別一句通話文本是否詐騙的準確性
  ### 實驗二
  對比不同LLM在分析詐騙文本並給出針對性建議的表現 
