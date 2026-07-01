# Cadru software conversațional bazat pe arhitectura Retrieval-Augmented Generation (RAG) pentru analiza inteligentă a datelor

**Autor:** Nicoleta-Leontina BUTARU  
**Coordonatori:** Asist.drd.ing. Alexandru PESCARU, Conf.dr.ing. Dan PESCARU  
**Instituție:** Universitatea Politehnica Timișoara, Facultatea de Automatică și Calculatoare  
**Sesiune:** Iulie 2026  

---

## 1. Descrierea proiectului
Acest repository conține codul sursă integral al proiectului de licență, reprezentând un asistent virtual (chatbot) bazat pe arhitectura deterministic Retrieval-Augmented Generation (RAG). Aplicația procesează seturi de date tabulare (CSV), efectuează calcule statistice in-memory și generează răspunsuri în limbaj natural acompaniate de grafice dinamice.

**Adresa Repository-ului:** https://github.com/nicoletabutaru/Proiect-Licenta

> **Notă privind accesul:** Repository-ul este configurat ca fiind *Public*. Repository-ul nu conține fișiere binare compilate, baza de date tranzacțională (aceasta se auto-generează) sau folderul mediului virtual (`venv`).

---

## 2. Structura Codului Sursă
Proiectul respectă o arhitectură modulară, separând logica de business de interfața grafică și de stratul de date:

* `app.py` - Orchestratorul principal (Controller) scris în Flask care expune endpoint-urile HTTP.
* `core/` - Directorul cu logica de business:
    * `data_loader.py` - Ingestia și pre-procesarea setului de date Pandas.
    * `dynamic_analysis.py` - Motorul NLP condus de configurare (Regex).
    * `retriever.py` - Gestionarea modelului neural Sentence-BERT.
    * `visualizer.py` - Randarea in-memory a graficelor cu Matplotlib.
    * `history_manager.py` - Jurnalizarea interacțiunilor în baza de date SQLite.
* `config/` - Conține `settings.json`, dicționarul generalizabil care dictează intențiile, filtrele și răspunsurile sistemului expert.
* `data/` - Directorul destinat fișierelor statice (ex: `appointments.csv`).
* `templates/` - Conține componenta de frontend (fișierul `index.html` care gestionează interfața web asincronă).
* `requirements.txt` - Lista tuturor dependențelor software necesare pentru rularea aplicației.

---

## 3. Cerințe preliminare (Prerequisites)

Pentru a rula și compila acest proiect, mediul gazdă trebuie să dispună de:
* **Python:** Versiunea 3.10 sau superioară.
* **Sistem de operare:** Linux (Ubuntu 22.04 LTS recomandat), macOS sau Windows (preferabil prin WSL2).
* **Memorie RAM:** Minim 4 GB (pentru încărcarea rapidă a modelului Sentence-BERT și procesarea Pandas).

---

## 4. Pași de instalare și lansare a aplicației

Aplicația este dezvoltată în Python, prin urmare "compilarea" constă în instanțierea mediului virtual și descărcarea pachetelor necesare. Deschideți un terminal și executați următorii pași:

**Pasul 1: Clonarea repository-ului**
git clone [https://github.com/nicoletabutaru/Proiect-Licenta.git](https://github.com/nicoletabutaru/Proiect-Licenta.git)
cd Proiect-Licenta

**Pasul 2: Crearea mediului virtual izolat (venv)**
# Pe Windows
python -m venv venv

# Pe Linux / WSL / macOS
python3 -m venv venv

**Pasul 3: Activarea mediului virtual**
# Pe Windows
venv\Scripts\activate

# Pe Linux / WSL / macOS
source venv/bin/activate

**Pasul 4: Instalarea dependențelor (Stiva Tehnologică)**
pip install --upgrade pip
pip install -r requirements.txt

**Pasul 5: Rularea aplicație**
# Pe Windows
python app.py

# Pe Linux / WSL / macOS
python3 app.py
