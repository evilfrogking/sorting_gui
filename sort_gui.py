"""This module provides a graphical user interface (GUI) for a searching algorithm.

This application creates a tkinter GUI containing a canvas with 10 bars of varying heights,
an entry box for inputting a search value, a search button for executing the search,
and a label for displaying whether the input value has been found among the bar heights.
"""


import tkinter as tk
import random


# Constants
NUM_OF_BARS = 20
DELAY = 200
SHAPE_COLOR = "pink"
BOARDER_COLOR = "black"

# Sorting App
def main():
    """Initialize a tkinter application for searching a specific value among 10 bars."""
    # Set up the window and canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, bg="light blue", width=600, height=150)
    root.title("Search Algorithms App")

    # Create 20 bars on Canvas
    bar_list = create_bars(canvas)

    # Entry box
    entry_box = tk.Entry(root)

    # Create a StringVar object to update the text in the indicator_label
    done_indicator_text = tk.StringVar()   # or, indicator_label = tk.Label(root, text="")

    # Label: text showing whether the value is found when the search is done
    # Connected with done_indicator_text
    indicator_label = tk.Label(root, textvariable=done_indicator_text)

    # Button
    search_button = tk.Button(
        root,
        text="SEARCH",
        command=lambda: search_button_clicked(canvas, entry_box, done_indicator_text, bar_list)
        )

    # Layout of the GUI
    canvas.grid(column=0, row=0)
    search_button.grid(column=0, row=2)
    indicator_label.grid(column=1, row=0)
    entry_box.grid(column=1, row=2)

    # Apply configurations to all children widgets of the root container
    # padding configuration (padx=10, pady=10)
    for widget in root.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    root.mainloop()

def create_bars(canvas):
    """Create 10 bars in a tkinter canvas widget, and return a list containing their IDs.
  
    Args:
        canvas (tk.Canvas): The canvas on which the bars will be drawn.
    
    Returns:
        list: A list containing the IDs of the bars created on the canvas.
    """
    # The following constants define the appearance and positioning of the bars.
    BAR_WIDTH = 15    # The width of each bar
    BAR_GAP = 15      # The gap between each bar
    MIN_HEIGHT = 10   # The minimum height a bar can have
    MAX_HEIGHT = 125  # The maximum height a bar can have
    X_OFFSET = 10     # The x-coordinate for the bars' left edge
    Y_OFFSET = 10     # The y-coordinate for the bars' top edge

    bar_id_list = []
    for count in range(NUM_OF_BARS):
        # Create a random height
        random_height = random.randint(MIN_HEIGHT, MAX_HEIGHT)

        bar_id = canvas.create_rectangle(
                                        # x0
                                        (BAR_WIDTH + BAR_GAP) * count + X_OFFSET,
                                        # y0
                                        (MAX_HEIGHT - random_height) + Y_OFFSET,
                                        # x1
                                        (BAR_WIDTH + BAR_GAP) * count + X_OFFSET + BAR_WIDTH,
                                        # y1
                                        MAX_HEIGHT + Y_OFFSET,
                                        fill=SHAPE_COLOR,
                                        outline=BOARDER_COLOR
                                        )

        bar_id_list.append(bar_id)

        # Show bar height beneath each bar
        x_text = (BAR_WIDTH + BAR_GAP) * count + X_OFFSET + 10
        y_text = MAX_HEIGHT + Y_OFFSET + 10
        canvas.create_text(x_text, y_text, text=f"{random_height}")

    return bar_id_list

def change_shape_color(canvas, shape_id, color):
    """Change the color of a shape on a tkinter Canvas.

    Args:
        canvas (tk.Canvas): The canvas which contains the shape.
        shape_id (int): The ID of the shape.
        color (str): The color to set for the shape.
    """
    canvas.itemconfig(shape_id, fill=color)


def search_value(canvas, value, delay_factor, shape_height, shape_id):
    """Search for a given value and modifies the shape color on the canvas.

    Args:
        canvas (tk.Canvas): The canvas on which the shape is drawn.
        value (int): The target value being searched.
        delay_factor (int): The factor applied to the base delay for changing the shape color.
        shape_height (int): The height of the shape being compared.
        shape_id (int): The unique identifier of the shape on the canvas.

    Returns:
        bool: True if the value is found, False otherwise.
    """
    # Initialize a flag to check whether a value is found
    value_found = False
    # If the height of the current shape equals the target value
    if value == shape_height:
        # Change the shape color to green and set the flag to True
        canvas.after(delay_factor*DELAY, change_shape_color, canvas, shape_id, "green")
        value_found = True
    else:
        # If target value is not found, change the shape color to yellow
        canvas.after(delay_factor*DELAY, change_shape_color, canvas, shape_id, "yellow")

    return value_found

def move_rectangle(canvas, bar_id):
    canvas.move(bar_id, 0,0)



def search_button_clicked(canvas, entry, indicator_text_var, shape_id_list):
    """Handle the event when the search button is clicked.

    This function retrieves an integer value from the Entry widget,
    then searches for a shape of that height in the list of shapes.
    The color of the shapes will be changed according to the search results,
    and the result will be displayed on the GUI.

    Args:
        canvas (tk.Canvas): The canvas which contains the shapes.
        entry (tk.Entry): The Entry widget from which the target value is retrieved.
        strvar_obj (tk.StringVar): StringVar object tied to the label that displays search results.
        shape_id_list (list): The list of shape IDs to be searched.
    """
    # Jason
    for id in shape_id_list:
      change_shape_color(canvas, id, SHAPE_COLOR)

    # Get target value from the user input. Expect an integer value.
    try:
        value = int(entry.get())
    except ValueError:
        print("Please enter an integer.")
        return

    # Initialize a flag to check whether a value is found
    value_found = False
    # Loop through each shape in the list
    for index, shape_id in enumerate(shape_id_list, 1):
        print(shape_id)
        
        # canvas.coords() returns a list of coordinates for the given item in ARGS
        # e.g. (x0, y0, x1, y1)
        current_id_coords = canvas.coords(shape_id)
        # Calculate the height of the current shape
        current_shape_height = current_id_coords[3] - current_id_coords[1]


        value_found = search_value(canvas, value, index, current_shape_height, shape_id) or \
                      value_found

    # Display search result using done_indicator_text
    # Display the result after all bars have been processed
    # i.e., after NUM_OF_BARS*DELAY milliseconds
    if value_found:
        move_rectangle(canvas, shape_id)
        # indicator_label.config(text=f"{value} found!")
        # done_indicator_text.set(f"{value} found!")
        canvas.after(NUM_OF_BARS*DELAY, indicator_text_var.set, f"{value} found!")

    else:
        # indicator_label.config(text=f"{value} not found!")
        # done_indicator_text.set(f"{value} not found!")
        canvas.after(NUM_OF_BARS*DELAY, indicator_text_var.set, f"{value} not found!")


# Merge Sort Class

def merge_sort(lst: list) -> list:
    """Sort a list in ascending order using the merge sort algorithm.

    Args:
        lst (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    if len(lst) < 2:
        return lst
    # otherwise, find the mid point
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    # Merge sorted halves
    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into one single, sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: A single, sorted list that merges the left and right lists.
    """
    sorted_list = []
    # Point to the begining of the left & right of the list
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append the left half to the list if the right half is done first
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Append the right half to the list if the left half is done first
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    
    return sorted_list

if __name__ == "__main__":
    main()
