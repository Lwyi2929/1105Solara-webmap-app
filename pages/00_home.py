import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 台北GIS儀表板
        歡迎來到台北GIS儀表板！這個應用程式展示了台北市的地理資訊系統（GIS）功能，讓您可以探索城市的各種地理數據和地圖視覺化。
        """
        

        solara.Markdown(markdown)