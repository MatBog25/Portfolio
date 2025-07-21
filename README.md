# 🚀 Portfolio - Nowoczesne Portfolio Flask z Tailwind CSS

Profesjonalne, responsywne portfolio stworzone z wykorzystaniem Flask i Tailwind CSS. Zawiera animacje, dark mode, formularz kontaktowy i wiele innych nowoczesnych funkcji.

## ✨ Funkcjonalności

- 🎨 **Nowoczesny design** - Minimalistyczny i profesjonalny wygląd
- 🌓 **Dark/Light Mode** - Przełączanie między trybami jasnym i ciemnym
- 📱 **Responsywny** - Perfekcyjne wyświetlanie na wszystkich urządzeniach
- ⚡ **Animacje** - Płynne animacje i przejścia
- 🎭 **Dynamiczne tło** - Animowane tło z efektami cząsteczek
- 📧 **Formularz kontaktowy** - Funkcjonalny formularz z walidacją
- 🎯 **SEO-friendly** - Optymalizowane pod kątem wyszukiwarek
- 🔧 **Łatwa kustomizacja** - Modularna struktura kodu

## 🛠️ Technologie

### Backend
- **Flask** - Framework webowy
- **Python 3.8+** - Język programowania
- **Flask-Mail** - Obsługa poczty elektronicznej
- **Gunicorn** - Serwer WSGI do produkcji

### Frontend
- **Tailwind CSS** - Framework CSS
- **JavaScript (ES6+)** - Interaktywność
- **Alpine.js** - Reaktywne komponenty
- **AOS** - Animacje przy przewijaniu
- **Font Awesome** - Ikony

## 📦 Instalacja

### Wymagania systemowe
- Python 3.8 lub nowszy
- Node.js 16 lub nowszy
- npm lub yarn

### Krok 1: Klonowanie repozytorium
```bash
git clone https://github.com/your-username/portfolio-flask.git
cd portfolio-flask
```

### Krok 2: Tworzenie środowiska wirtualnego
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Krok 3: Instalacja zależności Python
```bash
pip install -r requirements.txt
```

### Krok 4: Instalacja zależności Node.js
```bash
npm install
```

### Krok 5: Konfiguracja zmiennych środowiskowych
Utwórz plik `.env` na podstawie `.env.example`:
```bash
# Skopiuj przykładowy plik
cp .env.example .env

# Edytuj plik .env i dodaj swoje dane
```

Przykład konfiguracji `.env`:
```env
SECRET_KEY=your-secret-key-here
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
FLASK_ENV=development
```

### Krok 6: Budowanie CSS
```bash
# Dla developmentu (z watch)
npm run build-css

# Dla produkcji (zminifikowane)
npm run build-css-prod
```

### Krok 7: Uruchomienie aplikacji
```bash
python app.py
```

Aplikacja będzie dostępna pod adresem: `http://localhost:5000`

## 🎨 Kustomizacja

### Kolory i style
Edytuj plik `tailwind.config.js` aby zmienić:
- Kolory główne (primary, dark)
- Animacje
- Czcionki
- Breakpoints

### Zawartość
Główne pliki do edycji:
- `app.py` - Dane projektów, umiejętności, doświadczenie
- `templates/` - Szablony HTML
- `static/src/input.css` - Niestandardowe style CSS

### Konfiguracja maila
W pliku `app.py` skonfiguruj:
```python
app.config['MAIL_SERVER'] = 'smtp.your-provider.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
```

## 📁 Struktura projektu

```
portfolio-flask/
├── app.py                 # Główna aplikacja Flask
├── requirements.txt       # Zależności Python
├── package.json          # Zależności Node.js
├── tailwind.config.js    # Konfiguracja Tailwind CSS
├── README.md             # Dokumentacja
├── .env.example          # Przykład zmiennych środowiskowych
├── templates/            # Szablony HTML
│   ├── base.html        # Szablon bazowy
│   ├── index.html       # Strona główna
│   ├── about.html       # O mnie
│   ├── projects.html    # Projekty
│   └── contact.html     # Kontakt
└── static/              # Pliki statyczne
    ├── css/             # Style CSS (generowane)
    ├── js/              # JavaScript
    │   └── main.js      # Główny plik JS
    └── src/             # Źródła CSS
        └── input.css    # Plik wejściowy CSS
```

## 🚀 Deployment

### Heroku
1. Zainstaluj Heroku CLI
2. Utwórz aplikację: `heroku create your-app-name`
3. Dodaj zmienne środowiskowe: `heroku config:set SECRET_KEY=your-key`
4. Deploy: `git push heroku main`

### Vercel
1. Zainstaluj Vercel CLI: `npm i -g vercel`
2. Deploy: `vercel`
3. Skonfiguruj zmienne środowiskowe w panelu Vercel

### Tradycyjny hosting
1. Zbuduj CSS: `npm run build-css-prod`
2. Skonfiguruj Gunicorn: `gunicorn app:app`
3. Ustaw serwer web (Nginx/Apache) jako reverse proxy

## 🔧 Rozwój

### Uruchomienie w trybie development
```bash
# Terminal 1 - Aplikacja Flask
python app.py

# Terminal 2 - Tailwind CSS watch
npm run build-css
```

### Dodawanie nowych projektów
Edytuj listę `projects_data` w pliku `app.py`:
```python
projects_data.append({
    'title': 'Nowy Projekt',
    'description': 'Opis projektu',
    'technologies': ['Python', 'React'],
    'image': 'project.jpg',
    'github': 'https://github.com/...',
    'demo': 'https://demo.com'
})
```

### Modyfikacja stylów
1. Edytuj `static/src/input.css`
2. Dodaj klasy w `tailwind.config.js`
3. Przebuduj CSS: `npm run build-css`

## 📋 TODO / Planowane funkcjonalności

- [ ] Blog system
- [ ] Multilanguage support
- [ ] Advanced analytics
- [ ] Project filtering
- [ ] Admin panel
- [ ] API endpoints
- [ ] Database integration
- [ ] User authentication

## 🤝 Współpraca

Zachęcam do współpracy! Jeśli chcesz dodać nową funkcjonalność lub poprawić błąd:

1. Fork repozytorium
2. Utwórz branch: `git checkout -b feature/amazing-feature`
3. Commituj zmiany: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Utwórz Pull Request

## 📝 Licencja

Ten projekt jest dostępny na licencji MIT. Zobacz plik `LICENSE` dla szczegółów.

## 📞 Kontakt

- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/your-profile)
- **GitHub**: [Your GitHub](https://github.com/your-username)

## 🙏 Podziękowania

- [Tailwind CSS](https://tailwindcss.com/) - Za wspaniały framework CSS
- [Flask](https://flask.palletsprojects.com/) - Za prosty i potężny framework
- [Font Awesome](https://fontawesome.com/) - Za ikony
- [AOS](https://michalsnik.github.io/aos/) - Za animacje
- [Unsplash](https://unsplash.com/) - Za zdjęcia (jeśli używane)

---

⭐ **Jeśli ten projekt Ci się podoba, zostaw gwiazdkę!** ⭐ 