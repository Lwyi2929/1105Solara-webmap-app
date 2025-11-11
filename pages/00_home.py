import solara
import leafmap.maplibregl as leafmap

@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 🗺️ 台北GIS儀表板
        歡迎來到台北GIS儀表板！這個應用程式展示了台北市的地理資訊系統功能，讓您可以探索城市的各種地理數據和地圖視覺化。

        ![image](https://github.com/user-attachments/assets/efc9e43b-99c0-40b4-af08-4971e8b96919)
        """
        

    solara.Markdown(markdown)