import solara
import leafmap.maplibregl as leafmap

def create_map():
    base_dir = os.path.dirname(__file__) if "__file__" in globals() else os.getcwd()
    geojson_path = os.path.join(base_dir, "..", "data", "tpeMRT.geojson")

    m = leafmap.Map(
        center=[121.55555, 25.08722],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )
    m.add_basemap("CartoDB.DarkMatter")
    
    m.add_geojson("/workspaces/1105Solara-webmap-app/data/tpeMRT.geojson", name="routes")

    return m

@solara.component
def Page():
    m = create_map()
    return m.to_solara()