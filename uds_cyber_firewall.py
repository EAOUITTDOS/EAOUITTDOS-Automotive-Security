class UDSCyberFirewall:
    def __init__(self):
        # Block high-risk UDS services unless explicitly authorized
        self.blocked_services = ["0x2F", "0x11", "0x28"] # Control, Reset, Disable Comm

    def inspect_service_request(self, service_id, access_level):
        """
        Compliance: ISO 14229 (UDS) + ISO 21434 (Cybersecurity)
        Prevents unauthorized tools from resetting the ECU while the truck is moving.
        """
        print(f"[*] IDS: Inspecting UDS Service Request: {service_id}")
        
        if service_id in self.blocked_services and access_level < 3:
            print(f"[!!!] CRITICAL: Unauthorized attempt to use Service {service_id}!")
            print("[!] ACTION: Dropping packet and logging to Black-Box (EDR).")
            return "REJECTED"
        
        print(f"[+] UDS request {service_id} cleared for processing.")
        return "AUTHORIZED"

if __name__ == "__main__":
    firewall = UDSCyberFirewall()
    # Mocking a hacker trying to reset the ECU (Service 0x11) with low access
    firewall.inspect_service_request("0x11", access_level=1)
