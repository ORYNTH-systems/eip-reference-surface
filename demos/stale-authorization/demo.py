import time
import hashlib
import json


def generate_digest(state):
    serialized = json.dumps(state, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()


print("\n=== EIP STALE AUTHORIZATION DEMO ===\n")

# STEP 1 — Initial authorization snapshot
authorized_state = {
    "user": "agent-42",
    "role": "admin",
    "action": "delete.customer.record"
}

authorized_digest = generate_digest(authorized_state)

print("[AUTHORIZED]")
print(f"Authorized State: {authorized_state}")
print(f"Continuity Digest: {authorized_digest}\n")

# STEP 2 — Simulate execution delay
print("[EXECUTION DELAY]")
time.sleep(3)

# STEP 3 — State changes during delay
current_state = {
    "user": "agent-42",
    "role": "viewer",
    "action": "delete.customer.record"
}

current_digest = generate_digest(current_state)

print("[STATE CHANGED]")
print(f"Current State: {current_state}")
print(f"Current Digest: {current_digest}\n")

# STEP 4 — Continuity verification
print("[CONTINUITY VERIFICATION]")

if current_digest != authorized_digest:
    print("\n[CONTINUITY FAILURE DETECTED]")
    print("[EXECUTION BLOCKED]")
    print("[PROOF-OF-BLOCK GENERATED]\n")

else:
    print("\n[CONTINUITY VERIFIED]")
    print("[EXECUTION AUTHORIZED]\n")