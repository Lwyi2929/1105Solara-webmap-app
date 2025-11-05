import solara
import leafmap.leafmap as leafmap


def create_map():

    m = leafmap.Map(
        style="CartoDB.DarkMatter",
        projection="globe",
        height="750px",
        center=[121.5, 25.05], # <-- 更改中心點到台北 (捷運路線的合理位置)
        zoom=10,               # <-- 調整縮放級別
        sidebar_visible=True,
    )
    
    # 🚨 修正：假設您已經將 TpeMRTRoutes_TWD97.shp 轉換為 TpeMRTRoutes.geojson
    road_data = "pages/data/TpeMRTRoutes.geojson" 
    
    # 定義 GeoJSON 的樣式，通常使用 style_callback 或 style 參數
    # 在 Leafmap 中，直接傳遞 MapLibre style 字典給 GeoJSON 可能不如 add_pmtiles 直接，
    # 但我們可以定義一個簡單的樣式字典來控制線條顏色和寬度：
    line_style = {
        "color": "#ffffff",  # 線條顏色
        "weight": 2,         # 線條寬度
        "opacity": 1,        # 透明度
    }
    
    # 🚨 修正：使用 m.add_geojson() 方法來添加 GeoJSON 資料
    try:
        m.add_geojson(
            road_data, 
            style=line_style, 
            tooltip=True, 
            layer_name="MRT Routes" # 給予圖層名稱
        )
    except Exception as e:
        # 在實際部署時，如果檔案路徑或格式有問題，這裡可以捕獲錯誤
        print(f"Error adding GeoJSON: {e}") 
        
    return m


@solara.component
def Page():
    m = create_map()
    # Leafmap 實例 m 必須調用其 to_solara() 方法才能在 Solara 中正確顯示
    return m.to_solara()