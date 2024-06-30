import requests

API_KEY =''
BASE_URL =f" {API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def conver_currency(base):
  currencies = ",".join(CURRENCIES)
  url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
  try:
    response = requests.get(url);
    data = response.json();
    return data["data"]
  except :
    print("Invalid currency.")
    return None
  
while True:
  base = input("enter the base currency (q for quit): ").upper()

  if base == "Q":
    break

  data = conver_currency(base)
  if not data:
    continue;
  del data[base]
  for ticker, value in data.items():
    print(f"{ticker}: {value}")
