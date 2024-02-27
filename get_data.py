import bluetooth

def get_data(device_address, port):
	try:
		client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM);
		client_socket.connect((device_address, port));

		print(f"Connected to {device_address} on port {port}");
	
		car_start = get_car_start(client_socket);
		door_lock = get_door_lock(client_socket);
		vehicle_speed = get_vehicle_speed(client_socket);

		print(f"Car Start : {car_start}");
		print(f"door_lock : {door_lock}");
		print(f"vehicle_speed : {vehicle_speed}");
		
		client_socket.close();

		return {"car_start" : car_start, "door_lock" : door_lock, "vehicle_speed" : vehicle_speed};

	except Exception as e:
		print(f"Error: {e}");

def get_car_start(socket):
	try:
		message = "010C" + chr(13) + chr(10);
		socket.send(message);
		data = socket.recv(1024);
		if(data[15] == 48):
			return False;
		else:
			return True;
	except Exception as e:
		print(f"Error: {e}");

def get_vehicle_speed(socket):
	try:
		message = "010D" + chr(13) + chr(10);
		socket.send(message);
		data = socket.recv(1024);
		return 16 * ascii_to_dec(data[11]) + ascii_to_dec(data[12]);
	except Exception as e:
		print(f"Error: {e}")

def get_door_lock(socket):
	try:
		message = "0110" + chr(13) + chr(10);
		socket.send(message);
		data = socket.recv(1024);
		if(data[15] == 48):
			return False;
		else:
			return True;
	except Exception as e:
		print(f"Error: {e}");

def ascii_to_dec(c):
	if(c >= 48 and c <= 57):
		return c - 48;
	elif(c >= 65 and c <= 70):
		return c - 55;
	else:
		return 0;

if __name__ == "__main__":
	device_address = input("Enter the Bluetooth device address: ");
	port = int(input("Enter the RFCOMM port: "));

	get_data(device_address, port);