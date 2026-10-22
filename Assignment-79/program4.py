import tkinter as tk

root = tk.Tk()

root.title("----Vote Eligibility----")

root.geometry("400x300")

tk.Label(root,text="Vote Eligibility Application",font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter Name:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root,text="Enter Age:").pack()
entry2 = tk.Entry(root)
entry2.pack()

def Check():
  name = entry1.get()
  age = int(entry2.get())

  if age >= 18:
    result = f"Name :{name}\nEligible for voting"
  else:
    result = f"Name :{name}\nNot Eligible for voting"

  labelresult.config(text=result)
  
  
tk.Button(root,text="CheckEligibility",command=Check).pack(pady=15)

labelresult = tk.Label(root,text="",font=("Arial",14))

labelresult.pack()

root.mainloop()