
# Import libraries
import json
import requests
import time # Used to regulate poll frequency
import yeelight as ye

poll_interval = 5 # seconds

def get_btc_price():
    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
  
    # requesting data from url
    data = requests.get(key)  
    data = data.json()
    #print(f"{data['symbol']} price is {data['price']}")
    return float(data['price'])

def poll_for_price_change():
    # Get initial BTC price
    current_price = get_btc_price()
    time.sleep(poll_interval)

    while True:
        last_price = current_price
        current_price = get_btc_price()

        if current_price > last_price: # price increase
            difference = round(current_price - last_price, 2)
            print(f"BTC increased by ${difference} USD")
            return "increasing"
            
        elif current_price < last_price: # price decrease
            difference = round(last_price - current_price, 2)
            print(f"BTC decreased by ${difference} USD")
            return "decreasing"
        else: # No change, so keep wait then keep polling
            time.sleep(poll_interval)

    
def main():

    print("Starting bitcoin_light!")

    # Initialize YeeLight
    bulb = ye.Bulb(ip="192.168.1.24")
    bulb.turn_on()
    bulb.set_rgb(0, 0, 255)  # Unknown BTC increase/decrease so light begins in blue state
    bulb.set_brightness(100)

    while True: # Loop forever
        price_state = poll_for_price_change() # Blocking call
        if price_state == "increasing":
            bulb.set_rgb(0, 255, 0)
        elif price_state == "decreasing":
            bulb.set_rgb(255, 0, 0)
        else:
            print("Error while polling BTC price")


if __name__ == "__main__":
    main()