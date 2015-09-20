import requests
import time
import json
from firebase import firebase

firebase = firebase.FirebaseApplication('https://ghosttoast.firebaseio.com', None)

idle = {
	'time': 0,
	'type': 'none',
	'status': 'Idling',
	'request': 'none'}
toast = {
	'time': 80,
	'type': 'toast',
	'status': 'Toasting',
	'request': 'none'}
light_toast = {
	'time': 65,
	'type': 'light_toast',
	'status': 'Lightly toasting',
	'request': 'none'}
while True:
	r = requests.get("https://ghosttoast.firebaseio.com/toasters/alpha.json");
	returned = json.loads(r.content);
	if returned['status'] == 'Toasting':
		print "TOASSTTTTTT"
		firebase.put('/toasters', 'alpha', idle);
		time.sleep(5)
	elif returned['status'] == 'Lightly Toasting':
		print "LIGHT TOASTTTTTT"
		firebase.put('/toasters', 'alpha', idle)
		time.sleep(5)
	else:
		time.sleep(2)