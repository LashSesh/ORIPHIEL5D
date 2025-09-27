from fastapi import FastAPI
from app.models import SeedInjection, QueryRequest, MutationRequest
from app.spiral import create_segment
from app.resonance import query_resonance, mutate_segment
from app.storage import storage
import logging

logging.basicConfig(
    filename="logs/events.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = FastAPI(
    title="ORIPHIEL-5D",
    description="Resonance-based semantic spiral architecture API",
    version="1.0.0"
)

@app.post("/inject")
def inject_seed(payload: SeedInjection):
    segment = create_segment(payload)
    storage.add_segment(segment["id"], segment)
    logging.info(f"Injected segment {segment['id']}")
    return {"status": "ok", "segment": segment}

@app.get("/query")
def query_memory(payload: QueryRequest):
    results = query_resonance(payload, storage.get_all())
    logging.info(f"Query with psi={payload.psi_target}, results={len(results)}")
    return {"status": "ok", "results": results}

@app.post("/mutate")
def mutate(payload: MutationRequest):
    new_segment = mutate_segment(payload, storage)
    logging.info(f"Mutated segment {payload.origin_segment} -> {new_segment['id']}")
    return {"status": "ok", "new_segment": new_segment}
