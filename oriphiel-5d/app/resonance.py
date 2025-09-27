import numpy as np
import uuid


def resonance_score(segment, psi_target, omega_phase):
    psi_diff = abs(segment["psi"] - psi_target)
    omega_diff = abs(segment["omega"] - omega_phase)
    return np.exp(-(psi_diff**2 + omega_diff**2))


def query_resonance(payload, all_segments):
    results = []
    for seg_id, seg in all_segments.items():
        score = resonance_score(seg, payload.psi_target, payload.omega_phase)
        if score > payload.threshold:
            results.append({"id": seg_id, "score": score, "data": seg})
    return sorted(results, key=lambda x: -x["score"])


def mutate_segment(payload, storage):
    origin = storage.segments[payload.origin_segment]
    coords = np.array(origin["coordinates"]) + np.array(payload.mutation_vector)
    psi = float(coords[3])
    omega = float(coords[4])
    seg_id = f"S{uuid.uuid4().hex[:6]}"
    new_seg = {
        "id": seg_id,
        "coordinates": coords.tolist(),
        "psi": psi,
        "omega": omega,
        "timestamp": origin["timestamp"],
        "tokens": origin["tokens"],
        "cluster": origin["cluster"],
        "mutation_reason": payload.reason
    }
    storage.add_segment(seg_id, new_seg)
    return new_seg
