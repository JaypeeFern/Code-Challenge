def checkStepNumbers(system_names, step_numbers):
    current_system_name, current_system_step = system_names[0], step_numbers[0]
    for system_name, step in zip(system_names[1:], step_numbers[1:]):
        if system_name == current_system_name:
            if step <= current_system_step:
                return False
        else:
            current_system_name, current_system_step = system_name, step
    return True

# Test cases

system_names = ["tree_1", "tree_2", "house", "tree_1", "tree_2", "house"]
step_numbers = [1, 33, 10, 2, 44, 20]
print(checkStepNumbers(system_names, step_numbers)) # True

system_names = ["tree_1", "tree_1", "house"]
step_numbers = [2, 1, 10]
print(checkStepNumbers(system_names, step_numbers)) # False