from sklearn.metrics import matthews_corrcoef
import data

endpoints_data = data.get_endpoints_data()

y_true = endpoints_data["linguistic"]["AmorphousURI"]
y_pred = endpoints_data["design"]["isMisusingCookies"]

result = matthews_corrcoef(y_true, y_pred)
print(result)
