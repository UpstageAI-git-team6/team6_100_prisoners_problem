from random import shuffle

successes = 0
failures = 0
master_loop_count = 1
while master_loop_count < 101:
    # Create the prisoner participants by assigning each one a number
    prisoner_number = []
    loop_count = 1
    while loop_count < 101:
        prisoner_number.append(loop_count)
        loop_count += 1