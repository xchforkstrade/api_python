from xchforks import xchforksConnector as Connector
import json
key = ''  # key
secret = ''  # secret key
connector = Connector(key, secret, trading_allowed=True)

# Show open orders
open_orders = json.loads(connector.get_your_orders())
print(open_orders)

