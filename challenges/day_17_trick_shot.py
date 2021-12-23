def highest_y(goal_min_y):
    # since the probe passes y=0 with the exact opposite velocity it had when being launched,
    # the highest launch velocity is the one that means the opposite velocity just avoids
    # overshooting the target area on the way down, which means that it goes from 0 to
    # the minimum target y in just one step.
    initial_y_velocity = -goal_min_y
    return initial_y_velocity * (initial_y_velocity - 1) / 2
