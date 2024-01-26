# Dynamic-Scorecard
Dynamic Scorecard for ICC Cricket World 2023

Dyanmic scorecard is basically used to fetch the runs scored and wickets fallen betweeen 2 given overs in the 2023 Cricket World. We select the match, innings and mention the start over and the end over so that it displays the runs scored, wickets fallen, highest run scorer and most economic bowler between those 2 overs. It also displays a runs-over graph to show the run rate between the 2 overs.

Use:
This can be used for data analysis purpose to find who is the better batsman and better bowler between 2 given overs so that they can be used more efficiently in the successive matches. 

Packages Used:

1.Tkinter: Python's standard GUI (Graphical User Interface) package.

2.mysql-connector-python: A MySQL driver for Python to connect to and interact with MySQL databases.

3.matplotlib: A 2D plotting library for Python, used for creating plots and graphs.

[Cricsheet](https://cricsheet.org/)  (Datasets were taken from this site for extraction).

Imports: The necessary libraries are imported including tkinter for GUI, mysql.connector for MySQL database connection, and matplotlib for plotting graphs.

Function Definitions:

fetch_match_names(): Fetches the match numbers and team information from the database and updates a combobox with the fetched data.
fetch_and_display_info(): Fetches batting-related information based on user-selected parameters like match, innings, and over numbers. It displays total runs scored, total wickets fallen, and plots a graph of runs scored over overs.
plot_runs_overs_graph(): Fetches data from the database to plot a graph of runs scored over overs for a specific match, innings, and over range.
fetch_wickets_count(): Fetches wicket count for a specified match, innings, and over number.
display_additional_info(): Displays additional information such as the highest run scorer and the most economic bowler for a specific match, innings, and over range.
GUI Creation:

The main window is created using tk.Tk().
Labels, comboboxes, entries, buttons, and text widgets are created and placed within the window using grid layout management.
Widgets are configured and initialized.
Event Handling:

Button click events are handled to fetch and display information based on user selections.
Error handling is implemented to handle potential MySQL errors.
Main Event Loop:

The main event loop (root.mainloop()) is started to run the GUI application.
Overall, this code represents a GUI application for fetching and displaying cricket match statistics stored in a MySQL database, allowing users to interactively select parameters and view relevant information and graphs.
