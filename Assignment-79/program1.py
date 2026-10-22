import tkinter as tk

root = tk.Tk()

root.title("----Addition----")

root.geometry("400x300")

tk.Label(root,text="Addition Application",font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root,text="Enter Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

def Addition():
  no1 = int(entry1.get())
  no2 = int(entry2.get())

  result = no1 + no2

  labelresult.configure(text = "Addition is:"+str(result))

tk.Button(root,text="Addition",command=Addition).pack(pady=15)

labelresult = tk.Label(root,text="",font=("Arial",14))

labelresult.pack()

root.mainloop()
