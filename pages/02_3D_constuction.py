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
    m.add_basemap("CartoDB Positron", visible=False)
    m.add_overture_3d_buildings(template="simple")
    m.add_geojson("https://raw.githubusercontent.com/leoluyi/taipei_mrt/345dd492fa9c0138c126b3de75483a2881ed8991/stations.geojson", name="station")
    m.add_geojson("https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson", name="routes")

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()