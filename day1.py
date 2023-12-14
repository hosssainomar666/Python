def find_minimum_difficulty(jobs, d):
  

  # Sort the tasks in decreasing order of difficulty.
  jobs.sort(reverse=True)

  # Initialize the difficulty of each day.
  difficulty = [0] * d

  # Keep track of which tasks have been completed.
  completed_tasks = set()

  # Initialize the queue of tasks to be scheduled.
  queue = jobs[:]

  # Iterate over the days.
  for i in range(d):
    # Find the task with the highest difficulty that can be completed on that day, taking into account task dependencies.
    while queue and not all(job in completed_tasks for job in queue[:i]):
      queue.pop(0)

    # If there are no tasks that can be completed on that day, then we are done.
    if not queue:
      break

    # Schedule the task with the highest difficulty that has no dependencies.
    while queue and queue[0] in completed_tasks:
      queue.pop(0)

    if queue:
      difficulty[i] = queue.pop(0)
      completed_tasks.add(difficulty[i])

  # Return the sum of the difficulty of each day.
  return sum(difficulty)


# Example usage:
jobs = [3, 4, 7, 15]
d = 10

minimum_difficulty = find_minimum_difficulty(jobs, d)

print("The minimum difficulty faced by Simon is:", minimum_difficulty)
