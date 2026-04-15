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
