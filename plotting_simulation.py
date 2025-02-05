import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplotlib.pyplot as plt
import numpy as np
import time

def animated_plot(car, road, time_step, dynamics_initialized):

    simulated_time, position_list = dynamics_initialized.dynamics(car, road)

    positions = np.array(position_list)
    y_axis = np.ones(len(positions)) * 40  # A way to choose where the fixed y-axis is.

    fig, ax = plt.subplots(figsize=(7, 5))

    line, = ax.plot([], [], color='green', label="Car", linewidth=car.width * 2)

    ax.plot([road.starting_position, road.end_position], [45, 45], color='black',
            linestyle='-', linewidth=1.1, label='Road edge')
    ax.plot([road.starting_position, road.end_position], [35, 35], color='black',
            linestyle='-', linewidth=1.1)

    ax.set_xlim([-20, road.length + 20])
    ax.set_ylim([-20, road.length + 20])
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    fig.tight_layout()

    ax.set_xlabel('Space [m]')
    ax.set_ylabel('Space [m]')
    ax.set_title('Traffic simulation')
    ax.legend([f'Car (speed: {car.speed} m/s)', 'Road edge'], facecolor='white',
              edgecolor='black', borderpad=1.5)

    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

    time_text = ax.text(
        0.05, 0.9, '',
        transform=ax.transAxes, fontsize=10, color='Black',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3', alpha=0.8))

    #start_time = time.time()

    is_paused = [False]

    def update(frame):

        if is_paused[0]:

            return line, time_text
        
        line.set_xdata(positions[frame])
        line.set_ydata([y_axis[frame], y_axis[frame]])

        #elapsed_time = time.time() - start_time
        elapsed_time = frame * time_step
        time_text.set_text(f'Time: {elapsed_time:.2f} s')

        return line, time_text

    animated_plot = animation.FuncAnimation(fig, update, frames=len(positions),
                                            interval=100, blit=True)

    button_ax = plt.axes([0.4, 0.02, 0.2, 0.075])
    pause_button = Button(button_ax, 'Pause/Play')

    def toggle_pause(event):

        is_paused[0] = not is_paused[0]

    pause_button.on_clicked(toggle_pause)

    plt.show()

    return animated_plot

# The pause button and real timer work but simulation doesn't stop.