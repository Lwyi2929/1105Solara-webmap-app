import solara
import leafmap.leafmap as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[-100, 40],
        zoom=4,
        sidebar_visible=True,
    )

   
    road_pmtiles = "pages/data/TpeMRTRoutes_TWD97.shp"
   
    road_style = {
        "layers": [
            {
                "id": "Roads",
                "source": "transportation",
                "source-layer": "segment",
                "type": "line",
                "paint": {
                    "line-color": "#ffffff",
                    "line-width": 2,
                },
            },
        ]
    }
   
    m.add_pmtiles(road_pmtiles, style=road_style, tooltip=True, fit_bounds=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()