import solara

@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
       ## 台北GIS儀表板
    台北GIS儀表板是一個以 **Solara** 為基礎開發的互動式三維地圖應用程式，
    結合 **Leafmap** 與 **MapLibre GL** 技術，能即時呈現台北地區的地理空間資訊。
    """

        solara.Markdown(markdown)
    