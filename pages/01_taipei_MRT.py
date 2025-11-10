import os
import solara
import leafmap

def create_map():
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else os.getcwd()
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
    html = m.to_html()  # ✅ 取代 to_solara()
    return solara.HTML(tag="div", unsafe_innerHTML=html)
