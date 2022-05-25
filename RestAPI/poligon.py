import geopandas as gpd
from shapely.geometry import Polygon


coordinates = [(4.812267, 52.328369), (4.823540, 52.456206),
               (5.050146, 52.458870), (5.081713, 52.317657)]


def create_polygon(coords, polygon_name):
    """ Create a polygon from coordinates """
    polygon = Polygon(coordinates)
    gdf = gpd.GeoDataFrame(crs={'init': 'epsg: 4326'})
    gdf.loc[0, 'name'] = polygon_name
    gdf.loc[0, 'geometry'] = polygon
    return gdf
