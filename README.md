# 資料結構
## HW1 籃球員選拔標準與數據分析方法
### [籃球員數據csv檔](https://github.com/eason-lin0213/data_structure/blob/main/basketball_stats.csv)
### [建立各代理人團隊](https://github.com/eason-lin0213/data_structure/blob/main/multiAgent.py)
### [要求各代理人根據該批次資料進行分析，並提供球員選拔建議](https://github.com/eason-lin0213/data_structure/blob/main/dataAgent.py)
### [對話結果](https://github.com/eason-lin0213/data_structure/blob/main/all_conversation_log.csv)
---
## 功能介紹

- **單一查詢範例（main.py）**  
  從 `.env` 載入 Gemini API 金鑰，使用 `OpenAIChatCompletionClient` 連接 Gemini 模型，並發送一個查詢訊息，回傳結果印出至終端機。

- **多代理人對話範例（multiAgent.py）**  
  利用 AutoGen 框架建立一個多代理人團隊：
  - **AssistantAgent** 與 **MultimodalWebSurfer**：負責回答與資訊檢索。
  - **UserProxyAgent**：模擬使用者參與對話。  
  團隊以輪詢方式進行對話，直到對話中出現 `"exit"` 關鍵字為止。

---
