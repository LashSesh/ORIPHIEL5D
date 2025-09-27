from pydantic import BaseModel
from typing import List


class SeedInjection(BaseModel):
    token_sequence: List[str]
    embedding_space: str = "R5"
    timestamp: float


class QueryRequest(BaseModel):
    psi_target: float
    omega_phase: float
    spatial_radius: float
    threshold: float


class MutationRequest(BaseModel):
    origin_segment: str
    mutation_vector: List[float]
    reason: str
