import os
import json
import solara
import leafmap

def create_map():
    geojson_path = "/workspaces/1105Solara-webmap-app/data/tpeMRT.geojson"

    # 讀取 GeoJSON
    if os.path.exists(geojson_path):
        with open(geojson_path, "r", encoding="utf-8") as f:
            geojson_data = json.load(f)
    else:
        geojson_data = None

    # 建立地圖
    m = leafmap.Map(
        projection="globe",
        height="750px",
        center=[25.05, 121.5],
        zoom=10,
        sidebar_visible=True,
    )
    m.add_basemap("CartoDB.DarkMatter")

    # 加入 GeoJSON
    if geojson_data:
        m.add_geojson(
            geojson_data,
            style={"color": "#ffffff", "weight": 2, "opacity": 1},
            tooltip=True,
            layer_name="MRT Routes",
        )
    else:
        m.add_text("⚠️ 找不到 data/tpeMRT.geojson", position="topright")

    return m

@solara.component
def Page():
    m = create_map()
    html = m.to_html()  # Leafmap 0.57.2 不支援 to_solara()
    return solara.HTML(tag="div", unsafe_innerHTML=html)
