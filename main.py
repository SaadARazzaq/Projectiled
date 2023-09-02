import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to calculate projectile motion
def projectile_motion(angle, initial_velocity, gravity=9.81):
    angle_radians = np.radians(angle)
    time_of_flight = (2 * initial_velocity * np.sin(angle_radians)) / gravity
    max_height = (initial_velocity**2) * (np.sin(angle_radians)**2) / (2 * gravity)
    
    time_steps = 100
    time = np.linspace(0, time_of_flight, time_steps)
    
    x = initial_velocity * np.cos(angle_radians) * time
    y = initial_velocity * np.sin(angle_radians) * time - 0.5 * gravity * time**2
    
    return x, y

# Set up initial values
initial_angle = 45  # degrees
initial_velocity = 20  # m/s

# Create the figure and axes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the layout to make room for sliders

# Plot the initial trajectory
x_vals, y_vals = projectile_motion(initial_angle, initial_velocity)
trajectory, = plt.plot(x_vals, y_vals)

# Set axis labels and title
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("Projectile Motion Simulation")

# Add sliders for angle and initial velocity
ax_angle = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
ax_velocity = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor="lightgoldenrodyellow")

s_angle = Slider(ax_angle, "Launch Angle (degrees)", 0, 90, valinit=initial_angle)
s_velocity = Slider(ax_velocity, "Initial Velocity (m/s)", 0, 100, valinit=initial_velocity)

# Function to update the plot when sliders change
def update(val):
    angle = s_angle.val
    velocity = s_velocity.val
    
    x_vals, y_vals = projectile_motion(angle, velocity)
    trajectory.set_xdata(x_vals)
    trajectory.set_ydata(y_vals)
    fig.canvas.draw_idle()

# Attach the update function to the slider events
s_angle.on_changed(update)
s_velocity.on_changed(update)

# Show the plot
plt.show()
