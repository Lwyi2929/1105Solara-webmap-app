import os
import json
import requests
import solara
import leafmap

def load_taipei_mrt_geojson():
    # 資料來源 URL，這裡以政府平台路網資料為例
    url = "https://data.gov.tw/dataset/121208/download/json"  # 假設為下載路徑
    # 備註：請到該資料頁面確認正確的下載 URL
    resp = requests.get(url)
    resp.raise_for_status()
    geojson_data = resp.json()
    return geojson_data

def create_map():
    # 建立地圖
    m = leafmap.Map(
        projection="globe",
        height="750px",
        center=[25.05, 121.5],
        zoom=10,
        sidebar_visible=True,
    )
    m.add_basemap("CartoDB.DarkMatter")

    try:
        geojson_data = load_taipei_mrt_geojson()
        m.add_geojson(
            geojson_data,
            style={"color": "#ffffff", "weight": 2, "opacity": 1},
            tooltip=True,
            layer_name="Taipei MRT Routes",
        )
    except Exception as e:
        m.add_text(f"⚠️ 載入捷運資料失敗：{e}", position="topright")

    return m

@solara.component
def Page():
    m = create_map()
    html = m.to_html()
    return solara.HTML(tag="div", unsafe_innerHTML=html)