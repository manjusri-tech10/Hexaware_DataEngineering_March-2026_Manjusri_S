use("library_db")
//MEMBERS COLLECTION
db.members.insertMany([
  { member_id: 1, name: "Aarav", city: "Hyderabad", membership_type: "Gold" },
  { member_id: 2, name: "Priya", city: "Bangalore", membership_type: "Silver" },
  { member_id: 3, name: "Rahul", city: "Mumbai", membership_type: "Gold" },
  { member_id: 4, name: "Sneha", city: "Delhi", membership_type: "Silver" },
  { member_id: 5, name: "Kiran", city: "Hyderabad", membership_type: "Gold" }
])
//BOOKS COLLECTION
db.books.insertMany([
  { book_id: 101, title: "MongoDB Basics", category: "Database", author: "John Smith", price: 500 },
  { book_id: 102, title: "Python Fundamentals", category: "Programming", author: "Alice Brown", price: 650 },
  { book_id: 103, title: "Data Engineering Intro", category: "Data", author: "Mark Lee", price: 800 },
  { book_id: 104, title: "SQL for Beginners", category: "Database", author: "David Miller", price: 450 },
  { book_id: 105, title: "Machine Learning Start", category: "AI", author: "Sara Khan", price: 900 }
])
//BORROWINGS COLLECTION
db.borrowings.insertMany([
  { borrow_id: 1001, member_id: 1, book_id: 101, days_borrowed: 5, borrow_date: "2026-03-01" },
  { borrow_id: 1002, member_id: 2, book_id: 102, days_borrowed: 3, borrow_date: "2026-03-02" },
  { borrow_id: 1003, member_id: 1, book_id: 103, days_borrowed: 7, borrow_date: "2026-03-03" },
  { borrow_id: 1004, member_id: 3, book_id: 104, days_borrowed: 4, borrow_date: "2026-03-05" },
  { borrow_id: 1005, member_id: 5, book_id: 105, days_borrowed: 10, borrow_date: "2026-03-07" },
  { borrow_id: 1006, member_id: 5, book_id: 101, days_borrowed: 2, borrow_date: "2026-03-08" }
])

//1
db.members.find()

//2

db.books.find()

//3

db.borrowings.find()

//Filter
//4

db.members.find({city:"Hyderabad"})

//5

db.books.find({category:"Database"})

//6

db.books.find({price:{$gt:600}})

//7

db.borrowings.find({days_borrowed:{$gt:5}})

//Sorting

//8

db.books.find().sort({price:-1})

//9

db.members.find().sort({name:1})

//Count

//10

db.members.countDocuments()

//11

db.books.countDocuments()

//12

db.books.countDocuments({category: "Database"})

//Aggregate

//13

db.books.aggregate([
  { $group: { _id: null, avg_price: {$avg: "$price"} } }
])

//14

db.books.aggregate([
  { $group: { _id: null, max_price: {$max: "$price"} } }
])

//15

db.books.aggregate([
  { $group: { _id: null, min_price: {$min: "$price"} } }
])

//16

db.borrowings.aggregate([
  { $group: { _id: "$member_id", total_days: {$sum: "$days_borrowed"} } }
])

//Queries using $lookup

//17

db.borrowings.aggregate([
  {
    $lookup: {
      from: "members",
      localField: "member_id",
      foreignField: "member_id",
      as: "member_details"
    }
  }
])

//18

db.borrowings.aggregate([
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book_details"
    }
  }
])

//19

db.borrowings.aggregate([
  {
    $lookup: {
      from: "members",
      localField: "member_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  {
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      member_name: { $arrayElemAt: ["$member.name", 0] },
      book_title: { $arrayElemAt: ["$book.title", 0] }
    }
  }])

//20

db.borrowings.aggregate([
  { $group: { _id: "$book_id", total_borrowed: { $sum: 1 } } },
  {
    $lookup: {
      from: "books",
      localField: "_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      book_title: { $arrayElemAt: ["$book.title", 0] },
      total_borrowed: 1
    }
  }
])
//Adv Aggregate
//21

db.borrowings.aggregate([
  { $group: { _id: "$member_id", total_books: { $sum: 1 } } }])
//22

db.borrowings.aggregate([
  { $group: { _id: "$book_id", borrow_count: { $sum: 1 } } },
  { $sort: { borrow_count: -1 } },
  { $limit: 1 },
  {
    $lookup: {
      from: "books",
      localField: "_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  {
    $project: {
      book_title: { $arrayElemAt: ["$book.title", 0] },
      borrow_count: 1
    }
  }])
//23

db.borrowings.aggregate([{
    $lookup: {
      from: "books",
      localField: "book_id",
      foreignField: "book_id",
      as: "book"
    }
  },
  { $unwind: "$book" },
  { $group: { _id: "$book.category", total_borrowings: { $sum: 1 } } }])
//24

db.borrowings.aggregate([
  { $group: { _id: "$member_id", total_books: { $sum: 1 } } },
  { $match: { total_books: { $gt: 1 } } }])

//25
db.borrowings.aggregate([
  { $group: { _id: "$member_id", total_books: { $sum: 1 } } },
  {
    $lookup: {
      from: "members",
      localField: "_id",
      foreignField: "member_id",
      as: "member"
    }
  },
  { $unwind: "$member" },
  {
    $project: {
      member_name: "$member.name",
      city: "$member.city",
      total_books: 1
    }
  },
  { $sort: { total_books: -1 } }])
