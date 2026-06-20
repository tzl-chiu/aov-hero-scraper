# Arena of Valor (AoV) Hero Scraper

這是一個自動化資料收集專案，旨在從《傳說對決》(Arena of Valor) 官方網站爬取所有英雄的基礎資訊，並將資料結構化後儲存至本地的 MySQL 資料庫中。

## 專案功能

* **網頁爬蟲**：利用 `requests` 與 `BeautifulSoup` 抓取官方網站英雄列表頁。
* **資料處理**：將非結構化的網頁標籤資料轉換為 `pandas` DataFrame。
* **自動儲存**：透過 `SQLAlchemy` 將整理好的資料自動寫入 MySQL 資料庫，支援快速更新。

## 技術棧

* **Python** 3.x
* **Web Scraping**: `requests`, `beautifulsoup4`
* **Data Processing**: `pandas`
* **Database**: `SQLAlchemy`, `pymysql`
* **Security**: `python-dotenv` (環境變數管理)

## 如何開始

### 1. 前置準備
* 安裝 [Python](https://www.python.org/)
* 安裝並啟動 [MySQL](https://www.mysql.com/) 資料庫
* 在 MySQL 中建立一個資料庫（例如名稱為 `aov`）

### 2. 安裝依賴
在終端機執行以下指令來安裝所需的套件：

```bash
pip install pandas sqlalchemy pymysql beautifulsoup4 requests python-dotenv



### 3. 設定環境變數
為了安全性，請勿將帳號密碼直接寫在程式碼中。

在專案根目錄建立一個 .env 檔案。
參考 .env.example 格式填寫你的資料庫資訊：

DB_USER=你的帳號
DB_PASSWORD=你的密碼
DB_HOST=localhost
DB_NAME=aov

###  4. 執行程式
直接執行你的主程式：

Bash
python main.py
專案結構
Plaintext
aov-hero-scraper/
├── .env                # 環境變數 (請勿上傳至 GitHub)
├── .env.example        # 環境變數範本
├── .gitignore          # 忽略隱私檔案設定
├── aov.py             # 核心爬蟲與儲存邏輯
├── requirements.txt    # 專案套件列表
└── README.md           # 專案說明文件
截圖展示
下圖展示了成功抓取資料並存入 MySQL 資料庫的結果：

<img src="https://i.ibb.co/BVHX7q59/2026-06-20-18-16-15.png">

注意事項
本專案僅供個人學習與資料分析使用，爬取頻率請斟酌，請遵守該網站的 robots.txt 規範。

記得將 .env 加入 .gitignore，以保護你的資料庫安全！
