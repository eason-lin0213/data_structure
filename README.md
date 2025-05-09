# 資料結構
## HW1 籃球員選拔標準與數據分析方法 [影片連結](https://youtu.be/RLTrnSKFbCA)
### [籃球員數據csv檔](https://github.com/eason-lin0213/data_structure/blob/main/basketball_stats.csv)
### [建立各代理人團隊，並要求各代理人根據該批次資料進行分析，並提供球員選拔建議](https://github.com/eason-lin0213/data_structure/blob/main/dataAgent.py)
### [對話結果](https://github.com/eason-lin0213/data_structure/blob/main/all_conversation_log.csv)
### ![image](https://github.com/eason-lin0213/data_structure/blob/main/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E4%BD%9C%E6%A5%AD1.jpg)
---
## HW2 DRai相關程式碼作業
### [體育賽事播報csv檔](https://github.com/eason-lin0213/data_structure/blob/main/sports_commentary.csv)
### [評分完csv檔](https://github.com/eason-lin0213/data_structure/blob/main/sports_commentary_batch.csv)
### [HW2程式碼](https://github.com/eason-lin0213/data_structure/blob/main/DRai.py)
### ![image](https://github.com/user-attachments/assets/0f218f77-c98c-4853-bb1b-c4007e265994)
### ![image](https://github.com/user-attachments/assets/e35f3af2-53a4-4fa4-bcac-f1318bd906b9)

---
## HW3 playwright控制瀏覽器
### [HW3程式碼](https://github.com/eason-lin0213/data_structure/blob/main/postAI.py)
### ![image](https://github.com/user-attachments/assets/f68120c5-b736-4e19-8de7-8713128073eb)

---
## HW4 生成PDF
### [HW4程式碼](https://github.com/eason-lin0213/data_structure/blob/main/getPDF.py)
### [HW4生成PDF檔](https://github.com/eason-lin0213/data_structure/blob/main/report_20250401_203801.pdf)
### ![image](https://github.com/user-attachments/assets/3a0a0385-3481-4a0a-a97e-7957758a112d)
### ![image](https://github.com/user-attachments/assets/ed8dc078-089e-4ea7-84d4-997b25c1c76d)
### ![image](https://github.com/user-attachments/assets/9f63bdbd-0282-4394-8339-7e6c3faae62c)

---
## HW5 前端畫面
### [HW5程式碼](https://github.com/eason-lin0213/data_structure/tree/main/EMO)
### ![image](https://github.com/user-attachments/assets/472c78ee-a66c-4f29-8831-cf9150bcca64)
### ![image](https://github.com/user-attachments/assets/08b5f797-185b-4300-91c5-611528b47113)
)
)



---
## 功能介紹

- **單一查詢範例（main.py）**  
  從 `.env` 載入 Gemini API 金鑰，使用 `OpenAIChatCompletionClient` 連接 Gemini 模型，並發送一個查詢訊息，回傳結果印出至終端機。

- **多代理人對話範例（multiAgent.py）**  
  利用 AutoGen 框架建立一個多代理人團隊：
  - **AssistantAgent** 與 **MultimodalWebSurfer**：負責回答與資訊檢索。
  - **UserProxyAgent**：模擬使用者參與對話。  
  團隊以輪詢方式進行對話，直到對話中出現 `"exit"` 關鍵字為止。

- **多代理人檔案 I/O 範例（dataAgent.py）**  
  利用 AutoGen 框架建立一個多代理人團隊：
  - **DataAgent** 與 **MultimodalWebSurfer**：分別負責 CSV 資料分析、外部資訊檢索與問題解答。
  - **UserProxyAgent**：模擬使用者參與對話。  
  團隊以輪詢方式進行對話，直到對話中出現 `"exit"` 關鍵字為止。

---
