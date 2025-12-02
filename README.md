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
使用Android Studio開發  
##  後端部署
  查看[後端部署文檔](https://zeroscam-team.gitbook.io/zeroscam-docs/backend/bert-mo-xing-bu-shu-jiao-xue)
##  實驗
  ### 實驗一
  對比 Bert 與 LLM 識別一句通話文本是否詐騙的準確性  
  
實驗方法：
對於LLMs下promt，要求讀取一段對話，判斷是否為詐騙，是輸出1，不是就輸出0。如果LLMs輸出的值是非0/非1，分母移除掉再做計算。  
對於BERT，輸入測試集獲取詐騙機率，機率大於50%就判斷成1，否則判斷為0

  ### 實驗二
`Experiment/Experiment_Two/result`  
  
  對比不同LLM在分析詐騙文本並給出針對性建議的表現 
實驗目標在於LLM是否能提供具體且正確的行動指引，協助使用者防騙  

實驗方法，我們輸入promt讓LLM對每筆詐騙句子產生針對性的建議  
手工依照以下標準對LLM的回答進行評分：  

如果LLM只生成了適用於所有詐騙電話場景的原因和建議，我們評分為60分  
如果LLM有根據電話內容給出針對性的原因和建議，給100分，有其一就給80分  
如果LLM提供了錯誤資訊或有害建議，這評為0分  
