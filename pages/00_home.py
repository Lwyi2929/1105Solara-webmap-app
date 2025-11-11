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
    m = create_map()
    markdown = """
    ## 台北GIS儀表板
    台北GIS儀表板是一個以 **Solara** 為基礎開發的互動式三維地圖應用程式，整合 **Leafmap** 與 **MapLibre GL** 技術，能即時呈現台北地區的地理空間資訊。
    """

    with solara.Column(align="center"):
        solara.Markdown(markdown)
        solara.FigurePlotly(m.to_solara())
    