from selenium import webdriver
from bs4 import BeautifulSoup 
import time , os
import requests
import re
import pandas as pd
from sqlalchemy import create_engine


url = "https://moba.garena.tw/game/heroes"

res = requests.get(url)

soup = BeautifulSoup(res.text,"html.parser")

html = soup.find("div",id="h_list") 

hero_info = html.find_all("li")

#print(hero_info)

#建立空 hero_details ,存英雄資料
hero_details = []

for i in hero_info:
    
    hero_name = i.get('data-filter')
    print("英雄名稱: " + hero_name)
    
    #英雄分類
    hero_category = str(i.get('data-tags'))
    dict1 = {
        "tank":"坦克" , 
        "archer":"射手" , 
        "aid":"輔助",
        "master":"法師",
        "assassin":"刺客" ,
        "soldier":"戰士"   }
    hero_category_zh = dict1[hero_category]
    print("類別: " + hero_category_zh)
    
    #英雄網址
    hero_url = 'https://moba.garena.tw'+ i.a.get("href")
    print("網址: " + hero_url)
    
    # 圖片處理
    pic = i.div.get('style')
    match = re.search(r'url\((.*?)\)', pic)
    if match:
        clean_pic = match.group(1)
        clean_pic_url = 'https:'+ clean_pic
    print("圖片: " + clean_pic_url)
    print()
    
    #寫進list
    hero_details.append({
        "英雄名稱": hero_name, 
        "類別": hero_category_zh, 
        "網址": hero_url ,
        "圖片": clean_pic_url })

df = pd.DataFrame(hero_details)

df.to_csv("傳說對決英雄.csv" ,index=False , encoding="utf-8-sig")



# 以下程式碼為 存入localhost 資料庫


def process_and_save_to_db_mysql(df):
    print("開始執行資料庫存檔程序...") # 偵錯：確認函式被呼叫
    
    try:
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        db_name = os.getenv("DB_NAME")
        
        # 建立引擎
        db_connection_str = f"mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4"
        engine = create_engine(db_connection_str)
        
        print(f"嘗試連線至: {host}，資料庫: {db_name}") # 偵錯：確認連線參數
        
        # 寫入資料庫
        df.to_sql('heroes', con=engine, if_exists='replace', index=False)
        
        print("【成功】資料已存入 MySQL 資料庫！") # 偵錯：確認完成
        
    except Exception as e:
        # 如果有任何錯誤，這裡會強制印出來
        print(f"【嚴重錯誤】程式無法執行: {e}")

# --- 關鍵：確保這裡有呼叫函式 ---
if __name__ == "__main__":
    # 這裡確保你的 df 已經在上面準備好了
    # 檢查是否有抓到資料
    if not df.empty:
        process_and_save_to_db_mysql(df)
    else:
        print("錯誤：DataFrame 是空的，請檢查前面的爬蟲程式是否抓到資料。")