#!/usr/bin/env python3
"""
PNG to WEBP Converter
將當前資料夾中的所有PNG檔案轉換為WEBP格式
"""

import os
import sys
from PIL import Image
import glob

def convert_png_to_webp(input_path, output_path=None, quality=85):
    """
    將PNG檔案轉換為WEBP格式
    
    Args:
        input_path (str): 輸入PNG檔案路徑
        output_path (str): 輸出WEBP檔案路徑，如果為None則自動生成
        quality (int): WEBP品質 (0-100)，預設85
    """
    try:
        # 開啟PNG檔案
        with Image.open(input_path) as img:
            # 如果沒有指定輸出路徑，則自動生成
            if output_path is None:
                base_name = os.path.splitext(input_path)[0]
                output_path = f"{base_name}.webp"
            
            # 轉換並儲存為WEBP
            img.save(output_path, 'WEBP', quality=quality, optimize=True)
            print(f"✓ 成功轉換: {input_path} -> {output_path}")
            return True
            
    except Exception as e:
        print(f"✗ 轉換失敗 {input_path}: {str(e)}")
        return False

def main():
    """主函數"""
    print("PNG to WEBP 轉換器")
    print("=" * 50)
    
    # 檢查是否安裝了Pillow
    try:
        from PIL import Image
    except ImportError:
        print("錯誤: 請先安裝Pillow套件")
        print("執行: pip install Pillow")
        sys.exit(1)
    
    # 獲取當前資料夾
    current_dir = os.getcwd()
    print(f"當前資料夾: {current_dir}")
    
    # 尋找所有PNG檔案
    png_files = glob.glob("*.png") + glob.glob("*.PNG")
    
    if not png_files:
        print("在當前資料夾中找不到PNG檔案")
        return
    
    print(f"找到 {len(png_files)} 個PNG檔案")
    print("-" * 30)
    
    # 設定轉換參數
    quality = 85  # 可以調整品質 (0-100)
    
    # 轉換統計
    success_count = 0
    total_count = len(png_files)
    
    # 逐一轉換PNG檔案
    for png_file in png_files:
        if convert_png_to_webp(png_file, quality=quality):
            success_count += 1
    
    # 顯示結果
    print("-" * 30)
    print(f"轉換完成: {success_count}/{total_count} 個檔案")
    
    if success_count > 0:
        print(f"品質設定: {quality}")
        print("所有WEBP檔案已儲存在當前資料夾中")

def convert_single_file(filename, quality=85):
    """
    轉換單一檔案的輔助函數
    
    Args:
        filename (str): PNG檔案名稱
        quality (int): WEBP品質
    """
    if os.path.exists(filename) and filename.lower().endswith('.png'):
        return convert_png_to_webp(filename, quality=quality)
    else:
        print(f"檔案不存在或不是PNG格式: {filename}")
        return False

if __name__ == "__main__":
    # 檢查命令列參數
    if len(sys.argv) > 1:
        # 如果有參數，轉換指定的檔案
        for filename in sys.argv[1:]:
            convert_single_file(filename)
    else:
        # 沒有參數時，轉換當前資料夾所有PNG檔案
        main()