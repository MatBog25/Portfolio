# 🚀 Portfolio - Nowoczesne Portfolio Flask z Tailwind CSS

Profesjonalne, responsywne portfolio stworzone z wykorzystaniem Flask i Tailwind CSS.

## 🛠️ Technologie

### Backend
- **Flask** - Framework
- **Python 3.8+** - Język programowania

### Frontend
- **Tailwind CSS** - Framework CSS
- **JavaScript (ES6+)** - Interaktywność
- **Alpine.js** - Komponenty
- **AOS** - Animacje przy przewijaniu
- **Font Awesome** - Ikony

## 📦 Instalacja

### Wymagania systemowe
- Python 3.8 lub nowszy
- Node.js 16 lub nowszy
- npm lub yarn

### Krok 1: Tworzenie środowiska wirtualnego
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Krok 2: Instalacja zależności Python
```bash
pip install -r requirements.txt
```

### Krok 3: Instalacja zależności Node.js
```bash
npm install
```

### Krok 4: Uruchomienie aplikacji
```bash
python app.py
```

Aplikacja będzie dostępna pod adresem: `http://localhost:5000`

## 📁 Struktura projektu

```
portfolio-flask/
├── app.py                 # Główna aplikacja Flask
├── requirements.txt       # Zależności Python
├── package.json          # Zależności Node.js
├── tailwind.config.js    # Konfiguracja Tailwind CSS
├── README.md             # Dokumentacja
├── templates/            # Szablony HTML
│   ├── base.html        # Szablon bazowy
│   ├── index.html       # Strona główna
│   ├── about.html       # O mnie
│   ├── projects.html    # Projekty
│   └── contact.html     # Kontakt
└── static/              # Pliki statyczne
    ├── css/             # Style CSS
    ├── js/              # JavaScript
    │   └── main.js      # Główny plik JS
    └── src/             # Źródła CSS
        └── input.css    # Plik wejściowy CSS
```

### Modyfikacja stylów
1. Edytuj `static/src/input.css`
2. Dodaj klasy w `tailwind.config.js`
3. Przebuduj CSS: `npm run build-css`

## 📝 Licencja

Ten projekt jest dostępny na licencji MIT. Zobacz plik `LICENSE` dla szczegółów.

## 📞 Kontakt

- **Email**: mateusz.boguszewski.it@gmail.com