import numpy as np
import matplotlib.pyplot as plt

def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5

def calculate_gradient(x, y):  # Gradient vector
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)

x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

current_pos1 = (0.7, 0.4, z_function(0.7, 0.4))
current_pos2 = (0.3, 0.8, z_function(0.3, 0.8))
current_pos3 = (-0.5, 0.5, z_function(-0.5, 0.5))

learning_rate = 0.00001
ax = plt.subplot(projection='3d')

for _ in range(100):
    # Update position 1
    X_derivative, Y_derivative = calculate_gradient(current_pos1[0], current_pos1[1])
    X_new, Y_new = current_pos1[0] - learning_rate * X_derivative, current_pos1[1] - learning_rate * Y_derivative
    current_pos1 = (X_new, Y_new, z_function(X_new, Y_new))

    # Update position 2
    X_derivative, Y_derivative = calculate_gradient(current_pos2[0], current_pos2[1])
    X_new, Y_new = current_pos2[0] - learning_rate * X_derivative, current_pos2[1] - learning_rate * Y_derivative
    current_pos2 = (X_new, Y_new, z_function(X_new, Y_new))

    # Update position 3
    X_derivative, Y_derivative = calculate_gradient(current_pos3[0], current_pos3[1])
    X_new, Y_new = current_pos3[0] - learning_rate * X_derivative, current_pos3[1] - learning_rate * Y_derivative
    current_pos3 = (X_new, Y_new, z_function(X_new, Y_new))

    # Plot surface and points
    ax.plot_surface(X, Y, Z, cmap='viridis', zorder=0, alpha=0.8)
    ax.scatter(current_pos1[0], current_pos1[1], current_pos1[2], color='magenta', zorder=1)
    ax.scatter(current_pos2[0], current_pos2[1], current_pos2[2], color='orange', zorder=1)
    ax.scatter(current_pos3[0], current_pos3[1], current_pos3[2], color='cyan', zorder=1)
    plt.pause(0.001)
    ax.cla()  # Clear axis instead of clearing figure
