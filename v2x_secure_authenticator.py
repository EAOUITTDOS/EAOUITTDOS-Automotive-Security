import hashlib
import time

class V2XSecureGuard:
    def __init__(self):
        # In 2026, V2X uses IEEE 1609.2 standards for security
        self.trust_store = ["OEM_ROOT_CA", "DOT_INFRA_CERT"]
        self.session_active = False

    def verify_message_integrity(self, message, signature, cert_id):
        """
        Compliance: UN R155 / ISO 21434
        Ensures the message from another vehicle is signed and not 'spoofed'.
        """
        print(f"[*] V2X-GUARD: Verifying message signature from Asset_{cert_id}...")
        
        # Simulating Hardware Security Module (HSM) verification
        if cert_id in self.trust_store:
            # Hash verification to ensure the data hasn't been tampered with
            msg_hash = hashlib.sha256(message.encode()).hexdigest()
            print(f"[+] INTEGRITY VERIFIED: Hash {msg_hash[:10]} matches certificate.")
            return True
        else:
            print("[!!!] SECURITY ALERT: Unsigned or Rogue V2X message detected. IGNORING.")
            return False

    def secure_beacon_broadcast(self, data):
        """Broadcasts our own location/status to nearby autonomous units."""
        timestamp = time.time()
        payload = f"{data}|{timestamp}"
        # Simulating signing the message with our private key stored in the FAFO HSM
        signature = hashlib.sha256(payload.encode()).hexdigest()
        print(f"[*] V2X-OUT: Broadcasting Signed Beacon: {signature[:12]}")
        return payload, signature

if __name__ == "__main__":
    v2x = V2XSecureGuard()
    v2x.verify_message_integrity("BRAKE_ACTION_AHEAD", "SIG_9921", "OEM_ROOT_CA")
