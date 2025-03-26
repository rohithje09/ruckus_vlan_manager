# Ruckus VLAN Manager  

A Python script to manage VLANs on Ruckus switches via SSH.  

## 📌 Features  
- Connect to a Ruckus switch via SSH  
- Create and delete VLANs using CLI commands  
- Automate VLAN management for network admins  

## 📦 Installation  
Ensure you have Python  installed, then install dependencies:  

```bash
pip install -r requirements.txt
```

## 🚀 Usage  
1. Edit `ruckus_vlan_manager.py` and update:  
   - `hostname` (Switch IP)  
   - `username` (Admin username)  
   - `password` (Admin password)  

2. Run the script:  
```bash
python ruckus_vlan_manager.py
```

## 🔧 Example  
```python
manager.create_vlan(100, "Guest_Network")
manager.delete_vlan(100)
```

## 🛠️ Dependencies  
- `paramiko` (for SSH communication)  

## ⚠️ Notes  
- Ensure SSH is enabled on your Ruckus switch.  
- Use secure methods (e.g., environment variables) to store credentials.  
