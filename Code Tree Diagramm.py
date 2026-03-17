#!/usr/bin/env python3
#         o                                                  o              o                o           o                                                      
#        <|>                                                <|>            <|>              <|>         <|>                                                     
#        / \                                                / \            / \              / \         < \                                                     
#      o/   \o       \o__ __o   \o__ __o     o__ __o        \o/            \o/    o__ __o/  \o/    o__ __o/  \o__ __o__ __o      o__ __o/  \o__ __o   \o__ __o  
#     <|__ __|>       |     |>   |     |>   /v     v\        |              |    /v     |    |    /v     |    |     |     |>    /v     |    |     |>   |     |> 
#     /       \      / \   < >  / \   / \  />       <\      < >            < >  />     / \  / \  />     / \  / \   / \   / \   />     / \  / \   / \  / \   / \ 
#   o/         \o    \o/        \o/   \o/  \         /       \o    o/\o    o/   \      \o/  \o/  \      \o/  \o/   \o/   \o/   \      \o/  \o/   \o/  \o/   \o/ 
#  /v           v\    |          |     |    o       o         v\  /v  v\  /v     o      |    |    o      |    |     |     |     o      |    |     |    |     |  
# />             <\  / \        / \   / \   <\__ __/>          <\/>    <\/>      <\__  / \  / \   <\__  / \  / \   / \   / \    <\__  / \  / \   / \  / \   / \ 
#

#
# /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$        /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$$$$$$$/$$$$$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$ /$$   /$$
#| $$$ | $$ /$$__  $$ /$$__  $$/$$__  $$|_  $$_/       /$$__  $$ /$$__  $$| $$  | $$| $$$ | $$| $$_____/_  $$_/| $$__  $$| $$_____/| $$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$| $$$ | $$
#| $$$$| $$| $$  \ $$| $$  \__/ $$  \__/  | $$        | $$  \__/| $$  \__/| $$  | $$| $$$$| $$| $$       | $$  | $$  \ $$| $$      | $$  \ $$| $$$$  /$$$$| $$  \ $$| $$$$| $$| $$$$| $$
#| $$ $$ $$| $$$$$$$$|  $$$$$$|  $$$$$$   | $$        |  $$$$$$ | $$      | $$$$$$$$| $$ $$ $$| $$$$$    | $$  | $$  | $$| $$$$$   | $$$$$$$/| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$| $$ $$ $$
#| $$  $$$$| $$__  $$ \____  $$\____  $$  | $$         \____  $$| $$      | $$__  $$| $$  $$$$| $$__/    | $$  | $$  | $$| $$__/   | $$__  $$| $$  $$$| $$| $$__  $$| $$  $$$$| $$  $$$$
#| $$\  $$$| $$  | $$ /$$  \ $$/$$  \ $$  | $$         /$$  \ $$| $$    $$| $$  | $$| $$\  $$$| $$       | $$  | $$  | $$| $$      | $$  \ $$| $$\  $ | $$| $$  | $$| $$\  $$$| $$\  $$$
#| $$ \  $$| $$  | $$|  $$$$$$/  $$$$$$/ /$$$$$$      |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$| $$$$$$$$/$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$| $$ \/  | $$| $$  | $$| $$ \  $$| $$ \  $$
#|__/  \__/|__/  |__/ \______/ \______/ |______/       \______/  \______/ |__/  |__/|__/  \__/|________/______/|_______/ |________/|__/  |__/|__/     |__/|__/  |__/|__/  \__/|__/  \__/
#
# =============================================================================
# NASSI-SHNEIDERMAN-DIAGRAMM-GENERATOR
# =============================================================================

import subprocess
import sys

# Funktion zur Installation von Modulen
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Liste der benötigten Module
required_modules = [
    'ast',  # Standardmodul, benötigt keine Installation
    'tkinter',  # Standardmodul, benötigt keine Installation
    'traceback',  # Standardmodul, benötigt keine Installation
    're',  # Standardmodul, benötigt keine Installation
    'io',  # Standardmodul, benötigt keine Installation
    'sys',  # Standardmodul, benötigt keine Installation
    'tokenize',  # Standardmodul, benötigt keine Installation
    'keyword',  # Standardmodul, benötigt keine Installation
    'os',  # Standardmodul, benötigt keine Installation
    'subprocess',  # Standardmodul, benötigt keine Installation
    'tempfile',  # Standardmodul, benötigt keine Installation
]

# Überprüfen und Installieren von nicht-Standardmodulen
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        install(module)


import ast
import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import traceback
import re
from io import StringIO
import sys
import tokenize
from keyword import iskeyword
import os
import subprocess
import tempfile

TRUNCATE_LEN = 47  # Max chars before truncation (leaves room for "..." suffix)

class AdvancedCodeTreeGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced Code Tree Generator")
        self.root.geometry("1000x800")
        
        # Set theme if available
        try:
            self.root.tk.call("source", "azure.tcl")
            self.root.tk.call("set_theme", "light")
            self.has_theme = True
        except tk.TclError:
            self.has_theme = False
        
        # Initialize languages dictionary BEFORE setup_ui is called
        self.languages = {
            "Python": {
                "extensions": [".py"],
                "parser": self.parse_python,
                "description": "Native support using Python's AST module"
            },
            "C": {
                "extensions": [".c", ".h"],
                "parser": self.parse_c,
                "description": "Using external parser (requires clang)"
            },
            "C++": {
                "extensions": [".cpp", ".hpp", ".cc", ".h"],
                "parser": self.parse_cpp,
                "description": "Using external parser (requires clang++)"
            },
            "C#": {
                "extensions": [".cs"],
                "parser": self.parse_csharp,
                "description": "Using regex-based parser"
            },
            "Kotlin": {
                "extensions": [".kt", ".kts"],
                "parser": self.parse_kotlin,
                "description": "Using regex-based parser"
            }
        }
        
        # Current language
        self.current_language = "Python"
            
        self.setup_ui()
        self.syntax_errors = []
        self.last_file_dir = os.path.expanduser("~")
        self.last_save_dir = os.path.expanduser("~")
        
    def setup_ui(self):
        # Configure main window
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="5")
        file_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        file_frame.grid_columnconfigure(1, weight=1)
        
        # Input file selection
        ttk.Label(file_frame, text="Code File:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.file_entry = ttk.Entry(file_frame, width=70)
        self.file_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_file).grid(row=0, column=2, padx=5, pady=5)
        
        # Output file selection
        ttk.Label(file_frame, text="Save Tree As:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.save_entry = ttk.Entry(file_frame, width=70)
        self.save_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_save).grid(row=1, column=2, padx=5, pady=5)
        
        # Language selection
        ttk.Label(file_frame, text="Language:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.language_var = tk.StringVar(value="Python")
        language_combo = ttk.Combobox(file_frame, textvariable=self.language_var, 
                                     values=list(self.languages.keys()),
                                     state="readonly", width=15)
        language_combo.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        language_combo.bind("<<ComboboxSelected>>", self.on_language_change)
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="5")
        options_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        # Checkboxes for options
        self.ignore_errors_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Try to fix syntax errors", variable=self.ignore_errors_var).grid(row=0, column=0, sticky="w", padx=5, pady=2)
        
        self.show_comments_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(options_frame, text="Include comments", variable=self.show_comments_var).grid(row=0, column=1, sticky="w", padx=5, pady=2)
        
        self.show_line_numbers_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Show line numbers", variable=self.show_line_numbers_var).grid(row=0, column=2, sticky="w", padx=5, pady=2)
        
        self.compact_mode_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(options_frame, text="Compact mode", variable=self.compact_mode_var).grid(row=0, column=3, sticky="w", padx=5, pady=2)
        
        self.use_colors_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Use colors", variable=self.use_colors_var).grid(row=0, column=4, sticky="w", padx=5, pady=2)
        
        # Button frame
        button_frame = ttk.Frame(options_frame)
        button_frame.grid(row=1, column=0, columnspan=5, sticky="ew", padx=5, pady=5)
        
        # Generate button
        ttk.Button(button_frame, text="Generate Tree", command=self.generate_tree, style="Accent.TButton" if self.has_theme else "").grid(row=0, column=0, padx=5, pady=5)
        
        # Clear button
        ttk.Button(button_frame, text="Clear", command=self.clear_text).grid(row=0, column=1, padx=5, pady=5)
        
        # Copy button
        ttk.Button(button_frame, text="Copy to Clipboard", command=self.copy_all).grid(row=0, column=2, padx=5, pady=5)
        
        # Result frame with notebook
        result_frame = ttk.Frame(self.root)
        result_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        result_frame.grid_columnconfigure(0, weight=1)
        result_frame.grid_rowconfigure(0, weight=1)
        
        # Create notebook
        self.notebook = ttk.Notebook(result_frame)
        self.notebook.grid(row=0, column=0, sticky="nsew")
        
        # Tree tab
        tree_frame = ttk.Frame(self.notebook)
        self.notebook.add(tree_frame, text="Tree View")
        tree_frame.grid_columnconfigure(0, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)
        
        # Result display with scrollbar
        self.result_text = scrolledtext.ScrolledText(
            tree_frame, 
            wrap=tk.NONE,
            font=('Consolas', 10)  # Monospace font for better tree alignment
        )
        self.result_text.grid(row=0, column=0, sticky="nsew")
        
        # Configure text tags for colors
        self.result_text.tag_configure("function", foreground="blue")
        self.result_text.tag_configure("class", foreground="green")
        self.result_text.tag_configure("control", foreground="purple")
        self.result_text.tag_configure("import", foreground="brown")
        self.result_text.tag_configure("variable", foreground="black")
        self.result_text.tag_configure("attribute", foreground="orange")
        self.result_text.tag_configure("call", foreground="darkblue")
        self.result_text.tag_configure("constant", foreground="darkgreen")
        self.result_text.tag_configure("operator", foreground="red")
        self.result_text.tag_configure("fstring", foreground="teal")
        self.result_text.tag_configure("marker", foreground="gray")
        self.result_text.tag_configure("error", foreground="red")
        self.result_text.tag_configure("normal", foreground="black")
        
        # Errors tab
        errors_frame = ttk.Frame(self.notebook)
        self.notebook.add(errors_frame, text="Errors")
        errors_frame.grid_columnconfigure(0, weight=1)
        errors_frame.grid_rowconfigure(0, weight=1)
        
        self.errors_text = scrolledtext.ScrolledText(
            errors_frame,
            wrap=tk.WORD,
            font=('Consolas', 10)
        )
        self.errors_text.grid(row=0, column=0, sticky="nsew")
        
        # Help tab
        help_frame = ttk.Frame(self.notebook)
        self.notebook.add(help_frame, text="Help")
        help_frame.grid_columnconfigure(0, weight=1)
        help_frame.grid_rowconfigure(0, weight=1)
        
        # Create a notebook for help sections
        help_notebook = ttk.Notebook(help_frame)
        help_notebook.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Overview tab
        overview_frame = ttk.Frame(help_notebook)
        help_notebook.add(overview_frame, text="Overview")
        
        overview_text = scrolledtext.ScrolledText(
            overview_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 10),
            padx=10,
            pady=10
        )
        overview_text.pack(fill="both", expand=True)
        overview_text.insert(tk.END, self.get_overview_help())
        overview_text.config(state=tk.DISABLED)
        
        # Features tab
        features_frame = ttk.Frame(help_notebook)
        help_notebook.add(features_frame, text="Features")
        
        features_text = scrolledtext.ScrolledText(
            features_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 10),
            padx=10,
            pady=10
        )
        features_text.pack(fill="both", expand=True)
        features_text.insert(tk.END, self.get_features_help())
        features_text.config(state=tk.DISABLED)
        
        # Colors tab
        colors_frame = ttk.Frame(help_notebook)
        help_notebook.add(colors_frame, text="Color Coding")
        
        colors_text = scrolledtext.ScrolledText(
            colors_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 10),
            padx=10,
            pady=10
        )
        colors_text.pack(fill="both", expand=True)
        colors_text.insert(tk.END, self.get_colors_help())
        
        # Apply color examples
        self.apply_color_examples(colors_text)
        colors_text.config(state=tk.DISABLED)
        
        # Languages tab
        languages_frame = ttk.Frame(help_notebook)
        help_notebook.add(languages_frame, text="Languages")
        
        languages_text = scrolledtext.ScrolledText(
            languages_frame,
            wrap=tk.WORD,
            font=('Segoe UI', 10),
            padx=10,
            pady=10
        )
        languages_text.pack(fill="both", expand=True)
        languages_text.insert(tk.END, self.get_languages_help())
        languages_text.config(state=tk.DISABLED)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=3, column=0, sticky="ew")
        
        # Context menu
        self.setup_context_menu()
        
        # Try to load logo if it exists
        try:
            logo_path = "LogoFlow.webp"
            if os.path.exists(logo_path):
                from PIL import Image, ImageTk
                logo_img = Image.open(logo_path)
                logo_img = logo_img.resize((100, 100), Image.LANCZOS)
                logo_tk = ImageTk.PhotoImage(logo_img)
                
                # Create a label for the logo
                logo_frame = ttk.Frame(main_frame)
                logo_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5)
                
                logo_label = ttk.Label(logo_frame, image=logo_tk)
                logo_label.image = logo_tk  # Keep a reference
                logo_label.pack(padx=5, pady=5)
        except Exception:
            # Logo loading is optional, continue if it fails
            pass
    
    def apply_color_examples(self, text_widget):
        """Apply color examples to the help text"""
        text_widget.tag_configure("function", foreground="blue")
        text_widget.tag_configure("class", foreground="green")
        text_widget.tag_configure("control", foreground="purple")
        text_widget.tag_configure("import", foreground="brown")
        text_widget.tag_configure("variable", foreground="black")
        text_widget.tag_configure("attribute", foreground="orange")
        text_widget.tag_configure("call", foreground="darkblue")
        text_widget.tag_configure("constant", foreground="darkgreen")
        text_widget.tag_configure("operator", foreground="red")
        text_widget.tag_configure("fstring", foreground="teal")
        text_widget.tag_configure("marker", foreground="gray")
        
        # Find and tag color examples
        content = text_widget.get("1.0", tk.END)
        
        # Function example
        start = content.find("Functions (blue):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("function", f"{line_start}.0", f"{line_start}.17")
        
        # Class example
        start = content.find("Classes (green):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("class", f"{line_start}.0", f"{line_start}.15")
        
        # Control example
        start = content.find("Control structures (purple):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("control", f"{line_start}.0", f"{line_start}.26")
        
        # Import example
        start = content.find("Imports (brown):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("import", f"{line_start}.0", f"{line_start}.16")
        
        # Variable example
        start = content.find("Variables (black):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("variable", f"{line_start}.0", f"{line_start}.17")
        
        # Attribute example
        start = content.find("Attributes (orange):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("attribute", f"{line_start}.0", f"{line_start}.19")
        
        # Call example
        start = content.find("Function calls (dark blue):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("call", f"{line_start}.0", f"{line_start}.26")
        
        # Constant example
        start = content.find("Constants (dark green):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("constant", f"{line_start}.0", f"{line_start}.23")
        
        # Operator example
        start = content.find("Operators (red):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("operator", f"{line_start}.0", f"{line_start}.16")
        
        # F-string example
        start = content.find("F-strings (teal):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("fstring", f"{line_start}.0", f"{line_start}.17")
        
        # Marker example
        start = content.find("Markers (gray):")
        if start != -1:
            line_start = content[:start].count('\n') + 1
            text_widget.tag_add("marker", f"{line_start}.0", f"{line_start}.15")
    
    def get_overview_help(self):
        """Return the overview help text"""
        return """# Code Tree Generator written by Arno Waldmann

The Code Tree Generator is a tool for visualizing the structure of code files as an ASCII tree. It supports multiple programming languages and provides a clear hierarchical view of code elements.

## What It Does

This tool parses code files and generates a tree representation that shows the structure of:
- Classes and their methods
- Functions and their parameters
- Control structures (if, for, while, etc.)
- Variable declarations
- Import statements
- And more...

## How to Use

1. Select a code file using the "Browse..." button
2. Choose the appropriate language from the dropdown
3. Set your desired options (colors, line numbers, etc.)
4. Click "Generate Tree" to create the tree view
5. View the results in the Tree View tab
6. Save the tree to a file if needed

## Compact Mode

The Compact Mode option truncates long strings and values in the tree view to improve readability. When enabled:
- Long strings are cut off after 50 characters and end with "..."
- Docstrings and comments are shortened
- The overall display becomes more compact

This is particularly useful when analyzing large files or code with many long string literals that would otherwise make the tree structure difficult to read.

## Benefits

- Quickly understand the structure of unfamiliar code
- Identify patterns and relationships between code elements
- Document code structure for reference or documentation
- Compare different implementations visually
"""
    
    def get_features_help(self):
        """Return the features help text"""
        return """# Features

## Core Features

- **Multi-language Support**: Parse and visualize code in Python, C, C++, C#, and Kotlin
- **Syntax Error Recovery**: Attempt to fix common syntax errors to generate a tree even with imperfect code
- **Color Coding**: Different code elements are displayed in different colors for better readability
- **Line Numbers**: Option to show line numbers for each code element
- **Compact Mode**: Truncate long strings and values for better overview
- **Comment Inclusion**: Option to include or exclude comments and docstrings

## Interface Features

- **Tree View**: Main view showing the code structure as a tree
- **Error View**: Separate tab showing any syntax errors or parsing issues
- **Help Documentation**: Comprehensive help with examples and explanations
- **File Operations**: Save tree to file, copy to clipboard
- **Context Menu**: Right-click menu for common operations

## Tree Generation Options

- **Try to fix syntax errors**: Attempts to recover from common syntax errors
- **Include comments**: Shows docstrings and comments in the tree
- **Show line numbers**: Displays the line number for each code element
- **Compact mode**: Truncates long strings and values
- **Use colors**: Applies color coding to different elements

## Supported Languages

- **Python**: Native support using Python's AST module
- **C/C++**: Support via external parser (requires clang)
- **C#**: Support via regex-based parser
- **Kotlin**: Support via regex-based parser

## Navigation

- Use the notebook tabs to switch between Tree View, Errors, and Help
- Scroll through the tree to explore the code structure
- Use the context menu (right-click) for quick actions
"""
    
    def get_colors_help(self):
        """Return the colors help text"""
        return """# Color Coding

The Code Tree Generator uses color coding to make it easier to identify different types of code elements at a glance. When the "Use colors" option is enabled, the following color scheme is applied:

Functions (blue): Methods and function definitions

Classes (green): Class definitions

Control structures (purple): If statements, loops, try blocks

Imports (brown): Import statements

Variables (black): Variable names and references

Attributes (orange): Object attributes and properties

Function calls (dark blue): Invocations of functions or methods

Constants (dark green): String literals, numbers, and other constants

Operators (red): Mathematical and logical operators

F-strings (teal): Formatted string literals (Python)

Markers (gray): Special markers like "else block" or "finally block"

## Benefits of Color Coding

- **Quick Identification**: Instantly recognize the type of each code element
- **Improved Readability**: Distinguish between similar structures more easily
- **Pattern Recognition**: Identify patterns in code structure through color patterns
- **Focus**: Concentrate on specific types of elements by looking for their color

## Using Color Coding Effectively

- Use color coding in combination with the tree structure to understand code organization
- Look for patterns in the colors to identify repeated structures
- Pay attention to the nesting of differently colored elements to understand scope
- Toggle colors on/off to see the code structure in different ways

Color coding can be enabled or disabled using the "Use colors" checkbox in the options panel.
"""
    
    def get_languages_help(self):
        """Return the languages help text"""
        return """# Supported Languages

The Code Tree Generator supports multiple programming languages, each with its own parser and features.

## Python

- **Native Support**: Uses Python's built-in Abstract Syntax Tree (AST) module
- **Full Feature Set**: All features are available for Python code
- **Comprehensive Parsing**: Handles all Python syntax elements including f-strings
- **Error Recovery**: Can attempt to fix common Python syntax errors

## C

- **Parser**: Uses external Clang-based parser
- **Requirements**: Requires clang to be installed on the system
- **Features**: Supports functions, structs, enums, typedefs, and preprocessor directives
- **Limitations**: May not handle all complex C constructs

## C++

- **Parser**: Uses external Clang-based parser
- **Requirements**: Requires clang++ to be installed on the system
- **Features**: Supports classes, templates, namespaces, and other C++ features
- **Limitations**: Complex template metaprogramming may not be fully represented

## C#

- **Parser**: Uses regex-based parser
- **Features**: Supports classes, methods, properties, and other C# constructs
- **Limitations**: May not handle all advanced C# features or complex expressions

## Kotlin

- **Parser**: Uses regex-based parser
- **Features**: Supports classes, functions, properties, and other Kotlin constructs
- **Limitations**: May not handle all Kotlin-specific features or complex expressions

## Selecting a Language

Choose the appropriate language from the dropdown menu before generating the tree. The file extension is used to suggest the language automatically when you select a file.

## Language-Specific Notes

- **Python**: Best supported with full feature set
- **C/C++**: Requires external tools for full parsing
- **C#/Kotlin**: Uses pattern matching for basic structure recognition

Each language parser extracts the code structure according to the language's syntax and conventions, providing a consistent tree view across different languages.
"""
    
    def setup_context_menu(self):
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Copy", command=self.copy_text)
        self.context_menu.add_command(label="Copy All", command=self.copy_all)
        self.context_menu.add_command(label="Select All", command=self.select_all)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Clear", command=self.clear_text)
        
        self.result_text.bind("<Button-3>", self.show_context_menu)
        self.errors_text.bind("<Button-3>", self.show_context_menu)
    
    def show_context_menu(self, event):
        try:
            widget = event.widget
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def copy_text(self):
        self.root.clipboard_clear()
        widget = self.root.focus_get()
        if widget in (self.result_text, self.errors_text):
            selected_text = widget.get("sel.first", "sel.last")
            if selected_text:
                self.root.clipboard_append(selected_text)
                self.show_status("Selected text copied to clipboard")
    
    def copy_all(self):
        self.root.clipboard_clear()
        widget = self.notebook.select()
        if self.notebook.index(widget) == 0:  # Tree tab
            text = self.result_text.get("1.0", tk.END)
        else:  # Errors tab
            text = self.errors_text.get("1.0", tk.END)
        
        if text:
            self.root.clipboard_append(text)
            self.show_status("All text copied to clipboard")
    
    def select_all(self):
        widget = self.root.focus_get()
        if widget in (self.result_text, self.errors_text):
            widget.tag_add(tk.SEL, "1.0", tk.END)
            widget.mark_set(tk.INSERT, "1.0")
            widget.see(tk.INSERT)
    
    def clear_text(self):
        self.result_text.delete(1.0, tk.END)
        self.errors_text.delete(1.0, tk.END)
        self.show_status("Display cleared")
    
    def on_language_change(self, event):
        """Handle language selection change"""
        self.current_language = self.language_var.get()
        self.show_status(f"Language set to {self.current_language}")
    
    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select Code File",
            initialdir=self.last_file_dir,
            filetypes=[
                ("All Supported Files", "*.py *.c *.cpp *.h *.hpp *.cc *.cs *.kt *.kts"),
                ("Python Files", "*.py"),
                ("C Files", "*.c *.h"),
                ("C++ Files", "*.cpp *.hpp *.cc *.h"),
                ("C# Files", "*.cs"),
                ("Kotlin Files", "*.kt *.kts"),
                ("All Files", "*.*")
            ]
        )
        if filename:
            self.last_file_dir = os.path.dirname(filename)
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)
            
            # Auto-detect language based on file extension
            ext = os.path.splitext(filename)[1].lower()
            for lang, info in self.languages.items():
                if ext in info["extensions"]:
                    self.language_var.set(lang)
                    self.current_language = lang
                    break
            
            # Auto-generate save filename
            base_name = os.path.basename(filename)
            name_without_ext = os.path.splitext(base_name)[0]
            save_path = os.path.join(self.last_save_dir, f"{name_without_ext}_tree.txt")
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, save_path)
    
    def browse_save(self):
        filename = filedialog.asksaveasfilename(
            title="Save Tree As",
            initialdir=self.last_save_dir,
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.last_save_dir = os.path.dirname(filename)
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, filename)
    
    def generate_tree(self):
        input_file = self.file_entry.get()
        output_file = self.save_entry.get()
        
        if not input_file:
            self.show_status("Error: Please select an input file", is_error=True)
            return
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                code = f.read()
            
            self.clear_text()
            self.syntax_errors = []
            
            # Parse the code based on selected language
            language = self.current_language
            if language not in self.languages:
                self.show_status(f"Error: Unsupported language {language}", is_error=True)
                return
                
            parser = self.languages[language]["parser"]
            tree = parser(code)
            
            # Generate and display the tree
            if self.use_colors_var.get():
                # Use colored tree generation
                self.generate_colored_tree(tree)
            else:
                # Use plain text tree generation
                ascii_tree = self.generate_ascii_tree(tree)
                self.result_text.insert(tk.END, ascii_tree)
            
            # Show syntax errors if any
            if self.syntax_errors:
                self.errors_text.insert(tk.END, "=== SYNTAX ERRORS ===\n")
                for error in self.syntax_errors:
                    self.errors_text.insert(tk.END, f"- {error}\n")
                self.notebook.select(1)  # Switch to errors tab
            
            # Save to file if specified
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(self.result_text.get("1.0", tk.END))
                self.show_status(f"Success: Tree saved to {output_file}")
            else:
                self.show_status("Success: Tree generated")
        
        except Exception as e:
            error_msg = self.get_full_error(e)
            self.show_error(error_msg)
    
    def show_status(self, message, is_error=False):
        self.status_var.set(message)
        if is_error:
            self.status_bar.config(foreground="red")
        else:
            self.status_bar.config(foreground="black")
    
    def show_error(self, error_msg):
        self.errors_text.delete(1.0, tk.END)
        self.errors_text.insert(tk.END, f"ERROR:\n{error_msg}\n\n")
        self.errors_text.insert(tk.END, "Full traceback:\n")
        self.errors_text.insert(tk.END, traceback.format_exc())
        self.notebook.select(1)  # Switch to errors tab
        self.show_status(f"Error: {error_msg.splitlines()[0]}", is_error=True)
    
    def get_full_error(self, error):
        buffer = StringIO()
        traceback.print_exception(type(error), error, error.__traceback__, file=buffer)
        return buffer.getvalue()
    
    #
    # Language-specific parsers
    #
    
    def parse_python(self, code):
        """Parse Python code using the built-in AST module"""
        # First try standard parsing
        try:
            return ast.parse(code)
        except SyntaxError as e:
            if not self.ignore_errors_var.get():
                raise
            
            # Try to fix common syntax errors
            fixed_code = self.try_fix_python_syntax(code, e)
            if fixed_code:
                try:
                    return ast.parse(fixed_code)
                except SyntaxError as e2:
                    self.syntax_errors.append(f"Could not fully fix syntax: {str(e2)}")
                    return self.create_partial_ast(code)
            
            self.syntax_errors.append(f"Original syntax error: {str(e)}")
            return self.create_partial_ast(code)
    
    def try_fix_python_syntax(self, code, error):
        """Attempt to automatically fix common Python syntax errors"""
        lines = code.split('\n')
        error_line = error.lineno - 1  # Convert to 0-based index
        
        if error_line >= len(lines):
            return None
        
        # Handle unterminated strings
        if "unterminated string literal" in str(error):
            # Check for common string patterns
            line = lines[error_line]
            
            # Case 1: Missing closing quote
            if line.count('"') % 2 == 1:
                lines[error_line] += '"'
                return '\n'.join(lines)
            elif line.count("'") % 2 == 1:
                lines[error_line] += "'"
                return '\n'.join(lines)
            
            # Case 2: Missing closing parenthesis for function call
            if '(' in line and line.count('(') > line.count(')'):
                lines[error_line] += ')'
                return '\n'.join(lines)
            
            # Case 3: Multiline string with proper indentation
            next_line = lines[error_line + 1] if error_line + 1 < len(lines) else ""
            if next_line.strip().startswith(('"', "'")):
                lines[error_line] += '""'  # Add empty string to close
                return '\n'.join(lines)
        
        # Handle indentation errors
        elif "unexpected indent" in str(error).lower():
            # Remove unexpected indentation
            lines[error_line] = lines[error_line].lstrip()
            return '\n'.join(lines)
        elif "expected an indented block" in str(error).lower():
            # Add indentation
            lines[error_line] = "    " + lines[error_line]
            return '\n'.join(lines)
        
        # Handle missing colons
        elif "expected ':'" in str(error).lower():
            lines[error_line] = lines[error_line].rstrip() + ":"
            return '\n'.join(lines)
        
        # Handle unmatched parentheses
        elif "unmatched ')'" in str(error).lower():
            # Add opening parenthesis at the beginning of the line
            lines[error_line] = "(" + lines[error_line]
            return '\n'.join(lines)
        elif "unexpected EOF while parsing" in str(error).lower():
            # Check for unmatched parentheses
            open_count = code.count('(')
            close_count = code.count(')')
            if open_count > close_count:
                # Add missing closing parentheses
                lines[-1] = lines[-1] + ')' * (open_count - close_count)
                return '\n'.join(lines)
        
        return None
    
    def create_partial_ast(self, code):
        """Create a partial AST even with syntax errors"""
        # Use tokenize to get a rough structure
        try:
            tokens = list(tokenize.generate_tokens(StringIO(code).readline))
        except Exception:
            tokens = []
        
        # Create a minimal module
        module = ast.Module(body=[], type_ignores=[])
        
        # Add error information
        if self.syntax_errors:
            for error in self.syntax_errors:
                module.body.append(
                    ast.Expr(value=ast.Constant(value=f"# ERROR: {error}"))
                )
        
        return module
    
    def parse_c(self, code):
        """Parse C code using external clang parser or regex fallback"""
        try:
            # Try to use clang if available
            return self.parse_c_with_clang(code)
        except Exception as e:
            self.syntax_errors.append(f"Clang parser error: {str(e)}")
            # Fall back to regex-based parser
            return self.parse_c_with_regex(code)
    
    def parse_c_with_clang(self, code):
        """Parse C code using clang"""
        # Check if clang is available
        try:
            subprocess.run(["clang", "--version"], capture_output=True, check=True)
        except (subprocess.SubprocessError, FileNotFoundError):
            raise Exception("Clang is not available")
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix=".c", mode="w", delete=False) as temp:
            temp.write(code)
            temp_name = temp.name
        
        try:
            # Run clang with AST dump
            result = subprocess.run(
                ["clang", "-Xclang", "-ast-dump", "-fsyntax-only", temp_name],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                self.syntax_errors.append(f"Clang error: {result.stderr}")
                raise Exception("Clang parsing failed")
            
            # Create a pseudo-AST from the clang output
            return self.create_c_ast_from_clang(result.stdout)
        finally:
            # Clean up the temporary file
            try:
                os.unlink(temp_name)
            except OSError:
                pass

    def create_c_ast_from_clang(self, clang_output):
        """Create a pseudo-AST from clang AST dump"""
        # Create a minimal module
        module = ast.Module(body=[], type_ignores=[])
        
        # Parse the clang output
        lines = clang_output.split('\n')
        current_depth = 0
        stack = [module]
        
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Calculate depth based on indentation
            indent = len(line) - len(line.lstrip('`-| '))
            depth = indent // 2
            
            # Adjust stack based on depth
            while depth < current_depth:
                stack.pop()
                current_depth -= 1
            
            # Extract node type and content
            content = line.strip('`-| ')
            node_type = content.split(' ')[0]
            
            # Create a node based on type
            node = None
            
            if node_type == "FunctionDecl":
                # Extract function name
                match = re.search(r"FunctionDecl.*'(\w+)'", content)
                if match:
                    func_name = match.group(1)
                    node = ast.FunctionDef(
                        name=func_name,
                        args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=[],
                        decorator_list=[]
                    )
            elif node_type == "RecordDecl":
                # Extract struct/union name
                match = re.search(r"RecordDecl.*'(\w+)'", content)
                if match:
                    struct_name = match.group(1)
                    node = ast.ClassDef(
                        name=struct_name,
                        bases=[],
                        keywords=[],
                        body=[],
                        decorator_list=[]
                    )
            elif node_type == "VarDecl":
                # Extract variable name
                match = re.search(r"VarDecl.*'(\w+)'", content)
                if match:
                    var_name = match.group(1)
                    node = ast.Assign(
                        targets=[ast.Name(id=var_name, ctx=ast.Store())],
                        value=ast.Constant(value=None)
                    )
            elif node_type == "TypedefDecl":
                # Extract typedef name
                match = re.search(r"TypedefDecl.*'(\w+)'", content)
                if match:
                    typedef_name = match.group(1)
                    node = ast.Assign(
                        targets=[ast.Name(id=f"typedef {typedef_name}", ctx=ast.Store())],
                        value=ast.Constant(value=None)
                    )
            elif node_type == "EnumDecl":
                # Extract enum name
                match = re.search(r"EnumDecl.*'(\w+)'", content)
                enum_name = match.group(1) if match else "anonymous"
                node = ast.ClassDef(
                    name=f"enum {enum_name}",
                    bases=[],
                    keywords=[],
                    body=[],
                    decorator_list=[]
                )
            
            # Add the node to the current parent if created
            if node:
                if hasattr(stack[-1], 'body'):
                    stack[-1].body.append(node)
                
                # Push the node onto the stack
                stack.append(node)
                current_depth = depth + 1
        
        return module
    
    def parse_c_with_regex(self, code):
        """Parse C code using regex patterns"""
        # Create a minimal module
        module = ast.Module(body=[], type_ignores=[])
        
        # Function pattern
        function_pattern = r"(\w+)\s+(\w+)\s*\([^)]*\)\s*\{"
        for match in re.finditer(function_pattern, code):
            return_type, func_name = match.groups()
            
            # Create a function node
            func_node = ast.FunctionDef(
                name=func_name,
                args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            func_node.lineno = line_number
            
            module.body.append(func_node)
        
        # Struct pattern
        struct_pattern = r"struct\s+(\w+)\s*\{"
        for match in re.finditer(struct_pattern, code):
            struct_name = match.group(1)
            
            # Create a class node for the struct
            struct_node = ast.ClassDef(
                name=f"struct {struct_name}",
                bases=[],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            struct_node.lineno = line_number
            
            module.body.append(struct_node)
        
        # Enum pattern
        enum_pattern = r"enum\s+(\w+)\s*\{"
        for match in re.finditer(enum_pattern, code):
            enum_name = match.group(1)
            
            # Create a class node for the enum
            enum_node = ast.ClassDef(
                name=f"enum {enum_name}",
                bases=[],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            enum_node.lineno = line_number
            
            module.body.append(enum_node)
        
        # Typedef pattern
        typedef_pattern = r"typedef\s+.*\s+(\w+)\s*;"
        for match in re.finditer(typedef_pattern, code):
            typedef_name = match.group(1)
            
            # Create an assignment node for the typedef
            typedef_node = ast.Assign(
                targets=[ast.Name(id=f"typedef {typedef_name}", ctx=ast.Store())],
                value=ast.Constant(value=None)
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            typedef_node.lineno = line_number
            
            module.body.append(typedef_node)
        
        # Include pattern
        include_pattern = r"#include\s+[<\"]([^>\"]+)[>\"]"
        for match in re.finditer(include_pattern, code):
            include_name = match.group(1)
            
            # Create an import node for the include
            include_node = ast.Import(
                names=[ast.alias(name=include_name, asname=None)]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            include_node.lineno = line_number
            
            module.body.append(include_node)
        
        # Define pattern
        define_pattern = r"#define\s+(\w+)(?:\s+(.+))?"
        for match in re.finditer(define_pattern, code):
            define_name = match.group(1)
            define_value = match.group(2) or ""
            
            # Create an assignment node for the define
            define_node = ast.Assign(
                targets=[ast.Name(id=f"#define {define_name}", ctx=ast.Store())],
                value=ast.Constant(value=define_value)
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            define_node.lineno = line_number
            
            module.body.append(define_node)
        
        return module
    # Problem bei Verwednung CLANG
    #def parse_cpp(self, code):
    #    """Parse C++ code using external clang++ parser or regex fallback"""
    #    try:
    #        # Try to use clang++ if available
    #        return self.parse_cpp_with_clang(code)
    #    except Exception as e:
    #        self.syntax_errors.append(f"Clang++ parser error: {str(e)}")
    #        # Fall back to regex-based parser
    #        return self.parse_cpp_with_regex(code)
    """
    Hinweis: Dieses Problem tritt auf, wenn Clang++ installiert ist, aber die Standard-C++-Header nicht gefunden werden.
    Dies ist ein häufiges Problem unter Windows. Es gibt zwei mögliche Lösungen:

    1. Schnelle Lösung: Regex-Parser verwenden (empfohlen)
       - Diese Methode wurde geändert, um direkt den Regex-Parser zu nutzen und Clang zu umgehen.
       - Dadurch werden grundlegende C++-Strukturen erkannt, ohne externe Abhängigkeiten.

    2. Vollständige Lösung: Clang-Installation korrigieren
       - Visual Studio mit C++-Unterstützung installieren.
       - Die Umgebungsvariable INCLUDE auf den Pfad der C++-Header setzen, z. B.:
         C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.xx.xxxxx\\include
       - Alternativ den MSVC-Compiler-Wrapper von Clang mit dem -fms-compatibility-Flag nutzen.

    Für die meisten Anwendungsfälle reicht die erste Lösung aus.
    """
#

    def parse_cpp(self, code):
        """Parse C++ code using regex-based parser"""
        # Direkt den Regex-Parser verwenden, ohne Clang zu versuchen
        return self.parse_cpp_with_regex(code)

    
    def parse_cpp_with_clang(self, code):
        """Parse C++ code using clang++"""
        # Check if clang++ is available
        try:
            subprocess.run(["clang++", "--version"], capture_output=True, check=True)
        except (subprocess.SubprocessError, FileNotFoundError):
            raise Exception("Clang++ is not available")
        
        # Create a temporary file
        with tempfile.NamedTemporaryFile(suffix=".cpp", mode="w", delete=False) as temp:
            temp.write(code)
            temp_name = temp.name
        
        try:
            # Run clang++ with AST dump
            result = subprocess.run(
                ["clang++", "-Xclang", "-ast-dump", "-fsyntax-only", temp_name],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                self.syntax_errors.append(f"Clang++ error: {result.stderr}")
                raise Exception("Clang++ parsing failed")
            
            # Create a pseudo-AST from the clang++ output
            return self.create_cpp_ast_from_clang(result.stdout)
        finally:
            # Clean up the temporary file
            try:
                os.unlink(temp_name)
            except OSError:
                pass

    def create_cpp_ast_from_clang(self, clang_output):
        """Create a pseudo-AST from clang++ AST dump"""
        # Similar to C but with additional C++ specific nodes
        module = ast.Module(body=[], type_ignores=[])
        
        # Parse the clang output
        lines = clang_output.split('\n')
        current_depth = 0
        stack = [module]
        
        for line in lines:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Calculate depth based on indentation
            indent = len(line) - len(line.lstrip('`-| '))
            depth = indent // 2
            
            # Adjust stack based on depth
            while depth < current_depth:
                stack.pop()
                current_depth -= 1
            
            # Extract node type and content
            content = line.strip('`-| ')
            node_type = content.split(' ')[0]
            
            # Create a node based on type
            node = None
            
            if node_type == "FunctionDecl" or node_type == "CXXMethodDecl":
                # Extract function name
                match = re.search(r"(?:FunctionDecl|CXXMethodDecl).*'(\w+)'", content)
                if match:
                    func_name = match.group(1)
                    node = ast.FunctionDef(
                        name=func_name,
                        args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                        body=[],
                        decorator_list=[]
                    )
            elif node_type == "CXXRecordDecl":
                # Extract class name
                match = re.search(r"CXXRecordDecl.*'(\w+)'", content)
                if match:
                    class_name = match.group(1)
                    node = ast.ClassDef(
                        name=class_name,
                        bases=[],
                        keywords=[],
                        body=[],
                        decorator_list=[]
                    )
            elif node_type == "NamespaceDecl":
                # Extract namespace name
                match = re.search(r"NamespaceDecl.*'(\w+)'", content)
                if match:
                    namespace_name = match.group(1)
                    node = ast.ClassDef(
                        name=f"namespace {namespace_name}",
                        bases=[],
                        keywords=[],
                        body=[],
                        decorator_list=[]
                    )
            elif node_type == "VarDecl":
                # Extract variable name
                match = re.search(r"VarDecl.*'(\w+)'", content)
                if match:
                    var_name = match.group(1)
                    node = ast.Assign(
                        targets=[ast.Name(id=var_name, ctx=ast.Store())],
                        value=ast.Constant(value=None)
                    )
            elif node_type == "TemplateDecl":
                # Extract template name
                match = re.search(r"TemplateDecl.*'(\w+)'", content)
                if match:
                    template_name = match.group(1)
                    node = ast.ClassDef(
                        name=f"template {template_name}",
                        bases=[],
                        keywords=[],
                        body=[],
                        decorator_list=[]
                    )
            
            # Add the node to the current parent if created
            if node:
                if hasattr(stack[-1], 'body'):
                    stack[-1].body.append(node)
                
                # Push the node onto the stack
                stack.append(node)
                current_depth = depth + 1
        
        return module
    
    def parse_cpp_with_regex(self, code):
        """Parse C++ code using regex patterns"""
        # Create a minimal module
        module = ast.Module(body=[], type_ignores=[])
        
        # Class pattern
        class_pattern = r"class\s+(\w+)(?:\s*:\s*(?:public|protected|private)\s+(\w+))?\s*\{"
        for match in re.finditer(class_pattern, code):
            class_name = match.group(1)
            base_class = match.group(2)
            
            # Create a class node
            class_node = ast.ClassDef(
                name=class_name,
                bases=[ast.Name(id=base_class, ctx=ast.Load())] if base_class else [],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            class_node.lineno = line_number
            
            module.body.append(class_node)
        
        # Function pattern (including methods)
        function_pattern = r"(?:virtual\s+)?(?:static\s+)?(?:inline\s+)?(?:const\s+)?(\w+(?:::\w+)?)\s+(\w+)\s*\([^)]*\)(?:\s*const)?\s*(?:override)?\s*(?:=\s*0)?\s*\{?"
        for match in re.finditer(function_pattern, code):
            return_type, func_name = match.groups()
            
            # Create a function node
            func_node = ast.FunctionDef(
                name=func_name,
                args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            func_node.lineno = line_number
            
            module.body.append(func_node)
        
        # Namespace pattern
        namespace_pattern = r"namespace\s+(\w+)\s*\{"
        for match in re.finditer(namespace_pattern, code):
            namespace_name = match.group(1)
            
            # Create a class node for the namespace
            namespace_node = ast.ClassDef(
                name=f"namespace {namespace_name}",
                bases=[],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            namespace_node.lineno = line_number
            
            module.body.append(namespace_node)
        
        # Template pattern
        template_pattern = r"template\s*<[^>]*>\s*(?:class|struct)\s+(\w+)"
        for match in re.finditer(template_pattern, code):
            template_name = match.group(1)
            
            # Create a class node for the template
            template_node = ast.ClassDef(
                name=f"template {template_name}",
                bases=[],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            template_node.lineno = line_number
            
            module.body.append(template_node)
        
        # Include pattern
        include_pattern = r"#include\s+[<\"]([^>\"]+)[>\"]"
        for match in re.finditer(include_pattern, code):
            include_name = match.group(1)
            
            # Create an import node for the include
            include_node = ast.Import(
                names=[ast.alias(name=include_name, asname=None)]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            include_node.lineno = line_number
            
            module.body.append(include_node)
        
        return module
    
    def parse_csharp(self, code):
        """Parse C# code using regex patterns"""
        # Create a minimal module
        module = ast.Module(body=[], type_ignores=[])
        
        # Namespace pattern
        namespace_pattern = r"namespace\s+([.\w]+)\s*\{"
        for match in re.finditer(namespace_pattern, code):
            namespace_name = match.group(1)
            
            # Create a class node for the namespace
            namespace_node = ast.ClassDef(
                name=f"namespace {namespace_name}",
                bases=[],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            namespace_node.lineno = line_number
            
            module.body.append(namespace_node)
        
        # Class pattern
        class_pattern = r"(?:public|private|protected|internal)?\s*(?:static|abstract|sealed)?\s*class\s+(\w+)(?:\s*:\s*([^{]+))?\s*\{"
        for match in re.finditer(class_pattern, code):
            class_name = match.group(1)
            base_classes = match.group(2)
            
            # Create a class node
            class_node = ast.ClassDef(
                name=class_name,
                bases=[ast.Name(id=base.strip(), ctx=ast.Load()) for base in base_classes.split(',')] if base_classes else [],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            class_node.lineno = line_number
            
            module.body.append(class_node)
        
        # Interface pattern
        interface_pattern = r"(?:public|private|protected|internal)?\s*interface\s+(\w+)(?:\s*:\s*([^{]+))?\s*\{"
        for match in re.finditer(interface_pattern, code):
            interface_name = match.group(1)
            base_interfaces = match.group(2)
            
            # Create a class node for the interface
            interface_node = ast.ClassDef(
                name=f"interface {interface_name}",
                bases=[ast.Name(id=base.strip(), ctx=ast.Load()) for base in base_interfaces.split(',')] if base_interfaces else [],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            interface_node.lineno = line_number
            
            module.body.append(interface_node)
        
        # Method pattern
        method_pattern = r"(?:public|private|protected|internal)?\s*(?:static|virtual|abstract|override|sealed)?\s*(?:async\s+)?(\w+)\s+(\w+)\s*\([^)]*\)(?:\s*=>\s*[^;]+;|\s*\{)"
        for match in re.finditer(method_pattern, code):
            return_type, method_name = match.groups()
            
            # Create a function node for the method
            method_node = ast.FunctionDef(
                name=method_name,
                args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            method_node.lineno = line_number
            
            module.body.append(method_node)
        
        # Property pattern
        property_pattern = r"(?:public|private|protected|internal)?\s*(?:static|virtual|abstract|override)?\s*(\w+)\s+(\w+)\s*\{\s*(?:get;)?\s*(?:set;)?\s*\}"
        for match in re.finditer(property_pattern, code):
            property_type, property_name = match.groups()
            
            # Create an assignment node for the property
            property_node = ast.Assign(
                targets=[ast.Name(id=f"property {property_name}", ctx=ast.Store())],
                value=ast.Constant(value=property_type)
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            property_node.lineno = line_number
            
            module.body.append(property_node)
        
        # Using pattern
        using_pattern = r"using\s+([.\w]+)(?:\s*=\s*([.\w]+))?\s*;"
        for match in re.finditer(using_pattern, code):
            using_name = match.group(1)
            alias = match.group(2)
            
            # Create an import node for the using statement
            using_node = ast.Import(
                names=[ast.alias(name=using_name, asname=alias)]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            using_node.lineno = line_number
            
            module.body.append(using_node)
        
        return module
    
    def parse_kotlin(self, code):
        """Parse Kotlin code using regex patterns"""
        # Create a minimal module
        module = ast.Module(body=[], type_ignores=[])
        
        # Package pattern
        package_pattern = r"package\s+([.\w]+)"
        for match in re.finditer(package_pattern, code):
            package_name = match.group(1)
            
            # Create an import node for the package
            package_node = ast.Import(
                names=[ast.alias(name=f"package {package_name}", asname=None)]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            package_node.lineno = line_number
            
            module.body.append(package_node)
        
        # Class pattern
        class_pattern = r"(?:open|abstract|sealed|data)?\s*class\s+(\w+)(?:<[^>]+>)?(?:\s*\([^)]*\))?(?:\s*:\s*([^{]+))?\s*\{"
        for match in re.finditer(class_pattern, code):
            class_name = match.group(1)
            base_classes = match.group(2)
            
            # Create a class node
            class_node = ast.ClassDef(
                name=class_name,
                bases=[ast.Name(id=base.strip(), ctx=ast.Load()) for base in base_classes.split(',')] if base_classes else [],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            class_node.lineno = line_number
            
            module.body.append(class_node)
        
        # Interface pattern
        interface_pattern = r"interface\s+(\w+)(?:<[^>]+>)?(?:\s*:\s*([^{]+))?\s*\{"
        for match in re.finditer(interface_pattern, code):
            interface_name = match.group(1)
            base_interfaces = match.group(2)
            
            # Create a class node for the interface
            interface_node = ast.ClassDef(
                name=f"interface {interface_name}",
                bases=[ast.Name(id=base.strip(), ctx=ast.Load()) for base in base_interfaces.split(',')] if base_interfaces else [],
                keywords=[],
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            interface_node.lineno = line_number
            
            module.body.append(interface_node)
        
        # Function pattern
        function_pattern = r"(?:private|public|protected|internal)?\s*(?:suspend\s+)?fun\s+(?:<[^>]+>\s+)?(\w+)\s*\([^)]*\)(?:\s*:\s*([^{]+))?\s*(?:=|{)"
        for match in re.finditer(function_pattern, code):
            func_name = match.group(1)
            return_type = match.group(2)
            
            # Create a function node
            func_node = ast.FunctionDef(
                name=func_name,
                args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                body=[],
                decorator_list=[]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            func_node.lineno = line_number
            
            module.body.append(func_node)
        
        # Property pattern
        property_pattern = r"(?:private|public|protected|internal)?\s*(?:val|var)\s+(\w+)(?:\s*:\s*([^=]+))?(?:\s*=\s*[^{]+|\s*by\s+.+|\s*\{)"
        for match in re.finditer(property_pattern, code):
            property_name = match.group(1)
            property_type = match.group(2)
            
            # Create an assignment node for the property
            property_node = ast.Assign(
                targets=[ast.Name(id=property_name, ctx=ast.Store())],
                value=ast.Constant(value=property_type.strip() if property_type else "Any")
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            property_node.lineno = line_number
            
            module.body.append(property_node)
        
        # Import pattern
        import_pattern = r"import\s+([.\w]+)(?:\s+as\s+(\w+))?"
        for match in re.finditer(import_pattern, code):
            import_name = match.group(1)
            alias = match.group(2)
            
            # Create an import node
            import_node = ast.Import(
                names=[ast.alias(name=import_name, asname=alias)]
            )
            
            # Add line number if available
            line_number = code[:match.start()].count('\n') + 1
            import_node.lineno = line_number
            
            module.body.append(import_node)
        
        return module
    
    def get_node_color(self, node):
        """Determine the color tag for a node based on its type"""
        if not isinstance(node, ast.AST):
            if isinstance(node, str):
                return "marker"
            return "normal"
            
        if isinstance(node, ast.FunctionDef):
            return "function"
        elif isinstance(node, ast.ClassDef):
            return "class"
        elif isinstance(node, (ast.If, ast.For, ast.While, ast.Try)):
            return "control"
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            return "import"
        elif isinstance(node, ast.Name):
            return "variable"
        elif isinstance(node, ast.Attribute):
            return "attribute"
        elif isinstance(node, ast.Call):
            return "call"
        elif isinstance(node, ast.Constant):
            return "constant"
        elif isinstance(node, (ast.BinOp, ast.UnaryOp, ast.Compare)):
            return "operator"
        elif isinstance(node, ast.JoinedStr):
            return "fstring"
        elif isinstance(node, ast.FormattedValue):
            return "fstring"
        else:
            return "normal"
    
    def generate_colored_tree(self, node, depth=0, is_last=False, prefix=''):
        """Generate a colored tree representation in the result_text widget"""
        if not isinstance(node, ast.AST):
            # Handle string markers (like "<else block>") or other non-AST objects
            if isinstance(node, str):
                line_prefix = prefix + ('└── ' if is_last else '├── ') if depth > 0 else ''
                node_info = f"Marker: {node}"
                self.result_text.insert(tk.END, line_prefix, "normal")
                self.result_text.insert(tk.END, node_info + "\n", "marker")
            return
                
        if isinstance(node, ast.Module):
            self.result_text.insert(tk.END, "Module\n", "normal")
            children = list(ast.iter_child_nodes(node))
            for i, child in enumerate(children):
                self.generate_colored_tree(
                    child, depth + 1, i == len(children) - 1, prefix
                )
            return
        
        # Determine the current line's prefix
        line_prefix = prefix + ('└── ' if is_last else '├── ') if depth > 0 else ''
        
        # Get node information
        node_info = self.get_node_info(node)
        
        # Add line numbers if enabled
        if self.show_line_numbers_var.get() and hasattr(node, 'lineno'):
            node_info += f" (line {node.lineno})"
        
        # Get the color tag for this node
        color_tag = self.get_node_color(node)
        
        # Insert the text with appropriate color
        self.result_text.insert(tk.END, line_prefix, "normal")
        self.result_text.insert(tk.END, node_info + "\n", color_tag)
        
        # Process children
        children = self.get_node_children(node)
        if children:
            new_prefix = prefix + ('    ' if is_last else '│   ')
            for i, child in enumerate(children):
                self.generate_colored_tree(
                    child, depth + 1, i == len(children) - 1, new_prefix
                )
    
    def generate_ascii_tree(self, node, depth=0, is_last=False, prefix=''):
        """Generate a plain text tree representation"""
        # Check if node is a string or other non-AST object
        if not isinstance(node, ast.AST):
            # Handle string markers (like "<else block>") or other non-AST objects
            if isinstance(node, str):
                line_prefix = prefix + ('└── ' if is_last else '├── ') if depth > 0 else ''
                return line_prefix + f"Marker: {node}\n"
            else:
                # Skip other non-AST objects
                return ""
                
        if isinstance(node, ast.Module):
            result = "Module\n"
            children = list(ast.iter_child_nodes(node))
            for i, child in enumerate(children):
                result += self.generate_ascii_tree(
                    child, depth + 1, i == len(children) - 1, prefix
                )
            return result
        
        # Determine the current line's prefix
        line_prefix = prefix + ('└── ' if is_last else '├── ') if depth > 0 else ''
        
        # Get node information
        node_info = self.get_node_info(node)
        
        # Add line numbers if enabled
        if self.show_line_numbers_var.get() and hasattr(node, 'lineno'):
            node_info += f" (line {node.lineno})"
        
        result = line_prefix + node_info + "\n"
        
        # Process children
        children = self.get_node_children(node)
        if children:
            new_prefix = prefix + ('    ' if is_last else '│   ')
            for i, child in enumerate(children):
                result += self.generate_ascii_tree(
                    child, depth + 1, i == len(children) - 1, new_prefix
                )
        
        return result
    
    def get_node_info(self, node):
        """Get descriptive information about a node"""
        # Check if node is a string or other non-AST object
        if not isinstance(node, ast.AST):
            if isinstance(node, str):
                return f"Marker: {node}"
            return f"Non-AST: {type(node).__name__}"
            
        node_type = type(node).__name__
        
        # Handle specific node types
        if isinstance(node, ast.Constant):
            value_repr = repr(node.value)
            # Truncate long strings in compact mode
            if self.compact_mode_var.get() and isinstance(node.value, str) and len(value_repr) > 50:
                value_repr = value_repr[:TRUNCATE_LEN] + "...'"
            return f"{node_type}: {value_repr}"
        
        if isinstance(node, ast.Name):
            prefix = "Keyword" if iskeyword(node.id) else "Name"
            return f"{prefix}: {node.id}"
        
        if isinstance(node, ast.FunctionDef):
            decorators = ""
            if hasattr(node, 'decorator_list') and node.decorator_list:
                decorator_count = len(node.decorator_list)
                decorators = f" [{decorator_count} decorator{'s' if decorator_count > 1 else ''}]"
            return f"Function: {node.name}{decorators}"
        
        if isinstance(node, ast.ClassDef):
            bases = ""
            if hasattr(node, 'bases') and node.bases:
                base_names = []
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        base_names.append(base.id)
                    else:
                        base_names.append("<complex>")
                bases = f" (inherits: {', '.join(base_names)})"
            return f"Class: {node.name}{bases}"
        
        if isinstance(node, ast.Call):
            func_name = ""
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
            elif isinstance(node.func, ast.Attribute):
                # Fix: Safely handle nested attribute access
                try:
                    if isinstance(node.func.value, ast.Name):
                        func_name = f"{node.func.value.id}.{node.func.attr}"
                    elif isinstance(node.func.value, ast.Call):
                        func_name = f"(...).{node.func.attr}"
                    elif isinstance(node.func.value, ast.Attribute):
                        func_name = f"....{node.func.attr}"
                    else:
                        func_name = f"<expr>.{node.func.attr}"
                except AttributeError:
                    func_name = f"<unknown>.{node.func.attr}"
            
            # Add argument count
            arg_count = len(node.args) + len(node.keywords) if hasattr(node, 'args') else 0
            arg_info = f" [{arg_count} arg{'s' if arg_count != 1 else ''}]" if arg_count > 0 else ""
            
            return f"Call: {func_name}{arg_info}"
        
        if isinstance(node, ast.Assign):
            try:
                if hasattr(ast, 'unparse'):  # Python 3.9+
                    targets = ", ".join(ast.unparse(t) for t in node.targets)
                    return f"Assign to: {targets}"
                else:
                    # Fallback for older Python versions
                    targets = []
                    for t in node.targets:
                        if isinstance(t, ast.Name):
                            targets.append(t.id)
                        else:
                            targets.append("<complex_target>")
                    return f"Assign to: {', '.join(targets)}"
            except (AttributeError, ValueError):
                # Fallback if unparse fails
                targets = []
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        targets.append(t.id)
                    else:
                        targets.append("<complex_target>")
                return f"Assign to: {', '.join(targets)}"
        
        if isinstance(node, ast.AnnAssign):
            target = ""
            if isinstance(node.target, ast.Name):
                target = node.target.id
            else:
                target = "<complex_target>"
            
            annotation = ""
            if isinstance(node.annotation, ast.Name):
                annotation = f": {node.annotation.id}"
            else:
                annotation = ": <complex_type>"
                
            return f"Annotated Assign: {target}{annotation}"
        
        if isinstance(node, ast.AugAssign):
            target = ""
            if isinstance(node.target, ast.Name):
                target = node.target.id
            else:
                target = "<complex_target>"
            
            op = type(node.op).__name__
            return f"AugAssign: {target} {op}="
        
        if isinstance(node, ast.Import):
            names = ", ".join(alias.name for alias in node.names)
            return f"Import: {names}"
        
        if isinstance(node, ast.ImportFrom):
            names = ", ".join(alias.name for alias in node.names)
            module_name = node.module if node.module else ""
            return f"ImportFrom: {module_name}.{names}"
        
        if isinstance(node, ast.Attribute):
            try:
                if isinstance(node.value, ast.Name):
                    return f"Attribute: {node.value.id}.{node.attr}"
                else:
                    return f"Attribute: <expr>.{node.attr}"
            except AttributeError:
                return f"Attribute: <unknown>.{node.attr}"
        
        if isinstance(node, ast.BinOp):
            return f"BinOp: {type(node.op).__name__}"
        
        if isinstance(node, ast.UnaryOp):
            return f"UnaryOp: {type(node.op).__name__}"
        
        if isinstance(node, ast.Compare):
            ops = [type(op).__name__ for op in node.ops]
            return f"Compare: {', '.join(ops)}"
        
        if isinstance(node, ast.If):
            return "If statement"
        
        if isinstance(node, ast.For):
            target = ""
            if isinstance(node.target, ast.Name):
                target = node.target.id
            else:
                target = "<complex_target>"
            return f"For loop: {target}"
        
        if isinstance(node, ast.While):
            return "While loop"
        
        if isinstance(node, ast.Try):
            return "Try block"
        
        if isinstance(node, ast.ExceptHandler):
            if node.name:
                return f"Except: {node.name}"
            elif node.type and isinstance(node.type, ast.Name):
                return f"Except: {node.type.id}"
            else:
                return "Except"
                
        if isinstance(node, ast.With):
            return "With statement"
            
        if isinstance(node, ast.Lambda):
            arg_count = len(node.args.args) if hasattr(node, 'args') and hasattr(node.args, 'args') else 0
            return f"Lambda: [{arg_count} arg{'s' if arg_count != 1 else ''}]"
            
        if isinstance(node, ast.ListComp):
            return "List comprehension"
            
        if isinstance(node, ast.DictComp):
            return "Dict comprehension"
            
        if isinstance(node, ast.SetComp):
            return "Set comprehension"
            
        if isinstance(node, ast.GeneratorExp):
            return "Generator expression"
            
        if isinstance(node, ast.Yield):
            return "Yield"
            
        if isinstance(node, ast.YieldFrom):
            return "Yield From"
            
        if isinstance(node, ast.Return):
            return "Return statement"
            
        if isinstance(node, ast.Break):
            return "Break statement"
            
        if isinstance(node, ast.Continue):
            return "Continue statement"
            
        if isinstance(node, ast.Assert):
            return "Assert statement"
            
        if isinstance(node, ast.Delete):
            return "Delete statement"
            
        if isinstance(node, ast.Raise):
            return "Raise statement"
            
        if isinstance(node, ast.Pass):
            return "Pass statement"
            
        if isinstance(node, ast.JoinedStr):
            return "f-string"
            
        if isinstance(node, ast.FormattedValue):
            return "Formatted value in f-string"
            
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            # This is likely a docstring or comment
            if self.show_comments_var.get():
                value = node.value.value
                if self.compact_mode_var.get() and len(value) > 50:
                    value = value[:TRUNCATE_LEN] + "..."
                return f"Docstring: {value}"
            else:
                return "Docstring"
        
        # Default case
        return node_type
    
    def get_node_children(self, node):
        """Get the children of a node in a consistent way"""
        # Check if node is a string or other non-AST object
        if not isinstance(node, ast.AST):
            return []  # Non-AST objects have no children
            
        # Special handling for JoinedStr (f-strings)
        if isinstance(node, ast.JoinedStr):
            return node.values if hasattr(node, 'values') else []
            
        children = []
        
        # Handle specific node types with known child attributes
        if hasattr(node, 'body') and not isinstance(node.body, ast.JoinedStr):
            # Make sure body is iterable
            if hasattr(node.body, '__iter__'):
                children.extend(node.body)
            else:
                # If body is not iterable, add it as a single item
                children.append(node.body)
        
        if hasattr(node, 'orelse') and node.orelse:
            # Add a marker node for else blocks
            if isinstance(node, (ast.If, ast.For, ast.While)):
                children.append("<else block>")  # Use string as marker
            
            # Make sure orelse is iterable
            if hasattr(node.orelse, '__iter__'):
                children.extend(node.orelse)
            else:
                # If orelse is not iterable, add it as a single item
                children.append(node.orelse)
        
        if hasattr(node, 'finalbody') and node.finalbody:
            # Add a marker for finally blocks
            children.append("<finally block>")  # Use string as marker
            
            # Make sure finalbody is iterable
            if hasattr(node.finalbody, '__iter__'):
                children.extend(node.finalbody)
            else:
                # If finalbody is not iterable, add it as a single item
                children.append(node.finalbody)
            
        # If we already added children, return them
        if children:
            return children
            
        # Handle other common attributes that might contain children
        for attr_name in ['values', 'targets', 'args', 'keywords', 'elts', 
                          'comparators', 'handlers', 'decorator_list']:
            if hasattr(node, attr_name):
                attr_value = getattr(node, attr_name)
                if isinstance(attr_value, list):
                    children.extend(attr_value)
                elif attr_value is not None:
                    # If attribute is not a list but has a value, add it as a single item
                    children.append(attr_value)
        
        # Handle binary operations
        if hasattr(node, 'left'):
            children.append(node.left)
        if hasattr(node, 'right'):
            children.append(node.right)
            
        # Handle unary operations and calls
        if hasattr(node, 'operand'):
            children.append(node.operand)
        if hasattr(node, 'func'):
            children.append(node.func)
        if hasattr(node, 'value'):
            children.append(node.value)
            
        # If we still have no children, fall back to ast.iter_child_nodes
        if not children:
            try:
                children = list(ast.iter_child_nodes(node))
            except TypeError:
                # Handle case where node is not a proper AST node
                children = []
            
        return children

if __name__ == "__main__":
    app = AdvancedCodeTreeGenerator()
    app.root.mainloop()
