use("online_store_db");

//Customers Collection
db.customers.insertMany([
  { customer_id: 1, name: "Aarav",  city: "Hyderabad", membership: "Gold",   age: 24 },
  { customer_id: 2, name: "Priya",  city: "Bangalore",  membership: "Silver", age: 28 },
  { customer_id: 3, name: "Rahul",  city: "Mumbai",     membership: "Gold",   age: 32 },
  { customer_id: 4, name: "Sneha",  city: "Delhi",      membership: "Silver", age: 26 },
  { customer_id: 5, name: "Kiran",  city: "Hyderabad",  membership: "Gold",   age: 30 },
  { customer_id: 6, name: "Meera",  city: "Chennai",    membership: "Bronze", age: 27 }
]);

//Products Collection
db.products.insertMany([
  { product_id: 101, name: "Laptop",  category: "Electronics", price: 75000, stock: 10 },
  { product_id: 102, name: "Phone",   category: "Electronics", price: 50000, stock: 15 },
  { product_id: 103, name: "Desk",    category: "Furniture",   price: 15000, stock: 8  },
  { product_id: 104, name: "Chair",   category: "Furniture",   price: 7000,  stock: 20 },
  { product_id: 105, name: "Tablet",  category: "Electronics", price: 30000, stock: 12 },
  { product_id: 106, name: "Printer", category: "Electronics", price: 12000, stock: 5  }
]);

//Orders Collection
db.orders.insertMany([
  { order_id: 1001, customer_id: 1, product_id: 101, quantity: 1, order_date: "2026-03-01", status: "Delivered"  },
  { order_id: 1002, customer_id: 2, product_id: 102, quantity: 2, order_date: "2026-03-02", status: "Delivered"  },
  { order_id: 1003, customer_id: 1, product_id: 105, quantity: 1, order_date: "2026-03-03", status: "Pending"    },
  { order_id: 1004, customer_id: 3, product_id: 103, quantity: 1, order_date: "2026-03-05", status: "Delivered"  },
  { order_id: 1005, customer_id: 5, product_id: 102, quantity: 3, order_date: "2026-03-07", status: "Cancelled"  },
  { order_id: 1006, customer_id: 6, product_id: 104, quantity: 4, order_date: "2026-03-08", status: "Delivered"  },
  { order_id: 1007, customer_id: 4, product_id: 106, quantity: 2, order_date: "2026-03-09", status: "Pending"    },
  { order_id: 1008, customer_id: 3, product_id: 101, quantity: 1, order_date: "2026-03-10", status: "Delivered"  }
]);

// 1
db.customers.find();

// 2
db.products.find();

// 3
db.orders.find();

// 4
db.customers.find({ city: "Hyderabad" });

// 5
db.products.find({ category: "Electronics" });

// 6
db.orders.find({ status: "Delivered" });

// 7
db.products.find({ price: { $gt: 30000 } });

// 8
db.products.find({ price: { $gte: 10000, $lte: 50000 } });

// 9
db.customers.find({ age: { $gt: 26 } });

// 10
db.orders.find({ quantity: { $gt: 1 } });

// 11
db.products.find({ stock: { $lte: 10 } });

// 12
db.orders.find({ status: { $ne: "Cancelled" } });

// 13
db.customers.find({ city: { $in: ["Hyderabad", "Mumbai"] } });

// 14
db.customers.find({}, { _id: 0, name: 1, city: 1 });

// 15
db.products.find({}, { _id: 0, name: 1, category: 1, price: 1 });

// 16
db.orders.find({}, { _id: 0, order_id: 1, quantity: 1, status: 1 });

// 17
db.products.find().sort({ price: 1 });

// 18
db.products.find().sort({ price: -1 });

// 19
db.products.find().sort({ price: -1 }).limit(3);

// 20
db.products.find().sort({ price: 1 }).limit(2);

// 21
db.products.find().skip(2);

// 22
db.customers.find().sort({ age: -1 });

// 23
db.products.updateOne(
  { name: "Laptop" },
  { $set: { price: 78000 } }
);

// 24
db.products.updateMany(
  { category: "Electronics" },
  { $set: { discount: 10 } }
);

// 25
db.orders.updateMany(
  { status: "Pending" },
  { $set: { priority: "High" } }
);

// 26
db.customers.updateOne(
  { name: "Meera" },
  { $set: { membership: "Silver" } }
);

// 27
db.products.deleteOne({ name: "Printer" });

// 28
db.products.deleteMany({ category: "Furniture" });

// 29
db.orders.deleteMany({ status: "Cancelled" });

// 30
db.customers.countDocuments();

// 31
db.products.countDocuments({ category: "Electronics" });

// 32
db.orders.countDocuments({ status: "Delivered" });

// 33
db.customers.countDocuments({ city: "Hyderabad" });

// 34
db.products.aggregate([
  { $group: { _id: "$category", totalStock: { $sum: "$stock" } } }
]);

// 35
db.products.aggregate([
  { $group: { _id: "$category", avgPrice: { $avg: "$price" } } }
]);

// 36
db.products.aggregate([
  { $group: { _id: null, maxPrice: { $max: "$price" } } }
]);

// 37
db.products.aggregate([
  { $group: { _id: null, minPrice: { $min: "$price" } } }
]);

// 38
db.products.aggregate([
  {
    $group: {
      _id: null,
      totalInventoryValue: { $sum: { $multiply: ["$price", "$stock"] } }
    }
  }
]);

// 39
db.orders.aggregate([
  { $group: { _id: "$product_id", totalQuantity: { $sum: "$quantity" } } }
]);

// 40
db.orders.aggregate([
  { $group: { _id: "$customer_id", totalQuantity: { $sum: "$quantity" } } }
]);

// 41
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customerDetails"
    }
  }
]);

// 42
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "productDetails"
    }
  }
]);

// 43
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer"
    }
  },
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "product"
    }
  },
  {
    $project: {
      _id: 0,
      customerName: { $arrayElemAt: ["$customer.name", 0] },
      productName:  { $arrayElemAt: ["$product.name",  0] }
    }
  }
]);

// 44
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer"
    }
  },
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "product_id",
      as: "product"
    }
  },
  {
    $project: {
      _id: 0,
      customerName: { $arrayElemAt: ["$customer.name", 0] },
      city:         { $arrayElemAt: ["$customer.city", 0] },
      productName:  { $arrayElemAt: ["$product.name",  0] },
      quantity:     1,
      status:       1
    }
  }
]);
