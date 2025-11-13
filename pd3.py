import requests
 requests.get('https://68c9628cceef5a150f64a0b6.mockapi.io/restaurante')
curl -X POST https://68c9628cceef5a150f64a0b6.mockapi.io/restaurante \
  -H "Content-Type: application/json" \
  -d {
    "nome": "Feijoada Tradicional",
    "bebida": "Água Mineral",
    "mesa": 3
  }
