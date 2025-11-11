import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        center=[121.55555, 25.08722],
        zoom=16,
        pitch=60,
        bearing=-17,
        style="positron",
        height="750px",
        sidebar_visible=True,
    )

    m.add_ee_layer(asset_id="ESA/WorldCover/v200", opacity=0.8)

    m.add_legend_to_sidebar(
        builtin_legend="ESA_WorldCover", title="Land Cover Type", shape_type="rectangle"
    )
    m.add_colorbar_to_sidebar(cmap="terrain", label="Elevation")

    return m

@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 🗺️ 台北GIS儀表板
        歡迎來到台北GIS儀表板！這個應用程式展示了台北市的地理資訊系統功能，讓您可以探索城市的各種地理數據和地圖視覺化。
        """
        

        solara.Markdown(markdown)
    m = create_map()
    return m.to_solara()