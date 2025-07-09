
import tkinter as tk
from tkinter import ttk

# Skin configurations
skins = {
    'Classic': {
        'bg': '#f0f0f0',
        'fg': '#000000',
        'button_bg': '#e1e1e1',
        'button_fg': '#000000',
        'accent': '#0078d4',
        'text_bg': '#ffffff',
        'text_fg': '#000000'
    },
    'Dark': {
        'bg': '#2b2b2b',
        'fg': '#ffffff',
        'button_bg': '#404040',
        'button_fg': '#ffffff',
        'accent': '#0078d4',
        'text_bg': '#1e1e1e',
        'text_fg': '#ffffff'
    },
    'Neon': {
        'bg': '#0a0a0a',
        'fg': '#00ff00',
        'button_bg': '#1a1a1a',
        'button_fg': '#00ff00',
        'accent': '#ff00ff',
        'text_bg': '#050505',
        'text_fg': '#00ff00'
    },
    'Blue Ocean': {
        'bg': '#1e3a5f',
        'fg': '#e6f3ff',
        'button_bg': '#2d5a8c',
        'button_fg': '#ffffff',
        'accent': '#4dabf7',
        'text_bg': '#0d1929',
        'text_fg': '#e6f3ff'
    },
    'Sunset': {
        'bg': '#2d1b42',
        'fg': '#ffd0a6',
        'button_bg': '#4a2c6b',
        'button_fg': '#ffd0a6',
        'accent': '#ff6b6b',
        'text_bg': '#1a0d2e',
        'text_fg': '#ffd0a6'
    },
    'Forest': {
        'bg': '#1a3d2e',
        'fg': '#c8e6c9',
        'button_bg': '#2e5d47',
        'button_fg': '#c8e6c9',
        'accent': '#66bb6a',
        'text_bg': '#0d1f17',
        'text_fg': '#c8e6c9'
    },
    'Cyberpunk': {
        'bg': '#0f0f0f',
        'fg': '#ff073a',
        'button_bg': '#1a1a1a',
        'button_fg': '#ff073a',
        'accent': '#39ff14',
        'text_bg': '#000000',
        'text_fg': '#ff073a'
    },
    'Monokai': {
        'bg': '#272822',
        'fg': '#f8f8f2',
        'button_bg': '#3e3d32',
        'button_fg': '#f8f8f2',
        'accent': '#fd971f',
        'text_bg': '#1e1f1c',
        'text_fg': '#f8f8f2'
    },
    'Solarized Light': {
        'bg': '#fdf6e3',
        'fg': '#657b83',
        'button_bg': '#eee8d5',
        'button_fg': '#657b83',
        'accent': '#268bd2',
        'text_bg': '#ffffff',
        'text_fg': '#657b83'
    },
    'Solarized Dark': {
        'bg': '#002b36',
        'fg': '#839496',
        'button_bg': '#073642',
        'button_fg': '#839496',
        'accent': '#268bd2',
        'text_bg': '#001e26',
        'text_fg': '#839496'
    },
    'Dracula': {
        'bg': '#282a36',
        'fg': '#f8f8f2',
        'button_bg': '#44475a',
        'button_fg': '#f8f8f2',
        'accent': '#bd93f9',
        'text_bg': '#1e1f29',
        'text_fg': '#f8f8f2'
    },
    'Nord': {
        'bg': '#2e3440',
        'fg': '#d8dee9',
        'button_bg': '#3b4252',
        'button_fg': '#d8dee9',
        'accent': '#88c0d0',
        'text_bg': '#242933',
        'text_fg': '#d8dee9'
    },
    'Gruvbox': {
        'bg': '#282828',
        'fg': '#ebdbb2',
        'button_bg': '#3c3836',
        'button_fg': '#ebdbb2',
        'accent': '#fabd2f',
        'text_bg': '#1d2021',
        'text_fg': '#ebdbb2'
    },
    'One Dark': {
        'bg': '#21252b',
        'fg': '#abb2bf',
        'button_bg': '#2c323c',
        'button_fg': '#abb2bf',
        'accent': '#61afef',
        'text_bg': '#1e2127',
        'text_fg': '#abb2bf'
    },
    'Material': {
        'bg': '#263238',
        'fg': '#eeffff',
        'button_bg': '#37474f',
        'button_fg': '#eeffff',
        'accent': '#80cbc4',
        'text_bg': '#1e272c',
        'text_fg': '#eeffff'
    },
    'Tokyo Night': {
        'bg': '#1a1b26',
        'fg': '#a9b1d6',
        'button_bg': '#24283b',
        'button_fg': '#a9b1d6',
        'accent': '#7aa2f7',
        'text_bg': '#16161e',
        'text_fg': '#a9b1d6'
    }
}

def apply_skin(root, output_text, title_label, current_skin):
    skin = skins[current_skin]
    
    # Configure root window
    root.configure(bg=skin['bg'])
    
    # Configure styles for better Linux compatibility
    style = ttk.Style()
    
    # Try to use a more Linux-friendly theme
    try:
        available_themes = style.theme_names()
        if 'clam' in available_themes:
            style.theme_use('clam')
        elif 'alt' in available_themes:
            style.theme_use('alt')
    except:
        pass  # Use default theme if theme setting fails
    
    # Configure notebook
    style.configure('TNotebook', background=skin['bg'])
    style.configure('TNotebook.Tab', background=skin['button_bg'], foreground=skin['button_fg'])
    style.map('TNotebook.Tab', background=[('selected', skin['accent'])])
    
    # Configure frames
    style.configure('TFrame', background=skin['bg'])
    style.configure('TLabelframe', background=skin['bg'], foreground=skin['fg'])
    style.configure('TLabelframe.Label', background=skin['bg'], foreground=skin['fg'])
    
    # Configure labels
    style.configure('TLabel', background=skin['bg'], foreground=skin['fg'])
    
    # Configure buttons
    style.configure('TButton', background=skin['button_bg'], foreground=skin['button_fg'])
    style.map('TButton', background=[('active', skin['accent'])])
    
    # Configure entry and combobox
    style.configure('TEntry', fieldbackground=skin['text_bg'], foreground=skin['text_fg'])
    style.configure('TCombobox', fieldbackground=skin['text_bg'], foreground=skin['text_fg'])
    
    # Configure output text
    output_text.configure(bg=skin['text_bg'], fg=skin['text_fg'], 
                              insertbackground=skin['text_fg'])
    
    # Update title label
    if hasattr(title_label, 'configure'):
        title_label.configure(foreground=skin['accent'])

