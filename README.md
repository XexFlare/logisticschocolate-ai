# LogisticsForce AI Demo

**LogisticsForce AI** is a demo logistics analytics assistant that combines SQL-based analytics with retrieval-style knowledge lookup over logistics documentation.

This repository is designed as a portfolio-friendly demonstration of a system originally described as:

> Built an AI-driven logistics analytics assistant over 80,000+ truck records, enabling real-time queries on shipments, routes, volumes, and revenue performance; combines SQL-based analytics with RAG-powered knowledge retrieval for fast, accurate insights.

## What this demo shows

- Real-time logistics KPI queries over truck movement records
- Shipment, route, volume, and revenue analytics
- SQL-powered operational reporting
- RAG-style retrieval from logistics knowledge documents
- A Streamlit interface suitable for screenshots, demos, and interviews

## Demo data

The repo includes a synthetic dataset generator. It creates fake logistics records with fields such as:

- shipment date
- truck ID
- route
- origin and destination
- cargo type
- tonnage
- delivery status
- revenue
- delay hours

No real company, customer, shipment, or financial data is included.

## Project structure

```text
logisticsforce-ai-demo/
├── app/
│   ├── streamlit_app.py
│   ├── analytics.py
│   └── rag_search.py
├── data/
│   └── generate_sample_data.py
├── docs/
│   ├── logistics_kpi_guide.md
│   └── route_operations_notes.md
├── sql/
│   └── sample_queries.sql
├── requirements.txt
├── .gitignore
└── README.md
```

## Quick start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-USERNAME/logisticsforce-ai-demo.git
cd logisticsforce-ai-demo

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate demo data
python data/generate_sample_data.py

# 5. Run the app
streamlit run app/streamlit_app.py
```

## Example questions to try

- What is the total revenue by route?
- Which routes have the highest average delays?
- Show monthly tonnage trends.
- Which cargo types generate the most revenue?
- What does the KPI guide say about route performance?
- How should delayed shipments be interpreted?

## Screenshots to add later

After running the app, add screenshots under `/assets` and update this section.

## Disclaimer

This is a public demo using synthetic data. It is intended for portfolio, interview, and GitHub demonstration purposes only.
