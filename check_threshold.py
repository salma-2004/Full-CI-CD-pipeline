with open("accuracy.txt", "r") as f:
    acc = float(f.read())

print("Accuracy:", acc)

if acc < 0.85:
    raise Exception("Model accuracy below threshold!")

print("Model passed")
