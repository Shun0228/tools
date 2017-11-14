import numpy as np
import matplotlib.pyplot as plt

def judge_inside(check_point, xy_range):
    """
    input
        check_point : point which is judged inside or outside
        xy_range : Defined range area (must be closed loop)

    output
        judge_result : If point is inside range area, value is True (Type:Bool)
    """

    # Check range area is close or not
    if np.allclose(xy_range[0,:], xy_range[-1,:]):
        print("")
        print("Range is close.")
        print("")

    else:
        print("")
        print("Range area is not close.")
        print("Connect first point and last point automatically.")
        print("")

        point_first = xy_range[0,:]
        xy_range = np.vstack((xy_range, point_first))

    # Initialize count of line cross number
    cross_num = 0

    # Count number of range area
    point_num = xy_range[:,0].size

    # Judge inside or outside by cross number
    for point in range(point_num - 1):

        point_ymin = np.min(xy_range[point:point+2, 1])
        point_ymax = np.max(xy_range[point:point+2, 1])

        if check_point[1] == xy_range[point, 1]:

            if check_point[0] < xy_range[point, 0]:
                cross_num += 1

            else:
                pass


        elif point_ymin < check_point[1] < point_ymax:

            dx = xy_range[point+1, 0] - xy_range[point, 0]
            dy = xy_range[point+1, 1] - xy_range[point, 1]

            if dx == 0.0:
                # Line is parallel to y-axis
                judge_flag = xy_range[point, 1] - xy_point[1]

            elif dy == 0.0:
                # Line is parallel to x-axis
                judge_flag = -1.0

            else:
                # y = ax + b (a:slope,  b:y=intercept)
                slope = dy / dx
                y_intercept = xy_range[point, 1] - slope * xy_range[point, 0] 

                # left:y,  right:ax+b
                left_eq = check_point[1]
                right_eq = slope * check_point[0] + y_intercept

                judge_flag = slope * (left_eq - right_eq)


            if judge_flag > 0.0:
                # point places left side of line 
                cross_num += 1.0

            elif judge_flag < 0.0:
                # point places right side of line
                pass

        else:
            pass

    # odd number : inside,  even number : outside
    judge_result = np.mod(cross_num, 2)

    # Convert from float to bool (True:inside,  False:outside)
    judge_result = judge_result.astype(np.bool)

    return judge_result


if __name__ == "__main__":

    print("test mode : judge inside")

    # Define range
    point_range = np.array([[34.735715,	139.420922],
                            [34.731750,	139.421719],
                            [34.733287,	139.424590],
                            [34.736955,	139.426038],
                            [34.738908,	139.423597],
                            [34.740638,	139.420681],
                            [34.741672,	139.417387],
                            [34.735715,	139.420922],
                            ])

    # Define target point (x,y)
    drop_point = np.array([34.74, 139.42])

    judge_result = judge_inside(drop_point, point_range)

    print("Judge Result : " + str(judge_result))

    # Check on graph
    plt.plot(point_range[:, 0], point_range[:, 1])
    plt.plot(drop_point[0], drop_point[1], '.')
    plt.show()