import tkinter as tk
from tkinter import Label, ttk, Entry, Button, messagebox
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fetch_match_names():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="icc_cwc"
        )
        cursor = connection.cursor()

        query = "SELECT DISTINCT m.match_no, CONCAT(m.team1, ' vs ', m.team2) FROM matches m JOIN scores s ON m.match_no = s.match_no"
        cursor.execute(query)
        matches_data = cursor.fetchall()

        if not matches_data:
            messagebox.showinfo("No Matches", "No matches available.")
            return

        match_combobox['values'] = [f"{match[0]} - {match[1]}" for match in matches_data]

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def fetch_and_display_info():
    selected_match = match_combobox.get().split(" - ")[0] 
    selected_innings = innings_combobox.get()
    start_over_no = start_over_no_entry.get()
    end_over_no = end_over_no_entry.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="icc_cwc"
        )
        cursor = connection.cursor()

        query = f"""
            SELECT 
                SUM(bat_score + ext_score),
                MAX(wicket_count)
            FROM 
                scores s
            JOIN 
                matches m ON s.match_no = m.match_no
            WHERE 
                s.match_no = {selected_match} AND
                s.innings = {selected_innings} AND
                s.over_no BETWEEN {start_over_no} AND {end_over_no}
        """
        cursor.execute(query)
        summary_data = cursor.fetchall()

        if not summary_data or summary_data[0][0] is None:
            messagebox.showinfo("No Data", f"No batting data available for the specified parameters.")
            return

        total_runs = summary_data[0][0]
        total_wickets = summary_data[0][1]

        info_text.config(state=tk.NORMAL)
        info_text.delete("1.0", tk.END)
        info_text.insert(tk.END, f"Total Runs Scored: {total_runs}\n")
        info_text.insert(tk.END, f"Total Wickets Fallen: {total_wickets}\n")
        info_text.config(state=tk.DISABLED)

        display_additional_info(selected_match, selected_innings, start_over_no, end_over_no, cursor)

        plot_runs_overs_graph(selected_match, selected_innings, start_over_no, end_over_no, cursor)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def plot_runs_overs_graph(selected_match, selected_innings, start_over_no, end_over_no, cursor):
    try:
        query = f"""
            SELECT 
                over_no, 
                SUM(bat_score + ext_score) 
            FROM 
                scores 
            WHERE 
                match_no = {selected_match} AND 
                innings = {selected_innings} AND 
                over_no BETWEEN {start_over_no} AND {end_over_no} 
            GROUP BY 
                over_no
        """
        cursor.execute(query)
        data = cursor.fetchall()

        over_no_values = [row[0] for row in data]
        runs_values = [row[1] for row in data]

        fig, ax = plt.subplots()
        ax.plot(over_no_values, runs_values, marker='o')
        ax.set_title(f"Runs-Overs - Match No: {selected_match}, Innings: {selected_innings}")
        ax.set_xlabel("Over No")
        ax.set_ylabel("Runs")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

def fetch_wickets_count(cursor, selected_match, selected_innings, over_no):
    query = f"SELECT wicket_count FROM scores WHERE match_no = {selected_match} AND innings = {selected_innings} AND over_no = {over_no}"
    cursor.execute(query)
    wickets_data = cursor.fetchall()
    return wickets_data[0][0] if wickets_data else 0

def display_additional_info(selected_match, selected_innings, start_over_no, end_over_no, cursor):
    query = f"SELECT batsman, SUM(bat_score + ext_score) AS total_runs FROM scores WHERE match_no = {selected_match} AND innings = {selected_innings} AND over_no BETWEEN {start_over_no} AND {end_over_no} GROUP BY batsman ORDER BY total_runs DESC LIMIT 1"
    cursor.execute(query)
    highest_scorer_data = cursor.fetchall()

    query = f"SELECT bowler, AVG(bat_score + ext_score) AS economy FROM scores WHERE match_no = {selected_match} AND innings = {selected_innings} AND over_no BETWEEN {start_over_no} AND {end_over_no} GROUP BY bowler ORDER BY economy LIMIT 1"
    cursor.execute(query)
    economic_bowler_data = cursor.fetchall()

    highest_scorer = highest_scorer_data[0][0] if highest_scorer_data else "N/A"
    economic_bowler = economic_bowler_data[0][0] if economic_bowler_data else "N/A"

    additional_info_text.config(state=tk.NORMAL)
    additional_info_text.delete("1.0", tk.END)
    additional_info_text.insert(tk.END, f"Highest Run Scorer: {highest_scorer}\n")
    additional_info_text.insert(tk.END, f"Most Economic Bowler: {economic_bowler}\n")
    additional_info_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Batsman Stats Retrieval and Plotting")

label_match = Label(root, text="Select Match:")
label_match.grid(row=0, column=0, padx=10, pady=10, sticky="e")

match_combobox = ttk.Combobox(root)
match_combobox.grid(row=0, column=1, padx=10, pady=10)

fetch_match_names()

label_innings = Label(root, text="Select Innings:")
label_innings.grid(row=1, column=0, padx=10, pady=10, sticky="e")

innings_combobox = ttk.Combobox(root, values=["1", "2"])
innings_combobox.grid(row=1, column=1, padx=10, pady=10)

label_start_over_no = Label(root, text="Enter Start Over No:")
label_start_over_no.grid(row=2, column=0, padx=10, pady=10, sticky="e")

start_over_no_entry = Entry(root)
start_over_no_entry.grid(row=2, column=1, padx=10, pady=10)

label_end_over_no = Label(root, text="Enter End Over No:")
label_end_over_no.grid(row=3, column=0, padx=10, pady=10, sticky="e")

end_over_no_entry = Entry(root)
end_over_no_entry.grid(row=3, column=1, padx=10, pady=10)

button_fetch_info = Button(root, text="Fetch and Display Info", command=fetch_and_display_info)
button_fetch_info.grid(row=4, column=0, columnspan=2, pady=10)

info_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
info_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

additional_info_text = tk.Text(root, height=2, width=50, state=tk.DISABLED)
additional_info_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
