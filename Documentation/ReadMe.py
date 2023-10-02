'''
Konventionen des Projekts:

(0) Sprache

Verwendung findet hier innerhalb des Codes die englische Sprache.

(1) Namensgebung

- Dateinamen werden mit Großbuchstaben beginnend geschrieben, jedes Folgewort auch groß

- Klassennamen werden mit Großbuchstaben beginnend geschrieben, jedes Folgewort auch groß

- Klassenmember werden im Camel Case geschrieben

- Funktionen werden im Camel Case geschrieben mit Interpreter Hints (def func(var : int) -> int)

- Variablen werden im Camel Case geschrieben mit Interpreter Hints (var : int = 10)

- Konstanten werden in Caps Lock geschrieben mit Interpreter Hints (CONST : int = 10)


(2) Code Aufbau

- Absätze nach Funktionsdefinitionen genügen einer Freizeile (Klassen werden analog behandelt)
    def func() -> bool :
        
        return True 

- Nach ende der Funktionsdefinition werden 2 Freizeilen gelassen

- Nicht zusammenhängende Codeblöcke werden durch Freizeilen getrennt

- if- , while- Bedingungen genügen einem einfachen Absatz und keiner Klammerung
    if condition : 
        break

- Sonderzeichen genügen einem Leerzeichen

    Auftreten : Doppelpunkt, Pfeil ->,...

- Aufzählungen erfolgen über Kommata nach einem beliebigen Wort über Sigma* und einem folgenden Leerzeichen

- Angabe von Strings erfolgt über Einzelabstrophe


(3) Benutzte Module

- Pygame


(4) Aufbau des Projekts

Der Aufbau erfolgt in folgender Ordnerstruktur

Projekt
|
- Dependencies : externe Dateien
|
|
- Source
|    |
|    - Engine
|    |
|    - Game
|    |
|    - Algorithms
|
|
- Documentation



'''