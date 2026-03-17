# Nassi-Shneidermann Diagram Generator

Ein leistungsstarkes Desktop-Tool zur automatischen Erzeugung von **Nassi-Shneidermann-Struktogrammen** (Structograms) und **Code-Tree-Diagrammen** direkt aus C++-Quellcode – mit interaktiver GUI, Syntax-Highlighting und SVG/PNG-Export.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-informational?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

- **Automatische Diagramm-Erzeugung** – lädt C++-Quelldateien und rendert Struktogramme auf Knopfdruck
- **Code-Tree-Ansicht** – zeigt die Struktur des Codes als hierarchischen Baum
- **Mehrere Beispieldateien** – von einfachen Menüs bis hin zu Templates und OOP-Konzepten
- **SVG / PNG Export** – Diagramme als Vektorgrafik oder Rasterbild speichern
- **Interaktive GUI** – gebaut mit Python & tkinter, direkt ausführbar ohne Installation

---

## Screenshots

### Beispiel 1 – Einfaches Spielmenü (`example.cpp`)

Ein klassisches textbasiertes Abenteuerspiel-Menü mit Funktionen für Store, Character, Inventory und Wilderness – ideal als Einstieg in Kontrollflusstruktogramme.

![Code Tree – example.cpp](PrtScr.png)

---

### Beispiel 2 – Factory Pattern (`example II.cpp`)

Modernes C++ mit Templates, `std::unique_ptr`, `std::function` und einem generischen Factory-Pattern zur dynamischen Objekterzeugung.

![Code Tree – example II.cpp](PrtScr%20II.png)

---

## Enthaltene Beispieldateien

### `example.cpp` – Spielmenü (Beginner)

```cpp
void Mainmenu() {
    string choice;
    cout << "1: Attack creature" << endl;
    cout << "2: Buy equipment"   << endl;
    // ...
    cin >> choice;
    if (choice == "1") Wilderness();
    else if (choice == "2") Store();
    // ...
}
```

Demonstriert:
- Sequenz, Selektion (`if / else if / else`), Schleifen mit `goto`
- Funktionsaufrufe und Rücksprünge
- Arrays und String-Eingabe

---

### `example II.cpp` – Factory Pattern (Advanced)

```cpp
template <typename Base, typename... Args>
class Factory {
public:
    template <typename Derived>
    void registerType(const std::string& name);
    std::unique_ptr<Base> create(const std::string& name, Args... args) const;
private:
    std::map<std::string, CreatorFunc> creators;
};
```

Demonstriert:
- Klassen, Vererbung, virtuelle Methoden, `override`
- Templates mit variadic Arguments (`typename... Args`)
- Smart Pointer (`std::unique_ptr`)
- `std::function`, `std::map`, Lambda-Ausdrücke
- `static_assert` und `std::is_base_of`

---

### `BankAccount_Example.cpp` – Bankkonto-System (OOP)

Ein vollständiges Bankkonto-System als weiteres Demo-Beispiel für den Diagramm-Generator.

Demonstriert:
- `enum class`, `struct` mit Konstruktor
- `class` mit privaten Membern, statischem Zähler, Getter-Methoden
- Einzahlung, Abhebung, Überweisung mit Fehlerbehandlung (`throw` / `try` / `catch`)
- Ausgabeformatierung mit `<iomanip>` und `<vector>`

---

## Voraussetzungen

- Python **3.8** oder neuer
- Windows (primäre Plattform)

---

## Installation

### 1. Repository klonen

```bash
git clone https://github.com/Flying-Bolt/Nassi-Schneidermann.git
cd Nassi-Schneidermann
```

### 2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Oder manuell:

```bash
pip install Pillow
```

### 3. Anwendung starten

```bash
python "Code Tree Diagramm.py"
```

---

## Verwendung

1. Anwendung starten
2. Über **Datei öffnen** eine `.cpp`-Datei laden (z. B. `example.cpp`)
3. Das Struktogramm wird automatisch erzeugt und angezeigt
4. Über **Exportieren** als SVG oder PNG speichern

---

## Projektstruktur

```
Nassi-Schneidermann/
├── Code Tree Diagramm.py     # Hauptanwendung
├── example.cpp               # Beispiel: Spielmenü (Beginner)
├── example II.cpp            # Beispiel: Factory Pattern (Advanced)
├── BankAccount_Example.cpp   # Beispiel: Bankkonto OOP-System
├── PrtScr.png                # Screenshot – example.cpp Diagramm
├── PrtScr II.png             # Screenshot – example II.cpp Diagramm
├── .gitignore
└── README.md
```

---

## Technische Details

### Unterstützte C++-Konstrukte

| Konstrukt | Darstellung im Struktogramm |
|-----------|----------------------------|
| Sequenz | Einfaches Rechteck |
| `if / else` | Entscheidungsblock (Dreieck) |
| `for / while / do-while` | Schleifenblock |
| Funktionsaufruf | Rechteck mit doppelten Seitenlinien |
| `try / catch` | Fehlerbehandlungsblock |
| Klassen & Methoden | Hierarchische Baumstruktur |

### Abhängigkeiten

| Paket | Zweck |
|-------|-------|
| `tkinter` | GUI (Python-Standardbibliothek) |
| `Pillow` | Bildverarbeitung & PNG-Export |
| `ast` | Python-Code-Analyse (intern) |

---

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

---

## Mitwirken

Pull Requests sind willkommen. Bitte öffnen Sie bei größeren Änderungen zuerst ein Issue.
