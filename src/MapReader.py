import geojson
from descartes import PolygonPatch
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np




def MapReader(mapRoute):
    with open("aez-w-greenland.geojson") as json_file:
        json_data = geojson.load(json_file)

    plt.clf()
    ax = plt.figure(figsize=(10, 10)).add_subplot(111)  # fig.gca()

    m = Basemap(projection='robin', lon_0=0, resolution='c')
    m.drawmapboundary(fill_color='white', zorder=-1)
    m.drawparallels(np.arange(-90., 91., 30.), labels=[1, 0, 0, 1], dashes=[1, 1], linewidth=0.25, color='0.5', fontsize=14)
    m.drawmeridians(np.arange(0., 360., 60.), labels=[1, 0, 0, 1], dashes=[1, 1], linewidth=0.25, color='0.5', fontsize=14)
    m.drawcoastlines(color='0.6', linewidth=1)

    for i in range(3):
        coordlist = json_data.features[i]['geometry']['coordinates'][0]
        if i < 2796:
            name = json_data.features[i]['properties']['CTRYNAME']
            aez = json_data.features[i]['properties']['AEZ']

        for j in range(len(coordlist)):
            for k in range(len(coordlist[j])):
                coordlist[j][k][0], coordlist[j][k][1] = m(coordlist[j][k][0], coordlist[j][k][1])

        poly = {"type": "Polygon", "coordinates": coordlist}  # coordlist
        ax.add_patch(PolygonPatch(poly, fc=[0, 0.5, 0], ec=[0, 0.3, 0], zorder=0.2))

    ax.axis('scaled')
    # plt.draw()
    # plt.show()
    return m
