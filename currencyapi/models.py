from django.db import models
import requests
class Country(models.Model):
    name = models.CharField(max_length=100)
    currencies = models.CharField(max_length=100)

    @classmethod
    def fetch_countries_data(cls):
        response = requests.get("https://restcountries.com/v3.1/all")
        countries_data = response.json()
        for country in countries_data:
            if "currencies" in country:
                Country.objects.create(name=country["name"]["common"], currencies=next(iter(country["currencies"].values()))["name"])


# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     currencies = models.CharField(max_length=100)

#     @classmethod
#     def fetch_countries_data(cls):
#         response = requests.get("https://restcountries.com/v3.1/all")
#         countries_data = response.json()
#         for country_data in countries_data:
#             name = country_data['name']['common']

#             # Handling currencies data
#             currencies_data = country_data.get('currencies', [])
#             currencies = ', '.join(currency.get('name', '') for currency in currencies_data)

#             Country.objects.create(name=name, currencies=currencies)
