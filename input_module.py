import csv
import os
from datetime import datetime

# 定義資料儲存的檔案名稱
DATA_FILE = 'expenses.csv'

def initialize_file():
    """如果檔案不存在，則建立檔案並寫入標頭"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 欄位：日期, 金額, 類別, 備註
            writer.writerow(['Date', 'Amount', 'Category', 'Notes'])

def get_user_input():
    """獲取使用者輸入並回傳字典"""
    print("=== 新增消費紀錄 ===")
    
    # 1. 日期 (預設為今天)
    date_str = input(f"請輸入日期 (YYYY-MM-DD，預設為 {datetime.now().strftime('%Y-%m-%d')}): ").strip()
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    # 2. 金額 (必須是數字)
    while True:
        try:
            amount = float(input("請輸入金額: "))
            if amount < 0:
                print("金額不能為負數。")
                continue
            break
        except ValueError:
            print("輸入錯誤，請輸入有效的數字。")

    # 3. 類別
    print("常見類別: 食物, 交通, 娛樂, 購物, 帳單, 其他")
    category = input("請輸入類別: ").strip()
    if not category:
        category = "其他"

    # 4. 備註 (選填)
    notes = input("備註 (選填): ").strip()

    return [date_str, amount, category, notes]

def save_to_csv(data):
    """將資料寫入 CSV"""
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(f"成功儲存：{data}")

def main():
    initialize_file()
    while True:
        data = get_user_input()
        save_to_csv(data)
        
        cont = input("\n是否繼續新增？ (y/n): ").lower()
        if cont != 'y':
            break
    print("輸入程式結束。")

if __name__ == "__main__":
    main()