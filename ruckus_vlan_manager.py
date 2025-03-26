#!/usr/bin/env python3
import paramiko

class RuckusVlanManager:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        """Establish SSH connection to the Ruckus switch."""
        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            print(f"Connected to {self.hostname}")
        except Exception as e:
            print(f"Connection failed: {e}")
    
    def execute_command(self, command):
        """Execute a CLI command on the switch."""
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if error:
                print(f"Error: {error}")
            return output
        except Exception as e:
            print(f"Command execution failed: {e}")
    
    def create_vlan(self, vlan_id, vlan_name):
        """Create a VLAN with the given ID and name."""
        command = f"config\nvlan {vlan_id} name {vlan_name}\nexit"
        print(f"Creating VLAN {vlan_id} - {vlan_name}")
        return self.execute_command(command)
    
    def delete_vlan(self, vlan_id):
        """Delete a VLAN by ID."""
        command = f"config\nno vlan {vlan_id}\nexit"
        print(f"Deleting VLAN {vlan_id}")
        return self.execute_command(command)

    def close_connection(self):
        """Close the SSH connection."""
        self.ssh_client.close()
        print("Connection closed.")

if __name__ == "__main__":
    # Example usage (Update credentials)
    hostname = "192.168.1.1"
    username = "admin"
    password = "password"

    manager = RuckusVlanManager(hostname, username, password)
    manager.connect()
    print(manager.create_vlan(100, "Guest_Network"))
    print(manager.delete_vlan(100))
    manager.close_connection()
