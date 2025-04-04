# HW3 playwright控制瀏覽器
from playwright.sync_api import sync_playwright

def play_youtube_music_trending():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 顯示瀏覽器
        page = browser.new_page()
        
        print("啟動瀏覽器，前往 YouTube Music...")
        page.goto("https://music.youtube.com/")
        page.wait_for_timeout(5000)  # 等待頁面載入
        
        print("等待搜尋框出現...")
        search_box = page.locator("input#input")
        search_box.wait_for(state="visible", timeout=10000)

        print("輸入搜尋關鍵字...")
        search_box.click()
        page.keyboard.type("kpop", delay=100)  # 模擬真人輸入
        page.keyboard.press("Enter")

        print("等待搜尋結果...")
        page.wait_for_timeout(5000)  # 等待搜尋結果載入

        print("點擊第一首歌曲...")
        first_result = page.locator("ytmusic-shelf-renderer ytmusic-responsive-list-item-renderer").first
        first_result.wait_for(state="visible", timeout=10000)
        first_result.click()

        print("正在播放kpop！")
        page.wait_for_timeout(5000)  # 等待歌曲開始播放

        # 保持瀏覽器開啟，讓音樂持續播放
        input("音樂正在播放，按 Enter 鍵關閉瀏覽器...")
        browser.close()

if __name__ == "__main__":
    play_youtube_music_trending()
