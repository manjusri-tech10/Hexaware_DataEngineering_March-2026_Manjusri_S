use supply_chain

db.createCollection("shipment_logs")

db.shipment_logs.insertMany([
{
    shipment_id: 101,
    order_id: 1,
    supplier: "ABC Supplies",
    status: "Delivered",
    location: "Chennai",
    timestamp: new Date()
},
{
    shipment_id: 102,
    order_id: 2,
    supplier: "Global Traders",
    status: "In Transit",
    location: "Bangalore",
    timestamp: new Date()
},
{
    shipment_id: 103,
    order_id: 3,
    supplier: "Fast Logistics",
    status: "Delayed",
    location: "Mumbai",
    timestamp: new Date()
}
])

db.shipment_logs.find()

db.shipment_logs.find({status:"Delayed"})

db.shipment_logs.createIndex({order_id:1})

db.shipment_logs.getIndexes()