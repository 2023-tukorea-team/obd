import bluetooth

def scan_devices():
	devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=True);
	print("Nearby devices:");
	for addr, name, _ in devices:
		print(f"Device Name: {name}, Address: {addr}");
	return devices;
if __name__ == "__main__":
	scan_devices();