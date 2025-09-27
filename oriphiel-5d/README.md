# ORIPHIEL-5D – Full Open Source Implementation

Dieses Repository implementiert eine prototypische ORIPHIEL-5D Architektur inklusive FastAPI-Backend, Spiral-Speicher und Resonanzlogik. Die Struktur entspricht der angeforderten Open-Source-Referenz und ermöglicht einen schnellen Einstieg in Experimente mit der Spiral-Semantik.

## Projektstruktur

```
oriphiel-5d/
├── app/
│   ├── init.py
│   ├── main.py
│   ├── models.py
│   ├── spiral.py
│   ├── resonance.py
│   ├── storage.py
│   ├── security.py
│   └── visualize.py
├── logs/
│   └── events.log
├── tests/
│   └── test_api.py
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation & Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest
```

## Docker

```bash
docker build -t oriphiel-5d .
docker run -p 8000:8000 oriphiel-5d
```
