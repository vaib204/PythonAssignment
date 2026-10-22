import tkinter as tk

root = tk.Tk()

root.title("----Area Of Circle----")

root.geometry("400x300")

tk.Label(root,text="Area Of circle",font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter Radius:").pack()
entry1 = tk.Entry(root)
entry1.pack()


def Calculate():
  no1 = int(entry1.get())
  PI = 3.14159
  result = PI * no1*no1

  labelresult.configure(text = "Area is:"+str(result)+"cm2")

tk.Button(root,text="Calculate Area",command=Calculate).pack(pady=15)

labelresult = tk.Label(root,text="",font=("Arial",14))

labelresult.pack()

root.mainloop()