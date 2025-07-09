
import tkinter as tk
from tkinter import ttk, scrolledtext
import os
from .skins import skins, apply_skin
from .commands import run_command
from .utils import browse_directory, clear_output, save_output
from .ui_components import (
    create_project_tab,
    create_build_tab,
    create_testing_tab,
    create_nuget_tab,
    create_tooling_tab,
    create_info_tab
)

class DotNetGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(".NET CLI Manager")
        self.root.geometry("900x700")
        
        self.current_skin = 'Classic'
        self.working_directory = tk.StringVar(value=os.getcwd())
        
        self.setup_ui()
        self.apply_skin_to_gui()
        
    def setup_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        
        # Title and skin selector
        title_frame = ttk.Frame(self.main_frame)
        title_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.title_label = ttk.Label(title_frame, text=".NET CLI Manager", font=('Arial', 16, 'bold'))
        self.title_label.pack(side=tk.LEFT)
        
        skin_frame = ttk.Frame(title_frame)
        skin_frame.pack(side=tk.RIGHT)
        
        ttk.Label(skin_frame, text="Skin:").pack(side=tk.LEFT, padx=(0, 5))
        self.skin_var = tk.StringVar(value=self.current_skin)
        self.skin_combo = ttk.Combobox(skin_frame, textvariable=self.skin_var, values=list(skins.keys()), 
                                      state="readonly", width=10)
        self.skin_combo.pack(side=tk.LEFT)
        self.skin_combo.bind('<<ComboboxSelected>>', self.change_skin_handler)
        
        # Working directory
        dir_frame = ttk.Frame(self.main_frame)
        dir_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        dir_frame.columnconfigure(1, weight=1)
        
        ttk.Label(dir_frame, text="Working Directory:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.dir_var = tk.StringVar(value=self.working_directory.get())
        self.dir_entry = ttk.Entry(dir_frame, textvariable=self.dir_var, state="readonly")
        self.dir_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        self.browse_btn = ttk.Button(dir_frame, text="Browse", command=self.browse)
        self.browse_btn.grid(row=0, column=2)
        
        # Create notebook for categories
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Create tabs
        create_project_tab(self.notebook, self.working_directory, self.append_output)
        create_build_tab(self.notebook, self.working_directory, self.append_output)
        create_testing_tab(self.notebook, self.working_directory, self.append_output)
        create_nuget_tab(self.notebook, self.working_directory, self.append_output)
        create_tooling_tab(self.notebook, self.working_directory, self.append_output)
        create_info_tab(self.notebook, self.working_directory, self.append_output)
        
        # Output area
        output_frame = ttk.LabelFrame(self.main_frame, text="Output", padding="5")
        output_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=10, wrap=tk.WORD)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Control buttons
        control_frame = ttk.Frame(self.main_frame)
        control_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.clear_btn = ttk.Button(control_frame, text="Clear Output", command=self.clear)
        self.clear_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.save_btn = ttk.Button(control_frame, text="Save Output", command=self.save)
        self.save_btn.pack(side=tk.LEFT)
        
        # Configure main frame weights
        self.main_frame.rowconfigure(2, weight=1)
        self.main_frame.rowconfigure(3, weight=1)

    def append_output(self, text):
        def update_text():
            self.output_text.insert(tk.END, text)
            self.output_text.see(tk.END)
        
        self.root.after(0, update_text)

    def browse(self):
        browse_directory(self.working_directory, self.dir_var)

    def clear(self):
        clear_output(self.output_text)

    def save(self):
        save_output(self.output_text)

    def apply_skin_to_gui(self):
        apply_skin(self.root, self.output_text, self.title_label, self.current_skin)

    def change_skin_handler(self, event):
        self.current_skin = self.skin_var.get()
        self.apply_skin_to_gui()
