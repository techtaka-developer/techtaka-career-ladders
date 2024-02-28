import matplotlib.pyplot as plt
import numpy as np

class RadarChart:
    def __init__(self, categories, levels, yticks_labels=None):
        self.categories = categories
        self.levels = levels
        self.num_vars = len(categories)
        self.yticks_labels = yticks_labels if yticks_labels else {}

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
        plt.yticks([1, 2, 3, 4, 5], ["", "", "", "", ""], color="grey", size=7)

        plt.ylim(0, 5)

        # Plot data and fill with color
        values = [self.levels[cat] for cat in self.categories] + [self.levels[self.categories[0]]]
        ax.plot(angles, values, linewidth=2, linestyle='solid')
        ax.fill(angles, values, alpha=0.25)

        # Add custom y-tick labels if provided
        if self.yticks_labels:
            for cat, angle in zip(self.categories, angles):
                if cat in self.yticks_labels:
                    for level, label in enumerate(self.yticks_labels[cat], start=1):
                        ax.text(angle, level, label, horizontalalignment='center', size=7, color='grey')

        # Add a title
        plt.title('Level guide for each segment', size=20, color="black", y=1.1)
        plt.show()
        # Save the figure
        plt.savefig(output_filename, bbox_inches='tight')
        plt.close()


# Example usage:
categories = ['Technology', 'System', 'People', 'Process', 'Influence']

levels = {
    'Technology': 3,
    'System': 2,
    'People': 5,
    'Process': 4,
    'Influence': 5
}
# Define custom y-tick labels for each category
yticks_labels = {
    'Technology': ["Adopts", "Specializes", "Evangelizes", "Masters", "Creates"],
    'System': ["Enhances", "Designs", "Owns", "Evolves", "Leads"],
    'People': ["Learns", "Supports", "Mentors", "Coordinates", "Manages"],
    'Process': ["Follows", "Enforces", "Challenges", "Adjusts", "Defines"],
    'Influence': ["Individual", "Team", "Platform", "Engineering", "Company"],
}

# Create a RadarChart instance with the categories, levels, and custom y-ticks
radar_chart = RadarChart(categories, levels, yticks_labels)

# Generate and save the chart as a PNG file
radar_chart.create_chart('charts/radar_chart_with_yticks.png')
