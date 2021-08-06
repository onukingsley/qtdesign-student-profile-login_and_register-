import sys, json
from requests import request
from PyQt5.QtWidgets import QDialog, QApplication, QStyleFactory
from PyQt5.uic import loadUi


class Currency(QDialog):
    def __init__(self):
        super(Currency, self).__init__()
        loadUi('ui/currency.ui', self)
        self.setWindowTitle('My Currency Checker')
        try:
            self.api()
        except Exception as err:
            print(err)

        self.show()

    def api(self):
        base_url = "https://freecurrencyapi.net/api/v1/rates?base_currency=CAD"
        my_headers = {
            'accept': 'application/json',
            'content-type': 'application/json',
            'api-key': "3c887720-e93a-11eb-a2d1-03f25e5d63b5"
        }

        response = request("GET", base_url, headers=my_headers)
        content = json.loads(response.content)
        # countries = content['data']
        current_date = ''
        for date in content['data'].keys():
            current_date = date
        countries = content['data'][current_date].keys()

        for country in countries:
            self.cmbCountryBase.addItem(country)
            self.cmbCountryExc.addItem(country)

app = QApplication(sys.argv)
nnamdi = Currency()
print(QStyleFactory.keys())
app.setStyle('Fusion')
sys.exit(app.exec_())
