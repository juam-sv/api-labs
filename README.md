export TOKEN=$(curl -X POST -H "Content-Type: application/json" -d '{"username":"john", "password":"password1"}' http://localhost:5000/login | jq -r '.token')

curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/health
