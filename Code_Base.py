def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if (mini <= users_input) and (users_input < maximum):
                print(f"Received input: {users_input}")  # Debugging print statement

            if mini <= users_input <= maximum:
                return users_input

            else:
                print(f"Please enter a number between {mini} and {maximum}.")
        except ValueError:
            print("Sorry: Numbers only please")
        # except EOFError:
        #     print("End of input reached.")
        #     break


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry: Numbers only please")


def runners_data():
    with open("runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(",")
        runners_name.append(split_line[0])
        id = split_line[-1].strip("\n")
        runners_id.append(id)
    return runners_name, runners_id


def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.strip().split(",")  # Remove unnecessary strip("\n") and fix the split
        id.append(split_line[0])
        time_taken.append(int(split_line[-1]))  # Convert the last element to an integer
    return id, time_taken


def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        split = line.split("\n")
        location = split[0]
        races_location.append(location)
    return races_location


def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


def display_races(id, time_taken, venue, fastest_runner):
    minute = 60
    print(f"Results for {venue}")
    print(f"=" * 37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // minute)
        seconds.append(time_taken[i] % minute)
    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")


def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
    connection = open(f"{user_location}.txt", "a")
    races_location.append(user_location)
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner == 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner},", file=connection)
    connection.close()


def updating_races_file(races_location):
    connection = open(f"races.txt", "w")
    for i in range(len(races_location)):
        print(races_location[i], file=connection)
    connection.close()


def checkrunnerid(name):
    match name:
        case "Anna Fox":
            return "CK-24"
        case "Des Kelly":
            return "CK-23 "
        case "Ann Cahill":
            return "KY-43"
        case "Joe Flynn":
            return "CK-11"
        case "Sally Fox":
            return "KY-12"
        case "Joe Shine":
            return "TP-02"
        case "Lisa Collins":
            return "WD-32 "
        case "Sil Murphy":
            return "LK-73"
        case "Des Kelly":
            return "WD-19"


def competitors_by_county(name):
    print("Clare runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CL"):
            print(f"{name[i]} ({checkrunnerid(name[i])})")
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({checkrunnerid(name[i])})")
    print("Kerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({checkrunnerid(name[i])})")
    print("Limerick runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("LK"):
            print(f"{name[i]} ({checkrunnerid(name[i])})")
    print("Tipperary runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("TP"):
            print(f"{name[i]} ({checkrunnerid(name[i])})")
    print("Waterford runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("WD"):
            print(f"{name[i]} ({checkrunnerid(name[i])})")


def reading_race_results_of_relevant_runner(location, runner_id):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        id.append(split_line[0])
        time_taken.append(int(split_line[1].strip("\n")))
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    print("Venue             Winner")
    print("=" * 24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(races_location[i] + ": " + fastest_runner)


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input - 1]
    return runner, id


def convert_time_to_minutes_and_seconds(time_taken):
    minute = 60
    minutes = time_taken // minute
    seconds = time_taken % minute
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        split_line = line.split(",".strip("\n"))
        t = int(split_line[1].strip("\n"))
        time_taken.append(t)
    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-" * 35)
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race})")


def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)

    winners = []
    runners = []

    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)

        if fastest_runner not in winners:
            winners.append(fastest_runner)
            name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
            runners.append(name_of_runner)

    if len(winners) == 0:
        print("No runners have won a race.")
    else:
        for i, fastest_runner in enumerate(winners):
            print(f"{runners_name[i]}, {runners_id[i]}")


# task 7
def competitors_not_on_podium(races_location, runners_name, runners_id):
    print("Competitors who have not taken a podium position in any race:")
    print("=" * 60)

    podium_finishers = set()

    # Find all the podium finishers
    for location in races_location:
        id, time_taken = reading_race_results(location)
        if len(id) >= 3:  # Assuming the top 3 runners are on the podium
            podium_finishers.add(id[0])
            podium_finishers.add(id[1])
            podium_finishers.add(id[2])

    non_podium_competitors = []

    # Find competitors who are not on the podium in any race
    for runner_id in runners_id:
        found_on_podium = False
        for location in races_location:
            id, _ = reading_race_results(location)
            if runner_id in podium_finishers:
                found_on_podium = True
                break
        if not found_on_podium:
            non_podium_competitors.append(runner_id)

    if len(non_podium_competitors) == 0:
        print("All competitors have taken a podium position in at least one race.")
    else:
        for runner_id in non_podium_competitors:
            i = runners_id.index(runner_id)
            print(f"{runners_name[i]} ({runner_id})")

    # Rest of your code remains unchanged
    print("Competitors who have not taken a podium position in any race:")
    print("=" * 60)
    podium_finishers = []

    # Find all the podium finishers
    for location in races_location:
        race_results = reading_race_results(location)
        for i in range(3):
            if i < len(race_results):
                podium_finishers.append(race_results[i][0])  # Assuming the top 3 runners are on the podium

    non_podium_competitors = []

    # Find competitors who are not on the podium in any race
    for runner_id in runners_id:
        found_on_podium = False
        for location in races_location:
            race_results = reading_race_results(location)
            for result in race_results:
                if result[0] == runner_id:
                    found_on_podium = True
                    break
            if found_on_podium:
                break
        if not found_on_podium:
            non_podium_competitors.append(runner_id)

    if len(non_podium_competitors) == 0:
        print("All competitors have taken a podium position in at least one race.")
    else:
        for runner_id in non_podium_competitors:
            i = runners_id.index(runner_id)
            print(f"{runners_name[i]} ({runner_id})")


def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    menu = "\n\n1. Show the results for a race " \
           "\n2. Add results for a race " \
           "\n3. Show all competitors by county " \
           "\n4. Show the winner of each race " \
           "\n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race " \
           "\n7. Show all competitors who have not taken a podium-position in any race. " \
           "\n8. Quit \n "
    input_menu = read_integer_between_numbers(menu, 1, 8)
    while input_menu != 8:

        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)

        elif input_menu == 2:
            users_venue(races_location, runners_id)

        elif input_menu == 3:
            runners_name, runners_id = runners_data()
            competitors_by_county(runners_name)

        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)

        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)

        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)

        elif input_menu == 7:
            competitors_not_on_podium(races_location, runners_name, runners_id)

        elif input_menu == 8:
            quit()

        print()

        input_menu = read_integer_between_numbers(menu, 1, 8)
    updating_races_file(races_location)


main()
