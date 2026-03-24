import random

accuracy = 0.80  # fail first

run_id = "run_" + str(random.randint(1000, 9999))

with open("model_info.txt", "w") as f:
    f.write(run_id)

with open("accuracy.txt", "w") as f:
    f.write(str(accuracy))

print("Training done")
