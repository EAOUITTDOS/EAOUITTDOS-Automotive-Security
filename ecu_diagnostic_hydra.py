class ECUDiagnosticHydra:
    def __init__(self):
        self.diagnostic_session = False

    def start_security_access(self, seed):
        """
        Simulates the Security Access handshake (Seed/Key) 
        required to unlock high-level ECU functions.
        """
        print(f"[*] ECU-HYDRA: Attempting Security Access with Seed: {seed}")
        # In a real car, you'd calculate a Key from this Seed
        key = hex(int(seed, 16) ^ 0xFAFO) 
        print(f"[+] Key Calculated: {key}")
        self.diagnostic_session = True
        print("[!] ACCESS GRANTED: ECU Unlocked for Read/Write.")
        return key

    def read_dtc_codes(self):
        """Reads Diagnostic Trouble Codes (the 'Check Engine' secrets)."""
        if self.diagnostic_session:
            print("[*] Querying ECU for DTC logs...")
            return ["P0300", "P0171"] # Mock codes
        return "ERROR: Access Denied"

if __name__ == "__main__":
    tuner = ECUDiagnosticHydra()
    tuner.start_security_access("0xABCD")
    print(f"  [>] Codes Found: {tuner.read_dtc_codes()}")
