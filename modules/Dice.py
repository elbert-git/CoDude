import random

#main roll func
#rolls amount of dice in argument
#returns an array of successes and failures
def roll(dice_rolls):
    limit = 20
    if dice_rolls < limit:
        #get rolls
        roll_list = []
        for i in range(dice_rolls):
            roll_list.append(random.randrange(0,2))

        #convert to array of successes and failures
        success_count = 0
        for i in roll_list:
            if i == 1:
                success_count += 1
        failures_count =  dice_rolls - success_count

        return [success_count, failures_count]
    else:
        return "woops"

