# Cadru software conversațional bazat pe arhitectura Retrieval-Augmented Generation (RAG) pentru analiza inteligentă a datelor

**Autor:** Nicoleta-Leontina BUTARU
**Coordonatori:** Asist.drd.ing. Alexandru PESCARU, Conf.dr.ing. Dan PESCARU
**Instituție:** Universitatea Politehnica Timișoara, Facultatea de Automatică și Calculatoare
**Sesiune:** Iulie 2026

---

## Cuprins

1. [Descrierea proiectului](#1-descrierea-proiectului)
2. [Adresa repository-ului](#2-adresa-repository-ului)
3. [Structura codului sursă](#3-structura-codului-sursă)
4. [Cerințe preliminare](#4-cerințe-preliminare)
5. [Pașii de compilare a aplicației](#5-pașii-de-compilare-a-aplicației)
6. [Pașii de instalare și lansare a aplicației](#6-pașii-de-instalare-și-lansare-a-aplicației)
7. [Note privind livrabilul (fișiere binare / date generate)](#7-note-privind-livrabilul-fișiere-binare--date-generate)

---

## 1. Descrierea proiectului

Acest repository conține codul sursă integral al proiectului de licență, reprezentând un asistent virtual (chatbot) bazat pe arhitectura Retrieval-Augmented Generation (RAG). Aplicația procesează seturi de date tabulare (CSV), efectuează calcule statistice in-memory și generează răspunsuri în limbaj natural, însoțite de grafice generate dinamic.

Stiva tehnologică principală:
- **Backend:** Python 3, Flask
- **Procesare date:** Pandas
- **Model neural pentru regăsire semantică:** Sentence-BERT
- **Vizualizare:** Matplotlib
- **Persistență istoric conversații:** SQLite
- **Frontend:** HTML + JavaScript (interfață web asincronă)

## 2. Adresa repository-ului

Codul sursă al proiectului este găzduit public pe GitHub (nu a fost folosit gitlab.upt.ro pentru acest proiect):

**Repository:** https://github.com/nicoletabutaru/Proiect-Licenta

```
git clone https://github.com/nicoletabutaru/Proiect-Licenta.git
```

## 3. Structura codului sursă

Proiectul respectă o arhitectură modulară, separând logica de business de interfața grafică și de stratul de date:

```
Proiect-Licenta/
├── app.py                     # Orchestratorul principal (Controller, Flask) - expune endpoint-urile HTTP
├── core/                      # Logica de business
│   ├── data_loader.py         # Ingestia și pre-procesarea setului de date (Pandas)
│   ├── dynamic_analysis.py    # Motorul NLP condus de configurare (Regex)
│   ├── retriever.py           # Gestionarea modelului neural Sentence-BERT
│   ├── visualizer.py          # Randarea in-memory a graficelor (Matplotlib)
│   └── history_manager.py     # Jurnalizarea interacțiunilor (SQLite)
├── config/
│   └── settings.json          # Dicționarul care dictează intențiile, filtrele și răspunsurile
├── data/                      # Fișiere statice de date (ex: appointments.csv)
├── templates/
│   └── index.html             # Interfața web (frontend)
├── requirements.txt           # Dependențele software necesare
└── .gitignore
```

## 4. Cerințe preliminare

Pentru a compila și rula acest proiect, mediul gazdă trebuie să dispună de:

- **Python:** versiunea 3.10 sau superioară
- **Sistem de operare:** Linux (Ubuntu 22.04 LTS recomandat), macOS sau Windows (preferabil prin WSL2)
- **Memorie RAM:** minim 4 GB (pentru încărcarea modelului Sentence-BERT și procesarea cu Pandas)
- **Conexiune la internet** (la prima rulare, pentru descărcarea modelului Sentence-BERT și a dependențelor)

## 5. Pașii de compilare a aplicației

Fiind o aplicație Python, nu există o etapă de compilare într-un binar executabil; "compilarea" constă în crearea unui mediu virtual izolat și instalarea dependențelor declarate în `requirements.txt`. Pașii sunt detaliați mai jos, la secțiunea de instalare (pașii 2–4), deoarece instalarea dependențelor reprezintă echivalentul etapei de compilare pentru acest tip de proiect.

## 6. Pașii de instalare și lansare a aplicației

**Pasul 1 — Clonarea repository-ului**
```bash
git clone https://github.com/nicoletabutaru/Proiect-Licenta.git
cd Proiect-Licenta
```

**Pasul 2 — Crearea mediului virtual izolat (venv)**

Pe Windows:
```bash
python -m venv venv
```
Pe Linux / WSL / macOS:
```bash
python3 -m venv venv
```

**Pasul 3 — Activarea mediului virtual**

Pe Windows:
```bash
venv\Scripts\activate
```
Pe Linux / WSL / macOS:
```bash
source venv/bin/activate
```

**Pasul 4 — Instalarea dependențelor**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Pasul 5 — Lansarea aplicației**

Pe Windows:
```bash
python app.py
```
Pe Linux / WSL / macOS:
```bash
python3 app.py
```

După lansare, aplicația va fi disponibilă local (implicit la adresa afișată în consolă, de regulă `http://127.0.0.1:5000`). Deschideți acea adresă într-un browser web pentru a accesa interfața de chat.

## 7. Note privind livrabilul (fișiere binare / date generate)

- Repository-ul este **public** și conține **întregul cod sursă** al aplicației.
- Nu sunt incluse fișiere binare compilate.
- Baza de date tranzacțională (SQLite, folosită pentru istoricul conversațiilor) **nu este inclusă** în repository — aceasta se generează automat la prima rulare a aplicației.
- Folderul mediului virtual (`venv/`) **nu este inclus** în repository; acesta trebuie creat local, conform pașilor de mai sus.
