use("hospital_db")

//1. Create Patients Collection
db.patients.insertMany([
{ patient_id: 1, name: "Aarav", city: "Hyderabad", age: 29, gender: "Male" },
{ patient_id: 2, name: "Priya", city: "Bangalore", age: 34, gender: "Female" },
{ patient_id: 3, name: "Rahul", city: "Mumbai", age: 41, gender: "Male" },
{ patient_id: 4, name: "Sneha", city: "Delhi", age: 26, gender: "Female" },
{ patient_id: 5, name: "Kiran", city: "Hyderabad", age: 37, gender: "Male" },
{ patient_id: 6, name: "Meera", city: "Chennai", age: 31, gender: "Female" }
])

//2. Create Doctors Collection
db.doctors.insertMany([
{ doctor_id: 101, name: "Dr. Sharma", specialization: "Cardiology", consultation_fee: 1200, city: "Hyderabad" },
{ doctor_id: 102, name: "Dr. Iyer", specialization: "Dermatology", consultation_fee: 800, city: "Bangalore" },
{ doctor_id: 103, name: "Dr. Khan", specialization: "Orthopedics", consultation_fee: 1500, city: "Mumbai" },
{ doctor_id: 104, name: "Dr. Reddy", specialization: "Pediatrics", consultation_fee: 900, city: "Delhi" },
{ doctor_id: 105, name: "Dr. Mehta", specialization: "Neurology", consultation_fee: 2000, city: "Hyderabad" }
])


//3. Create Appointments Collection
db.appointments.insertMany([
{ appointment_id: 1001, patient_id: 1, doctor_id: 101, visit_date: "2026-03-01", status: "Completed", bill_amount: 1200 },
{ appointment_id: 1002, patient_id: 2, doctor_id: 102, visit_date: "2026-03-02", status: "Completed", bill_amount: 800 },
{ appointment_id: 1003, patient_id: 1, doctor_id: 105, visit_date: "2026-03-04", status: "Pending", bill_amount: 2000 },
{ appointment_id: 1004, patient_id: 3, doctor_id: 103, visit_date: "2026-03-05", status: "Completed", bill_amount: 1500 },
{ appointment_id: 1005, patient_id: 5, doctor_id: 101, visit_date: "2026-03-07", status: "Cancelled", bill_amount: 1200 },
{ appointment_id: 1006, patient_id: 6, doctor_id: 104, visit_date: "2026-03-08", status: "Completed", bill_amount: 900 },
{ appointment_id: 1007, patient_id: 4, doctor_id: 104, visit_date: "2026-03-09", status: "Pending", bill_amount: 900 },
{ appointment_id: 1008, patient_id: 3, doctor_id: 105, visit_date: "2026-03-10", status: "Completed", bill_amount: 2000 }
])

//1
db.patients.find()

//2
db.doctors.find()

//3
db.appointments.find()

//4
db.patients.find({ city: "Hyderabad" })

//5
db.doctors.find({ specialization: "Cardiology" })

//6
db.appointments.find({ status: "Completed" })

//7
db.patients.find({ age: { $gt: 30 } })

//8
db.doctors.find({ consultation_fee: { $gt: 1000 } })

//9
db.doctors.find({ consultation_fee: { $gte: 900, $lte: 1600 } })

//10
db.appointments.find({ bill_amount: { $gt: 1000 } })

//11
db.appointments.find({ status: { $ne: "Cancelled" } })

//12
db.patients.find({ city: { $in: ["Hyderabad", "Mumbai"] } })

//13
db.doctors.find({ city: { $in: ["Hyderabad", "Delhi"] } })

//14
db.patients.find({}, { _id: 0, name: 1, city: 1 })

//15
db.doctors.find({}, { _id: 0, name: 1, specialization: 1, consultation_fee: 1 })

//16
db.appointments.find({}, { _id: 0, appointment_id: 1, status: 1, bill_amount: 1 })

//17
db.doctors.find().sort({ consultation_fee: 1 })

//18
db.doctors.find().sort({ consultation_fee: -1 })

//19
db.doctors.find().sort({ consultation_fee: -1 }).limit(3)

//20
db.doctors.find().sort({ consultation_fee: 1 }).limit(2)

//21
db.patients.find().skip(2)

//22
db.patients.find().sort({ age: -1 })

//23
db.doctors.updateOne({ name: "Dr. Sharma" }, { $set: { consultation_fee: 1300 } })

//24
db.appointments.updateMany({ status: "Pending" }, { $set: { priority: "High" } })

//25
db.doctors.updateMany({ city: "Hyderabad" }, { $set: { available: true } })

//26
db.patients.updateOne({ name: "Meera" }, { $set: { city: "Bangalore" } })

//27
db.doctors.deleteOne({ name: "Dr. Iyer" })

//28
db.appointments.deleteMany({ status: "Cancelled" })

//29
db.patients.deleteMany({ city: "Delhi" })

//30
db.patients.countDocuments()

//31
db.doctors.countDocuments({ city: "Hyderabad" })

//32
db.appointments.countDocuments({ status: "Completed" })

//33
db.patients.countDocuments({ city: "Hyderabad" })

//34
db.doctors.aggregate([
  { $group: { _id: "$specialization", avg_fee: { $avg: "$consultation_fee" } } }
])

//35
db.doctors.aggregate([
  { $group: { _id: null, max_fee: { $max: "$consultation_fee" } } }
])

//36
db.doctors.aggregate([
  { $group: { _id: null, min_fee: { $min: "$consultation_fee" } } }
])

//37
db.appointments.aggregate([
  { $group: { _id: "$status", total_bill: { $sum: "$bill_amount" } } }
])

//38
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", total_appointments: { $sum: 1 } } }
])

//39
db.appointments.aggregate([
  { $group: { _id: "$patient_id", total_appointments: { $sum: 1 } } }
])

//40
db.patients.aggregate([
  { $group: { _id: "$city", avg_age: { $avg: "$age" } } }
])

//41
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", total_bill: { $sum: "$bill_amount" } } }
])

//42
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_info"
    }
  },
  { $unwind: "$patient_info" },
  { $group: { _id: "$patient_info.city", total_bill: { $sum: "$bill_amount" } } }
])

//43
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_details"
    }
  }
])

//44
db.appointments.aggregate([
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "doctor_details"
    }
  }
])

//45
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_info"
    }
  },
  { $unwind: "$patient_info" },
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "doctor_info"
    }
  },
  { $unwind: "$doctor_info" },
  {
    $project: {
      _id: 0,
      patient_name: "$patient_info.name",
      doctor_name: "$doctor_info.name"
    }
  }
])

//46
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_info"
    }
  },
  { $unwind: "$patient_info" },
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "doctor_info"
    }
  },
  { $unwind: "$doctor_info" },
  {
    $project: {
      _id: 0,
      patient_name: "$patient_info.name",
      city: "$patient_info.city",
      doctor_name: "$doctor_info.name",
      specialization: "$doctor_info.specialization",
      status: 1,
      bill_amount: 1
    }
  }
])

//47
db.patients.aggregate([
  {
    $lookup: {
      from: "appointments",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "appointments"
    }
  }
])

//48
db.doctors.aggregate([
  {
    $lookup: {
      from: "appointments",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "appointments"
    }
  }
])

//49
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", total_revenue: { $sum: "$bill_amount" } } },
  {
    $lookup: {
      from: "doctors",
      localField: "_id",
      foreignField: "doctor_id",
      as: "doctor_info"
    }
  },
  { $unwind: "$doctor_info" },
  { $project: { _id: 0, doctor_name: "$doctor_info.name", total_revenue: 1 } }
])

//50
db.appointments.aggregate([
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "doctor_info"
    }
  },
  { $unwind: "$doctor_info" },
  { $group: { _id: "$doctor_info.specialization", total_revenue: { $sum: "$bill_amount" } } }
])

//51
db.appointments.aggregate([
  { $group: { _id: "$patient_id", total_spent: { $sum: "$bill_amount" } } },
  { $sort: { total_spent: -1 } },
  { $limit: 1 },
  {
    $lookup: {
      from: "patients",
      localField: "_id",
      foreignField: "patient_id",
      as: "patient_info"
    }
  },
  { $unwind: "$patient_info" },
  { $project: { _id: 0, patient_name: "$patient_info.name", total_spent: 1 } }
])

//52
db.appointments.aggregate([
  { $group: { _id: "$doctor_id", total_appointments: { $sum: 1 } } },
  { $sort: { total_appointments: -1 } },
  { $limit: 1 },
  {
    $lookup: {
      from: "doctors",
      localField: "_id",
      foreignField: "doctor_id",
      as: "doctor_info"
    }
  },
  { $unwind: "$doctor_info" },
  { $project: { _id: 0, doctor_name: "$doctor_info.name", total_appointments: 1 } }
])

//53
db.appointments.aggregate([
  { $match: { status: "Completed" } },
  { $group: { _id: null, total_revenue: { $sum: "$bill_amount" } } }
])

//54
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_info"
    }
  },
  { $unwind: "$patient_info" },
  { $group: { _id: "$patient_info.city", total_appointments: { $sum: 1 } } },
  { $sort: { total_appointments: -1 } },
  { $limit: 1 }
])

//55
db.appointments.aggregate([
  {
    $lookup: {
      from: "patients",
      localField: "patient_id",
      foreignField: "patient_id",
      as: "patient_info"
    }
  },
  { $unwind: "$patient_info" },
  { $group: { _id: "$patient_info.city", total_bill: { $sum: "$bill_amount" } } },
  { $sort: { total_bill: -1 } },
  { $limit: 1 }
])

//56
db.appointments.aggregate([
  {
    $lookup: {
      from: "doctors",
      localField: "doctor_id",
      foreignField: "doctor_id",
      as: "doctor_info"
    }
  },
  { $unwind: "$doctor_info" },
  { $group: { _id: "$doctor_info.specialization", avg_bill: { $avg: "$bill_amount" } } },
  { $sort: { avg_bill: -1 } },
  { $limit: 1 }
])
