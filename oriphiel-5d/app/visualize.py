import matplotlib.pyplot as plt


def plot_spiral(segments, filename="spiral.png"):
    xs, ys, zs = [], [], []
    for seg in segments.values():
        coords = seg["coordinates"]
        xs.append(coords[0])
        ys.append(coords[1])
        zs.append(coords[2])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(xs, ys, zs, marker="o")
    ax.set_title("ORIPHIEL-5D Spiral Projection")
    plt.savefig(filename)
    return filename
