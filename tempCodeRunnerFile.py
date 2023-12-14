def find_minimum_difficulty(jobs, d):
  
  # Sort the tasks in decreasing order of difficulty.
  jobs.sort(reverse=True)

  # Initialize the difficulty of each day.
  difficulty = [0] * d

  # Iterate over the tasks and assign them to the days.
  for i in range(len(jobs)):
    # Find the day with the highest difficulty that has not been assigned a task yet.
    day = difficulty.index(min(difficulty))

    # Assign the task to the day.
    difficulty[day] = jobs[i]

  # Return the sum of the difficulty of each day.
  return sum(difficulty)


# Example usage:
jobs = [3, 4, 7, 15]
d = 10

minimum_difficulty = find_minimum_difficulty(jobs, d)

print("The minimum difficulty faced by Simon is:", minimum_difficulty)
