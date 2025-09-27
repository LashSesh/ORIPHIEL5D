import numpy as np
import uuid


def encode_token(token):
    return np.random.rand(5)  # Token → 5D-Vektor


def create_segment(payload):
    coords = np.mean([encode_token(t) for t in payload.token_sequence], axis=0)
    psi = float(coords[3])
    omega = float(coords[4])
    segment_id = f"S{uuid.uuid4().hex[:6]}"
    return {
        "id": segment_id,
        "coordinates": coords.tolist(),
        "psi": psi,
        "omega": omega,
        "timestamp": payload.timestamp,
        "tokens": payload.token_sequence,
        "cluster": "MetaMemory_A"
    }
