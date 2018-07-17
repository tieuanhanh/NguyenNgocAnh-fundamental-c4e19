from pymongo import MongoClient
import matplotlib

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

customers = db['customers']

sort_customers_by_events = db.customers.count( { 'ref': 'events' } )
sort_customers_by_ads = db.customers.count( { 'ref': 'ads' } )
sort_customers_by_wom = db.customers.count( { 'ref': 'wom' } )

print ("The number of customers by ads, events, word of mkt are: {0}, {1}, {2} respectively.".format ( sort_customers_by_ads, sort_customers_by_events, sort_customers_by_wom))

matplotlib.use("TkAgg")
from matplotlib import pyplot

labels = ['ads', 'events', 'wom']
values = [sort_customers_by_ads, sort_customers_by_events, sort_customers_by_wom]
colors = ['green', 'red', 'blue']

pyplot.pie(values, labels = labels, colors = colors, autopct = '%.2f')
pyplot.axis('equal')

pyplot.show()