import random
import custom_base64



for _ in range(10):
	dt=bytes([random.randint(0,255) for _ in range(random.randint(10,10000))])
	print(dt)
	e_dt=custom_base64.encode(dt)
	print(e_dt)
	d_dt=custom_base64.decode(e_dt)
	print(d_dt)
	if (d_dt!=dt):
		raise RuntimeError
