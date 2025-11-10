import solara
import leafmap.leafmap as leafmap


def create_map():

    m = leafmap.Map(
        projection="globe",
        height="750px",
        center=[121.5, 25.05], # <-- 更改中心點到台北 (捷運路線的合理位置)
        zoom=10,               # <-- 調整縮放級別
        sidebar_visible=True,
    )
    m.add_basemap("CartoDB.DarkMatter")

    road_data = "data/tpeMRT.geojson" 

    line_style = {
        "color": "#ffffff",  # 線條顏色
        "weight": 2,         # 線條寬度
        "opacity": 1,        # 透明度
    }
    m.add_geojson(
            road_data, 
            style=line_style, 
            tooltip=True, 
            layer_name="MRT Routes" # 給予圖層名稱
        )
  
        
    return m


@solara.component
def Page():
    m = create_map()
    return solara.FigureMatplotlib(m.to_html())
