import subprocess

def pairing(device_address, pin_code):
	try:
		command = f"echo -e 'pair {device_address} {pin_code}\n' | bluetoothctl";
		subprocess.run(command, shell=True, check=True);

		print("Pairing successful.");

	except subprocess.CalledProcessError as e:
		print(f"Error during pairing: {e}");

if __name__ == "__main__":
	device_address = input("Enter the Bluetooth device address: ");
	pin_code = input("Enter the PIN code: ");

	pairing(device_address, pin_code);