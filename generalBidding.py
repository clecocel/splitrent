if __name__ == '__main__':
	rent = float(raw_input('Rent\n'))
	
	rooms = int(raw_input('Number of rooms\n'))
	
	priceRooms = []
	for i in xrange(rooms):
		priceRooms += [rent / rooms]
	
	while True:
		priceStr = 'Prices '
		for room in xrange(rooms):
			priceStr += 'Room' + str(room+1) + ' ' + str(round(priceRooms[room])) + ', '
		
		print priceStr
		
		bid = raw_input('Choose a room to bid on\n')
		try:
			bid = int(bid)
		except:
			bid = 0
		
		while (bid < 1) or (bid > rooms + 1):
			bid = int(raw_input('Invalid room number\n'))
			try:
				bid = int(bid)
			except:
				bid = 0
		
		priceRooms[bid-1] += 10
		
		for roomId in [i for i in xrange(rooms) if i+1 != (bid)]:
			priceRooms[roomId] -= 10 / (rooms - 1.0)
		
		print sum(priceRooms)