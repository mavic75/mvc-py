# mvc-py
 
# URL DEPLOY



# URL PROYECTO

# 


 # CURL

 # $curl --location --request GET 'http://localhost:8000/usuarios'
 
 # curl --location --request POST 'http://localhost:8000/usuarios' \
# --form 'user_nombre="Nora Sanchez"' \
# --form 'user_edad="43"'

# curl --location --request PUT 'http://localhost:8000/usuarios/edit/2' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "user_nombre": "Paola Castro Marquez",
#     "user_edad": "28"
# }'

# curl --location --request DELETE 'http://localhost:8000/usuarios/delete/6'

# curl --location --request GET 'http://localhost:8000/usuarios/promedio-edad'

# curl --location --request GET 'http://localhost:8000/status'