class Role:
    GENESIS_ANCHOR = "anchor"
    VALIDATOR = "validator"
    CLUSTER = "cluster"


class Security:
    def __init__(self):
        self.permissions = {}

    def assign_role(self, segment_id, role):
        self.permissions[segment_id] = role

    def can_read(self, psi_diff, tau_r=0.1):
        return psi_diff < tau_r

    def can_write(self, segment_id):
        return self.permissions.get(segment_id) in [Role.VALIDATOR, Role.GENESIS_ANCHOR]

    def can_revoke(self, votes):
        return votes >= 3


security = Security()
