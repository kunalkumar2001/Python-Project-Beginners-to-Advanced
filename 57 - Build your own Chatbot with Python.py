import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2! How are you today?"]
    ],
    [
        r"(.*)(help|support)(.*)",
        ["I can help you 🙂 Tell me your problem."]
    ],
    [
        r"(.*)(your name|who are you)(.*)",
        ["I'm a Python GUI chatbot 🤖"]
    ],
    [
        r"(how are you|how r you)(.*)",
        ["I'm doing great!", "All good here 😄"]
    ],
    [
        r"sorry(.*)",
        ["No worries 👍", "It's okay 😊"]
    ],
    [
        r"(i am|i'm)(.*)(good|fine|okay|well)",
        ["Nice to hear that 😄", "That's great!"]
    ],
    [
        r"(hi|hello|hey|hola)(.*)",
        ["Hello 👋", "Hey there 🙂"]
    ],
    [
        r"(.*)(sports|game)(.*)",
        ["I like Cricket 🏏"]
    ],
    [
        r"(quit|exit|bye)",
        ["Bye! See you soon 👋"]
    ],
    [
        r"(.*)",
        ["Interesting 🤔 Tell me more.", "I see 👀"]
    ],
]

chatbot = Chat(pairs, reflections)

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("450x500")
        self.root.configure(bg= "#0f172a")
        
        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap = tk.WORD,
            bg = "#020617",
            fg = "white",
            font =("Consoals",11)            
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.insert(tk.END, "🤖 Bot: Hello! Type 'quit' to exit.\n")
        self.chat_area.config(state=tk.DISABLED)
        
        self.entry = tk.Entry(
            root,
            font=("Consolas", 12)
        )
        self.entry.pack(fill=tk.X, padx=10, pady=5)
        self.entry.bind("<Return>", self.send_message)
        
        self.send_btn = tk.Button(
            root,
            text="Send",
            command= self.send_message,
            bg = "#38bdf8",
            fg = "black"
        )
        self.send_btn.pack(pady=5)
        
    def send_message(self, event = None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"🧑 You: {user_input}\n")
        
        response = chatbot.respond(user_input.lower())
        self.chat_area.insert(tk.END, f"🤖 Bot: {response}\n\n")
        
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)
        self.entry.delete(0, tk.END)
        
        if user_input.lower() in ["quit", "bye", "exit"]:
            self.root.after(100, self.root.destroy)
            
if __name__ =="__main__":
    root = tk.Tk()
    ChatbotGUI(root)
    root.mainloop()
        