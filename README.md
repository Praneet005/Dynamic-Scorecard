# Dynamic-Scorecard
Dynamic Scorecard for ICC Cricket World 2023

Dyanmic scorecard is used to fetch the runs scored and wickets fallen betweeen 2 given overs in the 2023 Cricket World. We have to select the match, innings, mention the start over and the end over so that it displays the runs scored, wickets fallen, highest run scorer and most economic bowler between those 2 overs. It also displays a runs-over graph to calculate the run rate between the 2 overs.

Use:
This can be used for data analysis purpose to find who is the better batsman and better bowler between 2 given overs so that they can be used more efficiently in the successive matches. 

Packages Used:

1.Tkinter: Python's standard GUI (Graphical User Interface) package.

2.mysql-connector-python: A MySQL driver for Python to connect to and interact with MySQL databases.

3.matplotlib: A 2D plotting library for Python, used for creating plots and graphs.

[Cricsheet](https://cricsheet.org/)  Datasets were taken from this site and only the necessary details were extracted from each file.

Imports: The necessary libraries are imported including tkinter for GUI, mysql.connector for MySQL database connection, and matplotlib for plotting graphs.

Function Definitions:

Imports: The necessary libraries are imported including tkinter for GUI, mysql.connector for MySQL database connection, and matplotlib for plotting graphs.

Function Definitions:

1.fetch_match_names(): Fetches the match numbers and team information from the database and updates a combobox with the fetched data.

2.fetch_and_display_info(): Fetches batting-related information based on user-selected parameters like match, innings, and over numbers. It displays total runs scored, total wickets fallen, and plots a graph of runs scored over overs.

3.plot_runs_overs_graph(): Fetches data from the database to plot a graph of runs scored over overs for a specific match, innings, and over range.

4.fetch_wickets_count(): Fetches wicket count for a specified match, innings, and over number.

5.display_additional_info(): Displays additional information such as the highest run scorer and the most economic bowler for a specific match, innings, and over range.

GUI Creation:

1.The main window is created using tk.Tk().

2.Labels, comboboxes, entries, buttons, and text widgets are created and placed within the window using grid layout management.

3.Widgets are configured and initialized.

Event Handling:

1.Button click events are handled to fetch and display information based on user selections.

2.Error handling is implemented to handle potential MySQL errors.

Main Event Loop:The main event loop (root.mainloop()) is started to run the GUI application.


Overall, this code represents a GUI application for fetching and displaying cricket match statistics stored in a MySQL database, allowing users to interactively select parameters and view relevant information and graphs.

<img width="1512" alt="Dynamic Scorecard" src="https://github.com/Praneet005/Dynamic-Scorecard/assets/121420706/23e37ab8-5249-4c32-ae22-de90a4af2f41">
