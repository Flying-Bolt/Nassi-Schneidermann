#!/usr/bin/env python3
import sys
import os
import ast
import importlib
import pkgutil
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QComboBox, QSpinBox, QPushButton, QFileDialog, 
                            QTextEdit, QSplitter, QTabWidget, QMessageBox, QGroupBox,
                            QFormLayout, QCheckBox, QStatusBar, QGridLayout, QListWidget,
                            QLineEdit, QDialog, QDialogButtonBox, QAbstractItemView, QListWidgetItem)
from PyQt5.QtGui import QFont, QColor, QSyntaxHighlighter, QTextCharFormat, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRegularExpression

LOGO_FILE = "myLogo.webp"

class PythonHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for Python code"""
    
    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)
        
        self.highlighting_rules = []
        
        # Keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            "and", "as", "assert", "break", "class", "continue", "def", "del",
            "elif", "else", "except", "exec", "finally", "for", "from", "global",
            "if", "import", "in", "is", "lambda", "not", "or", "pass", "print",
            "raise", "return", "try", "while", "with", "yield"
        ]
        for word in keywords:
            pattern = QRegularExpression("\\b" + word + "\\b")
            rule = (pattern, keyword_format)
            self.highlighting_rules.append(rule)
        
        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))
        self.highlighting_rules.append((QRegularExpression("\".*\""), string_format))
        self.highlighting_rules.append((QRegularExpression("'.*'"), string_format))
        
        # Numbers
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))
        self.highlighting_rules.append((QRegularExpression("\\b[0-9]+\\b"), number_format))
        
        # Comments
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        self.highlighting_rules.append((QRegularExpression("#[^\n]*"), comment_format))
        
        # Functions
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))
        self.highlighting_rules.append((QRegularExpression("\\b[A-Za-z0-9_]+(?=\\()"), function_format))
    
    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

class CppHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for C++ code"""
    
    def __init__(self, parent=None):
        super(CppHighlighter, self).__init__(parent)
        
        self.highlighting_rules = []
        
        # Keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            "alignas", "alignof", "and", "and_eq", "asm", "auto", "bitand", "bitor",
            "bool", "break", "case", "catch", "char", "char16_t", "char32_t", "class",
            "compl", "const", "constexpr", "const_cast", "continue", "decltype", "default",
            "delete", "do", "double", "dynamic_cast", "else", "enum", "explicit", "export",
            "extern", "false", "float", "for", "friend", "goto", "if", "inline", "int",
            "long", "mutable", "namespace", "new", "noexcept", "not", "not_eq", "nullptr",
            "operator", "or", "or_eq", "private", "protected", "public", "register",
            "reinterpret_cast", "return", "short", "signed", "sizeof", "static",
            "static_assert", "static_cast", "struct", "switch", "template", "this",
            "thread_local", "throw", "true", "try", "typedef", "typeid", "typename",
            "union", "unsigned", "using", "virtual", "void", "volatile", "wchar_t",
            "while", "xor", "xor_eq"
        ]
        for word in keywords:
            pattern = QRegularExpression("\\b" + word + "\\b")
            rule = (pattern, keyword_format)
            self.highlighting_rules.append(rule)
        
        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))
        self.highlighting_rules.append((QRegularExpression("\".*\""), string_format))
        self.highlighting_rules.append((QRegularExpression("'.*'"), string_format))
        
        # Numbers
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))
        self.highlighting_rules.append((QRegularExpression("\\b[0-9]+\\b"), number_format))
        
        # Comments
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        self.highlighting_rules.append((QRegularExpression("//[^\n]*"), comment_format))
        
        # Functions
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))
        self.highlighting_rules.append((QRegularExpression("\\b[A-Za-z0-9_]+(?=\\()"), function_format))
    
    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

class KotlinHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for Kotlin code"""
    
    def __init__(self, parent=None):
        super(KotlinHighlighter, self).__init__(parent)
        
        self.highlighting_rules = []
        
        # Keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            "as", "as?", "break", "class", "continue", "do", "else", "false", "for",
            "fun", "if", "in", "interface", "is", "null", "object", "package", "return",
            "super", "this", "throw", "true", "try", "typealias", "typeof", "val", "var",
            "when", "while", "by", "catch", "constructor", "delegate", "dynamic", "field",
            "file", "finally", "get", "import", "init", "param", "property", "receiver",
            "set", "setparam", "value", "where", "abstract", "actual", "annotation",
            "companion", "const", "crossinline", "data", "enum", "expect", "external",
            "final", "infix", "inline", "inner", "internal", "lateinit", "noinline",
            "open", "operator", "out", "override", "private", "protected", "public",
            "reified", "sealed", "suspend", "tailrec", "vararg"
        ]
        for word in keywords:
            pattern = QRegularExpression("\\b" + word + "\\b")
            rule = (pattern, keyword_format)
            self.highlighting_rules.append(rule)
        
        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))
        self.highlighting_rules.append((QRegularExpression("\".*\""), string_format))
        self.highlighting_rules.append((QRegularExpression("'.*'"), string_format))
        
        # Numbers
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))
        self.highlighting_rules.append((QRegularExpression("\\b[0-9]+\\b"), number_format))
        
        # Comments
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        self.highlighting_rules.append((QRegularExpression("//[^\n]*"), comment_format))
        
        # Functions
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))
        self.highlighting_rules.append((QRegularExpression("\\b[A-Za-z0-9_]+(?=\\()"), function_format))
    
    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

class CodeElementExtractor:
    """Extracts classes and methods/functions from code"""
    
    @staticmethod
    def extract_python_elements(code):
        """Extract classes and methods/functions from Python code"""
        try:
            tree = ast.parse(code)
            classes = []
            functions = []
            
            # First pass: collect all classes
            class_nodes = {}
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)
                    class_nodes[node.name] = node
            
            # Second pass: collect functions and methods
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check if this function is a method of a class
                    is_method = False
                    for class_name, class_node in class_nodes.items():
                        if node in class_node.body:
                            functions.append(f"{class_name}.{node.name}")
                            is_method = True
                            break
                    
                    # If not a method, it's a top-level function
                    if not is_method:
                        functions.append(node.name)
            
            return classes, functions
        except Exception as e:
            print(f"Error extracting Python elements: {str(e)}")
            return [], []
    
    @staticmethod
    def extract_cpp_elements(code):
        """Extract classes and methods/functions from C++ code"""
        classes = []
        functions = []
        
        # Simple regex-based extraction for C++
        # Class pattern
        class_pattern = r'class\s+(\w+)'
        for match in re.finditer(class_pattern, code):
            classes.append(match.group(1))
        
        # Function pattern (simplified)
        func_pattern = r'(?:void|int|bool|float|double|char|auto)\s+(\w+)\s*\([^)]*\)'
        for match in re.finditer(func_pattern, code):
            functions.append(match.group(1))
        
        # Method pattern (very simplified)
        method_pattern = r'class\s+(\w+).*?{(.*?)};'
        for match in re.finditer(method_pattern, code, re.DOTALL):
            class_name = match.group(1)
            class_body = match.group(2)
            
            for func_match in re.finditer(func_pattern, class_body):
                functions.append(f"{class_name}.{func_match.group(1)}")
        
        return classes, functions
    
    @staticmethod
    def extract_kotlin_elements(code):
        """Extract classes and methods/functions from Kotlin code"""
        classes = []
        functions = []
        
        # Simple regex-based extraction for Kotlin
        # Class pattern
        class_pattern = r'class\s+(\w+)'
        for match in re.finditer(class_pattern, code):
            classes.append(match.group(1))
        
        # Function pattern
        func_pattern = r'fun\s+(\w+)\s*\([^)]*\)'
        for match in re.finditer(func_pattern, code):
            functions.append(match.group(1))
        
        # Method pattern (simplified)
        method_pattern = r'class\s+(\w+).*?{(.*?)}'
        for match in re.finditer(method_pattern, code, re.DOTALL):
            class_name = match.group(1)
            class_body = match.group(2)
            
            for func_match in re.finditer(func_pattern, class_body):
                functions.append(f"{class_name}.{func_match.group(1)}")
        
        return classes, functions
    
    @staticmethod
    def extract_elements(code, language):
        """Extract classes and methods/functions based on language"""
        if language == "python":
            return CodeElementExtractor.extract_python_elements(code)
        elif language == "cpp":
            return CodeElementExtractor.extract_cpp_elements(code)
        elif language == "kotlin":
            return CodeElementExtractor.extract_kotlin_elements(code)
        else:
            return [], []

class ElementSelectionDialog(QDialog):
    """Dialog for selecting specific classes and methods/functions"""
    
    def __init__(self, parent=None, classes=None, methods=None, selected_classes=None, selected_methods=None):
        super(ElementSelectionDialog, self).__init__(parent)
        self.setWindowTitle("Element-Auswahl")
        self.setMinimumWidth(400)
        self.setMinimumHeight(500)
        
        # Logo als Dialogicon setzen
        try:
            dialog_icon = QIcon(LOGO_FILE)
            self.setWindowIcon(dialog_icon)
        except Exception as e:
            print(f"Fehler beim Laden des Logos als Dialog-Icon: {str(e)}")
        
        # Hauptlayout
        layout = QVBoxLayout(self)
        
        # Logo im Dialog anzeigen
        try:
            logo_label = QLabel()
            logo_pixmap = QPixmap(LOGO_FILE)
            if not logo_pixmap.isNull():
                logo_pixmap = logo_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                logo_label.setPixmap(logo_pixmap)
            logo_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(logo_label)
        except Exception as e:
            print(f"Fehler beim Laden des Logos im Dialog: {str(e)}")
        
        # Klassen-Auswahl
        classes_group = QGroupBox("Klassen")
        classes_layout = QVBoxLayout()
        
        # Suchfeld für Klassen
        self.class_search = QLineEdit()
        self.class_search.setPlaceholderText("Klassen filtern...")
        self.class_search.textChanged.connect(self.filter_classes)
        classes_layout.addWidget(self.class_search)
        
        # Liste der Klassen
        self.class_list = QListWidget()
        self.class_list.setSelectionMode(QAbstractItemView.MultiSelection)
        if classes:
            for cls in classes:
                item = QListWidgetItem(cls)
                self.class_list.addItem(item)
                # Vorherige Auswahl wiederherstellen
                if selected_classes and cls in selected_classes:
                    item.setSelected(True)
        classes_layout.addWidget(self.class_list)
        
        # Buttons für Klassenauswahl
        class_buttons_layout = QHBoxLayout()
        select_all_classes = QPushButton("Alle auswählen")
        select_all_classes.clicked.connect(self.select_all_classes)
        deselect_all_classes = QPushButton("Keine auswählen")
        deselect_all_classes.clicked.connect(self.deselect_all_classes)
        class_buttons_layout.addWidget(select_all_classes)
        class_buttons_layout.addWidget(deselect_all_classes)
        classes_layout.addLayout(class_buttons_layout)
        
        classes_group.setLayout(classes_layout)
        layout.addWidget(classes_group)
        
        # Methoden/Funktionen-Auswahl
        methods_group = QGroupBox("Methoden/Funktionen")
        methods_layout = QVBoxLayout()
        
        # Suchfeld für Methoden
        self.method_search = QLineEdit()
        self.method_search.setPlaceholderText("Methoden/Funktionen filtern...")
        self.method_search.textChanged.connect(self.filter_methods)
        methods_layout.addWidget(self.method_search)
        
        # Liste der Methoden
        self.method_list = QListWidget()
        self.method_list.setSelectionMode(QAbstractItemView.MultiSelection)
        if methods:
            for method in methods:
                item = QListWidgetItem(method)
                self.method_list.addItem(item)
                # Vorherige Auswahl wiederherstellen
                if selected_methods and method in selected_methods:
                    item.setSelected(True)
        methods_layout.addWidget(self.method_list)
        
        # Buttons für Methodenauswahl
        method_buttons_layout = QHBoxLayout()
        select_all_methods = QPushButton("Alle auswählen")
        select_all_methods.clicked.connect(self.select_all_methods)
        deselect_all_methods = QPushButton("Keine auswählen")
        deselect_all_methods.clicked.connect(self.deselect_all_methods)
        method_buttons_layout.addWidget(select_all_methods)
        method_buttons_layout.addWidget(deselect_all_methods)
        methods_layout.addLayout(method_buttons_layout)
        
        methods_group.setLayout(methods_layout)
        layout.addWidget(methods_group)
        
        # Dialog-Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        # Wenn keine vorherige Auswahl existiert, standardmäßig alle Elemente auswählen
        if not selected_classes and not selected_methods:
            self.select_all_classes()
            self.select_all_methods()
        
        # Speichern der ursprünglichen Listen für die Filterung
        self.original_classes = classes or []
        self.original_methods = methods or []
    
    def filter_classes(self, text):
        """Filtert die Klassenliste basierend auf dem Suchtext"""
        self.class_list.clear()
        for cls in self.original_classes:
            if text.lower() in cls.lower():
                item = QListWidgetItem(cls)
                self.class_list.addItem(item)
    
    def filter_methods(self, text):
        """Filtert die Methodenliste basierend auf dem Suchtext"""
        self.method_list.clear()
        for method in self.original_methods:
            if text.lower() in method.lower():
                item = QListWidgetItem(method)
                self.method_list.addItem(item)
    
    def select_all_classes(self):
        """Wählt alle Klassen aus"""
        for i in range(self.class_list.count()):
            self.class_list.item(i).setSelected(True)
    
    def deselect_all_classes(self):
        """Wählt keine Klasse aus"""
        for i in range(self.class_list.count()):
            self.class_list.item(i).setSelected(False)
    
    def select_all_methods(self):
        """Wählt alle Methoden aus"""
        for i in range(self.method_list.count()):
            self.method_list.item(i).setSelected(True)
    
    def deselect_all_methods(self):
        """Wählt keine Methode aus"""
        for i in range(self.method_list.count()):
            self.method_list.item(i).setSelected(False)
    
    def get_selected_classes(self):
        """Gibt die ausgewählten Klassen zurück"""
        return [item.text() for item in self.class_list.selectedItems()]
    
    def get_selected_methods(self):
        """Gibt die ausgewählten Methoden zurück"""
        return [item.text() for item in self.method_list.selectedItems()]

class NassiShneidermanVisitor(ast.NodeVisitor):
    """Visitor for generating ASCII Nassi-Shneiderman diagrams from Python AST"""
    
    def __init__(self, width=80, show_classes=True, show_methods=True, show_functions=True, 
                 show_procedures=True, selected_classes=None, selected_methods=None):
        self.width = width
        self.diagram = []
        self.indent = 0
        self.show_classes = show_classes
        self.show_methods = show_methods
        self.show_functions = show_functions
        self.show_procedures = show_procedures
        self.selected_classes = selected_classes or []
        self.selected_methods = selected_methods or []
    
    def get_diagram(self):
        return "\n".join(self.diagram)
    
    def add_line(self, line):
        self.diagram.append(" " * self.indent + line)
    
    def add_box(self, text, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Text (linksbündig)
        text_lines = text.split("\n")
        for line in text_lines:
            # Linksbündig mit etwas Abstand
            padded_line = " " + line.ljust(box_width - 3)
            self.add_line("|" + padded_line + "|")
        
        # Untere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_if_box(self, condition, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Bedingung
        condition_text = f"if {condition}:"
        # Linksbündig mit etwas Abstand
        padded_line = " " + condition_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_else_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Else
        # Linksbündig mit etwas Abstand
        padded_line = " else:".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_for_box(self, target, iter_expr, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # For-Schleife
        for_text = f"for {target} in {iter_expr}:"
        # Linksbündig mit etwas Abstand
        padded_line = " " + for_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_while_box(self, condition, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # While-Schleife
        while_text = f"while {condition}:"
        # Linksbündig mit etwas Abstand
        padded_line = " " + while_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_try_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Try
        # Linksbündig mit etwas Abstand
        padded_line = " try:".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_except_box(self, exception, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Except
        except_text = f"except {exception}:" if exception else "except:"
        # Linksbündig mit etwas Abstand
        padded_line = " " + except_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_finally_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Finally
        # Linksbündig mit etwas Abstand
        padded_line = " finally:".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def visit_Module(self, node):
        self.add_box("Modul")
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_FunctionDef(self, node):
        # Prüfen, ob es sich um eine Methode oder eine Funktion handelt
        is_method = False
        parent_class = None
        for parent in getattr(node, 'parent_classes', []):
            if isinstance(parent, ast.ClassDef):
                is_method = True
                parent_class = parent.name
                break
        
        # Entscheiden, ob die Funktion/Methode angezeigt werden soll
        if is_method:
            if not self.show_methods:
                return
            # Prüfen, ob die Methode in der ausgewählten Liste ist
            method_name = f"{parent_class}.{node.name}"
            if self.selected_methods and len(self.selected_methods) > 0:
                if method_name not in self.selected_methods:
                    return
        else:
            if not self.show_functions:
                return
            # Prüfen, ob die Funktion in der ausgewählten Liste ist
            if self.selected_methods and len(self.selected_methods) > 0:
                # Suche nach exaktem Funktionsnamen oder nach Funktionsnamen mit beliebigem Klassenpräfix
                found = False
                for method in self.selected_methods:
                    if method == node.name or method.endswith("." + node.name):
                        found = True
                        break
                if not found:
                    return
        
        args = ", ".join([arg.arg for arg in node.args.args])
        func_def = f"def {node.name}({args}):"
        self.add_box(func_def)
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_ClassDef(self, node):
        if not self.show_classes:
            return
        
        # Prüfen, ob die Klasse in der ausgewählten Liste ist
        if self.selected_classes and len(self.selected_classes) > 0:
            if node.name not in self.selected_classes:
                return
            
        bases = ", ".join([ast.unparse(base) for base in node.bases])
        class_def = f"class {node.name}({bases}):" if bases else f"class {node.name}:"
        self.add_box(class_def)
        self.indent += 2
        
        # Markiere Methoden als Teil dieser Klasse
        for stmt in node.body:
            if isinstance(stmt, ast.FunctionDef):
                if not hasattr(stmt, 'parent_classes'):
                    stmt.parent_classes = []
                stmt.parent_classes.append(node)
            self.visit(stmt)
        self.indent -= 2
    
    def visit_If(self, node):
        condition = ast.unparse(node.test)
        self.add_if_box(condition)
        
        # If-Block
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
        
        # Else-Block (falls vorhanden)
        if node.orelse:
            self.add_else_box()
            self.indent += 2
            for stmt in node.orelse:
                self.visit(stmt)
            self.indent -= 2
    
    def visit_For(self, node):
        target = ast.unparse(node.target)
        iter_expr = ast.unparse(node.iter)
        self.add_for_box(target, iter_expr)
        
        # Schleifenkörper
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
        
        # Else-Block (falls vorhanden)
        if node.orelse:
            self.add_else_box()
            self.indent += 2
            for stmt in node.orelse:
                self.visit(stmt)
            self.indent -= 2
    
    def visit_While(self, node):
        condition = ast.unparse(node.test)
        self.add_while_box(condition)
        
        # Schleifenkörper
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
        
        # Else-Block (falls vorhanden)
        if node.orelse:
            self.add_else_box()
            self.indent += 2
            for stmt in node.orelse:
                self.visit(stmt)
            self.indent -= 2
    
    def visit_Try(self, node):
        self.add_try_box()
        
        # Try-Block
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
        
        # Except-Blöcke
        for handler in node.handlers:
            exception = ast.unparse(handler.type) if handler.type else None
            self.add_except_box(exception)
            self.indent += 2
            for stmt in handler.body:
                self.visit(stmt)
            self.indent -= 2
        
        # Else-Block (falls vorhanden)
        if node.orelse:
            self.add_else_box()
            self.indent += 2
            for stmt in node.orelse:
                self.visit(stmt)
            self.indent -= 2
        
        # Finally-Block (falls vorhanden)
        if node.finalbody:
            self.add_finally_box()
            self.indent += 2
            for stmt in node.finalbody:
                self.visit(stmt)
            self.indent -= 2
    
    def visit_Assign(self, node):
        targets = ", ".join([ast.unparse(target) for target in node.targets])
        value = ast.unparse(node.value)
        self.add_box(f"{targets} = {value}")
    
    def visit_AugAssign(self, node):
        target = ast.unparse(node.target)
        op = self.get_op_symbol(node.op)
        value = ast.unparse(node.value)
        self.add_box(f"{target} {op}= {value}")
    
    def visit_Return(self, node):
        value = ast.unparse(node.value) if node.value else ""
        self.add_box(f"return {value}")
    
    def visit_Expr(self, node):
        expr = ast.unparse(node.value)
        self.add_box(expr)
    
    def visit_Call(self, node):
        call = ast.unparse(node)
        self.add_box(call)
    
    def visit_Import(self, node):
        names = ", ".join([name.name for name in node.names])
        self.add_box(f"import {names}")
    
    def visit_ImportFrom(self, node):
        names = ", ".join([name.name for name in node.names])
        module = node.module if node.module else ""
        self.add_box(f"from {module} import {names}")
    
    def visit_With(self, node):
        items = ", ".join([ast.unparse(item) for item in node.items])
        self.add_box(f"with {items}:")
        self.indent += 2
        for stmt in node.body:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_Assert(self, node):
        test = ast.unparse(node.test)
        msg = f", {ast.unparse(node.msg)}" if node.msg else ""
        self.add_box(f"assert {test}{msg}")
    
    def visit_Break(self, node):
        self.add_box("break")
    
    def visit_Continue(self, node):
        self.add_box("continue")
    
    def visit_Pass(self, node):
        self.add_box("pass")
    
    def get_op_symbol(self, op):
        op_map = {
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
            ast.FloorDiv: "//",
            ast.Mod: "%",
            ast.Pow: "**",
            ast.LShift: "<<",
            ast.RShift: ">>",
            ast.BitOr: "|",
            ast.BitXor: "^",
            ast.BitAnd: "&",
            ast.MatMult: "@"
        }
        return op_map.get(type(op), "?")
    
    def generic_visit(self, node):
        node_type = type(node).__name__
        self.add_box(f"Nicht unterstützt: {node_type}")

class SimpleCppParser:
    """A simple parser for C++ code that creates a pseudo-AST structure"""
    
    def __init__(self):
        self.ast = None
    
    def parse(self, code):
        """Parse C++ code and return a simplified AST-like structure"""
        # This is a very simplified parser for demonstration
        # In a real implementation, you would use a proper C++ parser like libclang
        
        lines = code.split('\n')
        root = {'type': 'Module', 'body': []}
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('//'):
                i += 1
                continue
            
            # Function definition
            if line.startswith('void ') or line.startswith('int ') or line.startswith('bool ') or \
               line.startswith('float ') or line.startswith('double ') or line.startswith('char '):
                if '(' in line and ')' in line and '{' in line:
                    func_name = line.split('(')[0].split()[-1]
                    func_node = {'type': 'FunctionDef', 'name': func_name, 'body': [], 'is_method': False}
                    
                    # Find the end of the function
                    brace_count = 1
                    j = i + 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to function body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                func_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                    
                    root['body'].append(func_node)
                    i = j
                    continue
            
            # Class definition
            if line.startswith('class ') and '{' in line:
                class_name = line.split('{')[0].replace('class', '').strip()
                class_node = {'type': 'ClassDef', 'name': class_name, 'body': []}
                
                # Find the end of the class
                brace_count = 1
                j = i + 1
                while j < len(lines) and brace_count > 0:
                    if '{' in lines[j]:
                        brace_count += lines[j].count('{')
                    if '}' in lines[j]:
                        brace_count -= lines[j].count('}')
                    
                    # Add statements to class body
                    if brace_count > 0:
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            # Check if this is a method definition inside the class
                            if ('(' in stmt and ')' in stmt and '{' in stmt and 
                                (stmt.startswith('void ') or stmt.startswith('int ') or 
                                 stmt.startswith('bool ') or stmt.startswith('float ') or 
                                 stmt.startswith('double ') or stmt.startswith('char '))):
                                method_name = stmt.split('(')[0].split()[-1]
                                method_node = {'type': 'FunctionDef', 'name': method_name, 'body': [], 'is_method': True, 'class_name': class_name}
                                class_node['body'].append(method_node)
                            else:
                                class_node['body'].append({'type': 'Statement', 'value': stmt})
                    j += 1
                
                root['body'].append(class_node)
                i = j
                continue
            
            # If statement
            if line.startswith('if ') and '(' in line and ')' in line:
                condition = line.split('(')[1].split(')')[0]
                if_node = {'type': 'If', 'condition': condition, 'body': [], 'orelse': []}
                
                # Find the end of the if block
                j = i + 1
                if '{' in line:
                    brace_count = 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to if body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                if_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                else:
                    # Single line if
                    if j < len(lines):
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            if_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                
                # Check for else
                if j < len(lines) and lines[j].strip().startswith('else'):
                    j += 1
                    if '{' in lines[j-1]:
                        brace_count = 1
                        while j < len(lines) and brace_count > 0:
                            if '{' in lines[j]:
                                brace_count += lines[j].count('{')
                            if '}' in lines[j]:
                                brace_count -= lines[j].count('}')
                            
                            # Add statements to else body
                            if brace_count > 0:
                                stmt = lines[j].strip()
                                if stmt and not stmt.startswith('//'):
                                    if_node['orelse'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    else:
                        # Single line else
                        if j < len(lines):
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                if_node['orelse'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                
                root['body'].append(if_node)
                i = j
                continue
            
            # For loop
            if line.startswith('for ') and '(' in line and ')' in line:
                for_parts = line.split('(')[1].split(')')[0].split(';')
                init = for_parts[0].strip() if len(for_parts) > 0 else ""
                condition = for_parts[1].strip() if len(for_parts) > 1 else ""
                increment = for_parts[2].strip() if len(for_parts) > 2 else ""
                
                for_node = {
                    'type': 'For', 
                    'init': init, 
                    'condition': condition, 
                    'increment': increment,
                    'body': []
                }
                
                # Find the end of the for block
                j = i + 1
                if '{' in line:
                    brace_count = 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to for body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                for_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                else:
                    # Single line for
                    if j < len(lines):
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            for_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                
                root['body'].append(for_node)
                i = j
                continue
            
            # While loop
            if line.startswith('while ') and '(' in line and ')' in line:
                condition = line.split('(')[1].split(')')[0]
                while_node = {'type': 'While', 'condition': condition, 'body': []}
                
                # Find the end of the while block
                j = i + 1
                if '{' in line:
                    brace_count = 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to while body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                while_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                else:
                    # Single line while
                    if j < len(lines):
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            while_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                
                root['body'].append(while_node)
                i = j
                continue
            
            # Try-catch block
            if line.startswith('try') and '{' in line:
                try_node = {'type': 'Try', 'body': [], 'handlers': []}
                
                # Find the end of the try block
                brace_count = 1
                j = i + 1
                while j < len(lines) and brace_count > 0:
                    if '{' in lines[j]:
                        brace_count += lines[j].count('{')
                    if '}' in lines[j]:
                        brace_count -= lines[j].count('}')
                    
                    # Add statements to try body
                    if brace_count > 0:
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            try_node['body'].append({'type': 'Statement', 'value': stmt})
                    j += 1
                
                # Check for catch
                if j < len(lines) and lines[j].strip().startswith('catch'):
                    catch_line = lines[j].strip()
                    exception = catch_line.split('(')[1].split(')')[0] if '(' in catch_line and ')' in catch_line else ""
                    
                    catch_node = {'type': 'Catch', 'exception': exception, 'body': []}
                    j += 1
                    
                    if '{' in catch_line:
                        brace_count = 1
                        while j < len(lines) and brace_count > 0:
                            if '{' in lines[j]:
                                brace_count += lines[j].count('{')
                            if '}' in lines[j]:
                                brace_count -= lines[j].count('}')
                            
                            # Add statements to catch body
                            if brace_count > 0:
                                stmt = lines[j].strip()
                                if stmt and not stmt.startswith('//'):
                                    catch_node['body'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    else:
                        # Single line catch
                        if j < len(lines):
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                catch_node['body'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    
                    try_node['handlers'].append(catch_node)
                
                root['body'].append(try_node)
                i = j
                continue
            
            # Other statements
            root['body'].append({'type': 'Statement', 'value': line})
            i += 1
        
        self.ast = root
        return root

class SimpleKotlinParser:
    """A simple parser for Kotlin code that creates a pseudo-AST structure"""
    
    def __init__(self):
        self.ast = None
    
    def parse(self, code):
        """Parse Kotlin code and return a simplified AST-like structure"""
        # This is a very simplified parser for demonstration
        # In a real implementation, you would use a proper Kotlin parser
        
        lines = code.split('\n')
        root = {'type': 'Module', 'body': []}
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('//'):
                i += 1
                continue
            
            # Function definition
            if line.startswith('fun '):
                func_name = line.split('(')[0].replace('fun', '').strip()
                func_node = {'type': 'FunctionDef', 'name': func_name, 'body': [], 'is_method': False}
                
                # Find the end of the function
                if '{' in line:
                    brace_count = line.count('{')
                    j = i + 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to function body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                func_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                    
                    root['body'].append(func_node)
                    i = j
                    continue
            
            # Class definition
            if line.startswith('class '):
                class_name = line.split('{')[0].replace('class', '').strip()
                if '(' in class_name:
                    class_name = class_name.split('(')[0].strip()
                
                class_node = {'type': 'ClassDef', 'name': class_name, 'body': []}
                
                # Find the end of the class
                if '{' in line:
                    brace_count = line.count('{')
                    j = i + 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to class body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                # Check if this is a method definition inside the class
                                if stmt.startswith('fun '):
                                    method_name = stmt.split('(')[0].replace('fun', '').strip()
                                    method_node = {'type': 'FunctionDef', 'name': method_name, 'body': [], 'is_method': True, 'class_name': class_name}
                                    class_node['body'].append(method_node)
                                else:
                                    class_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                    
                    root['body'].append(class_node)
                    i = j
                    continue
            
            # If statement
            if line.startswith('if ') and '(' in line:
                condition = line.split('(')[1].split(')')[0]
                if_node = {'type': 'If', 'condition': condition, 'body': [], 'orelse': []}
                
                # Find the end of the if block
                if '{' in line:
                    brace_count = line.count('{')
                    j = i + 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to if body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                if_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                else:
                    # Single line if
                    j = i + 1
                    if j < len(lines):
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            if_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                
                # Check for else
                if j < len(lines) and lines[j].strip().startswith('else'):
                    j += 1
                    if '{' in lines[j-1]:
                        brace_count = lines[j-1].count('{')
                        while j < len(lines) and brace_count > 0:
                            if '{' in lines[j]:
                                brace_count += lines[j].count('{')
                            if '}' in lines[j]:
                                brace_count -= lines[j].count('}')
                            
                            # Add statements to else body
                            if brace_count > 0:
                                stmt = lines[j].strip()
                                if stmt and not stmt.startswith('//'):
                                    if_node['orelse'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    else:
                        # Single line else
                        if j < len(lines):
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                if_node['orelse'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                
                root['body'].append(if_node)
                i = j
                continue
            
            # For loop
            if line.startswith('for ') and 'in' in line:
                for_parts = line.split('in')
                target = for_parts[0].replace('for', '').strip()
                iter_expr = for_parts[1].split('{')[0].strip() if '{' in for_parts[1] else for_parts[1].strip()
                
                for_node = {
                    'type': 'For', 
                    'target': target, 
                    'iter': iter_expr,
                    'body': []
                }
                
                # Find the end of the for block
                if '{' in line:
                    brace_count = line.count('{')
                    j = i + 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to for body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                for_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                else:
                    # Single line for
                    j = i + 1
                    if j < len(lines):
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            for_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                
                root['body'].append(for_node)
                i = j
                continue
            
            # While loop
            if line.startswith('while ') and '(' in line:
                condition = line.split('(')[1].split(')')[0]
                while_node = {'type': 'While', 'condition': condition, 'body': []}
                
                # Find the end of the while block
                if '{' in line:
                    brace_count = line.count('{')
                    j = i + 1
                    while j < len(lines) and brace_count > 0:
                        if '{' in lines[j]:
                            brace_count += lines[j].count('{')
                        if '}' in lines[j]:
                            brace_count -= lines[j].count('}')
                        
                        # Add statements to while body
                        if brace_count > 0:
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                while_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                else:
                    # Single line while
                    j = i + 1
                    if j < len(lines):
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            while_node['body'].append({'type': 'Statement', 'value': stmt})
                        j += 1
                
                root['body'].append(while_node)
                i = j
                continue
            
            # Try-catch block
            if line.startswith('try') and '{' in line:
                try_node = {'type': 'Try', 'body': [], 'handlers': []}
                
                # Find the end of the try block
                brace_count = line.count('{')
                j = i + 1
                while j < len(lines) and brace_count > 0:
                    if '{' in lines[j]:
                        brace_count += lines[j].count('{')
                    if '}' in lines[j]:
                        brace_count -= lines[j].count('}')
                    
                    # Add statements to try body
                    if brace_count > 0:
                        stmt = lines[j].strip()
                        if stmt and not stmt.startswith('//'):
                            try_node['body'].append({'type': 'Statement', 'value': stmt})
                    j += 1
                
                # Check for catch
                if j < len(lines) and lines[j].strip().startswith('catch'):
                    catch_line = lines[j].strip()
                    exception = catch_line.split('(')[1].split(')')[0] if '(' in catch_line and ')' in catch_line else ""
                    
                    catch_node = {'type': 'Catch', 'exception': exception, 'body': []}
                    
                    if '{' in catch_line:
                        brace_count = catch_line.count('{')
                        j += 1
                        while j < len(lines) and brace_count > 0:
                            if '{' in lines[j]:
                                brace_count += lines[j].count('{')
                            if '}' in lines[j]:
                                brace_count -= lines[j].count('}')
                            
                            # Add statements to catch body
                            if brace_count > 0:
                                stmt = lines[j].strip()
                                if stmt and not stmt.startswith('//'):
                                    catch_node['body'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    else:
                        # Single line catch
                        j += 1
                        if j < len(lines):
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                catch_node['body'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    
                    try_node['handlers'].append(catch_node)
                
                # Check for finally
                if j < len(lines) and lines[j].strip().startswith('finally'):
                    finally_node = {'type': 'Finally', 'body': []}
                    
                    if '{' in lines[j]:
                        brace_count = lines[j].count('{')
                        j += 1
                        while j < len(lines) and brace_count > 0:
                            if '{' in lines[j]:
                                brace_count += lines[j].count('{')
                            if '}' in lines[j]:
                                brace_count -= lines[j].count('}')
                            
                            # Add statements to finally body
                            if brace_count > 0:
                                stmt = lines[j].strip()
                                if stmt and not stmt.startswith('//'):
                                    finally_node['body'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    else:
                        # Single line finally
                        j += 1
                        if j < len(lines):
                            stmt = lines[j].strip()
                            if stmt and not stmt.startswith('//'):
                                finally_node['body'].append({'type': 'Statement', 'value': stmt})
                            j += 1
                    
                    try_node['finally'] = finally_node
                
                root['body'].append(try_node)
                i = j
                continue
            
            # Other statements
            root['body'].append({'type': 'Statement', 'value': line})
            i += 1
        
        self.ast = root
        return root

class CppNassiShneidermanVisitor:
    """Visitor for generating ASCII Nassi-Shneiderman diagrams from C++ pseudo-AST"""
    
    def __init__(self, width=80, show_classes=True, show_methods=True, show_functions=True, 
                 show_procedures=True, selected_classes=None, selected_methods=None):
        self.width = width
        self.diagram = []
        self.indent = 0
        self.show_classes = show_classes
        self.show_methods = show_methods
        self.show_functions = show_functions
        self.show_procedures = show_procedures
        self.selected_classes = selected_classes or []
        self.selected_methods = selected_methods or []
    
    def get_diagram(self):
        return "\n".join(self.diagram)
    
    def add_line(self, line):
        self.diagram.append(" " * self.indent + line)
    
    def add_box(self, text, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Text (linksbündig)
        text_lines = text.split("\n")
        for line in text_lines:
            # Linksbündig mit etwas Abstand
            padded_line = " " + line.ljust(box_width - 3)
            self.add_line("|" + padded_line + "|")
        
        # Untere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_if_box(self, condition, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Bedingung
        condition_text = f"if ({condition})"
        # Linksbündig mit etwas Abstand
        padded_line = " " + condition_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_else_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Else
        # Linksbündig mit etwas Abstand
        padded_line = " else".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_for_box(self, init, condition, increment, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # For-Schleife
        for_text = f"for ({init}; {condition}; {increment})"
        # Linksbündig mit etwas Abstand
        padded_line = " " + for_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_while_box(self, condition, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # While-Schleife
        while_text = f"while ({condition})"
        # Linksbündig mit etwas Abstand
        padded_line = " " + while_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_try_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Try
        # Linksbündig mit etwas Abstand
        padded_line = " try".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_catch_box(self, exception, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Catch
        catch_text = f"catch ({exception})" if exception else "catch (...)"
        # Linksbündig mit etwas Abstand
        padded_line = " " + catch_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def visit(self, node):
        """Visit a node in the AST"""
        method = 'visit_' + node['type']
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)
    
    def visit_Module(self, node):
        self.add_box("C++ Modul")
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_FunctionDef(self, node):
        # Prüfen, ob es sich um eine Methode oder eine Funktion handelt
        is_method = node.get('is_method', False)
        class_name = node.get('class_name', '')
        
        # Entscheiden, ob die Funktion/Methode angezeigt werden soll
        if is_method:
            if not self.show_methods:
                return
            # Prüfen, ob die Methode in der ausgewählten Liste ist
            method_name = f"{class_name}.{node['name']}"
            if self.selected_methods and method_name not in self.selected_methods:
                return
        else:
            if not self.show_functions:
                return
            # Prüfen, ob die Funktion in der ausgewählten Liste ist
            if self.selected_methods and node['name'] not in self.selected_methods:
                return
        
        self.add_box(f"Function: {node['name']}")
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_ClassDef(self, node):
        if not self.show_classes:
            return
        
        # Prüfen, ob die Klasse in der ausgewählten Liste ist
        if self.selected_classes and node['name'] not in self.selected_classes:
            return
            
        self.add_box(f"Class: {node['name']}")
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_If(self, node):
        self.add_if_box(node['condition'])
        
        # If-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
        
        # Else-Block (falls vorhanden)
        if node.get('orelse', []):
            self.add_else_box()
            self.indent += 2
            for stmt in node['orelse']:
                self.visit(stmt)
            self.indent -= 2
    
    def visit_For(self, node):
        self.add_for_box(node['init'], node['condition'], node['increment'])
        
        # Schleifenkörper
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_While(self, node):
        self.add_while_box(node['condition'])
        
        # Schleifenkörper
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_Try(self, node):
        self.add_try_box()
        
        # Try-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
        
        # Catch-Blöcke
        for handler in node.get('handlers', []):
            self.visit(handler)
    
    def visit_Catch(self, node):
        self.add_catch_box(node['exception'])
        
        # Catch-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_Statement(self, node):
        self.add_box(node['value'])
    
    def generic_visit(self, node):
        self.add_box(f"Nicht unterstützt: {node['type']}")

class KotlinNassiShneidermanVisitor:
    """Visitor for generating ASCII Nassi-Shneiderman diagrams from Kotlin pseudo-AST"""
    
    def __init__(self, width=80, show_classes=True, show_methods=True, show_functions=True, 
                 show_procedures=True, selected_classes=None, selected_methods=None):
        self.width = width
        self.diagram = []
        self.indent = 0
        self.show_classes = show_classes
        self.show_methods = show_methods
        self.show_functions = show_functions
        self.show_procedures = show_procedures
        self.selected_classes = selected_classes or []
        self.selected_methods = selected_methods or []
    
    def get_diagram(self):
        return "\n".join(self.diagram)
    
    def add_line(self, line):
        self.diagram.append(" " * self.indent + line)
    
    def add_box(self, text, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Text (linksbündig)
        text_lines = text.split("\n")
        for line in text_lines:
            # Linksbündig mit etwas Abstand
            padded_line = " " + line.ljust(box_width - 3)
            self.add_line("|" + padded_line + "|")
        
        # Untere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_if_box(self, condition, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Bedingung
        condition_text = f"if ({condition})"
        # Linksbündig mit etwas Abstand
        padded_line = " " + condition_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_else_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Else
        # Linksbündig mit etwas Abstand
        padded_line = " else".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_for_box(self, target, iter_expr, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # For-Schleife
        for_text = f"for {target} in {iter_expr}"
        # Linksbündig mit etwas Abstand
        padded_line = " " + for_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_while_box(self, condition, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # While-Schleife
        while_text = f"while ({condition})"
        # Linksbündig mit etwas Abstand
        padded_line = " " + while_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_try_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Try
        # Linksbündig mit etwas Abstand
        padded_line = " try".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_catch_box(self, exception, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Catch
        catch_text = f"catch ({exception})" if exception else "catch"
        # Linksbündig mit etwas Abstand
        padded_line = " " + catch_text.ljust(box_width - 3)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def add_finally_box(self, box_width=None):
        if box_width is None:
            box_width = self.width - self.indent
        
        # Obere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
        
        # Finally
        # Linksbündig mit etwas Abstand
        padded_line = " finally".ljust(box_width - 2)
        self.add_line("|" + padded_line + "|")
        
        # Mittlere Linie
        self.add_line("+" + "-" * (box_width - 2) + "+")
    
    def visit(self, node):
        """Visit a node in the AST"""
        method = 'visit_' + node['type']
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)
    
    def visit_Module(self, node):
        self.add_box("Kotlin Modul")
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_FunctionDef(self, node):
        # Prüfen, ob es sich um eine Methode oder eine Funktion handelt
        is_method = node.get('is_method', False)
        class_name = node.get('class_name', '')
        
        # Entscheiden, ob die Funktion/Methode angezeigt werden soll
        if is_method:
            if not self.show_methods:
                return
            # Prüfen, ob die Methode in der ausgewählten Liste ist
            method_name = f"{class_name}.{node['name']}"
            if self.selected_methods and method_name not in self.selected_methods:
                return
        else:
            if not self.show_functions:
                return
            # Prüfen, ob die Funktion in der ausgewählten Liste ist
            if self.selected_methods and node['name'] not in self.selected_methods:
                return
            
        self.add_box(f"fun {node['name']}")
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_ClassDef(self, node):
        if not self.show_classes:
            return
        
        # Prüfen, ob die Klasse in der ausgewählten Liste ist
        if self.selected_classes and node['name'] not in self.selected_classes:
            return
            
        self.add_box(f"class {node['name']}")
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_If(self, node):
        self.add_if_box(node['condition'])
        
        # If-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
        
        # Else-Block (falls vorhanden)
        if node.get('orelse', []):
            self.add_else_box()
            self.indent += 2
            for stmt in node['orelse']:
                self.visit(stmt)
            self.indent -= 2
    
    def visit_For(self, node):
        self.add_for_box(node['target'], node['iter'])
        
        # Schleifenkörper
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_While(self, node):
        self.add_while_box(node['condition'])
        
        # Schleifenkörper
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_Try(self, node):
        self.add_try_box()
        
        # Try-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
        
        # Catch-Blöcke
        for handler in node.get('handlers', []):
            self.visit(handler)
        
        # Finally-Block (falls vorhanden)
        if 'finally' in node:
            self.visit_Finally(node['finally'])
    
    def visit_Catch(self, node):
        self.add_catch_box(node['exception'])
        
        # Catch-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_Finally(self, node):
        self.add_finally_box()
        
        # Finally-Block
        self.indent += 2
        for stmt in node['body']:
            self.visit(stmt)
        self.indent -= 2
    
    def visit_Statement(self, node):
        self.add_box(node['value'])
    
    def generic_visit(self, node):
        self.add_box(f"Nicht unterstützt: {node['type']}")

class ModuleLoader:
    """Utility class to automatically load modules"""
    
    @staticmethod
    def get_available_modules():
        """Get a list of available modules in the Python environment"""
        available_modules = []
        
        # Get all modules from sys.path
        for module_info in pkgutil.iter_modules():
            available_modules.append(module_info.name)
        
        return available_modules
    
    @staticmethod
    def load_module(module_name):
        """Attempt to load a module by name"""
        try:
            return importlib.import_module(module_name)
        except ImportError:
            return None

class NassiShneidermanGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASCII Nassi-Shneiderman Diagramm Generator")
        self.setGeometry(100, 100, 1200, 800)
        
        # Logo als Anwendungsicon setzen
        try:
            app_icon = QIcon(LOGO_FILE)
            self.setWindowIcon(app_icon)
        except Exception as e:
            print(f"Fehler beim Laden des Logos als Icon: {str(e)}")
        
        # Variablen
        self.current_file = None
        self.current_language = "python"  # Default-Sprache
        self.available_modules = []
        self.selected_classes = []
        self.selected_methods = []
        
        # Zentrales Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Hauptlayout
        main_layout = QVBoxLayout(central_widget)
        
        # Logo im Hauptfenster anzeigen
        try:
            logo_label = QLabel()
            logo_pixmap = QPixmap(LOGO_FILE)
            if not logo_pixmap.isNull():
                logo_pixmap = logo_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                logo_label.setPixmap(logo_pixmap)
            logo_label.setAlignment(Qt.AlignCenter)
            main_layout.addWidget(logo_label)
        except Exception as e:
            print(f"Fehler beim Laden des Logos im Hauptfenster: {str(e)}")
        
        # Steuerelemente
        control_group = QGroupBox("Steuerelemente")
        control_layout = QFormLayout()
        
        # Sprachauswahl
        self.language_combo = QComboBox()
        self.language_combo.addItems(["Python", "C++", "Kotlin"])
        self.language_combo.currentTextChanged.connect(self.on_language_changed)
        control_layout.addRow("Programmiersprache:", self.language_combo)
        
        # Datei laden
        file_layout = QHBoxLayout()
        self.file_label = QLabel("Keine Datei geladen")
        load_button = QPushButton("Datei laden")
        load_button.clicked.connect(self.load_file)
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(load_button)
        control_layout.addRow("Datei:", file_layout)
        
        # Diagrammbreite
        self.width_spin = QSpinBox()
        self.width_spin.setRange(40, 200)
        self.width_spin.setValue(80)
        control_layout.addRow("Diagrammbreite:", self.width_spin)
        
        # Elementauswahl
        element_group = QGroupBox("Elemente anzeigen")
        element_layout = QGridLayout()
        
        # Checkboxen für die Elementauswahl
        self.class_checkbox = QCheckBox("Klassen")
        self.class_checkbox.setChecked(True)
        element_layout.addWidget(self.class_checkbox, 0, 0)
        
        self.method_checkbox = QCheckBox("Methoden")
        self.method_checkbox.setChecked(True)
        element_layout.addWidget(self.method_checkbox, 0, 1)
        
        self.function_checkbox = QCheckBox("Funktionen")
        self.function_checkbox.setChecked(True)
        element_layout.addWidget(self.function_checkbox, 1, 0)
        
        self.procedure_checkbox = QCheckBox("Prozeduren")
        self.procedure_checkbox.setChecked(True)
        element_layout.addWidget(self.procedure_checkbox, 1, 1)
        
        # Alle auswählen Button
        select_all_button = QPushButton("Alle auswählen")
        select_all_button.clicked.connect(self.select_all_elements)
        element_layout.addWidget(select_all_button, 2, 0)
        
        # Spezifische Elemente auswählen Button
        select_specific_button = QPushButton("Spezifische Elemente...")
        select_specific_button.clicked.connect(self.select_specific_elements)
        element_layout.addWidget(select_specific_button, 2, 1)
        
        element_group.setLayout(element_layout)
        control_layout.addRow("", element_group)
        
        # Generieren-Button
        generate_button = QPushButton("Diagramm generieren")
        generate_button.clicked.connect(self.generate_diagram)
        
        # Logo neben dem Generieren-Button
        generate_layout = QHBoxLayout()
        generate_layout.addWidget(generate_button)
        
        try:
            button_logo = QLabel()
            button_logo_pixmap = QPixmap(LOGO_FILE)
            if not button_logo_pixmap.isNull():
                button_logo_pixmap = button_logo_pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                button_logo.setPixmap(button_logo_pixmap)
            generate_layout.addWidget(button_logo)
        except Exception as e:
            print(f"Fehler beim Laden des Logos neben dem Button: {str(e)}")
            
        control_layout.addRow("", generate_layout)
        
        control_group.setLayout(control_layout)
        main_layout.addWidget(control_group)
        
        # Splitter für Code und Diagramm
        splitter = QSplitter(Qt.Vertical)
        
        # Code-Editor
        code_group = QGroupBox("Quellcode")
        code_layout = QVBoxLayout()
        self.code_edit = QTextEdit()
        self.code_edit.setFont(QFont("Courier New", 10))
        code_layout.addWidget(self.code_edit)
        code_group.setLayout(code_layout)
        
        # Diagramm-Anzeige
        diagram_group = QGroupBox("Nassi-Shneiderman-Diagramm")
        diagram_layout = QVBoxLayout()
        self.diagram_edit = QTextEdit()
        self.diagram_edit.setFont(QFont("Courier New", 10))
        self.diagram_edit.setReadOnly(True)
        
        # Speichern-Button mit Logo
        save_layout = QHBoxLayout()
        save_button = QPushButton("Diagramm speichern")
        save_button.clicked.connect(self.save_diagram)
        save_layout.addWidget(save_button)
        
        try:
            save_logo = QLabel()
            save_logo_pixmap = QPixmap(LOGO_FILE)
            if not save_logo_pixmap.isNull():
                save_logo_pixmap = save_logo_pixmap.scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                save_logo.setPixmap(save_logo_pixmap)
            save_layout.addWidget(save_logo)
        except Exception as e:
            print(f"Fehler beim Laden des Logos neben dem Speichern-Button: {str(e)}")
        
        diagram_layout.addWidget(self.diagram_edit)
        diagram_layout.addLayout(save_layout)
        diagram_group.setLayout(diagram_layout)
        
        splitter.addWidget(code_group)
        splitter.addWidget(diagram_group)
        splitter.setSizes([300, 500])
        
        main_layout.addWidget(splitter)
        
        # Statusleiste mit Logo
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        try:
            status_logo = QLabel()
            status_logo_pixmap = QPixmap(LOGO_FILE)
            if not status_logo_pixmap.isNull():
                status_logo_pixmap = status_logo_pixmap.scaled(16, 16, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                status_logo.setPixmap(status_logo_pixmap)
            self.statusBar.addPermanentWidget(status_logo)
        except Exception as e:
            print(f"Fehler beim Laden des Logos in der Statusleiste: {str(e)}")
            
        self.statusBar.showMessage("Bereit")
        
        # Syntax-Highlighter
        self.python_highlighter = PythonHighlighter(self.code_edit.document())
        self.cpp_highlighter = CppHighlighter(self.code_edit.document())
        self.kotlin_highlighter = KotlinHighlighter(self.code_edit.document())
        
        # Aktuellen Highlighter setzen
        self.set_highlighter()
        
        # Automatisches Laden der Module
        self.load_available_modules()
    
    def select_specific_elements(self):
        """Öffnet einen Dialog zur Auswahl spezifischer Klassen und Methoden"""
        if not self.code_edit.toPlainText().strip():
            QMessageBox.warning(self, "Warnung", "Kein Code zum Analysieren vorhanden.")
            return
        
        try:
            # Extrahiere Klassen und Methoden aus dem Code
            code = self.code_edit.toPlainText()
            classes, methods = CodeElementExtractor.extract_elements(code, self.current_language)
            
            # Öffne den Auswahldialog mit vorherigen Auswahlen
            dialog = ElementSelectionDialog(
                self, 
                classes, 
                methods, 
                selected_classes=self.selected_classes,
                selected_methods=self.selected_methods
            )
            
            if dialog.exec_():
                # Speichere die ausgewählten Elemente
                self.selected_classes = dialog.get_selected_classes()
                self.selected_methods = dialog.get_selected_methods()
                
                # Aktualisiere die UI, um den aktiven Filtermodus anzuzeigen
                has_specific_selection = bool(self.selected_classes) or bool(self.selected_methods)
                
                # Deaktiviere die allgemeinen Checkboxen, wenn spezifische Auswahl aktiv ist
                self.class_checkbox.setEnabled(not has_specific_selection)
                self.method_checkbox.setEnabled(not has_specific_selection)
                self.function_checkbox.setEnabled(not has_specific_selection)
                self.procedure_checkbox.setEnabled(not has_specific_selection)
                
                # Aktualisiere die Statusleiste
                if has_specific_selection:
                    self.statusBar.showMessage(
                        f"Spezifische Auswahl aktiv: {len(self.selected_classes)} Klassen und {len(self.selected_methods)} Methoden/Funktionen. Klicken Sie auf 'Diagramm generieren' um das Diagramm zu erstellen."
                    )
                else:
                    self.statusBar.showMessage("Allgemeine Filterung aktiv (keine spezifische Auswahl). Klicken Sie auf 'Diagramm generieren' um das Diagramm zu erstellen.")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler bei der Elementauswahl: {str(e)}")
    
    def select_all_elements(self):
        """Wählt alle Elemente aus oder ab"""
        # Prüfen, ob alle Checkboxen bereits ausgewählt sind
        all_checked = (self.class_checkbox.isChecked() and 
                       self.method_checkbox.isChecked() and 
                       self.function_checkbox.isChecked() and 
                       self.procedure_checkbox.isChecked())
        
        # Wenn alle ausgewählt sind, alle abwählen, sonst alle auswählen
        self.class_checkbox.setChecked(not all_checked)
        self.method_checkbox.setChecked(not all_checked)
        self.function_checkbox.setChecked(not all_checked)
        self.procedure_checkbox.setChecked(not all_checked)
        
        # Zurücksetzen der spezifischen Auswahl
        self.selected_classes = []
        self.selected_methods = []
    
    def load_available_modules(self):
        """Lädt verfügbare Module und speichert sie in der Instanzvariable"""
        self.available_modules = ModuleLoader.get_available_modules()
        # Statusleiste aktualisieren, wenn sie bereits existiert
        if hasattr(self, 'statusBar') and self.statusBar is not None:
            self.statusBar.showMessage(f"{len(self.available_modules)} Module verfügbar")
    
    def set_highlighter(self):
        """Setzt den passenden Syntax-Highlighter basierend auf der ausgewählten Sprache"""
        # Deaktiviere alle Highlighter
        self.python_highlighter.setDocument(None)
        self.cpp_highlighter.setDocument(None)
        self.kotlin_highlighter.setDocument(None)
        
        # Aktiviere den passenden Highlighter
        if self.current_language == "python":
            self.python_highlighter.setDocument(self.code_edit.document())
        elif self.current_language == "cpp":
            self.cpp_highlighter.setDocument(self.code_edit.document())
        elif self.current_language == "kotlin":
            self.kotlin_highlighter.setDocument(self.code_edit.document())
    
    def on_language_changed(self, language):
        """Wird aufgerufen, wenn die Sprache geändert wird"""
        self.current_language = language.lower()
        self.set_highlighter()
        
        # Zurücksetzen der spezifischen Auswahl bei Sprachwechsel
        self.selected_classes = []
        self.selected_methods = []
        
        # Aktiviere die allgemeinen Checkboxen wieder
        self.class_checkbox.setEnabled(True)
        self.method_checkbox.setEnabled(True)
        self.function_checkbox.setEnabled(True)
        self.procedure_checkbox.setEnabled(True)
        
        self.statusBar.showMessage(f"Sprache geändert zu {language}")
    
    def load_file(self):
        """Lädt eine Datei"""
        file_filters = {
            "python": "Python-Dateien (*.py)",
            "cpp": "C++-Dateien (*.cpp *.h *.hpp)",
            "kotlin": "Kotlin-Dateien (*.kt)"
        }
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Datei öffnen",
            "",
            f"{file_filters[self.current_language]};;Alle Dateien (*.*)"
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            
            self.current_file = file_path
            self.file_label.setText(os.path.basename(file_path))
            self.code_edit.setText(code)
            
            # Zurücksetzen der spezifischen Auswahl bei Dateiladung
            self.selected_classes = []
            self.selected_methods = []
            
            # Aktiviere die allgemeinen Checkboxen wieder
            self.class_checkbox.setEnabled(True)
            self.method_checkbox.setEnabled(True)
            self.function_checkbox.setEnabled(True)
            self.procedure_checkbox.setEnabled(True)
            
            # Statusleiste aktualisieren
            self.statusBar.showMessage(f"Datei geladen: {file_path}. Klicken Sie auf 'Diagramm generieren' um das Diagramm zu erstellen.")
        
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Laden der Datei: {str(e)}")
    
    def generate_diagram(self):
        """Generiert das Nassi-Shneiderman-Diagramm"""
        try:
            code = self.code_edit.toPlainText()
            width = self.width_spin.value()
            
            if not code.strip():
                self.statusBar.showMessage("Kein Code zum Generieren vorhanden")
                return
            
            # Prüfen, ob spezifische Auswahl aktiv ist
            has_specific_selection = bool(self.selected_classes) or bool(self.selected_methods)
            
            # Elementauswahl auslesen - nur verwenden, wenn keine spezifische Auswahl aktiv ist
            show_classes = self.class_checkbox.isChecked() if not has_specific_selection else True
            show_methods = self.method_checkbox.isChecked() if not has_specific_selection else True
            show_functions = self.function_checkbox.isChecked() if not has_specific_selection else True
            show_procedures = self.procedure_checkbox.isChecked() if not has_specific_selection else True
            
            # Diagramm generieren basierend auf der Sprache
            if self.current_language == "python":
                tree = ast.parse(code)
                visitor = NassiShneidermanVisitor(
                    width, 
                    show_classes=show_classes, 
                    show_methods=show_methods, 
                    show_functions=show_functions, 
                    show_procedures=show_procedures,
                    selected_classes=self.selected_classes,
                    selected_methods=self.selected_methods
                )
                visitor.visit(tree)
                diagram = visitor.get_diagram()
            
            elif self.current_language == "cpp":
                parser = SimpleCppParser()
                tree = parser.parse(code)
                visitor = CppNassiShneidermanVisitor(
                    width, 
                    show_classes=show_classes, 
                    show_methods=show_methods, 
                    show_functions=show_functions, 
                    show_procedures=show_procedures,
                    selected_classes=self.selected_classes,
                    selected_methods=self.selected_methods
                )
                visitor.visit(tree)
                diagram = visitor.get_diagram()
            
            elif self.current_language == "kotlin":
                parser = SimpleKotlinParser()
                tree = parser.parse(code)
                visitor = KotlinNassiShneidermanVisitor(
                    width, 
                    show_classes=show_classes, 
                    show_methods=show_methods, 
                    show_functions=show_functions, 
                    show_procedures=show_procedures,
                    selected_classes=self.selected_classes,
                    selected_methods=self.selected_methods
                )
                visitor.visit(tree)
                diagram = visitor.get_diagram()
            
            # Diagramm anzeigen
            self.diagram_edit.setText(diagram)
            
            # Statusleiste aktualisieren
            filter_info = ""
            if has_specific_selection:
                filter_info = f" (spezifische Auswahl: {len(self.selected_classes)} Klassen, {len(self.selected_methods)} Methoden/Funktionen)"
            else:
                active_filters = []
                if show_classes: active_filters.append("Klassen")
                if show_methods: active_filters.append("Methoden")
                if show_functions: active_filters.append("Funktionen")
                if show_procedures: active_filters.append("Prozeduren")
                filter_info = f" (allgemeine Filter: {', '.join(active_filters)})"
            
            self.statusBar.showMessage(f"Diagramm erfolgreich generiert{filter_info}")
        
        except SyntaxError as e:
            QMessageBox.warning(self, "Syntax-Fehler", f"Der Code enthält Syntax-Fehler: {str(e)}")
            self.statusBar.showMessage("Fehler: Syntax-Fehler im Code")
        
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler bei der Diagramm-Generierung: {str(e)}")
            self.statusBar.showMessage("Fehler bei der Diagramm-Generierung")
    
    def save_diagram(self):
        """Speichert das generierte Diagramm"""
        if not self.diagram_edit.toPlainText().strip():
            QMessageBox.warning(self, "Warnung", "Kein Diagramm zum Speichern vorhanden.")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Diagramm speichern",
            "",
            "Textdateien (*.txt);;Alle Dateien (*.*)"
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.diagram_edit.toPlainText())
            
            QMessageBox.information(self, "Erfolg", f"Diagramm wurde gespeichert als:\n{file_path}")
            self.statusBar.showMessage(f"Diagramm gespeichert: {file_path}")
        
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Speichern des Diagramms: {str(e)}")
            self.statusBar.showMessage("Fehler beim Speichern des Diagramms")

def main():
    app = QApplication(sys.argv)
    
    # Anwendungsweites Logo setzen
    try:
        app.setWindowIcon(QIcon(LOGO_FILE))
    except Exception as e:
        print(f"Fehler beim Setzen des Anwendungslogos: {str(e)}")
        
    window = NassiShneidermanGenerator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
