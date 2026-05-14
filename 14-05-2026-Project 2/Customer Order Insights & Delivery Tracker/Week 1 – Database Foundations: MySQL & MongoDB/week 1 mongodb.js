use order_insights;
db.customer_feedback.insertMany([
  {
    customer_id: 1,
    name: "Alice Johnson",
    order_id: 101,
    feedback: "Package arrived very late, poor packaging.",
    rating: 2,
    date: new Date("2024-01-13")
  },
  {
    customer_id: 2,
    name: "Bob Smith",
    order_id: 102,
    feedback: "Delivery was smooth and on time!",
    rating: 5,
    date: new Date("2024-01-10")
  },
  {
    customer_id: 3,
    name: "Carol White",
    order_id: 103,
    feedback: "Wrong item delivered, very disappointed.",
    rating: 1,
    date: new Date("2024-01-16")
  }
]);

db.customer_feedback.createIndex({ customer_id: 1 });

db.customer_feedback.find({ customer_id: 1 });

db.customer_feedback.find().pretty();
