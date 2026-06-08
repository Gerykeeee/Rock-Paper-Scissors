

# 🎮 Terminal-Based Rock-Paper-Scissors (OOP Edition)

> **Rövid leírás / Project Overview**
> Ez a projekt egy parancssoros (CLI), objektumorientált (OOP) Kő-Papír-Olló játék. A kód fő vonzereje, hogy a kezdők által gyakran használt, nehezen karbantartható `if-else` spagettikód helyett professzionális szoftvertervezési mintákat alkalmaz. Enumerációkat (`Enum`) használ a szigorú típusbiztonság érdekében, a győzelmi feltételeket pedig egy Hash Map (szótár) segítségével képezi le. Ez a megoldás a lassabb, procedurális feltételvizsgálatokat **O(1) konstans időkomplexitású** memóriakereséssé alakítja, így a kód nemcsak elegáns (Clean Code), de rendkívül könnyen skálázható is marad.

> *A robust, object-oriented and data-driven approach to a classic game.*
> 
> 🌍 **Languages:** [English](#-english) | [Magyar](#-magyar)

---

## 🇬🇧 English

### 📖 Overview
While Rock-Paper-Scissors is a classic beginner project, this repository takes a professional software engineering approach to its implementation. By discarding deeply nested, procedural `if-elif` chains, this project serves as a demonstration of **Object-Oriented Programming (OOP)**, **Clean Code** principles, and **Data Structure Optimization**. 

It is designed to be highly maintainable, easily extensible (e.g., adding new moves like "Lizard" or "Spock"), and safe from runtime errors caused by invalid state management.

### 🏗️ Architecture & Technical Details
The codebase is structured around robust data types and separated responsibilities:
* **`Move` (Enum)**: Strictly defines the allowed game moves (ROCK, PAPER, SCISSORS). This prevents "magic numbers" and invalid string inputs from corrupting the game state.
* **`Game_Result` (Enum)**: Encapsulates the possible outcomes (TIE, WIN, LOSE) to ensure type-safe return values from the evaluation logic.
* **`Game_Logic` (Class)**: 
  * Implements a **Hash Map Evaluation**: Instead of calculating the winner procedurally, the winning conditions are statically mapped in a dictionary (`self.winning_combos`). This shifts the evaluation from O(n) logical branching to **O(1) constant time complexity** lookups.
  * Handles internal state encapsulation and continuous game loop execution.

### ✨ Key Features
* **Strict Type Safety:** Handled via Python's `Enum` to prevent data anomalies.
* **Algorithmic Efficiency:** Dictionary-based logic mapping completely replaces slow, procedural conditional statements.
* **Robust Input Handling:** Defensive programming using `try-except` blocks ensures graceful recovery during invalid user interactions (Input Validation).
* **Extensibility:** The data-driven architecture allows for easy modifications without rewriting the core engine logic.

### 🚀 Getting Started

**Prerequisites**
* Python 3.6 or higher installed on your system.


---

# Kő-Papír-Olló - Objektumorientált Python Implementáció

## Részletes Leírás

Bár a Kő-Papír-Olló az egyik leggyakoribb kezdő programozási feladat, ez a projekt szakít a hagyományos, procedurális megközelítéssel. Ahelyett, hogy végtelen és nehezen karbantartható `if-elif-else` elágazásokra épülne, a kód a modern szoftverfejlesztés legjobb gyakorlatait (Best Practices) és az **Objektumorientált Programozás (OOP)** alapelveit alkalmazza. Célja, hogy bemutassa a robusztus állapotkezelést, a tiszta kód (Clean Code) írásának szabályait, valamint az adatstruktúrák okos megválasztásával elérhető optimalizációt.

### Architektúra és Felépítés
A program logikája és adatkezelése szigorúan szét van választva, megelőzve ezzel a "spagettikód" kialakulását és garantálva a könnyű bővíthetőséget:

* **Szigorú Típusbiztonság (Enum):** A program mellőzi a "mágikus számok" (magic numbers) és az egyszerű, sebezhető szöveges bemenetek (stringek) használatát a belső logikában. A `Move` és a `Game_Result` enumerációk gondoskodnak arról, hogy a belső játékállapot (pl. a kiválasztott lépés vagy a végeredmény) kizárólag egy előre definiált, zárt halmazból kerülhessen ki. Ez drasztikusan csökkenti a nem várt adatokból fakadó futásidejű hibák esélyét.
* **O(1) Időkomplexitású Kiértékelés (Hash Map):** A `Game_Logic` osztály legfontosabb újítása, hogy a győzelmi feltételeket egy szótárba (`self.winning_combos`) szervezi leképezésként. A kód nem vizsgálja procedurálisan minden egyes körben, hogy "ha a játékos követ húzott és a gép ollót, akkor mi történik", hanem egy egyszerű kulcs-érték párosítással, konstans idő alatt (O(1)) megállapítja a nyertest. Ez az adatvezérelt megközelítés sokkal könnyebben skálázható: új lépések (például Gyík vagy Spock) bevezetése csupán a szótár kibővítését igényli, anélkül, hogy a motor magját módosítani kellene.
* **Defenzív Programozás és Bemenetkezelés:** A felhasználói adatbekérés egy robusztus ciklusban és egy `try-except` blokkban történik. A rendszer fel van készülve arra, hogy a felhasználó a várt számok helyett véletlenül érvénytelen karaktereket gépel be. Az alkalmazás ilyenkor nem omlik össze (mint egy hagyományos `int(input())` esetében történne), hanem a kivételt (Exception) elkapva, elegánsan figyelmezteti a játékost, és újbóli adatmegadást kér.
* **Egységbezárás (Encapsulation):** Az állapotkezelés és a metódusok egy dedikált osztályba (`Game_Logic`) lettek szervezve, a program belépési pontja pedig a standard `if __name__ == '__main__':` feltétellel van biztosítva.

### Kinek szól ez a kód?
Ez az implementáció tökéletes példa arra, hogyan lehet egy egyszerű alapötletet professzionális, ipari sztenderdekhez közelítő módon megvalósítani. Kiváló referenciaként szolgálhat azok számára, akik be akarják mutatni, hogy tisztában vannak a fejlettebb Python adatstruktúrák előnyeivel, az algoritmikus gondolkodással és a hibatűrő szoftvertervezés alapjaival.
