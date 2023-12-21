# littlelemon

Endpoints:

 - list menu items: GET http://localhost:8000/menu
 - view menu item: GET http://localhost:8000/menu/1 (1 = pk)
 - login / get token: POST http://localhost:8000/auth/token/login
 - list reservations / bookings (secured - should be logged in, auth: bearer): GET http://localhost:8000/bookings
 - create a new reservation / booking (secured - should be logged in, auth: bearer): POST http://localhost:8000/bookings


Register new user (via browser):
http://127.0.0.1:8000/auth/users/


NOTE: If you're using Insomnia to test REST APIs you can import the file "Insomnia_endpoints_config.json" to save time in setting up all the endpoints.