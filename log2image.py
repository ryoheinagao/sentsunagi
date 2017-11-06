import glob
import matplotlib.pyplot as plt
import gpxpy

lat, lon = [], []

fig = plt.figure(facecolor='black')
ax = plt.Axes(fig, [0., 0., 1., 1.], )
ax.set_aspect('equal')
ax.set_axis_off()
fig.add_axes(ax)

for filename in glob.glob('log/*'):
    gpx_file = open(filename, 'r')
    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        for point in track.segments[0].points[::50]:
            lat.append(point.latitude)
            lon.append(point.longitude)

    plt.plot(lon, lat, color='cyan', lw=0.5)
    lat, lon = [], []

plt.savefig("result.png", facecolor=fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=300)
