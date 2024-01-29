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
            password="****",
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

                    
    
                            #FULL CODE IS NOT ATTACHED.
