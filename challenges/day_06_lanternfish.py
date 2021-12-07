def fish_after_days(initial_fish: str, days: int):
    number_of_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in [int(val) for val in initial_fish.split(",")]:
        number_of_fish[fish] += 1
    for day in range(days):
        new_number_of_fish = {0: number_of_fish[1],
                              1: number_of_fish[2],
                              2: number_of_fish[3],
                              3: number_of_fish[4],
                              4: number_of_fish[5],
                              5: number_of_fish[6],
                              6: number_of_fish[7] + number_of_fish[0],
                              7: number_of_fish[8],
                              8: number_of_fish[0]}
        number_of_fish = new_number_of_fish
    return sum(number_of_fish.values())
