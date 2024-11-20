import numpy as np
import matplotlib.pyplot as plt

def y_function(x):
    return np.sin(x)

def y_derivative(x):
    return np.cos(x)

# Define the range for the curve
x = np.arange(-5, 5, 0.1)
y = y_function(x)

# Initial position
current_pos = (1.5, y_function(1.5) )

# Learning rate
learning_rate = 0.1

# Create the plot
plt.figure(figsize=(10, 6))

for _ in range(100):
    # Update the position using gradient descent
    new_x = current_pos[0] - learning_rate * y_derivative(current_pos[0])
    new_y = y_function(new_x)
    current_pos = (new_x, new_y)

    # Clear the current frame
    plt.clf()

    # Plot the curve
    plt.plot(x, y, label="y = x^2", color='blue')
    plt.scatter(current_pos[0], current_pos[1], color='red', label="Current Position")
    plt.title("Gradient Descent on y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()

    # Pause to create the animation effect
    plt.pause(0.05)

plt.show()
