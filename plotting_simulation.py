import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import numpy as np
import time

def animated_plot(cars, road, time_step, dynamics_initialized):

    simulated_time, position_list = dynamics_initialized.dynamics(cars, road)

    positions = np.array(position_list)
    print(positions)
    y_axis = np.ones(len(positions)) * road.vertical_position  # A way to choose where the fixed y-axis is.

    fig, ax = plt.subplots(figsize=(7, 5))

    # A color list to have different colored cars (can have up to 8 cars, but could theoretically have the whole matplotlib palette)
    color_list = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white', 'Lime', 'Fuchsia', 'Silver','Gray', 'Maroon','Olive','Purple','Teal','Navy']

    # Create a list of axes to plot for each car, with its own width (proportional to his length), label and color
    lines = [ax.plot([], [], linewidth=cars.width()[i]*0.5, color = color_list[i])[0] for i in range(len(cars))]
    
    # Instructions to have a pretty plot
    ax.plot([road.starting_position, road.end_position], [road.vertical_position + 3, road.vertical_position + 3],
            color='black', linestyle='-', linewidth=1.1, label='Road edge')
    ax.plot([road.starting_position, road.end_position], [road.vertical_position - 3, road.vertical_position - 3],
            color='black', linestyle='-', linewidth=1.1)
    ax.set_xlim([-20, road.length + 20])
    ax.set_ylim([-20, road.length + 20])
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    fig.tight_layout()
    ax.set_xlabel('Space [m]')
    ax.set_ylabel('Space [m]')
    ax.set_title('Traffic simulation')

    # Car label lists to have the car number and its speed
    car_labels = [f'Car {i} (speed: {cars.get_speeds()[i]} m/s)' for i in range(len(cars))]
    ax.legend(car_labels + ['Road edge'], facecolor='white', edgecolor='black', borderpad=1.5)

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

    # Timer plotting instructions
    time_text = ax.text(
        0.05, 0.9, '',
        transform=ax.transAxes, fontsize=10, color='Black',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3', alpha=0.8))

    is_paused = [False]

    # Initialization of the animation with an empty plot
    def init():
        for line in lines:
            line.set_data([], [])
        time_text.set_text('')
        return lines + [time_text]

    # Update function to animate the plot
    def update(frame):
        if is_paused[0]:
            return lines + [time_text]

        # Update the position of each car, where the[positions[frame, i, 0],positions[frame, i, 1]] represents the position of the front and the back of the car at the time setp of the frame
        for i in range(len(cars)):
            lines[i].set_data([positions[frame, i, 0],positions[frame, i, 1]], [y_axis[i], y_axis[i+1]])

        # Time elapsed since the beginning of the simulation
        elapsed_time = frame * time_step 
        time_text.set_text(f'Time: {elapsed_time:.2f} s')

        return lines + [time_text]

    # Animation instructions
    ani = animation.FuncAnimation(fig, update, init_func=init, frames=len(positions), interval=100, blit=True)

    # Pause button instructions
    button_ax = plt.axes([0.4, 0.02, 0.2, 0.075])
    pause_button = Button(button_ax, 'Pause/Play')

    def toggle_pause(event):
        is_paused[0] = not is_paused[0]

    pause_button.on_clicked(toggle_pause)

    plt.show()

    # The clearance time of the road is the time it takes for the last car to exit the road
    time_to_exit = len(positions)*time_step

    return animated_plot, time_to_exit
