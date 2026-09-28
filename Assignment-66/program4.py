X = float(input("Enter input:"))
weight = float(input("Enter weight:"))
bias =float(input("Enter bias:"))
target =float(input("Enter target output:"))
learning_rate = float(input("Enter learning rate:"))

#Step 2 : calculate predicition
prediction = (X * weight) + bias

#Step 3: Calculate error
error = target - prediction

#store old value
old_weight = weight
old_bias = bias

#Step 4:update weight using gradient descent logic
weight = weight + (learning_rate * error * X)

#update bias
bias = bias + (learning_rate * error)

#Step 5 : Display result
print("\n--- ANN Weight Update ---")
print("Prediction       :", prediction)
print("Target           :", target)
print("Error            :", error)
print("Old Weight       :", old_weight)
print("Updated Weight   :", weight)
print("Old Bias         :", old_bias)
print("Updated Bias     :", bias)