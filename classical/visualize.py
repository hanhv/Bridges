import matplotlib.pyplot as plt
import os


def visualize_classical(directory_out, list_2, list_3, list_4, list_5, list_unknown_4, list_unknown_5):
    # Data
    labels = ['2', '3', '4', '5', '3 or 4', '3, 4 or 5']
    data_points = [len(list_2), len(list_3), len(list_4), len(list_5), len(list_unknown_4), len(list_unknown_5)]

    # Plotting
    plt.figure(figsize=(10, 6))

    # Plotting labeled data with darkblue color
    bars1 = plt.bar(labels[:4], data_points[:4], color='darkblue')

    # Plotting unknown data with red color
    bars2 = plt.bar(labels[4:], data_points[4:], color='red')

    # Adding labels above bars
    for bars in [bars1, bars2]:
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(bar.get_height()), ha='center',
                     va='bottom', color='black')

    # Adding labels and title
    plt.xlabel('Bridge numbers')
    plt.ylabel('Number of data points')
    plt.title('Distribution of bridge numbers for classical knots')

    # Add legend
    plt.legend(['Labeled data', 'Unknown'], loc='upper right')

    # Save the plot
    plt.savefig(os.path.join(directory_out, 'bar_chart.png'))

    # Display the plot
    plt.show()
    # plt.pause(3)
