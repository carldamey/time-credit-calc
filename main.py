import tkinter as tk

window = tk.Tk()

test = tk.Label(text="hello world")

test.pack()

# window.mainloop()

def calculate_time(input_time, time_for_credit, credit_amount):
  ratio = credit_amount / time_for_credit
  calculated_time_minutes = float(input_time) * ratio
  calculated_time_hours = 0
  while calculated_time_minutes >= 60:
    calculated_time_hours += 1
    calculated_time_minutes -= 60
  return f"You can leave {calculated_time_hours} hours and {int(calculated_time_minutes)} minutes early."
  

  

converted_input_time = int(input("How many hours? ")) * 60 + int(input("How many minutes? "))

print(calculate_time(converted_input_time, 45, 30))



# X amount of time when every Y minutes you get Z credited