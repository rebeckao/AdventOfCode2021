def highest_y(goal_min_y):
    # since the probe passes y=0 with the exact opposite velocity it had when being launched,
    # the highest launch velocity is the one that means the opposite velocity just avoids
    # overshooting the target area on the way down, which means that it goes from 0 to
    # the minimum target y in just one step.
    initial_y_velocity = -goal_min_y
    return highest_point_reached_by_y_velocity(initial_y_velocity)


def highest_point_reached_by_y_velocity(initial_y_velocity):
    return initial_y_velocity * (initial_y_velocity - 1) / 2


def reaches_goal(goal_min_x, goal_max_x, goal_min_y, goal_max_y, original_x_velocity, original_y_velocity) -> bool:
    current_x_velocity = original_x_velocity
    current_y_velocity = original_y_velocity
    current_x = 0
    current_y = 0
    while current_x <= goal_max_x and current_y >= goal_min_y:
        if current_x >= goal_min_x and current_y <= goal_max_y:
            return True
        current_x += current_x_velocity
        current_y += current_y_velocity
        current_x_velocity = max(current_x_velocity - 1, 0)
        current_y_velocity -= 1
    return False


def number_of_different_velocities_landing_in_target(goal_min_x, goal_max_x, goal_min_y, goal_max_y):
    highest_possible_y = -goal_min_y
    lowest_possible_y = goal_min_y  # reaches the lowest part of goal after 1 step
    lowest_possible_x = 6  # 6 for example, 17 for the real input
    highest_possible_x = goal_max_x
    number_of_possible_velocities = 0
    possible_velocities = set()
    for x in range(lowest_possible_x, highest_possible_x + 1):
        for y in range(lowest_possible_y, highest_possible_y + 1):
            if reaches_goal(goal_min_x, goal_max_x, goal_min_y, goal_max_y, x, y):
                number_of_possible_velocities += 1
                possible_velocities.add((x, y))
    return number_of_possible_velocities
