import tkinter as tk
from datetime import datetime
import random

# ===== COMMAND ENGINE =====
def run_command(cmd):
    output.insert(tk.END, f"ShellAtolCONSOLE>>[{cmd}\n")

    if cmd == "help":
        output.insert(tk.END,
"""Commands:
help
clear
echo
time
date
version
about
whoami
random
calc
upper
lower
reverse
color
bg

""")

    elif cmd == "clear":
        output.delete(1.0, tk.END)
        return

    elif cmd.startswith("echo "):
        output.insert(tk.END, cmd[5:] + "\n\n")

    elif cmd.startswith("upper "):
        output.insert(tk.END, cmd[6:].upper() + "\n\n")

    elif cmd.startswith("lower "):
        output.insert(tk.END, cmd[6:].lower() + "\n\n")

    elif cmd.startswith("reverse "):
        output.insert(tk.END, cmd[8:][::-1] + "\n\n")

    elif cmd == "time":
        output.insert(tk.END, datetime.now().strftime("%H:%M:%S") + "\n\n")

    elif cmd == "date":
        output.insert(tk.END, datetime.now().strftime("%Y-%m-%d") + "\n\n")

    elif cmd == "version":
        output.insert(tk.END, "ShellAtol v1.0.0\n\n")

    elif cmd == "about":
        output.insert(tk.END, "ShellAtol Desktop Console System\n\n")

    elif cmd == "whoami":
        output.insert(tk.END, "guest\n\n")

    elif cmd == "random":
        output.insert(tk.END, str(random.randint(0, 100)) + "\n\n")

    elif cmd.startswith("calc "):
        try:
            result = eval(cmd[5:])
            output.insert(tk.END, str(result) + "\n\n")
        except:
            output.insert(tk.END, "Invalid calculation\n\n")

    elif cmd.startswith("color "):
        root.config(fg=cmd[6:])
        output.insert(tk.END, "Text color changed\n\n")

    elif cmd.startswith("bg "):
        root.config(bg=cmd[3:])
        output.config(bg=cmd[3:])
        entry.config(bg=cmd[3:])
        output.insert(tk.END, "Background changed\n\n")

    else:
        output.insert(tk.END, "Unknown command\n\n")

    output.see(tk.END)


# ===== ENTER HANDLER =====
def handle_enter(event):
    cmd = entry.get().strip()
    if cmd:
        run_command(cmd)
    entry.delete(0, tk.END)


# ===== UI SETUP =====
root = tk.Tk()
root.title("ShellAtol Console")
root.geometry("800x500")
root.configure(bg="black")

# Header
header = tk.Label(root, text="ShellAtolCONSOLE v1.0.0.", anchor="w",
                  bg="black", fg="#00ff00", font=("Courier", 12))
header.pack(fill="x", padx=5, pady=5)

# Output console
output = tk.Text(root, bg="black", fg="#00ff00",
                 font=("Courier", 10), insertbackground="#00ff00")
output.pack(expand=True, fill="both", padx=5)

# Input area
frame = tk.Frame(root, bg="black")
frame.pack(fill="x")

prompt = tk.Label(frame, text="ShellAtolCONSOLE>>[",
                  bg="black", fg="#00ff00", font=("Courier", 10))
prompt.pack(side="left")

entry = tk.Entry(frame, bg="black", fg="#00ff00",
                 insertbackground="#00ff00", font=("Courier", 10))
entry.pack(side="left", fill="x", expand=True)

entry.bind("<Return>", handle_enter)

# Footer
footer = tk.Label(root,
                  text="Copyright ShellAtol 2026 Software Developer",
                  bg="black", fg="#00ff00", font=("Courier", 8))
footer.pack(fill="x", pady=5)

entry.focus()

root.mainloop()