import matplotlib.pyplot as plt
import numpy as np
class RadarChart:
    def __init__(self, categories, levels):
        self.categories = categories
        self.levels = levels
        self.num_vars = len(categories)

    def create_chart(self, output_filename):
        # Calculate the angle for each category
        angles = [n / float(self.num_vars) * 2 * np.pi for n in range(self.num_vars)]
        angles += angles[:1]  # Complete the loop

        # Initiate the spider plot
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

        # Rotate the chart so that the first axis is at the top
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable and add labels
        plt.xticks(angles[:-1], self.categories)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=7)
        plt.ylim(0, 5)

        # Plot data and fill with color
        values = [self.levels[cat] for cat in self.categories] + [self.levels[self.categories[0]]]
        ax.plot(angles, values, linewidth=2, linestyle='solid')
        ax.fill(angles, values, alpha=0.25)

        # Add a title
        plt.title('Level guide for each segment', size=20, color="black", y=1.1)

        # Save the figure
        plt.savefig(output_filename, bbox_inches='tight')
        # plt.show()
        plt.close()

# Example usage:
categories = ['System', 'Technology', 'Influence', 'Process', 'People']
levels = {
    'Technology': 3,
    'System': 5,
    'People': 5,
    'Process': 4,
    'Influence': 5
}

# Create a RadarChart instance with the categories and levels
radar_chart = RadarChart(categories, levels)

# Generate and save the chart as a PNG file
radar_chart.create_chart('charts/radar_chart.png')
