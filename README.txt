enable wifi connection via bluetooth
steps:
- (a) sends msg to start exchange
- (b) sends ack
- (a) sends wireless connection info (ssid::password)
- (b) sends ack
- (b) sends connection attempt result
- (a) waits for msg to end bluetooth connection
- (b) sends msg to end bluetooth connection
- (a) and (b) close connection

