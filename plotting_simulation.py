import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time # To implement real time timer.

def animated_plot(car, road, time_step, dynamics_initialized):

    time, position_list = dynamics_initialized.dynamics(car, road)

    positions = np.array(position_list)
    y_axis = np.ones(len(positions)) * 40  # A way to choose where the fixed y-axis is.

    fig, ax = plt.subplots(figsize=(7, 5))

    line, = ax.plot([], [], color='green', label="Car", linewidth=car.width * 2)

    ax.plot([road.starting_position, road.end_position], [45, 45], color='black',
            linestyle='-', linewidth=1.1, label="Road edge")
    ax.plot([road.starting_position, road.end_position], [35, 35], color='black',
            linestyle='-', linewidth=1.1)

    ax.set_xlim([-20, road.length + 20])
    ax.set_ylim([-20, road.length + 20])
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    fig.tight_layout()

    ax.set_xlabel("Space [m]")
    ax.set_ylabel("Space [m]")
    ax.set_title("Traffic simulation")
    ax.legend()

    plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

    time_text = ax.text(
        0.05, 0.9, '',
        transform=ax.transAxes, fontsize=10, color='Black',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3', alpha=0.8))

    def update(frame):
        line.set_xdata(positions[frame])
        line.set_ydata([y_axis[frame], y_axis[frame]])
        elapsed_time = frame * time_step
        time_text.set_text(f"Time: {elapsed_time:.2f} s")

        return line, time_text

    animated_plot = animation.FuncAnimation(fig, update, frames=len(positions),
                                            interval=100, blit=True)
    plt.show()

    return animated_plot

# Let's add a pause button and a real time timer.