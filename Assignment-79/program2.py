import tkinter as tk

root = tk.Tk()

root.title("----LargestNumber----")

root.geometry("400x300")

tk.Label(root,text="Find Largest Number Application",font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root,text="Enter Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root,text="Enter Third Number:").pack()
entry3 = tk.Entry(root)
entry3.pack()

def Largest():
  no1 = int(entry1.get())
  no2 = int(entry2.get())
  no3 = int(entry3.get())

  if(no1 > no2 and no1 > no3):
   labelresult.configure(text = "Largest is:"+str(no1))
  elif(no2>no1 and no2 > no3):
    labelresult.configure(text = "Largest is:"+str(no2))
  else:
    labelresult.configure(text = "Largest is:"+str(no3)) 

  
tk.Button(root,text="Largest",command=Largest).pack(pady=15)

labelresult = tk.Label(root,text="",font=("Arial",14))

labelresult.pack()

root.mainloop()