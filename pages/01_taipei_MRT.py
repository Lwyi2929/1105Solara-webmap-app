import solara
import leafmap.leafmap as leafmap
import os
import solara
import leafmap

def create_map():
    # 使用 __file__ 取得當前檔案的真實位置
    base_dir = os.path.dirname(__file__)
    road_data = os.path.join(base_dir, "..", "data", "tpeMRT.geojson")

    m = leafmap.Map(
        projection="globe",
        height="750px",
        center=[25.05, 121.5],
        zoom=10,
        sidebar_visible=True,
    )
    m.add_basemap("CartoDB.DarkMatter")

    if os.path.exists(road_data):
        m.add_geojson(
            road_data,
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
    return m.to_solara()