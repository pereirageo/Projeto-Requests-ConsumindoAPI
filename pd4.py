import requests
 requests.get('https://68c9628cceef5a150f64a0b6.mockapi.io/restaurante')
curl -X POST https://68c9628cceef5a150f64a0b6.mockapi.io/restaurante \
  -H "Content-Type: application/json" \
  -d {
    "nome": "Pizza Margherita",
    "bebida": "Coca-Cola",
    "mesa": 4
  }
