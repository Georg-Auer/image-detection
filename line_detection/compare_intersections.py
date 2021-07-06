import numpy as np
import matplotlib.pyplot as plt
import os
from find_intersection import find_intersection_point

def compare_found_coordinates(picturenames):
    # find out lenght of picturenames
    # numpy works best if the size is already fixed
    print(f"Printing picturenames{picturenames}")

    arraylength = len(picturenames)
    print(f"Arraylenght of picturenames: {arraylength}")
    coordinates = np.zeros(shape=(arraylength,2))
    print("coordinates")
    print(coordinates)

    i = 0
    for filename in picturenames:
        print(f"Finding intersections for: {filename}")
        coordinate, lines, intersections = (find_intersection_point(filename))
        print("Mean of all intersection values is: ")
        print(i)
        print(coordinate)
        coordinates[i] = coordinate
        i += 1

    print("List of all found coordinates")
    print(coordinates)
    return(coordinates)

def plot_precision(coordinates):
    # calculate standard deviation along axis=0 meaning for x and y
    # https://numpy.org/doc/stable/reference/generated/numpy.std.html
    standard_deviation = (np.std(coordinates, axis=0))
    print(f"Standard deviation in pixel for x, y: {np.around(standard_deviation, decimals=2)}")
    #272 px = 1mm
    #0.272 px = 1um
    # pixel_per_um = 0.120 
    pixel_per_um = 0.272
    standard_deviation_um = np.true_divide(standard_deviation, pixel_per_um)
    print(f"Standard deviation in μm for x, y: {np.around(standard_deviation_um, decimals=2)}")

    means = np.mean(coordinates, axis=0)
    print(f"Means for all lines for x, y: {means}")
    coordinates_minus_mean = np.subtract(coordinates, means)
    print(f"Relative coordinates: {coordinates_minus_mean}")
    coordinates_relative_um = np.true_divide(coordinates_minus_mean, pixel_per_um)
    print(coordinates_relative_um)

    plt.boxplot(coordinates_relative_um[:], labels=["X","Y"])
    plt.title('Result')
    # plt.xlabel('Axis')
    plt.ylim([-15,15])
    plt.ylabel('Derivation in [μm]')
    plt.show()
    #fig = plt.figure(figsize=(12, 8))

    # alternatively: subplots with scatter plot, boxplot and histogram
    # def add_titlebox(ax, text):
    #     ax.text(.55, .8, text,
    #         horizontalalignment='center',
    #         transform=ax.transAxes,
    #         bbox=dict(facecolor='white', alpha=0.6),
    #         fontsize=12.5)
    #     return ax
    # gridsize = (3, 3)
    # ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=3, rowspan=2)
    # ax2 = plt.subplot2grid(gridsize, (2, 0))
    # ax3 = plt.subplot2grid(gridsize, (2, 1))
    # ax4 = plt.subplot2grid(gridsize, (2, 2))
    # ax1.set_title(f'Standard x/y deviation of the microscope [μm]\n {np.around(standard_deviation_um, decimals=2)}', fontsize=14)
    # ax1.plot(coordinates_relative_um[:,0], coordinates_relative_um[:,1], 'ro')
    # ax2.boxplot(coordinates_relative_um[:])
    # ax3.hist(coordinates_relative_um[:,0], bins='auto')
    # ax4.hist(coordinates_relative_um[:,1], bins='auto')
    # add_titlebox(ax2, 'Boxplot for x/y [μm]')
    # add_titlebox(ax3, 'Histogram: x axis [μm]')
    # add_titlebox(ax4, 'Histogram: y axis [μm]')
    # ax1.spines['left'].set_position(('data', 0))
    # ax1.spines['bottom'].set_position(('data', 0))
    # ax1.spines['top'].set_visible(False)
    # ax1.spines['right'].set_visible(False)
    # plt.show()

# Only relevant if run as __main__
if __name__ == '__main__':
    print("This module can find intersection points on pictures.")
    print("Additionally, the results can be plotted.")
    print(f"Current directory is {os.getcwd()}")

    #this is just for getting picturenames from one folder
    from os import listdir
    from os.path import isfile, join        
    #mypath = r'C:\SPOC\DOC\Calibration\images\set'
    # mypath = (os.path.join(os.getcwd(), "detection/line_detection/2,5plan"))
    # mypath = (os.path.join(os.getcwd(), "2,5plan/1"))
    experiment_path = "2,5plan"
    mypath = (os.path.join(os.getcwd(), experiment_path))
    os.chdir(mypath)
    mypath = os.getcwd()
    # get names of pictures in a folder
    print(f"Searching files in directory {mypath}")
    picturenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(picturenames)
    # use the list of picture names
    coordinates = compare_found_coordinates(picturenames)

    # use the following to plot the data:
    # plt.plot(coordinates[:,0], coordinates[:,1], 'ro')
    # or use the function to plot the data:
    plot_precision(coordinates)

else:
    print("Intersection finding module loaded:")
